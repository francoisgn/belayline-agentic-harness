# LinkedIn, November 2026: Belayline 0.4.0

Status: **ready to publish**. Author: the operator. First carousel in [direction A](../../identity.md).
LinkedIn document title: `Belayline 0.4.0: agent harness` (30 characters).

| File | What |
|---|---|
| [`carousel.pdf`](carousel.pdf) | Carousel, 8 pages, 1080 × 1350: navy cover and close, white pages in between |
| [`carousel-cover.png`](carousel-cover.png) | Page 1, as a preview |

## The post (paste as is)

```text
Belayline 0.4.0 is out. It is the harness I use to run coding agents on real projects, and it is free.

What it sets up in your repository:
- a repo ready for agents: AGENTS.md, labels, issue and PR templates, a CI that runs only when needed
- a loop: intent first, tests first, a review by another model, then merge
- collaboration between agents: claims on issues, a ledger, an orchestrator that gives each task to the right model
- upkeep: stewards for the docs and the issues
- less waste: bounded review loops, a timeout on every CI job, a dashboard that shows stuck runs and flaky jobs

Two choices make it different.
The context lives in the repository, not inside one long-running agent. Google's Elephant–Goldfish model keeps it in the "elephant"; here every agent and every person reads the same issues and pull requests.
Each task gets the model it needs, from any provider. Claude's new advisor pairs two Claude models in one conversation; Belayline routes each task to a model and has the work reviewed by a different one, ideally from another vendor.

I built it from years of running platforms and products, and I test it on real work: LightCraft, an open-source project with more than 100 contributors; iOS apps; corporate projects in a group of 100,000 people and 15,000 developers.

To try it, start your next project by asking your agent: "Check Belayline and take what is useful for me."

What should a harness enforce on your agents that nothing enforces today?

github.com/francoisgn/belayline-agentic-harness

#AgenticAI #OpenSource #PlatformEngineering
```

## The carousel, page by page

1. (navy) Belayline 0.4.0 · free · open source · MIT. A harness for coding agents, in your repository.
2. Your repository, ready for agents: rules every agent reads; labels and templates; a CI that runs when needed.
3. One loop for every change: intent, tests first, review by another model, merge; lessons feed the next intent.
4. Agents that work together: one agent per task (claims, ledger); the right model for each task, from any provider;
   stewards keep the docs and the issues true.
5. Less waste: 3 review rounds at most, 6 CI-tested pushes at most, a timeout on every CI job, a dashboard that
   flags stuck runs and jobs that pass only on a re-run.
6. Two choices that make it different: context in the repository (vs Elephant–Goldfish), a model per task from any
   provider (vs Claude's advisor).
7. Tested on real work: LightCraft, iOS apps, corporate projects; built from years of running platforms and products.
8. (navy) Try it: "Check Belayline and take what is useful for me." Link.

Rendered with [`carousel-direction-a.py`](../../templates/carousel-direction-a.py) (`python3 carousel-direction-a.py
out.html docs/assets/social-preview.svg`, then print `out.html` to PDF at 1080 × 1350 with a headless browser).

## Figures and claims

| Claim | Source |
|---|---|
| 3 review rounds, 6 CI-tested pushes | `docs/FINOPS.md` §3 |
| A timeout on every CI job; dashboard signals | `scripts/job-timeout.py`, `docs/FINOPS.md` §4 (0.4.0) |
| LightCraft, more than 100 contributors | 113 distinct commit authors on `storytold/lightcraft` `main`, 2026-10-17 → 2026-11-16 ([2026-11-software-factory](../2026-11-software-factory/README.md)) |
| A group of 100,000 people and 15,000 developers | The operator's employer, as stated by the operator; the employer is not named |
| Claude's advisor pairs two Claude models in one conversation | code.claude.com/docs/en/advisor, read 2026-11-17 |
| Elephant–Goldfish keeps the context in the "elephant" | the launch carousel, page 5 ([2026-11-launch](../2026-11-launch/README.md)) |
