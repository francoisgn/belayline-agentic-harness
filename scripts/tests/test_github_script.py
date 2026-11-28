"""Every actions/github-script `script:` of the harness compiles the way github-script v9 builds it.

github-script v9 runs the script as the body of an async function whose parameters are the injected names
(`INJECTED`, from its dist/index.js); redeclaring one of them with const/let is a SyntaxError at run time, in every
consumer's CI. This test finds every github-script step of the workflow and action files under `.github/` and
`templates/.github/` (recursive), extracts its `script:` whatever the YAML form (literal or folded block, chomping
and indentation indicators, trailing comment, inline scalar), and compiles it under Node with the same parameters,
without running it. A step whose script cannot be extracted fails the test, so nothing is skipped silently. Without
Node the test is skipped, except under CI (`CI` set), where it fails.
"""
import json
import os
import pathlib
import re
import shutil
import subprocess
import tempfile
import unittest

from test_pr_hygiene import INJECTED

ROOT = pathlib.Path(__file__).resolve().parents[2]
DIRS = [ROOT / ".github", ROOT / "templates" / ".github"]
NODE = shutil.which("node")
# `uses: actions/github-script@…`, optionally after the step's `- `, optionally quoted.
USES = re.compile(r"""^(\s*)(-\s+)?uses:\s*["']?actions/github-script@""", re.IGNORECASE)
# Independent count of github-script references (any form, any case, comments excluded), so a step the extractor's
# pattern does not recognise still shows up as a mismatch.
ANY_REF = re.compile(r"actions/github-script@", re.IGNORECASE)
STEP_START = re.compile(r"^(\s*)-\s")
SCRIPT = re.compile(r"""^(\s*)script:\s*(.*?)\s*$""")
BLOCK = re.compile(r"^([|>])([+-]?)([1-9]?)([+-]?)\s*(#.*)?$")
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


def indent_of(line):
    return len(line) - len(line.lstrip(" "))


def step_bounds(lines, i):
    """First and last line index of the step that holds line i (a sequence item `- …`)."""
    start = i
    while start >= 0 and not STEP_START.match(lines[start]):
        start -= 1
    if start < 0:
        return None
    dash = indent_of(lines[start])
    end = start + 1
    while end < len(lines):
        cur = lines[end]
        if cur.strip() and not cur.lstrip().startswith("#") and indent_of(cur) <= dash:
            break
        end += 1
    return start, end


# YAML 1.2.2 §5.7 escape sequences of a double-quoted scalar (https://yaml.org/spec/1.2.2/#57-escaped-characters).
YAML_ESCAPES = {"0": "\x00", "a": "\x07", "b": "\x08", "t": "\t", "\t": "\t", "n": "\n", "v": "\x0b", "f": "\x0c",
                "r": "\r", "e": "\x1b", " ": " ", '"': '"', "/": "/", "\\": "\\", "N": "\x85", "_": "\xa0",
                "L": "\u2028", "P": "\u2029"}
YAML_HEX = {"x": 2, "u": 4, "U": 8}


def decode_double_quoted(inner):
    """The value of a one-line double-quoted scalar, or None on an escape YAML does not define (reported as a step
    whose script could not be extracted, never compiled half-decoded)."""
    out, i = [], 0
    while i < len(inner):
        c = inner[i]
        if c != "\\":
            out.append(c)
            i += 1
            continue
        if i + 1 >= len(inner):
            return None
        e = inner[i + 1]
        if e in YAML_ESCAPES:
            out.append(YAML_ESCAPES[e])
            i += 2
        elif e in YAML_HEX:
            digits = inner[i + 2:i + 2 + YAML_HEX[e]]
            if len(digits) != YAML_HEX[e] or not all(d in "0123456789abcdefABCDEF" for d in digits):
                return None
            out.append(chr(int(digits, 16)))
            i += 2 + YAML_HEX[e]
        else:
            return None
    return "".join(out)


def unquote(value):
    """A one-line YAML scalar's value: double quotes decoded per §5.7, single quotes with `''` as one quote (§7.3.2);
    None when the value cannot be decoded."""
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return decode_double_quoted(value[1:-1])
    if len(value) >= 2 and value[0] == value[-1] == "'":
        return value[1:-1].replace("''", "'")
    return value


def read_script(lines, j):
    """The script value of the `script:` key at line j, or None when its form is not understood."""
    m = SCRIPT.match(lines[j])
    key_indent, value = len(m.group(1)), m.group(2)
    block = BLOCK.match(value)
    if not block:
        return unquote(value) if value and not value.startswith("#") else None
    body = []
    content_indent = None
    for k in range(j + 1, len(lines)):
        cur = lines[k]
        if cur.strip():
            if indent_of(cur) <= key_indent:
                break
            if content_indent is None:
                content_indent = indent_of(cur)
            body.append(cur[content_indent:])
        else:
            body.append("")
    while body and body[-1] == "":
        body.pop()
    if block.group(1) == ">":
        return fold(body)
    return "\n".join(body)


