# LinkedIn, November 2026: one toll in detail, the context read again

Status: **ready to publish**, after [2026-11-software-factory](../2026-11-software-factory/README.md) (the
motorway), which it refers to ("one of the tolls"). Author: the operator. Figures from one busy day of the
operator's Claude Code use billed per token (billing anonymised; no account, provider or project named); the
busiest-day figures are the operator's estimate. Image in [direction A](../../identity.md).

| File | What |
|---|---|
| [`visual.png`](visual.png) | The image, 1080 × 1350: "Claude Code, billed per token: up to $20,000 a month"; one month on one dollar axis ($5,000 for 20 busy days, split 45 / 43 / 12 %; up to $20,000 for 20 of the busiest days, estimate), against a $100/month flat plan drawn to the same scale (fixed price, usage capped by the plan's limits) |

## The post (paste as is)

```text
One busy day of Claude Code, billed per token, cost about $250. What the model wrote is 12% of that bill.

The other 88% is context, paid for twice.

43% went to reading the conversation again. It happens at every turn. A cached token costs $0.20 per million, which looks like nothing, but there were 531 million of them: 95% of all the tokens of the day.

45% went to writing that context into the cache, at $5 per million. This is the line I had not seen coming. Billed per token, outside a subscription, the cache lasts 5 minutes. When I wait longer than that for a CI run or a background task, the next turn writes the whole context again. The bill has no timestamps, so I cannot say how much of the 45% comes from those pauses. Probably a large part.

The unit prices are Anthropic's list prices, so nothing is wrong with the bill. And that was a busy day, not my busiest: those run 1.5 to 2.3 billion tokens, up to four times as much, up to about $1,000 a day at pay-as-you-go API prices. Over 20 working days, that would be $5,000 to $20,000 a month.

What I do now: one short session per task, and after a long pause I restart from a written state instead of waking the long session.

In the motorway picture, this is one of the tolls. The bar below shows the split.

Do you know what share of your agent bill is the model writing?

Details in the first comment.

#AgenticAI #FinOps #ClaudeCode
```

## The first comment (paste as is)

```text
How I measure it and what the harness does about it (cache lifetime, pauses, resuming from a written state): https://github.com/francoisgn/belayline-agentic-harness/blob/master/docs/FINOPS.md
```

## French version (secondary, same content)

```text
Une journée chargée de Claude Code, facturée au token, a coûté environ 250 $. Ce que le modèle a écrit représente 12 % de cette facture.

Les 88 % restants, c'est du contexte, payé deux fois.

43 % sont partis dans la relecture de la conversation. Elle a lieu à chaque tour. Un token en cache coûte 0,20 $ le million, ce qui ne paraît rien, mais il y en a eu 531 millions : 95 % de tous les tokens de la journée.

45 % sont partis dans l'écriture de ce contexte dans le cache, à 5 $ le million. C'est la ligne que je n'avais pas vue venir. Facturé au token, hors abonnement, le cache dure 5 minutes. Quand j'attends plus longtemps une CI ou une tâche de fond, le tour suivant réécrit tout le contexte. La facture n'a pas d'horodatage, je ne peux donc pas dire quelle part des 45 % vient de ces pauses. Probablement une grande part.

Les prix unitaires sont les prix publics d'Anthropic : la facture est juste. Et c'était une journée chargée, pas ma plus chargée : celles-là montent de 1,5 à 2,3 milliards de tokens, jusqu'à quatre fois plus, jusqu'à environ 1 000 $ par jour au tarif de l'API à l'usage. Sur 20 jours ouvrés, cela ferait de 5 000 à 20 000 $ par mois.

Ce que je fais maintenant : une session courte par tâche, et après une longue pause je repars d'un état écrit au lieu de réveiller la longue session.

Dans l'image de l'autoroute, c'est l'un des péages. La barre ci-dessous montre la répartition.

Savez-vous quelle part de votre facture d'agents correspond à ce que le modèle écrit ?

Détails en premier commentaire.

#AgenticAI #FinOps #ClaudeCode
```

French first comment:

```text
Comment je le mesure et ce que le harnais en fait (durée du cache, pauses, reprise depuis un état écrit) : https://github.com/francoisgn/belayline-agentic-harness/blob/master/docs/FINOPS.md
```

Length (counted by script): English post 1,402 characters; French post 1,566, above the ~1,300 target (to shorten,
drop the motorway sentence).

Notes for the operator:
- "The line I had not seen coming" and "What I do now" are your statements: keep them only if true. The two levers
  chosen are short sessions per task and resuming from a written state (both in `docs/FINOPS.md` §1). Others
  available, not used: Sonnet by default, fewer parallel subagents, short tool output.
- The model (Opus 5.5) is not in the post either; it is on the claims table for the image's caption if wanted.
- The $100/month plan appears on the image only, as a fixed price with usage capped by the plan's limits (the
  price is the operator's assumption; limits are not published in tokens). Not used in the text: the contrast with
  our subscription measures (reads 96–98 % of tokens, 40–50 % of usage; rebuilds 0.3–5.4 %
  where waits end inside a 1-hour cache, `docs/FINOPS.md` §1). Either would be a second idea; the second one makes
  a good reply to a comment.
- "Paid for twice" is a shortcut for "paid once to write it, then at every re-read"; replace by "paid for again and
  again" if you prefer it literal.
- The motorway line assumes that post is out. If it is not, drop the sentence.

## Claims and sources

Billing figures: operator's billing data, anonymised, one day in November 2026, as supplied by the operator (not
seen by this agent). Arithmetic re-done here from the supplied token counts and unit prices.

