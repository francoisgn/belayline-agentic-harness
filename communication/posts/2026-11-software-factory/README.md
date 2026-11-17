# LinkedIn, November 2026: the software factory as a motorway

Status: **draft**, not published; its white sketch carousel waits for the identity decision ([identity](../../identity.md)). Author: the operator. Figures as of **2026-11-16**: re-measure them
(below) if the post goes out later.

| File | What |
|---|---|
| [`carousel.pdf`](carousel.pdf) | Carousel, 8 slides, 1080 × 1350 (LinkedIn "document" post) |
| [`carousel-cover.png`](carousel-cover.png) | Its first slide, as a preview |
| [`motorway.png`](motorway.png) | The motorway picture, 3000 px wide (source: [`factory-motorway`](../../../docs/diagrams/factory-motorway.svg)) |
| [`ai-layers.png`](ai-layers.png) | The four layers of AI, 3000 px wide (source: [`ai-stack`](../../../docs/diagrams/ai-stack.svg)), for a later post |

## The post (paste as is)

```text
Coding agents are self-driving cars. They only work on a clean road.

I contribute to LightCraft, an open-source, clean-room alternative to Lightroom, written in Rust and built with coding agents.
Over the last 30 days:
→ 1,412 pull requests opened, 671 merged
→ 113 contributors
→ the code grew from 304,000 to 384,000 lines of Rust (174,000 in early October)
→ 910 pull requests are waiting for review, 607 of them for more than two weeks

Week after week, merges went 249, then 217, 112, 51. Code arrives faster than anyone can read it.

This is not a maintainer problem. It is a throughput problem, and the whole software factory has to be rethought. Writing code is no longer the bottleneck. The bottleneck is:
🚧 on-ramps: identities, tokens and accounts built for people, not for a hundred agents a day
🚧 tolls: CI on every push, and macOS minutes that cost ten times Linux
🚧 exits: human review that cannot keep the pace

The road needs signs set by a human (the roadmap, the intent of each lot), automatic radar, manual police (adversarial review, arbitration) and upkeep.

I see the same jams on my professional projects. That is what I am tooling with Belayline, an open-source harness I use every day, on personal and professional projects. The picture and the full software factory guide are in the repo.

Do you see the same jam where you work? Where?

🔗 github.com/francoisgn/belayline-agentic-harness
```

## The release update (paste as is)

```text
Belayline 0.4.0 is out.

Belayline is an open-source harness for building software with coding agents (Claude Code, Codex, Cursor…). Not a framework: a method, guardrails and tools, versioned, that you add to any repository.

In this release:
→ intent written before the code, an adversarial review by a different model, bounded loops (3 review rounds at most)
→ CI that runs only when it is useful, with a timeout checked on every job
→ a dashboard that flags tests passing only on a re-run, and stuck runs
→ lessons from real projects, with a rule to retire the ones that no longer help
→ a 7-part guide: why the software factory must be rethought when agents write the code

Full changelog in the release. Feedback welcome.

🔗 github.com/francoisgn/belayline-agentic-harness/releases/tag/v0.4.0
```

## The carousel, slide by slide

1. Coding agents are self-driving cars. They only work on a clean road.
2. LightCraft, 30 days (Oct 17 → Nov 16): 1,412 pull requests opened, 671 merged, 113 contributors, 304K → 384K
   lines of Rust.
3. Pull requests per week: opened 462, 387, 258, 186; merged 249, 217, 112, 51. The queue grows every week.
4. The queue: 910 pull requests waiting for review, 607 for more than two weeks. Not a maintainer problem, a
   throughput problem.
5. The motorway picture.
6. Writing code is no longer the bottleneck: on-ramps, tolls, exits.
7. What the road needs: signs set by a human, radar, police, upkeep.
8. Belayline: an open harness for building software with coding agents; used every day on personal and professional
   projects; link.

The PDF was rendered from HTML with the repository's hand-drawn font (Excalifont) by a script kept outside the
repository (no dependency here). To change it: edit the slide text above, then ask an agent to re-render it.

## Figures: sources and method

Repository `storytold/lightcraft`, window 2026-10-17 → 2026-11-16.

| Figure | How it was measured |
|---|---|
| 1,412 PRs opened, 671 merged | GitHub search API: `is:pull-request created:` / `is:merged merged:` over the window |
| 910 waiting, 607 older than 14 days | GitHub search API: `is:pull-request is:open`, and `created:<2026-11-02` |
| Weekly opened / merged | Same queries, one per week starting 2026-10-19, 10-26, 11-02, 11-09 |
| 113 contributors | Distinct commit authors on `main` (`git log --no-merges`); authors of unmerged PRs are not counted, so the real number is higher |
| 304K → 384K lines of Rust | Lines of the `*.rs` files in the tree of `main` on 2026-10-17 and 2026-11-16; 174K on 2026-10-09 |

Not used, on purpose: the gross "lines added" of the commits (about 3.1 million), inflated by the integration batches
that carry the same changes twice. No project of a client or employer is named.