def fold(lines):
    """YAML folding of a `>` block whose lines are already de-indented (YAML 1.2.2 §8.1.3, §6.5): a single break
    between two non-empty lines at the content indentation becomes a space; n empty lines between them become n
    breaks; a break next to a more-indented line (or an empty one) is kept."""
    out = ""
    prev = None  # previous non-empty line
    blanks = 0
    for line in lines:
        if line == "":
            blanks += 1
            continue
        if prev is None:
            out = "\n" * blanks + line
        else:
            spaced = line.startswith((" ", "\t")) or prev.startswith((" ", "\t"))
            if spaced:
                out += "\n" * (blanks + 1) + line
            elif blanks:
                out += "\n" * blanks + line
            else:
                out += " " + line
        prev, blanks = line, 0
    return out


def script_blocks(text, where):
    """([{where, script}], [location of a github-script step whose script was not extracted])."""
    lines = text.splitlines()
    found, missing = [], []
    for i, line in enumerate(lines):
        if not USES.match(line):
            continue
        bounds = step_bounds(lines, i)
        script = None
        at = i + 1
        if bounds:
            for j in range(bounds[0], bounds[1]):
                if SCRIPT.match(lines[j]):
                    script, at = read_script(lines, j), j + 1
                    break
        if script is None:
            missing.append(f"{where}:{i + 1}")
        else:
            found.append({"where": f"{where}:{at}", "script": script})
    return found, missing


def all_blocks():
    found, missing = [], []
    for d in DIRS:
        for f in sorted(p for p in d.rglob("*") if p.suffix in (".yml", ".yaml")):
            text = f.read_text(encoding="utf-8")
            got, lost = script_blocks(text, f.relative_to(ROOT).as_posix())
            found += got
            missing += lost
    return found, missing


def compile_blocks(blocks):
    with tempfile.TemporaryDirectory() as tmp:
        data = pathlib.Path(tmp) / "blocks.json"
        data.write_text(json.dumps(blocks), encoding="utf-8")
        js = pathlib.Path(tmp) / "compile.js"
        js.write_text(COMPILE, encoding="utf-8")
        return subprocess.run([NODE, str(js), str(data), json.dumps(INJECTED)], capture_output=True, text=True,
                              timeout=30, check=False)


class NodeRequiredInCiTests(unittest.TestCase):
    def test_node_present_under_ci(self):
        if os.environ.get("CI") and not NODE:
            self.fail("CI is set but node is not installed: the github-script compile tests would be skipped")


