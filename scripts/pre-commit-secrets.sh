#!/usr/bin/env bash
# Optional git pre-commit hook: scans the staged changes for secrets with gitleaks, before the commit exists
# (CI-BUDGET.md §3). Offered, never installed by the sync. Vendored as .harness/hooks/pre-commit-secrets.sh.
# Install it (a project that already has a pre-commit hook calls this script from it instead):
#   ln -s "$(git rev-parse --show-toplevel)/.harness/hooks/pre-commit-secrets.sh" "$(git rev-parse --git-path hooks)/pre-commit"
# gitleaks installed: runs `gitleaks git --pre-commit --redact --staged --verbose` (gitleaks's own hook) and refuses
# the commit on a finding. gitleaks missing: says so and lets the commit go on (CI still scans after the push).
# Exit codes: 0 = nothing found, or gitleaks not installed; otherwise gitleaks's (1 = finding or error).
set -uo pipefail

if ! command -v gitleaks >/dev/null 2>&1; then
  printf 'pre-commit-secrets: gitleaks is not installed: staged changes NOT scanned for secrets.\n' >&2
  printf '  Install it (https://github.com/gitleaks/gitleaks#installing); CI still scans after the push.\n' >&2
  exit 0
fi
gitleaks git --pre-commit --redact --staged --verbose
code=$?
if [ "$code" != 0 ]; then
  printf 'pre-commit-secrets: gitleaks found a secret or failed (exit %s): commit refused.\n' "$code" >&2
  printf '  Remove the secret from the staged files (keep it in the environment or a vault). If it was ever pushed,\n' >&2
  printf '  revoke it first: a committed secret is compromised.\n' >&2
fi
exit "$code"