| Claim in the post | Source |
|---|---|
| About $250 for one intensive day | Operator's billing data, anonymised. Check: 22.5 M × $5 + 531 M × $0.20 + 1.46 M × $20 + 0.33 M × $4 ≈ $249 |
| Output is 12 % of the bill | Same: 1.46 M × $20 ≈ $29, 11.7 % |
| 43 % for cache reads, 531 million tokens at $0.20 per million | Same: ≈ $106, 42.6 % |
| Reads are 95 % of the day's tokens | Same: 531 of 555.7 M tokens, 95.6 % |
| 45 % for cache writes at $5 per million | Same: 22.5 M × $5 = $112.5, 45.1 % |
| "The other 88 %" | 43 + 45; uncached input adds under 1 % (≈ $1.3) |
| The cache lasts 5 minutes outside a subscription | `docs/FINOPS.md` §1, citing https://code.claude.com/docs/en/prompt-caching (read 2026-11-19) |
| A wait longer than the cache makes the next turn write the whole context again | `docs/FINOPS.md` §1 ("the whole history is written again") |
| The share of the 45 % caused by pauses is not measured | Stated as such in the post; "probably a large part" is a judgment. `docs/FINOPS.md` §1 measured 30–34 % of usage in rebuilds for one orchestrator, on other data |
| Unit prices equal Anthropic's list prices | Billing data: Opus 5.5 input $4/M, 5-minute cache write $5/M, cache read $0.20/M, output $20/M; re-check the public price page on the day of posting |
| Busiest days 1.5 to 2.3 billion tokens, up to 4×, about $1,000 a day at API prices | Operator's own order of magnitude (2026-11-27), not measured per day; at the busy day's mix (556 M Opus tokens ≈ $250), 4× is about 2.3 B tokens and $1,000 |
| $5,000 to $20,000 a month | 20 working days × $250 (busy day) to × $1,000 (busiest days); a projection |
| One short session per task; restart from a written state after a long pause | `docs/FINOPS.md` §1 ("resumes from it in a fresh context"); `docs/ORCHESTRATION.md` §8 |

Figures in the post: eight numbers in the text, more than the "at most four" of a carousel page; the image carries
the two days, the split and the plan.

## Self-check against the launch review

| Flaw listed on 2026-11-17 | This post |
|---|---|
| Typo in the first line | First two paragraphs re-read word by word in both languages; none found. Read aloud once before pasting |
| Five topics in one post | One idea: the bill of a session is its context, written and read again, far more than what the model writes |
| LLM cadence ("X was never the hard part. Y is.") | The "price is known, cost is the context" pair is not used as a punchline; the post opens on a lived number |
| Arrow lists of five | No list, no arrow |
| Triads | None; two shares explained, two levers |
| Sentences that sound generated | First person, real amounts, one admitted blind spot ("I cannot say how much") |
| Broken sentence, stutter | "Probably a large part." is a deliberate short answer after a full sentence; merge with a comma if it reads as broken |
| Anti-call to action | None; one question the reader can answer from their own bill |
| No proof | The whole post is one measured day, with the limit of the measure stated |
| Carousel | Not applicable; one image |

Against `identity.md` › Voice: every figure has its source above; "one day in November" is the window; no client,
private project named; no adoption claim; one question; link in the first comment (same exception as
the Claude Ship post); three hashtags; no decorative emoji.


## Results

Not published yet.