class ExtractionTests(unittest.TestCase):
    def check(self, step, expected):
        text = "    steps:\n" + step + "      - run: echo next\n"
        found, missing = script_blocks(text, "t")
        self.assertEqual(missing, [])
        self.assertEqual([b["script"] for b in found], [expected])

    def test_literal_block(self):
        self.check("      - uses: actions/github-script@abc # v9\n        with:\n          script: |\n"
                   "            core.info('a')\n            core.info('b')\n", "core.info('a')\ncore.info('b')")

    def test_block_indicators_and_comment(self):
        for header in ("|-", "|+", "|2", "| # js", ">-"):
            body = "core.info('a')" if not header.startswith(">") else "core.info('a') core.info('b')"
            second = "" if not header.startswith(">") else "            core.info('b')\n"
            self.check(f"      - uses: actions/github-script@abc\n        with:\n          script: {header}\n"
                       f"            core.info('a')\n{second}", body)

    def test_inline_and_quoted(self):
        self.check("      - uses: actions/github-script@abc\n        with:\n          script: core.info('a')\n",
                   "core.info('a')")
        self.check("      - uses: \"actions/github-script@abc\"\n        with:\n"
                   "          script: \"core.info('a')\"\n", "core.info('a')")

    def test_double_quoted_escapes_are_decoded(self):
        # YAML decodes \n in a double-quoted scalar: the declaration is on its own line, not inside the comment.
        self.check('      - uses: actions/github-script@abc\n        with:\n'
                   '          script: "// note\\nconst glob = 1;"\n', "// note\nconst glob = 1;")
        self.check("      - uses: actions/github-script@abc\n        with:\n"
                   "          script: 'it''s'\n", "it's")

    def test_folded_block_never_hides_a_line_in_a_comment(self):
        found, _ = script_blocks("    steps:\n      - uses: actions/github-script@abc\n        with:\n"
                                 "          script: >\n            // note\n              const glob = 1;\n", "t")
        self.assertIn("\n", found[0]["script"].strip())

    def test_folded_same_indent_lines_are_joined(self):
        # YAML folds these into `const x = 1 const y = 2;`, which the runner rejects: so must the test.
        found, _ = script_blocks("    steps:\n      - uses: actions/github-script@abc\n        with:\n"
                                 "          script: >\n            const x = 1\n            const y = 2;\n", "t")
        self.assertEqual(found[0]["script"], "const x = 1 const y = 2;")
        if NODE:
            self.assertEqual(compile_blocks(found).returncode, 1)

    def test_folded_blank_lines_and_more_indented_keep_breaks(self):
        self.assertEqual(fold(["a", "b", "", "c", "  d", "e"]), "a b\nc\n  d\ne")

    def test_every_yaml_escape_is_decoded(self):
        self.assertEqual(decode_double_quoted("a\\Lb\\Pc\\N\\_\\x41\\u00e9\\U0001F600\\t\\\\\\\""),
                         "a\u2028b\u2029c\x85\xa0A\u00e9\U0001F600\t\\\"")

    def test_line_separator_escape_ends_the_comment(self):
        # \L is U+2028, a JavaScript line terminator: the declaration is outside the comment and must fail.
        found, missing = script_blocks('    steps:\n      - uses: actions/github-script@abc\n        with:\n'
                                       '          script: "// note\\Lconst glob = 1;"\n', "t")
        self.assertEqual((missing, found[0]["script"]), ([], "// note\u2028const glob = 1;"))
        if NODE:
            self.assertEqual(compile_blocks(found).returncode, 1)

    def test_unknown_escape_is_reported_not_compiled(self):
        found, missing = script_blocks('    steps:\n      - uses: actions/github-script@abc\n        with:\n'
                                       '          script: "a\\qb"\n', "t")
        self.assertEqual((found, missing), ([], ["t:2"]))

    def test_decoded_redeclaration_fails_compilation(self):
        if not NODE:
            self.skipTest("node not installed")
        found, _ = script_blocks('    steps:\n      - uses: actions/github-script@abc\n        with:\n'
                                 '          script: "// note\\nconst glob = 1;"\n', "t")
        self.assertEqual(compile_blocks(found).returncode, 1)

    def test_keys_before_uses(self):
        self.check("      - name: x\n        id: y\n        with:\n          github-token: t\n"
                   "          script: |\n            core.info('a')\n        uses: actions/github-script@abc\n",
                   "core.info('a')")

    def test_unindented_sequence(self):
        found, missing = script_blocks("steps:\n- uses: actions/github-script@abc\n  with:\n    script: |\n"
                                       "      core.info('a')\n- run: echo b\n", "t")
        self.assertEqual((missing, [b["script"] for b in found]), ([], ["core.info('a')"]))

    def test_step_without_script_is_reported(self):
        found, missing = script_blocks("    steps:\n      - uses: actions/github-script@abc\n        with:\n"
                                       "          github-token: t\n      - run: echo b\n", "t")
        self.assertEqual((found, missing), ([], ["t:2"]))


@unittest.skipUnless(NODE, "node not installed")
class GithubScriptBlocksTests(unittest.TestCase):
    def test_every_github_script_step_is_extracted(self):
        found, missing = all_blocks()
        self.assertEqual(missing, [])
        refs = sum(len(ANY_REF.findall(ln.split("#", 1)[0] if not ln.lstrip().startswith("#") else ""))
                   for d in DIRS for f in d.rglob("*") if f.suffix in (".yml", ".yaml")
                   for ln in f.read_text(encoding="utf-8").splitlines())
        self.assertEqual(len(found), refs)
        self.assertTrue(any("pr-hygiene.yml" in b["where"] for b in found), [b["where"] for b in found])

    def test_every_block_compiles_with_the_injected_parameters(self):
        found, _ = all_blocks()
        run = compile_blocks(found)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)

    def test_injected_names_match_github_script_v9(self):
        # dist/index.js 65100-65111 at 3a2844b; a name dropped from INJECTED would no longer be checked.
        self.assertEqual(sorted(INJECTED), sorted(["require", "__original_require__", "github", "octokit", "getOctokit",
                                                    "context", "core", "exec", "glob", "io"]))

    def test_a_redeclared_injected_name_is_caught(self):
        for name in INJECTED:
            run = compile_blocks([{"where": "sample", "script": f"const {name} = 1;"}])
            self.assertEqual(run.returncode, 1, name)
            self.assertIn("SyntaxError", run.stdout, name)


if __name__ == "__main__":
    unittest.main()
