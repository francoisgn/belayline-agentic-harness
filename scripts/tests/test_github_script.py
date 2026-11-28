"""Every actions/github-script `script:` block of the harness workflows compiles the way github-script v9 builds it.

github-script v9 passes the script `github`, `context`, `core`, `glob`, `io`, `exec`, `getOctokit` and `require` as
parameters of an async function; redeclaring one of them with const/let is a SyntaxError at run time, in every
consumer's CI (README at 3a2844b, "This action" and "V9 breaking changes"). This test compiles each block under Node
with the same parameters, without running it. Skipped without Node.
"""
import json
import pathlib
import re
import shutil
import subprocess
import tempfile
import unittest

from test_pr_hygiene import INJECTED

ROOT = pathlib.Path(__file__).resolve().parents[2]
DIRS = [ROOT / ".github" / "workflows", ROOT / "templates" / ".github" / "workflows"]
NODE = shutil.which("node")
USES = re.compile(r"^(\s*)-?\s*uses:\s*actions/github-script@")
COMPILE = """
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;
const blocks = JSON.parse(require('fs').readFileSync(process.argv[2], 'utf8'));
const params = JSON.parse(process.argv[3]);
let bad = 0;
for (const b of blocks) {
  try { new AsyncFunction(...params, b.script); }
  catch (e) { bad++; console.log(`${b.where}: ${e.name}: ${e.message}`); }
}
process.exit(bad ? 1 : 0);
"""


def script_blocks(text, where):
    """(location, body) of each `script: |` that belongs to a github-script step."""
    lines = text.splitlines()
    out = []
    for i, line in enumerate(lines):
        m = USES.match(line)
        if not m:
            continue
        step_indent = len(line) - len(line.lstrip(" -"))
        for j in range(i + 1, len(lines)):
            cur = lines[j]
            if cur.strip() and len(cur) - len(cur.lstrip()) < step_indent:
                break
            if cur.lstrip().startswith("- ") and len(cur) - len(cur.lstrip()) <= step_indent - 2:
                break
            if cur.strip() in ("script: |", "script: |-"):
                indent = len(cur) - len(cur.lstrip()) + 2
                body = []
                for k in range(j + 1, len(lines)):
                    b = lines[k]
                    if b.strip() and len(b) - len(b.lstrip()) < indent:
                        break
                    body.append(b[indent:])
                out.append({"where": f"{where}:{j + 1}", "script": "\n".join(body)})
                break
    return out


def all_blocks():
    blocks = []
    for d in DIRS:
        for f in sorted(d.glob("*.y*ml")):
            blocks += script_blocks(f.read_text(encoding="utf-8"), f.relative_to(ROOT).as_posix())
    return blocks


def compile_blocks(blocks):
    with tempfile.TemporaryDirectory() as tmp:
        data = pathlib.Path(tmp) / "blocks.json"
        data.write_text(json.dumps(blocks), encoding="utf-8")
        js = pathlib.Path(tmp) / "compile.js"
        js.write_text(COMPILE, encoding="utf-8")
        return subprocess.run([NODE, str(js), str(data), json.dumps(INJECTED)], capture_output=True, text=True,
                              timeout=30, check=False)


@unittest.skipUnless(NODE, "node not installed")
class GithubScriptBlocksTests(unittest.TestCase):
    def test_blocks_are_found(self):
        blocks = all_blocks()
        self.assertTrue(any("pr-hygiene.yml" in b["where"] for b in blocks), [b["where"] for b in blocks])

    def test_every_block_compiles_with_the_injected_parameters(self):
        run = compile_blocks(all_blocks())
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)

    def test_a_redeclared_injected_name_is_caught(self):
        for name in INJECTED:
            run = compile_blocks([{"where": "sample", "script": f"const {name} = 1;"}])
            self.assertEqual(run.returncode, 1, name)
            self.assertIn("SyntaxError", run.stdout, name)

    def test_extraction_stops_at_the_next_step(self):
        text = ("    steps:\n      - uses: actions/github-script@abc # v9\n        with:\n          script: |\n"
                "            core.info('a')\n      - run: echo b\n")
        self.assertEqual(script_blocks(text, "t"), [{"where": "t:4", "script": "core.info('a')"}])


if __name__ == "__main__":
    unittest.main()
