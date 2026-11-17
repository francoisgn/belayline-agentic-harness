# LinkedIn, November 2026: the launch of Belayline

Status: **published** around 2026-11-11 (LinkedIn showed "6 days" on 2026-11-17). Author: the operator. Format: text
post with an 8-page document (carousel). LinkedIn document title: "Keep coding agents on track: a…" (truncated in the
feed).

| File | What |
|---|---|
| [`carousel.pdf`](carousel.pdf) | The carousel as published: 8 slides, 1125 × 1407, navy brand (Inter, cyan and amber, compass) |

## The post, as published

The first word carries a typo ("I agents" for "AI agents"); kept as published.

```text
I agents now write code faster than any of us. Speed was never the hard part. Keeping them on track is. I've spent my career in production, where "it works on my machine" costs real money at 3 a.m.

This year, frontier models changed the game. In a few months I went from "useful autocomplete" to agents shipping whole features, on large open-source work: from a clean-room reimplementation of a product to the modernization of community apps nobody maintained anymore.

The leap is real. So is the drift: lost context, review loops that never end, CI burning minutes, tests that pass without the change.

And in my day job I keep seeing the same thing: developers left alone in front of an AI tool, with no method, no guardrails, and no way to see what it could really do for them.
So I wrote down what works, and open-sourced it: Belayline.

In 8 slides: → why runtime guards are not enough → the loop, from intent to lesson → why every change is reviewed by another model that never sees the author's reasoning → why the memory belongs in the repository, not in an expensive agent → and why "we approved tool X" says almost nothing for the people actually needing those tools.

Fresh-eyes review is having its moment: Google's Elephant–Goldfish Model makes the same split between author and reviewer. I've been running it on real projects for a few months, with one difference: the memory lives in the repo, not in a long-lived agent. Optimizing token consumption, avoid cold context rereading, ensure consistency and protect from compaction.

Open source, MIT, works with any coding agent that reads AGENTS.md. Repo and sources in the first comment. No engagement bait, no comment needed, no subscription to a newsletter subscription required.


#AgenticAI #SoftwareEngineering #OpenSource #DevEx #Harness
```

## The carousel, slide by slide

1. AI agents write fast. Who keeps them on track? An open harness for agentic development: a method, guardrails and
   checks, versioned in your repository.
2. The leap is real. So is the drift: lost context, review loops that never converge, CI burning minutes on trial
   pushes, tests that pass without the change, developers left alone with no method and no guardrails.
3. Guard the action. Govern the change: runtime guards ("may this command run now?") vs Belayline ("is this the change
   that was asked, proven, reviewed and measured?"). You want both.
4. From intent to lesson: the eight steps of the loop; loops bounded (3 review rounds, 6 CI-tested pushes).
5. Another model reviews, blind to the author: Elephant–Goldfish (Google) compared with Belayline.
6. The repository is the elephant: context in issues and PRs, agents replaceable, briefs not cold context, wake on
   events, the orchestrator conducts.
7. For managers: "We approved tool X" says almost nothing; one question per layer (presentation, agent, execution,
   inference).
8. Open source, built from real projects: any agent that reads AGENTS.md, Claude Code adapter, every block
   replaceable, MIT; link.

## Results

Snapshot on 2026-11-17 (LinkedIn, operator's screenshot, not kept here): 329 impressions, 8 reactions, 1 comment;
874 followers on the account. No later reading yet.

## Review (2026-11-17)

What worked:
- The opening idea ("speed was never the hard part; keeping them on track is") and the operator's production
  background are a real angle.
- The carousel is clean, consistent with the brand, one idea per slide title; slide 4 (the loop) and slide 3 (guard
  the action, govern the change) carry the message best.

What hurt:
- **Typo in the first word** ("I agents"), in the only two lines the feed shows before "…more".
- **Five topics in one post** (runtime guards, the loop, the reviewer, memory, managers): no single takeaway.
- **LLM cadence**, which readers now spot: "X was never the hard part. Y is."; "The leap is real. So is the drift.";
  arrow lists of five; triads. Several sentences sound generated rather than lived.
- **A broken sentence** ("Optimizing token consumption, avoid cold context rereading, ensure consistency and protect
  from compaction.") and a stutter ("no subscription to a newsletter subscription required").
- **Anti-call to action**: "no engagement bait, no comment needed" tells the reader not to react; the algorithm
  listens.
- **No proof**: no figure, no project named, no before/after. "Built from real projects" is asserted, not shown.
- **Carousel**: slides 4 to 7 are dense for a phone; the dark "tech template" look is clean but generic; the document
  title is cut in the feed.

For the next post: one idea, one proof with a figure, a human first line written by the author, a real question at
the end, a short document title (under ~30 characters), at most ~25 words per slide.
