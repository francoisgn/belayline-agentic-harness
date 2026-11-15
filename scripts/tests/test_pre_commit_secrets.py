"""Tests of scripts/pre-commit-secrets.sh (issue #113): the optional git pre-commit hook that scans the staged changes
with gitleaks. A fake `gitleaks` on PATH stands in for the real one: no network, no secret in the tests.

- gitleaks absent: the commit goes on (exit 0) and the hook says clearly that nothing was scanned;
- gitleaks present, nothing found: exit 0, called with the staged-changes arguments of gitleaks's own hook;
- gitleaks present, a finding: the commit is refused (gitleaks's exit code) with what to do.
"""
import os
import pathlib
import subprocess
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
HOOK = ROOT / "scripts/pre-commit-secrets.sh"
BASH = "/bin/bash"
GITLEAKS_ARGS = "git --pre-commit --redact --staged --verbose"


class PreCommitSecretsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.bin = pathlib.Path(self.tmp.name) / "bin"
        self.bin.mkdir()
        self.args_file = pathlib.Path(self.tmp.name) / "args"

    def tearDown(self):
        self.tmp.cleanup()

    def fake_gitleaks(self, code):
        fake = self.bin / "gitleaks"
        fake.write_text(f'#!{BASH}\nprintf "%s" "$*" >"{self.args_file}"\nexit {code}\n', encoding="utf-8")
        fake.chmod(0o755)

    def run_hook(self):
        env = {"PATH": str(self.bin), "HOME": self.tmp.name}
        return subprocess.run([BASH, str(HOOK)], env=env, capture_output=True, text=True, cwd=self.tmp.name,
                              check=False)

    def test_hook_is_executable(self):
        self.assertTrue(os.access(HOOK, os.X_OK))

    def test_gitleaks_absent_says_so_and_lets_the_commit_go_on(self):
        result = self.run_hook()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("gitleaks is not installed", result.stderr)
        self.assertIn("NOT scanned", result.stderr)

    def test_clean_staged_changes_pass(self):
        self.fake_gitleaks(0)
        result = self.run_hook()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.args_file.read_text(encoding="utf-8"), GITLEAKS_ARGS)
        self.assertNotIn("not installed", result.stderr)

    def test_finding_refuses_the_commit(self):
        self.fake_gitleaks(1)
        result = self.run_hook()
        self.assertEqual(result.returncode, 1)
        self.assertIn("commit refused", result.stderr)
        self.assertIn("revoke", result.stderr)


if __name__ == "__main__":
    unittest.main()
