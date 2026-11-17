# Identity: look and voice

One look and one voice across the README, the social preview, every post, carousel and diagram, so that a reader
recognises Belayline at a glance and the figures can be trusted. An identity is worked on step by step: it may evolve,
but when it does, everything listed under [When the identity changes](#when-the-identity-changes) moves together.

> **Status (2026-11-17): under review.** Two registers coexist and do not agree yet (below). A design-language analysis
> and a choice of direction are pending; until then, covers and brand assets use the brand register, explanations and
> diagrams the diagram register, and no new register is introduced.

## The two registers in use

| | Brand register | Diagram register |
|---|---|---|
| Where | README banner, GitHub social preview, launch carousel ([2026-11-launch](posts/2026-11-launch/README.md)) | Diagrams of the docs (`docs/diagrams/`), draft carousel ([2026-11-software-factory](posts/2026-11-software-factory/README.md)) |
| Background | Navy gradient `#10182c` → `#202c48` | White |
| Type | Inter (system sans-serif fallback) | Excalifont, the hand-drawn font of Excalidraw (OFL); not committed, the renderer takes it from the Excalidraw package |
| Accents | Cyan `#42d5e3` (also `#3aa3b6`, `#2b6f8c`), amber `#e8a94e`, off-white text `#f5f0e6`, muted `#8aa0c0` | One colour per meaning (table below), pastel hachure fills |
| Motif | A compass with a dashed amber trajectory between waypoints | Hand-drawn boxes, arrows and scenes (the layers, the motorway) |
| Sources | `docs/assets/banner.svg`, `docs/assets/social-preview.svg` | `docs/diagrams/*.excalidraw` with their stamped `.svg` |

Known contradictions: the background (navy vs white), the type (Inter vs Excalifont), and the colours (cyan and amber
carry the brand in one register; in the other, orange means a person and blue means agents).

### Colour code of the diagram register

In this register every colour means the same thing, in every diagram and slide. Stroke, then pale fill.

| Meaning | Stroke | Fill | Used for |
|---|---|---|---|
| A person: operator, intent, presentation | `#f08c00` | `#fff3bf` | the operator, the intent, where you talk to an AI |
| Agents | `#1971c2` | `#a5d8ff` | lot agents, reviewers, the agent layer; "opened" in charts |
| Execution and the repository | `#2f9e44` | `#b2f2bb` | where work runs, the repository, on-ramps; "merged" in charts |
| Checks and cost: CI, measure | `#e8590c` | `#ffd8a8` | CI, tolls, the dashboard, upkeep |
| Inference | `#0c8599` | `#c3fae8` | the model layer, convoys (lots), code growth |
| Decisions and arbitration | `#6741d9` | `#d0bfff` | the orchestrator, roadmap signs, drift, contributor counts |
| Exit, risk, waiting | `#e03131` | `#ffc9c9` | merge, the review queue, what is stuck |
| Context | `#868e96` | none (dashed) | kickers, notes, side boxes |
| Text | `#1e1e1e` | | body text |

## Formats

| Format | Size | File |
|---|---|---|
| Carousel (LinkedIn "document") | 1080 × 1350 px pages (the launch used 1125 × 1407), 6 to 10 slides, PDF; a document title under ~30 characters | `carousel.pdf`, plus `carousel-cover.png` |
| Single image | 3000 px wide PNG | `<topic>.png` |
| Social preview of the repository | 1280 × 640 PNG, under 1 MB | `docs/assets/social-preview.png` (checked by `check-framework.py`) |
| README banner | SVG with a PNG fallback | `docs/assets/banner.svg`, `.png` |

## When the identity changes

Change these together, in one PR, and add a line to the history below:

1. `docs/assets/banner.svg` and `.png` (README header).
2. `docs/assets/social-preview.svg` and `.png` (GitHub › Settings › Social preview: upload it again by hand).
3. This file: registers, palette, type, motif, formats.
4. The templates or generators of posts and carousels, and the next post; published posts stay as they were.
5. Diagrams only if the diagram register itself changes (then re-export every `docs/diagrams/*.svg`).

## Voice

- **Every figure has a source and a date** in the post's `README.md` (query, command, window). A figure that cannot be
  re-measured is not posted. Prefer a defensible number to a large one (net lines of code, not gross lines added).
- **No name of a client, employer or private project.** Open-source projects may be named, with a neutral framing:
  their maintainers are not the subject, throughput is.
- No star counts, no "10×", no adoption claim the repository cannot show. Say "I use it" only for what is true.
- Plain words, short lines. Emojis only as markers (`→`, `🚧`, `🔗`), never decorative.
- End with one question to the reader and the repository link.
- Posts in English unless the audience is French-speaking; the post's folder keeps every language it was published in.

## Folder of a post

`communication/posts/YYYY-MM-<topic>/` with `README.md` (status, files, the text as published or ready to paste,
slide-by-slide text, sources and method of the figures, then the date, the link, the results and a short review once
published), the carousel and the images. One row in [the index](README.md).

## History

| Date | Change |
|---|---|
| 2026-11 (0.3.0 → 0.4.0) | Brand register: navy banner and social preview with the compass |
| 2026-11-11 | Launch carousel in the brand register |
| 2026-11-17 | Diagram register written down; both registers recorded; direction under review |
