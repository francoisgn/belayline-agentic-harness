# LinkedIn, November 2026: Claude Ship, and the road around review

Status: **ready to publish** (planned Thursday 2026-11-26, about 8:30–9:00 Paris time; links in the first comment,
the operator's choice). Author: the operator. Carousel in [direction A](../../identity.md), with Anthropic's
illustrations from its announcement (credited on each page; the operator cleared their use). LinkedIn document title:
`Claude Ship and Belayline` (25 characters). Teases the next post, [2026-11-software-factory](../2026-11-software-factory/README.md)
(the motorway).

| File | What |
|---|---|
| [`carousel.pdf`](carousel.pdf) | Carousel, 9 pages, 1080 × 1350: navy cover and close, white pages in between |
| [`carousel-cover.png`](carousel-cover.png) | Page 1, as a preview |

## The post (paste as is)

```text
On 23 November, Anthropic introduced Claude Ship, with one goal: "ship code as fast as teams write it". I think it is good news for everyone who delivers software.

I work on that gap every day: agents write code faster than a team can review and merge it.

Ship puts Claude on the pull request. Code Review is generally available, with review levels. PR Steward, in beta, fixes failing checks and merge conflicts. Claude Approvals, also in beta, "works like a smarter CODEOWNERS file", and Anthropic recommends starting in observe-only mode. Their figure: on the Claude Code team, merged pull requests "more than doubled" from June to September, while the share reverted fell by more than 40%.

With Anthropic's reach, I expect this to make delivery more reliable in many teams.

Review is one stretch of the road, though. Delivering fast also takes the intent written before the code, CI that can absorb the load, and, in a company, accounts, tokens and compliance rules built for people rather than agents. Ship does not cover that, nor does it claim to. More on that road in my next post.

The managed agents are for Team and Enterprise plans, on GitHub. If you don't have that subscription, or want to go further, my repository is open. Belayline (MIT) comes from my own projects. It works with any agent that reads AGENTS.md, starts at the issue, and has each change reviewed by another model than its author. The carousel puts both side by side.

Which of these checks would you hand to an agent first?

Links in the first comment.

#AgenticAI #OpenSource #ClaudeCode
```

## The first comment (paste as is)

```text
Anthropic's announcement, worth reading in full for the figures of their own team: https://claude.com/resources/articles/introducing-claude-ship

Belayline, my open-source harness, to read, pick from or adopt: https://github.com/francoisgn/belayline-agentic-harness
```

French:

```text
L'annonce d'Anthropic, à lire en entier pour les chiffres de leur propre équipe : https://claude.com/resources/articles/introducing-claude-ship

Belayline, mon harnais open source, à lire, à piocher ou à adopter : https://github.com/francoisgn/belayline-agentic-harness
```

"Read, pick from or adopt" are the three ways of use in `README.md` ("Read", "Pick", "Adopt"). Post the comment
right after the post, before sharing it.

## French version (secondary, same content)

```text
Le 23 novembre, Anthropic a présenté Claude Ship, avec un objectif : « ship code as fast as teams write it ». Je pense que c'est une bonne nouvelle pour tous ceux qui livrent du logiciel.

Je travaille sur cet écart tous les jours : les agents écrivent le code plus vite qu'une équipe ne peut le relire et le fusionner.

Ship installe Claude sur la pull request. Code Review est disponible pour tous, avec des niveaux de revue. PR Steward, en bêta, corrige les checks en échec et les conflits de fusion. Claude Approvals, en bêta aussi, « works like a smarter CODEOWNERS file », et Anthropic recommande de commencer en mode observation. Leur chiffre : dans l'équipe Claude Code, les PR fusionnées ont plus que doublé de juin à septembre, et la part de PR annulées a baissé de plus de 40 %.

Avec la portée d'Anthropic, je m'attends à ce que cela rende la livraison plus fiable dans beaucoup d'équipes.

La revue n'est qu'un tronçon de la route. Livrer vite demande aussi l'intention écrite avant le code, une CI qui absorbe la charge et, en entreprise, des comptes, des jetons et des règles de conformité pensés pour des personnes, pas pour des agents. Ship ne couvre pas cela, et ne le prétend pas. J'y reviens dans mon prochain post.

Les agents managés sont réservés aux offres Team et Enterprise, sur GitHub. Si vous n'avez pas cet abonnement, ou si vous voulez aller plus loin, mon dépôt est ouvert. Belayline (MIT) vient de mes propres projets. Il fonctionne avec tout agent qui lit AGENTS.md, part de l'issue et fait relire chaque changement par un autre modèle que son auteur. Le carrousel les met côte à côte.

Lequel de ces contrôles confieriez-vous en premier à un agent ?

Liens en premier commentaire.

#AgenticAI #OpenSource #ClaudeCode
```

Why a French version this time: the operator asked twice and writes in French, so part of his network is likely
French-speaking; this is a guess, not a measurement. English stays primary, as `identity.md` says. Post one or the
other, not both in the same week. The two quotes stay in English because they are Anthropic's words.

Length (counted by script, version 5): English post 1,574 characters; French post 1,750, both above the ~1,300
target since the "one stretch of the road" paragraph (LinkedIn's limit is 3,000); to shorten, cut the sentence with
Anthropic's figure (about 190 characters).

Notes for the operator:
- "I think it is good news", "I expect…", "I work on that gap every day" and "comes from my own projects"
  are your statements: keep them only if true as written. "I find it well designed" is dropped.
- No figure about Belayline, no "vs", no claim that Ship lacks anything. The only limit stated is the plan of the
  managed agents. `/ship` is not in the post (it is in the carousel's scope); so the post never implies that other
  plans have nothing.
- "The share reverted" is the brief's wording of Anthropic's figure; check the exact term on the announcement
  page before pasting, and adjust the French "annulées" to match.
- "23 November" is the publication date of the announcement, now sourced.

## The carousel, page by page

1. (navy) Claude now helps ship your pull requests. Good news: reach and reliability; next to Belayline, the
   open-source harness used for the same job. "Not a pitch: what each does, and what each leaves to you."
2. Three agents on your pull request: Anthropic's "How Claude Ship works" picture with its own disclaimer; the goal
   "ship code as fast as teams write it"; Team and Enterprise, GitHub; local `/ship` rolling out; Anthropic's own
   figure for its Claude Code team, labelled as theirs.
3. Review. Ship: Code Review (GA), multiple lenses, adversarially verified findings, Quick / Standard / Deep.
   Belayline: two reviews, a reviewer of another model in a fresh context against the issue's intent, a code review
   once per head, each verdict on the PR with its model.
4. Fix. Ship: PR Steward (beta) keeps the PR green, says what it changed and how to undo it, "@claude stop",
   designed not to approve or merge. Belayline: one commit per round, the class not the instance; 3 review rounds
   and 6 CI-tested pushes, then a human.
5. Approve. Ship: Claude Approvals (beta), "a smarter CODEOWNERS file", observe-only first, then a required check.
   Belayline: no approving bot; a merge gate (CI green, threads resolved, adversarial review approved on the head),
   then your merge policy.
6. Where it starts. Ship: at the pull request (`/ship`). Belayline: at the issue (intent, claim, lot in TDD); plan
   and progress live in issues and PRs.
7. Access and cost: who, cost, upkeep, side by side; the local `/ship` and `/steward` have no plan stated in the docs.
8. The gaps, both ways: what Ship does that Belayline does not (native and managed, review levels, a managed fixing
   agent and a required-check approval, reach); what Belayline adds (before the PR, a reviewer of another model,
   bounded loops and traced verdicts, any agent and replaceable blocks); both leave to you what to build and who may
   merge. Closing line: review is one stretch of the road; intent, CI capacity and, in a company, accounts, tokens and
   compliance built for agents; more in the next post.
9. (navy) On Team or Enterprise? Turn Claude Ship on. Want to go further, or on another setup? Belayline is there.
   Built from the operator's own experience; links in the first comment.

Images on pages 2 to 6: Anthropic, claude.com, announcement of 23 Nov 2026
(https://claude.com/resources/articles/introducing-claude-ship), credited on each page; cropped to leave out the
Claude logo; no customer logo. Belayline images: `docs/diagrams/cycle.svg`, `docs/diagrams/review-scanning.svg`,
the compass of `docs/assets/social-preview.svg`.

## Claims and sources

Anthropic's facts come from three pages, as verified and supplied by the coordinator on 2026-11-25 (not re-read by
this agent): the announcement https://claude.com/resources/articles/introducing-claude-ship (published 2026-11-23),
https://code.claude.com/docs/en/claude-ship.md and https://code.claude.com/docs/en/ship-command.md. Belayline: files
of the repository `Agentic-Harness`.

| Claim in the post | Source |
|---|---|
| Introduced on 23 November | Announcement, publication date 2026-11-23 |
| Goal: "ship code as fast as teams write it" | Announcement, quoted |
| Code Review is generally available, with review levels | Announcement; claude-ship.md |
| PR Steward is in beta and fixes failing checks and merge conflicts | Announcement; claude-ship.md (also acts on review feedback; "designed not to approve or merge") |
| Claude Approvals is in beta, "works like a smarter CODEOWNERS file" | Announcement, quoted; claude-ship.md (`.claude/approvals.yml`) |
| Observe-only mode recommended first | Announcement; claude-ship.md, setup section |
| Claude Code team: merged PRs "more than doubled" June to September; share reverted down by more than 40% | Announcement, Anthropic's own figure, attributed in the post; not re-measurable by us |
| Managed agents for Team and Enterprise plans, repositories on GitHub | Announcement; claude-ship.md |
| "I expect this to make delivery more reliable in many teams" | Operator's opinion, worded as an expectation |
| Belayline is open source, MIT | `LICENSE`; `README.md` §License |
| Written from the operator's own projects | `README.md` §Versions ("distilled from real projects"); `docs/POSITIONING.md` §2 (rules in use in SwiftHFR before packaging) |
| Works with any agent that reads AGENTS.md | `README.md` (AGENTS.md block, "read natively or to be enabled, depending on the tool") |
| Starts at the issue, before the pull request | `README.md` table (intent on each issue); `docs/METHODOLOGY.md` §2 bis |
| Each change is reviewed by another model than its author | `docs/ORCHESTRATION.md` §3 ("fresh subagent on another model") |

Left out on purpose: "Teams set the pace" (one quote is enough), `/ship` rolling out and counted as regular Claude
Code usage, token billing, Belayline's bounded loops (3 rounds, 6 pushes), verdicts on the PR and memory in issues
(all good rows for the carousel), and every figure about Belayline.

## Self-check against the launch review

| Flaw listed on 2026-11-17 | This post |
|---|---|
| Typo in the first line | First two paragraphs re-read word by word in both languages; none found. Read aloud once before pasting |
| Five topics in one post | One idea: Claude Ship is good news for delivery, and an open repository exists for those who want more or lack the plan |
| LLM cadence ("X was never the hard part. Y is.") | No reversal pair, no punchline sentence |
| Arrow lists of five | No list at all |
| Triads | The three agents are Anthropic's three products, in sentences of unequal length. Belayline gets two sentences, not a list of three |
| Sentences that sound generated | First person, one opinion stated as an opinion, product names and a quoted figure |
| Broken sentence, stutter | Every sentence has a subject and a verb; no repeated word pair found |
| Anti-call to action | None; one question at the end |
| No proof | One figure, Anthropic's, attributed to them. None for Belayline, by the operator's choice |
| Carousel | Introduced in one line; its content is the other agent's |

Against `identity.md` › Voice: the only figure is sourced and dated; no client or employer named; no star count or
adoption claim; one question at the end, the links in the first comment (operator's choice, 2026-11-25; `identity.md` asks for the repository link at the end of the post, so this is a deliberate exception); three hashtags; no decorative emoji.

## Three alternative opening lines

1. `Anthropic introduced Claude Ship on 23 November. I work on the same problem, and I am glad they took it on.`
2. `"Ship code as fast as teams write it": that is the goal Anthropic gave Claude Ship on 23 November.`
3. `Agents write code faster than teams can merge it. On 23 November, Anthropic shipped its answer.`

## Results

Not published yet.

## Changelog

| Version | Change |
|---|---|
| 1 | First draft: Ship credited, Team/Enterprise limit, Belayline's two differences with the 3-round and 6-push bounds |
| 2 | Coordinator's correction: limit stated on the managed agents only; local `/ship` and `/steward` named; Belayline as a layer around those tools |
| 3 | Operator's feedback: no pitch and no "vs"; generous to Anthropic; announcement facts added (date, goal, GA and beta, CODEOWNERS quote, observe-only, Anthropic's figure, attributed); Belayline's figures and the list removed; "I find it well designed" dropped; visual is a carousel, one line; French version added |
| 5 | Operator's update (2026-11-25): review is one stretch of the road; delivering fast also needs intent, CI capacity and, in a company, accounts, tokens and compliance built for agents; Ship does not cover it nor claim to; teases the next post (the motorway, `communication/posts/2026-11-software-factory`) |
| 4 | Operator's update: no link in the post body, "Links in the first comment."; first comment written (announcement and repository, English and French); post trimmed to stay under ~1,300 characters |
