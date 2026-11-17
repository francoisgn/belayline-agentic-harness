# Posts: visual and editorial style

One look and one voice across every post, carousel and visual, so that a reader recognises Belayline at a glance and
the figures can be trusted. Applies to everything under `docs/posts/`. The diagrams of the docs follow the same palette.

## Look

- **White background**, always. No gradient, no photo, no logo other than the repository's own banner.
- **Font: Excalifont**, the hand-drawn font of Excalidraw (OFL), for slides and diagrams. Not committed: the renderer
  takes it from the Excalidraw package. Fallback: a plain sans-serif, never a serif.
- **Diagrams** come from the common Excalidraw scene in `docs/diagrams/` (`.excalidraw` + stamped `.svg`); a post uses a
  PNG render of the committed SVG, never a redrawn copy.
- **One idea per slide or image.** Big numbers (about 110 px on a 1080 px slide), short labels under them, at most four
  numbers on a slide.
- Grey kicker line at the top (context: project, period), slide counter `n/N` at the bottom right.
- Cards: 4 px border in the colour of their meaning, 24 px corner radius, no fill or a pale fill.

## Colour code

Every colour means the same thing in every post and diagram. Stroke, then pale fill.

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
| Carousel (LinkedIn "document") | 1080 × 1350 px pages, 6 to 10 slides, PDF | `carousel.pdf`, plus `carousel-cover.png` |
| Single image | 3000 px wide PNG, white background | `<topic>.png` |
| Social preview of the repository | 1280 × 640 PNG, under 1 MB | `docs/assets/social-preview.png` (checked by `check-framework.py`) |

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

`docs/posts/YYYY-MM-<topic>/` with `README.md` (status, files, the text ready to paste, slide-by-slide text, sources
and method of the figures, and the date and link once published), the carousel and the images. One row in
[the index](README.md).
