# Lessons to checks: inventory and context cost

Measured on 2026-11-15 at master `e8b5f03` for issue #115. A snapshot: it changes nothing in
[LESSONS](LESSONS.md) (no row moved, struck or retired; pruning is #114) and writes no check. Each proposal at the
end becomes an issue only after the operator's go.

## Summary

- **Lessons**: 92 rows; 3 are not `judgment` (L07 and L53 enforced, L75 "check to write"); **89 `judgment` rows**
  inventoried below: **7 yes**, **41 partly**, **41 no**. Strict reading: "yes" only when a deterministic check
  catches the failure the lesson describes with few false positives; a check that catches one clause, or a tool
  that only lists for a human to decide, is "partly". Column "Overlap" (input for #114): **19 rows** look like a
  duplicate or special case of another row or of a rule already in ESSENTIALS or CONVENTIONS; 31 more name a
  related row.
- **Top 5 "yes" by value**:
  1. **L83**: the `guard-git` hook refuses `checkout` / `switch` / `reset` / `stash` from a reviewer subagent, and
     `commit` on a detached HEAD (the hook already parses git commands; Claude Code gives hooks the subagent's
     `agent_type`).
  2. **L72** (and the last clause of L01): a filtered test run that executed zero tests fails the step.
  3. **L50**: a PR whose base is not the default branch and that adds or changes a workflow with an
     `issues` / `schedule` / `workflow_dispatch` / `pull_request_target` / `issue_comment` trigger, an issue form or
     the Dependabot config gets a warning that it is inert there.
  4. **L59**: the toolchain version pinned in the cloud setup script equals the CI's (same idea as the existing test
     that keeps `scripts/local-check.sh` in step with `ci.yml`).
  5. **L52**: a private repository whose workflows call CodeQL or Dependency Review (GitHub Advanced Security) fails,
     with a config switch for a repository that has the licence.
- **Context cost**: an adopted project's Claude Code session starts with about **15.5 kB, ~3,900 tokens** (chars/4)
  from the harness: `docs/ESSENTIALS.md` 35 %, agent descriptions 25 %, skill descriptions 23 %, the `CLAUDE.md`
  block 12 %, the SessionStart hook 4 %. The 9 compliance agents' descriptions (~650 tokens, 17 %) load in **every**
  session whatever `.harness/config.json` › `compliance` says. Proposals below save up to **~1,125 tokens per
  session** (~29 %).

## 1. Inventory of the `judgment` rows

Columns: **Check?** yes / partly / no; **Check** the script, hook, lint rule or test it would be; **Cost or risk**
of that check; **Overlap** a row or rule it duplicates or is a special case of (for #114, not acted on here).

| # | Check? | Check | Cost or risk | Overlap |
|---|---|---|---|---|
| L01 | partly | CI runs the tests the PR adds or changes against the base code and expects red; zero-test guard for the last clause (see L72) | Per-language plumbing, doubles test time; "through the real entry point" stays judgment | last clause = L72 |
| L02 | no | Which state a test asserts is semantic | | |
| L03 | no | "All combinations" is domain knowledge; property tests help but nothing detects their absence | | L04, L14 |
| L04 | no | Finding every path that acts needs understanding of the code | | L14 (near duplicate) |
| L05 | no | A claim being measured is not visible in a diff | | L82 |
| L06 | no | "Actionable" is a judgment of the message | | L32 |
| L08 | no | Doc versus behaviour equality is semantic; doc links already checked (`doc-links.py`) | | L09 |
| L09 | partly | Already partly: `pr-hygiene.yml` warns on a ready PR that changes code with no `Docs:` line; a check could also require a named tracking doc to change with its paths | Path-to-doc mapping per project; warn only | L08 |
| L10 | no | Whether a file duplicates another file's role is judgment | | |
| L11 | partly | Linter rule for missing doc comments on public API (SwiftLint `missing_docs`, ruff `D1`, `#![warn(missing_docs)]`) | Noisy on existing code (baseline needed); "why not what" stays judgment | |
| L12 | no | Needless copies and limit behaviour are semantic | | |
| L13 | partly | Duplicate-id checks per namespace the project names (labels, lesson ids, agent names, as `test_lesson_ids.py` does here) | Only for namespaces listed; "out of other namespaces" stays judgment | |
| L14 | no | Entry-point consistency spans UI surfaces | | L04 |
| L15 | partly | Lint for swallowed errors (`try?` on file/keychain calls, `except: pass`, Go `errcheck`) | False positives on deliberate ignores (inline reason); races stay judgment | |
| L16 | partly | `check-merge-conflict` pre-commit hook catches leftover markers only | Cheap; the "reread both parents" part stays judgment | |
| L17 | no | Reading a diff is the act itself | | |
| L18 | partly | `merge-gate.py` already prints and pins the head sha for a merge; a status comment could be generated with the sha read at post time | Only covers statuses produced by a script | L19 |
| L19 | no | "Already fixed / duplicate" needs reading; the rule is already in ESSENTIALS (last Quality bullet) | | ESSENTIALS, L18 |
| L20 | partly | `merge-gate.py` already refuses open threads at merge; a checkpoint script could list unanswered threads | Late bot posts after the check still slip | L45, L46 |
| L21 | no | Whether a fact is external and sourced is semantic | | ESSENTIALS "Nothing guessed" |
| L22 | partly | gitleaks already blocks secrets; real names or private content in fixtures are not pattern-detectable | gitleaks FPs on fixtures (allow-list) | ESSENTIALS "No secret" |
| L23 | no | The lesson is itself about an independent second check, designed per data set | | L24, L25 |
| L24 | no | Position-based redaction is a design choice | | L23 |
| L25 | no | Regex quoting bugs need review or tests per pattern | | special case of L24 |
| L26 | partly | `/lot-start` checks that the input paths a lot file declares exist | Needs a declared inputs list in the lot template | L27 |
| L27 | no | Fabricated data is not detectable | | special case of L26 |
| L28 | no | Reading real data before design is process | | |
| L29 | no | Oracle settings coverage is domain-specific | | L30 |
| L30 | no | Differential test design is domain-specific | | L29 |
| L31 | partly | Semgrep rule (project-specific): a URL from a response passed to the authenticated client without a scheme and host check | High FP rate without a project helper to whitelist | L65 |
| L32 | no | "Not found" versus "unreadable" is semantic | | L06 |
| L33 | partly | Semgrep rule: header-name comparison without trim and lowercase | Language-specific, FPs on constant comparisons | |
| L34 | partly | Lint ban on `Double` / `JSONSerialization` decoding in the module that round-trips foreign JSON | Project must name the module | |
| L35 | no | Compare-and-set placement needs concurrency reasoning | | L37 |
| L36 | partly | Run network-risk tests with networking off (`unshare -n`, test-runner network guard) so a real request fails | Linux-only sandboxing; "asserts the policy itself" stays judgment | L77 |
| L37 | no | Load ordering versus user marks is semantic | | L35 |
| L38 | no | "Normal code path" is semantic | | |
| L39 | no | Per-render work cost needs reading | | |
| L40 | partly | Semgrep rule: deletion calls (`removeItem`, `unlink`, `rmtree`) not routed through the project's validated helper | Needs the helper to exist; FPs on temp dirs | |
| L41 | no | Section ownership in shared docs is coordination | | L42 |
| L42 | partly | Merge gate refuses a rebase or squash merge of a PR whose base is another PR branch | Needs merge-method data from the API | L41 |
| L43 | partly | Script listing branches not merged into the integration branch | Listing only; the decision per branch stays judgment | |
| L44 | partly | Largely enforced by `merge-gate.py` (CI green on head, adversarial APPROVED naming the head, body lines); "has tests" and "spec" quality stay judgment | None new; row could cite the gate | ESSENTIALS Quality, merge-gate |
| L45 | partly | `merge-gate.py` refuses open threads; grouping fixes stays judgment | | special case of L20 |
| L46 | partly | Gate: the review bot's latest review `commit_id` equals the head sha | One API call; the `@mention` clause is an environment fact | L20 |
| L47 | partly | Dashboard signal (`flow-metrics.py`, #101) for jobs red in seconds with no log; one-rerun limit is judgment | Signal exists partly | L90, L91 |
| L48 | partly | Workflow lint: a `runs-on: macos*` job must be guarded by a draft or label condition | Cheap; layouts vary (allow-list); the other clauses are habits | ESSENTIALS CI budget, CI-BUDGET §2 |
| L49 | partly | Workflow lint: jobs gated by a change-detection job run when it did not succeed (`always()` and result test) | Many valid spellings of the condition | |
| L50 | **yes** | Warn on a PR to a non-default base that adds or changes a workflow with default-branch-only triggers, an issue form or `dependabot.yml` | One API call for the default branch; `session-start.sh` already warns on the same mismatch | |
| L51 | partly | actionlint already errors on an undeclared `runs-on` label; dynamic simulator choice stays judgment | None new | |
| L52 | **yes** | Fail when a private repository's workflows use `github/codeql-action` or `actions/dependency-review-action`, unless config says GHAS is licensed | Needs repo visibility (API or config) | |
| L54 | partly | Check that ShellCheck's input covers every tracked shell script (by extension and shebang); formatter hooks exclude fixture paths | Cheap; "byte for byte" needs the fixture paths named | |
| L55 | no | Environment fact for cloud sessions, not a code property | | |
| L56 | no | Environment fact (settings as code is already `repo-settings.py`) | | |
| L57 | no | Environment fact | | |
| L58 | no | Needs a compiler the container lacks; macOS CI settles it | | ESSENTIALS cloud session, MAC-HANDOFF |
| L59 | **yes** | Test that the toolchain version in the cloud setup script equals the CI workflow's | Both must read a parseable pin; few FPs | L60 (near duplicate) |
| L60 | partly | Same pin comparison for the linter; `local-check.sh` already says INCOMPLETE when a tool is missing | Hand-check clause stays judgment | L59 |
| L61 | partly | `pre-push` hook warns when tracked files are modified and unstaged | Legitimate local edits make it a warning, not a block | |
| L62 | partly | Grep rule: interpolating or printing a `Date` in Linux test targets | FPs on safe dates | L63, L64, L65 |
| L63 | no | Relying on `timeoutInterval` or redirect delegates is semantic | | L62 |
| L64 | **yes** | Grep rule: `URL.cachesDirectory` or `replaceItemAt` in code built on Linux | Cheap; the first already fails a Linux build, the second only at run time | L62 |
| L65 | no | Cookie carry-over is runtime behaviour | | special case of L31 |
| L66 | no | Thread ownership of a socket is semantic | | |
| L67 | no | Cancellation shape needs reading | | |
| L68 | partly | Grep rule for `@Test(arguments:` literals joined with `+` | The compiler already fails the target; the check only shortens diagnosis | |
| L69 | no | Typed-throws inference needs the compiler | | |
| L70 | no | Isolation inference needs the compiler | | |
| L71 | no | Recursion depth risk needs reading | | |
| L72 | **yes** | Test step fails when the run reports zero tests executed (parse the runner's summary or `xcresult`) | Per-runner parsing; few FPs | L01 last clause |
| L73 | no | Dialog state and capture semantics need reading | | |
| L74 | **yes** | For an XcodeGen project: regenerate and `git diff --exit-code` the `.pbxproj` | Needs XcodeGen in CI (Linux support to verify); only that strategy | |
| L76 | partly | SwiftLint custom rule banning `UIScreen.main` and `userInterfaceIdiom` | Labels, targets and Dynamic Type stay judgment | |
| L77 | no | Which component is "real" is a test-design choice | | L36 |
| L78 | partly | `.gitattributes` marks fixture paths `-text`; lint for text-mode reads in fixture loaders | Project names its fixture paths | |
| L79 | no | Write confirmation semantics need reading | | |
| L80 | partly | Test decodes a frozen save per released version; a check that a fixture exists for each release tag | Fixture upkeep per release | ESSENTIALS Persistence, CONVENTIONS §Persistence (duplicate) |
| L81 | partly | Script lists open PRs touching the same files (one API call); coordination stays judgment | | CONVENTIONS §Pull requests (duplicate) |
| L82 | partly | Dead-code tool (Periphery, vulture) flags functions with no caller | Tooling per language, FPs on reflection and entry points | special case of L05 |
| L83 | **yes** | `guard-git.py` refuses `checkout` / `switch` / `reset` / `stash` when the hook input's `agent_type` is a reviewer, and `commit` on a detached HEAD | Small change to an existing tested hook; a vendored-only project without the hook is not covered | |
| L84 | partly | Merge gate checks the verdict carries `Agent: <id> (<model>)` and that the model differs from the author model in the PR body | Stated model is self-reported | ESSENTIALS Quality |
| L85 | partly | `job-timeout.py` already enforces presence (#99); "from measured runs" stays judgment | None new | L86 |
| L86 | partly | Config check that the test runner has a per-test timeout set (e.g. pytest `timeout`, Swift `.timeLimit`) | Per-runner knowledge | L85, L87 |
| L87 | no | Documentation knowledge about Xcode options | | special case of L86 |
| L88 | partly | Lint for fixed sleeps in tests (`sleep(`, `Task.sleep`, `asyncAfter`) | FPs on bounded waits that sleep inside a poll | |
| L89 | no | Job layout is a project decision from measurements | | |
| L90 | partly | Warn when a diff adds skip or disable markers (`@skip`, `XCTSkip`, `.disabled`, `xit`) or deletes a test | Legitimate skips exist: warning with a reason line | special case of L47 |
| L91 | partly | Dashboard already flags a red base (#101); a rerun guard on PRs red on that job is possible | API calls per rerun | L47 |
| L92 | partly | Dashboard already flags runs queued with zero jobs (#101); the response stays judgment | None new | |

Count check: yes 7 (L50, L52, L59, L64, L72, L74, L83); partly 41; no 41; total 89.

## 2. Context cost per session

### Method

- Sizes from the files at `e8b5f03`: characters with Python `len(str)`, bytes with `len(str.encode("utf-8"))`;
  skill and agent descriptions are the frontmatter `description` value, bodies are the text after the frontmatter
  (the same split `check-framework.py` uses for its limits).
- **Tokens = characters / 4**, rounded. No tokenizer was available in the container (no `tiktoken`, no API key for
  the token-counting endpoint): an approximation, good to about ±20 % on English prose; treat the numbers as
  relative sizes.
- Not counted: the per-entry framing the client adds around each listed skill or agent, and the tool definitions
  themselves (not the harness's).

### What Claude Code loads (read on code.claude.com on 2026-11-15)

- **`CLAUDE.md` and its imports load in full at launch**: "imported files load together with the CLAUDE.md that
  imports them" ([memory](https://code.claude.com/docs/en/memory)). The harness block imports
  `.harness/docs/ESSENTIALS.md`, so both count. `AGENTS.md` is not read when a `CLAUDE.md` exists (default
  `claude-md-or-agents-md`), so its harness block (995 B) usually costs nothing in Claude Code.
- **Skills: descriptions at start, body on invocation**: "skill descriptions are loaded into context so Claude
  knows what's available, but full skill content only loads when invoked"; the body then "stays there across later
  turns". `disable-model-invocation: true` gives "Description not in context, full skill loads when invoked", and
  only the operator can then start the skill ([skills](https://code.claude.com/docs/en/skills)).
- **Subagents: descriptions in the main session, body only in the subagent**: "Those descriptions take up context,
  so keep them short" (warning above 15,000 tokens of custom descriptions); the body "becomes the system prompt"
  of the subagent and "only loads when that subagent runs"
  ([sub-agents](https://code.claude.com/docs/en/sub-agents)). `permissions.deny` with `Agent(<name>)` blocks a
  subagent; the page does not say whether that removes its description from context (to verify).
- **How the harness enables compliance agents**: `harness.manifest` vendors `plugins/harness/agents` as a whole
  tree into `.claude/agents/`; `.harness/config.json` › `compliance` only drives `compliance-plan.py` (which agent
  `/compliance-review` runs). The only way not to load a framework's description is the manual `exclude` list
  ([COMPLIANCE](COMPLIANCE.md) §2, [ADOPTION](ADOPTION.md)). So by default all 9 compliance descriptions load in
  every session of every adopted project, including projects with no compliance entry.

### Measured: every session

| Item | Chars | Bytes | ~Tokens |
|---|---|---|---|
| `CLAUDE.md` block (`templates/CLAUDE.md.block`) | 1,884 | 1,885 | 471 |
| `docs/ESSENTIALS.md` (imported) | 5,493 | 5,506 | 1,373 |
| 12 skill descriptions (+ 147 chars of names) | 3,602 | 3,602 | 901 |
| 13 agent descriptions (+ 203 chars of names) | 3,926 | 3,939 | 982 |
| of which 9 compliance agents | 2,588 | 2,592 | 647 |
| SessionStart hook output (`session-start.sh`, 603 B in a checkout without `.harness/`; an adopted project adds 1 to 3 lines) | ~603 | ~603 | ~151 |
| **Total** | **~15,508** | **~15,535** | **~3,877** |

If the operator also has the Belayline plugin installed at user scope in an adopted project, its skills are listed
again under `belayline:<name>` (+~900 tokens); its agents share names with the vendored ones, which win by priority.
The hook already silences the plugin's copy. Whether the duplicate skill listing appears is to verify in a session.

### Measured: per skill and agent

| Item | Desc chars | ~Tok | Body chars | ~Tok on use | Proposal | Saving per session |
|---|---|---|---|---|---|---|
| skill `compliance-review` | 406 | 102 | 1,590 | 398 | Shorten (drop the framework list); vendor only when `compliance` is set | ~50, or 102 without compliance |
| skill `feedback-triage` | 237 | 59 | 2,091 | 523 | Operator-started: `disable-model-invocation` | 59 |
| skill `harness-update` | 233 | 58 | 1,483 | 371 | Operator-started: `disable-model-invocation` | 58 |
| skill `intent` | 260 | 65 | 1,184 | 296 | Keep | 0 |
| skill `lesson-propose` | 270 | 68 | 1,789 | 447 | Keep (agents start it after review rounds) | 0 |
| skill `lessons-check` | 224 | 56 | 1,313 | 328 | Keep | 0 |
| skill `local-check` | 356 | 89 | 2,521 | 630 | Shorten (the when-clause) | ~30 |
| skill `lot-finish` | 301 | 75 | 4,716 | 1,179 | Shorten (drop the step list in parentheses) | ~35 |
| skill `lot-start` | 264 | 66 | 3,784 | 946 | Shorten ("following the Belayline harness", step list) | ~20 |
| skill `readme-update` | 359 | 90 | 2,424 | 606 | Shorten (drop the item list) | ~40 |
| skill `review-round` | 251 | 63 | 2,736 | 684 | Shorten slightly | ~15 |
| skill `status-report` | 294 | 74 | 933 | 233 | Operator-started: `disable-model-invocation` | 74 |
| agent `adversarial-reviewer` | 302 | 76 | 3,213 | 803 | Keep (the "give it only…" clause guides delegation) | 0 |
| agent `compliance-reviewer` | 299 | 75 | 1,757 | 439 | Vendor only when a `spec` entry exists | 75 if none |
| agent `compliance-eu-ai-act` | 298 | 74 | 3,882 | 970 | Vendor only when enabled | 74 if not enabled |
| agent `compliance-gdpr` | 241 | 60 | 3,818 | 954 | Vendor only when enabled | 60 if not enabled |
| agent `compliance-hds` | 316 | 79 | 3,937 | 984 | Vendor only when enabled | 79 if not enabled |
| agent `compliance-iso27001` | 263 | 66 | 3,316 | 829 | Vendor only when enabled | 66 if not enabled |
| agent `compliance-nis2` | 293 | 73 | 3,852 | 963 | Vendor only when enabled | 73 if not enabled |
| agent `compliance-pci` | 271 | 68 | 3,624 | 906 | Vendor only when enabled | 68 if not enabled |
| agent `compliance-soc2` | 299 | 75 | 3,262 | 816 | Vendor only when enabled | 75 if not enabled |
| agent `compliance-tisax` | 308 | 77 | 3,341 | 835 | Vendor only when enabled | 77 if not enabled |
| agent `doc-steward` | 367 | 92 | 2,564 | 641 | Shorten (started by a workflow, the item list is not needed to delegate) | ~45 |
| agent `flow-monitor` | 234 | 58 | 1,125 | 281 | Keep | 0 |
| agent `issue-steward` | 232 | 58 | 1,667 | 417 | Keep | 0 |

Savings, for a project with no compliance entry: compliance gating ~750 (9 agents 647 + the skill 102); shortening
~140 (five skills other than `compliance-review`, whose shortening overlaps its gating) + ~45 (`doc-steward`) ≈
185; operator-only skills 191. Total **up to ~1,125 tokens per session (~29 %)**; a project with compliance enabled
saves less (about 60 to 80 per framework it keeps). `disable-model-invocation` has a cost: Claude
can no longer start those three skills from a plain-language request ("update the harness"); the operator types the
command. `ESSENTIALS.md` (35 % of the load) is already capped by `check-framework.py` and is out of this issue.

## 3. Proposed follow-ups (for the orchestrator to file after the operator's go)

One `type: feature` issue per "yes", each naming the row it would retire (to `mechanical, enforced by <check>`):

1. `guard-git.py`: refuse branch-moving git commands from reviewer subagents and commits on a detached HEAD
   (retires L83).
2. Zero-tests guard for filtered test runs in `local-check.sh` and the CI templates (retires L72, the last clause of
   L01).
3. Warn on default-branch-only workflows, issue forms or Dependabot config changed on a PR to another base
   (retires L50).
4. Toolchain pin parity between the cloud setup script and CI (retires L59).
5. Private repository using GHAS-only actions (retires L52).
6. Linux-unavailable Foundation APIs grep rule for Swift projects (retires L64).
7. XcodeGen project regeneration diff for projects on that strategy (retires L74; first verify XcodeGen on Linux).

Context cost (`type: feature` unless noted):

1. `harness-sync.sh`: vendor a compliance agent (and `/compliance-review`, `compliance-reviewer`) only when
   `.harness/config.json` › `compliance` enables it; up to ~750 tokens per session.
2. Shorten the five longest descriptions (`compliance-review`, `readme-update`, `local-check`, `lot-finish`,
   `doc-steward`), and add a description length limit to `check-framework.py` (`type: chore`); ~200 tokens.
3. `disable-model-invocation: true` on `harness-update`, `feedback-triage`, `status-report` (operator decision on
   the trade-off above); ~190 tokens.
4. Verify in a session whether the user-scope plugin duplicates the skill listing in an adopted project; if so,
   document disabling it per project in ADOPTION (`type: chore`).

The "Overlap" column goes to #114 as input, unchanged.
