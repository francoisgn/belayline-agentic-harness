# Identity review, 2026-11-17

Design-language analysis of the three registers in use, made before choosing a direction ([identity](identity.md)).
Read-only review by an agent on the frontier tier; inputs: `docs/assets/banner.svg`, `social-preview.svg`, the launch
carousel ([2026-11-launch](posts/2026-11-launch/README.md)), its rendering in the LinkedIn feed, `docs/diagrams/*.svg`
and the draft white carousel ([2026-11-software-factory](posts/2026-11-software-factory/README.md)).

## Findings

| Register | LinkedIn | GitHub | "AI template" risk |
|---|---|---|---|
| Navy brand (banner, social preview) | Compass recognisable large; its 1 px strokes vanish small (logo chip) | Clean banner; small capitals at 10.5–11.5 px unreadable on a link card | Gradient and halo are the "dark tech" genre; the compass is the only own element |
| Launch carousel | Titles readable as thumbnails; kicker, footer and "SWIPE" unreadable; LinkedIn's title strip covers the logo; the compass takes ~45 % of page 1 and says nothing | n/a | Same template on 8 pages; "X. / Y." two-colour title on every page |
| White sketch (diagrams, draft carousel) | White readable, big numbers work; a landscape diagram shrunk into a portrait page is unreadable on a phone; paragraphs in Excalifont tire | `mechanisms` and `cycle` readable in the README | Low, but it is everyone's Excalidraw look: credible to engineers, not distinctive, less assured for managers |

Contradictions: background (the old style guide said "white, always"; banner, preview and the published carousel are
navy); type (Inter vs Excalifont, no rule); amber means the agent's path in the banner, a person in the diagram code,
"problem" or "step number" or "check" in the carousel; cyan is the brand in one register and "inference" in the other;
the draft uses orange for emphasis (it means "checks and cost") and blue for "Belayline" (it means "agents");
`factory-motorway.svg` colours tests in blue and rules in orange, against the table; the compass is absent from the
white register, the motorway absent from the brand.

## Three directions

| | A. Two layers | B. All paper | C. All navy |
|---|---|---|---|
| Principle | Navy signs, white explains | White everywhere, the brand reduced to an ink mark | One dark skin |
| Palette | Navy `#10182c`/`#202c48`, cyan `#42d5e3`, amber `#e8a94e`, text `#f5f0e6`, outside the colour code; on white: the diagram code only, ink `#1e1e1e` | White, ink `#10182c`, one accent `#0c8599`, plus the diagram code | Current palette plus the seven meanings re-tinted for a dark background |
| Type | Inter for titles and body on both; Excalifont in diagrams and big numbers | Excalifont titles and diagrams, Inter body | Inter only |
| Motif | Large compass on navy; simplified compass chip (2 rings, needle, strokes ≥ 3 px) on white pages | Compass redrawn by hand | Compass and grid |
| Carousel | First and last pages navy, no halo or grid; pages in between white: Inter title, one diagram or at most 4 numbers, chip bottom left | Like the draft, with a mark | Like the launch, diagrams dark |
| Banner, preview | Kept; fix the small capitals, lighten the halo | Redone in white | Unchanged |
| Diagrams | Unchanged; fix `factory-motorway.svg` | Ink `#10182c` | All 13 SVGs redrawn |
| Effort | 🟢 low | 🟠 medium | 🔴 high |
| Risks | 🟠 two styles if the rules are not held | 🔴 loses the navy already known; a white banner is harsh in GitHub's dark theme; identity confused with Excalidraw | 🔴 against the owner's taste for white; maximises the "dark tech" effect |

Rules of use for A: navy for the README banner, the social preview, the first and last carousel pages and a standalone
announcement image (name, promise, link; never a diagram or a figure; cyan and amber decorative, without meaning).
White for every page that explains: diagram, figures, comparison, table (no gradient; brand cyan and amber forbidden;
one colour = one meaning, no free emphasis).

**Recommendation: A.** It keeps what is published and recognised, respects the preference for white, redraws nothing,
and is the only one that can evolve by steps (template and identity file first, the chip next, the banner retouch last,
each step shipped together). It limits the dark rendering to two pages per carousel. Open point for the owner: Inter
for titles on white pages, which takes the titles away from Excalifont.

## Fixes for the next carousel, whatever the direction

1. Document title: the feed showed 30 characters ("Keep coding agents on track: a"); put the subject in the first 30.
2. Page 1: keep the top left free (covered by LinkedIn's title strip); move the title up.
3. A Belayline mark on every page.
4. Never shrink a landscape diagram into a portrait page: crop it into 2 or 3 zoomed pages or make a portrait variant.
5. No useful text under ~28 px on 1080; drop "SWIPE" and the repeated footer.
6. One idea per page, body text at most two lines.
7. Colours: no free emphasis colour; fix `factory-motorway.svg` before publishing it.
8. At most one "X. / Y." title per carousel.

Not checked: the draft's real rendering in the feed (only the navy carousel has a screenshot); some draft slides and
two diagrams were read from their source, not as images.
