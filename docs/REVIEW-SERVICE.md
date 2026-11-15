# Review service: the in-house equivalent of CodeRabbit

Definition of the harness's automatic PR review service: the **code** review ("is the code correct and clean?",
input = the diff). It **complements** the session's adversarial review, the **intent** review
([ORCHESTRATION](ORCHESTRATION.md) §3, [REVIEW-ROUNDS](REVIEW-ROUNDS.md) §The two reviews), and does not replace it. Implementation: reusable workflow
`.github/workflows/ai-review.yml` (action `anthropics/claude-code-action`, pinned by SHA).

## 1. Service contract

| Item | Definition |
|---|---|
| Trigger | **Ready** PR (`ready_for_review`, then `synchronize`); never a draft; project-local label `review: skip` → skipped |
| Inputs | Diff `base...head`, `CLAUDE.md`, `ESSENTIALS.md`, `LESSONS.md`, project instructions (`.harness/review-instructions.md`); the issue intent is the adversarial review's input, not this one's |
| Output | **One** review comment per head: verdict `APPROVED` / `CHANGES REQUESTED`, numbered findings (High / Medium / Low / Nit, `file:line`, failure scenario, fix), "Verified" list |
| Rights | Read the code; a PR **comment** only (`gh pr comment`), never a GitHub review: it cannot approve, even under prompt injection. No commit, no push, no merge |
| Model | Tier ≥ the issue's, **other** than the author if possible; default: solid; frontier for risky flows |
| Secrets | `ANTHROPIC_API_KEY` or `CLAUDE_CODE_OAUTH_TOKEN` (repository or organisation secret) |
| Forks | No secret → job skipped; this is why the check is **never required** in the ruleset |
| Cost | 1 Linux job + the tokens of one review; cancelled by a new push (`concurrency`); bounded turns |

## 2. What sets it apart from a generic bot
- It judges against **our** rules: lessons (`L..`), conventions, definition of done, cited sources, CI budget.
- It does not comment on style that a linter catches, and groups the cases of one class (fewer rounds).
- An exploitable flaw is never detailed publicly.
- Its findings follow [REVIEW-ROUNDS](REVIEW-ROUNDS.md) like CodeRabbit's: a claim to verify, one commit
  per round, one reply per thread.

## 3. Optimising rounds (agentic volume)
A repository where agents push most of the commits multiplies reviews. Levers, from most to least effective:
1. **Prevent**: `/lessons-check` and the adversarial review **before** "Ready"; the service must find only what
   escaped both. A finding already in LESSONS = the self-review needs tightening.
2. **One review per ready head**, not per push: frequent pushes to the draft while working (no review), one push per
   round once it is ready. CodeRabbit's defaults review every push: the harness seeds settings that do not
   ([§5](#5-coderabbit-in-a-harness-project)).
3. **Incremental review**: on the next round, instruct it to review only `last-reviewed-sha...head` (the service reads
   its previous review).
4. **Bound**: a round with no finding on the current head ends the loop; beyond 3 rounds, the orchestrator stops it
   ([FINOPS](FINOPS.md) §3). Settled findings are listed in the PR and not reopened without new evidence.
5. **Grade**: project-local label `review: skip` for trivial PRs (patch Dependabot, typo), frontier model only
   on the labels `type: security`, `difficulty: medium` or `difficulty: hard`.

## 4. Setting it up in a project
1. Secret `ANTHROPIC_API_KEY` (or Claude Code OAuth token); Claude GitHub app installed by the owner (L57).
2. In `.github/workflows/harness.yml`, enable the `review` job (commented template).
3. Optional: `.harness/review-instructions.md` (rules per directory, like CodeRabbit's `path_instructions`).
4. If CodeRabbit stays installed: keep both for a while, compare the relevant findings over 10 PRs, then
   keep only one (do not pay twice).

## 5. CodeRabbit in a harness project
CodeRabbit's defaults break "one review per ready head": `reviews.auto_review.auto_incremental_review` defaults to
`true` ("Re-run the review on each push") and `auto_pause_after_reviewed_commits` to `5`. Below 10 stars it does not
review on its own at all ("does not receive automatic reviews because it has fewer than 10 stars", ezzz/HFRnow#906);
a `@coderabbitai review` comment starts one.

**Seeded settings.** The sync creates `.coderabbit.yaml` from `templates/.coderabbit.yaml` when it is missing and
never rewrites it (`seed` in `harness.manifest`). Keys, as the
[configuration reference](https://docs.coderabbit.ai/reference/configuration) states them (read 2026-11-15):

| Key | CodeRabbit default | Seeded | Meaning (quoted) |
|---|---|---|---|
| `language` | `en-US` | `en-US` | "Set the language for reviews by using the corresponding ISO language code." Set the project's |
| `reviews.auto_review.enabled` | `true` | `true` | "Review PRs automatically." |
| `reviews.auto_review.drafts` | `false` | `false` | "Include draft PRs." |
| `reviews.auto_review.auto_incremental_review` | `true` | `false` | "Re-run the review on each push." |
| `reviews.auto_review.auto_pause_after_reviewed_commits` | `5` | `2` | "Pause automatic reviews after this many reviewed commits since the last pause. Set to 0 to disable." A backstop if incremental review is turned back on |

`@coderabbitai review` "Reviews the commits pushed since CodeRabbit's last review of the pull request" and "Works
whether or not automatic reviews are enabled for the repository"
([review commands](https://docs.coderabbit.ai/reference/review-commands), read 2026-11-15).

**Who asks for the review of a later head.** `.harness/config.json` › `coderabbit.agent_requests_review`, default
`false`; an operator turns it on for the repositories where agents may post the request themselves (operator
decision, 2026-11-15). On, `/review-round` posts `@coderabbitai review` followed by `Head: <sha>` itself, and only
when all hold: the PR is ready (never a draft); CodeRabbit has no review of that head; no comment already asks for
that head. At most one request per head SHA: if the bot stays silent after it, the round falls back as
[REVIEW-ROUNDS](REVIEW-ROUNDS.md) §The two reviews says, and never posts again for that head (no loop). A request
whose mention came out altered (cloud session, LESSONS L46) does not count: the operator posts it. Off, the agent
asks the operator to post it, as before.

**Draft to ready: to verify.** Neither page above says whether CodeRabbit reviews a PR when it moves from draft to
ready with these settings, and CodeRabbit skips this harness's repository, so it was not tested here. Test it once
on a real PR of a project with the seeded `.coderabbit.yaml` and write the result here:
1. Open a PR as a draft and push one commit: CodeRabbit must not review (`drafts: false`).
2. Mark it "Ready for review" without pushing, wait 10 minutes: note whether CodeRabbit reviews that head.
3. Push one more commit to the ready PR, wait 10 minutes: note whether it reviews it (expected: no, incremental
   review off). If step 2 gave no review, `@coderabbitai review` is the way to get the first one, as for later heads.
