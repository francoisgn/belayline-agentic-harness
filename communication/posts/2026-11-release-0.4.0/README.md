# LinkedIn, November 2026: Belayline 0.4.0

Status: **ready to publish**. Author: the operator. First carousel in [direction A](../../identity.md).
LinkedIn document title: `Belayline 0.4.0: agent harness` (30 characters).

| File | What |
|---|---|
| [`carousel.pdf`](carousel.pdf) | Carousel, 10 pages, 1080 × 1350: navy cover and close, white pages in between |
| [`carousel-cover.png`](carousel-cover.png) | Page 1, as a preview |

## The post (paste as is)

```text
Belayline 0.4.0 is out: a free, open-source harness to run coding agents like a team, from your repository.

Try it in one prompt. Ask your agent: "Check Belayline and take what is useful for me." It reads the harness, installs what fits your project, pinned to a version, and every rule can be switched off.

What it covers, end to end:
- bootstrap: AGENTS.md rules, labels, issue and PR templates, a living README, one local check that replays the CI
- CI and security: nothing costly on drafts, a timeout on every job, secrets and dependencies scanned
- the loop: intent, ready issue, claim, tests first, a review by another model, merge gate, measure, lesson
- collaboration: many agents, many developers, many models, on the same issues and pull requests
- less waste: bounded review loops, no pushing to see if the CI passes, the model each task needs

It is not tied to one company's playbook. It takes the best ideas and works differently:
- Google's Elephant–Goldfish Model brought the fresh-context reviewer. Belayline keeps it, and puts the context in the repository, shared by every agent and every developer, instead of in one assistant.
- Anthropic's Claude Code advisor escalates hard decisions to a stronger Claude model. Belayline picks a model per task from any provider, and its reviewer never reads the author's reasoning.

Built from years of running platforms and products, and tested on real work: LightCraft, an open-source project with 113 contributors and 1,412 pull requests in the last 30 days; iOS apps; corporate projects in a group of 100,000 people and 15,000 developers.

What should a harness enforce on your agents that nothing enforces today?

github.com/francoisgn/belayline-agentic-harness

#AgenticAI #OpenSource #PlatformEngineering
```

## The carousel, page by page

The post and the carousel tell the same story in the same order.

1. (navy) Run coding agents like a team, from your repository. Not a model, not a vendor's playbook. The contents of
   the next pages, numbered.
2. Try it in one prompt: "Check Belayline and take what is useful for me."; the agent reads the harness, installs
   what you keep (pinned, overrides listed), you stay in charge; any agent that reads AGENTS.md.
3. End to end, from an empty repository to merged work: bootstrap, CI and security, collaboration, delivery.
4. The loop, ten steps: intent, ready issue, claim and branch, lot in TDD, adversarial review, compliance review,
   ready PR and CI, merge gate, measure, lesson; bounded loops.
5. Many agents, many developers, many models.
6. Where agent work burns money, and the guard for each (seven rows).
7. Versus Google: Elephant–Goldfish Model (github.com/google/elephant-goldfish-model, Apache 2.0, "not an officially
   supported Google product"): what it does, what we keep, what Belayline does differently.
8. Versus Anthropic: Claude Code advisor (code.claude.com/docs/en/advisor, github.com/anthropics/claude-code): same.
9. Where it is tested: 113 contributors and 1,412 pull requests on LightCraft in 30 days; iOS apps; corporate
   projects.
10. (navy) Start your next project by asking your agent; link.

No third-party logo: Google's and Anthropic's names are set in type, with their links (their trademark guidelines
restrict the use of their logos).

Rendered with [`carousel-direction-a.py`](../../templates/carousel-direction-a.py) (`python3 carousel-direction-a.py
out.html docs/assets/social-preview.svg`, then print `out.html` to PDF at 1080 × 1350 with a headless browser).

## Figures and claims

| Claim | Source |
|---|---|
| 3 review rounds, 6 CI-tested pushes | `docs/FINOPS.md` §3 |
| A timeout on every CI job; dashboard signals | `scripts/job-timeout.py`, `docs/FINOPS.md` §4 (0.4.0) |
| LightCraft: 113 contributors, 1,412 pull requests in 30 days | 113 distinct commit authors; 1,412 PRs opened (GitHub search) on `storytold/lightcraft` `main`, 2026-10-17 → 2026-11-16 ([2026-11-software-factory](../2026-11-software-factory/README.md)) |
| A group of 100,000 people and 15,000 developers | The operator's employer, as stated by the operator; the employer is not named |
| Claude's advisor pairs two Claude models in one conversation | code.claude.com/docs/en/advisor, read 2026-11-17 |
| Elephant–Goldfish: the elephant keeps the context and drafts; goldfish reviewers have no earlier conversation; Apache 2.0; not an officially supported Google product | github.com/google/elephant-goldfish-model, README read 2026-11-17 |
