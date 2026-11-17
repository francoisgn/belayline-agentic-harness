# Identity: look and voice

One look and one voice across the README, the social preview, every post, carousel and diagram, so that a reader
recognises Belayline at a glance and the figures can be trusted. An identity is worked on step by step: it may evolve,
but when it does, everything listed under [When the identity changes](#when-the-identity-changes) moves together.

> **Direction A, "two layers" (decided by the operator on 2026-11-17).** The navy brand signs, the white page
> explains. Inter is the type of both. Analysis and alternatives: [identity-review-2026-11-17.md](identity-review-2026-11-17.md).

## Rules of use

| | Navy (brand layer) | White (explanation layer) |
|---|---|---|
| Where | README banner, GitHub social preview, the first and last pages of a carousel, a standalone announcement image | Every page that explains: diagram, figures, comparison, list |
| Says | The name, the promise, the link. Never a diagram or a figure | One idea per page; at most four numbers; body text at most two lines per item |
| Colour | Navy gradient, cyan `#42d5e3` and amber `#e8a94e`, decorative, without meaning | The colour code below, one colour = one meaning; brand cyan and amber are never used; no free emphasis colour |
| Type | Inter 800 titles, Inter body, off-white `#f5f0e6` | Inter 800 titles in navy ink `#10182c`, Inter body `#1e1e1e`; Excalifont only inside diagrams |
| Mark | The compass, large, from `docs/assets/social-preview.svg`; no halo or grid behind text | The compass chip (two rings and a needle, navy ink, strokes of 3 px) and "Belayline" bottom left, page number bottom right |

Carousel checklist: the subject in the first 30 characters of the LinkedIn document title; the top left of page 1
left free (LinkedIn lays its title strip there); no useful text under ~28 px on a 1080 px page; never a landscape
diagram shrunk into a portrait page (crop it into zoomed pages, or make a portrait variant); at most one two-colour
"X. / Y." title per carousel. Template: [`templates/carousel-direction-a.py`](templates/carousel-direction-a.py)
(standard library; it writes the HTML, a headless browser prints it to PDF; see its use in
[2026-11-release-0.4.0](posts/2026-11-release-0.4.0/README.md)).

## The two registers

| | Brand register | Diagram register |
|---|---|---|
| Where | README banner, GitHub social preview, launch carousel ([2026-11-launch](posts/2026-11-launch/README.md)) | Diagrams of the docs (`docs/diagrams/`), draft carousel ([2026-11-software-factory](posts/2026-11-software-factory/README.md)) |
| Background | Navy gradient `#10182c` → `#202c48` | White |
| Type | Inter (system sans-serif fallback) | Excalifont, the hand-drawn font of Excalidraw (OFL); not committed, the renderer takes it from the Excalidraw package |
| Accents | Cyan `#42d5e3` (also `#3aa3b6`, `#2b6f8c`), amber `#e8a94e`, off-white text `#f5f0e6`, muted `#8aa0c0` | One colour per meaning (table below), pastel hachure fills |
| Motif | A compass with a dashed amber trajectory between waypoints | Hand-drawn boxes, arrows and scenes (the layers, the motorway) |
| Sources | `docs/assets/banner.svg`, `docs/assets/social-preview.svg` | `docs/diagrams/*.excalidraw` with their stamped `.svg` |

Direction A resolves the contradictions found on 2026-11-17: each background has its role, Inter is shared, and the brand
cyan and amber stay on navy while the colour code stays on white.

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
| 2026-11-17 | Diagram register written down; both registers recorded; identity review |
| 2026-11-17 | Direction A decided; Inter shared; banner and social preview: small capitals enlarged (15 and 17 px), halo lightened |
