import re,sys
SP=open(sys.argv[2]).read()
comp=re.sub(r'<text[^>]*>.*?</text>','',SP,flags=re.S)
comp=re.sub(r'<rect width="1194" height="597" fill="url\(#(bg|halo)\)"/>','',comp)
comp=re.sub(r'viewBox="[^"]*"','viewBox="590 50 570 520"',comp,count=1).replace('<svg ','<svg class="compass" ',1)
INK="#10182c"; T="#1e1e1e"; K="#868e96"; G="#495057"
C=dict(person=("#f08c00","#fff3bf"),agents=("#1971c2","#a5d8ff"),repo=("#2f9e44","#b2f2bb"),checks=("#e8590c","#ffd8a8"),
       infer=("#0c8599","#c3fae8"),decide=("#6741d9","#d0bfff"),risk=("#e03131","#ffc9c9"))
N=10
chip=f'<svg width="40" height="40" viewBox="0 0 44 44"><circle cx="22" cy="22" r="19" fill="none" stroke="{INK}" stroke-width="3"/><circle cx="22" cy="22" r="9" fill="none" stroke="{INK}" stroke-width="3"/><path d="M22 6 L26 22 L22 38 L18 22 Z" fill="{INK}"/></svg>'
def white(n,kick,title,body):
    return f'<div class="s w"><div class="wk">{kick}</div><h2>{title}</h2>{body}<div class="foot">{chip}<span>Belayline</span><span class="pg">{n}/{N}</span></div></div>'
def card(kind,head,text,cls=""):
    s,f=C[kind]; return f'<div class="card {cls}" style="border-color:{s};background:{f}44"><b style="color:{s}">{head}</b><div>{text}</div></div>'
P=[]
toc=["Try it in one prompt","End to end, from an empty repository to merged work","The loop, step by step",
     "Many agents, many developers, many models","Where agent work burns money, and the guard for each",
     "How it differs from Google's Elephant–Goldfish","How it differs from Anthropic's advisor","Where it is tested"]
P.append(f'''<div class="s n">{comp}<div class="cov"><div class="kick">Belayline 0.4.0 · free · open source · MIT</div>
<h1>Run coding agents<br>like a team,<br><em>from your repository.</em></h1>
<p class="sub">Not a model, not a vendor's playbook: a harness that sets up the repo, the CI, the reviews and the way agents work together.</p>
<ol class="toc">{"".join(f"<li>{t}</li>" for t in toc)}</ol></div>
<div class="foot dark"><span>github.com/francoisgn/belayline-agentic-harness</span><span class="pg">1/{N}</span></div></div>''')
P.append(white(2,"Try it","Try it in one prompt",
 f'<div class="prompt">“Check Belayline and take<br>what is useful for me.”</div>'
 +card("agents","1 · Your agent reads the harness","what fits your project: rules, labels, CI baseline, reviews, stewards")
 +card("repo","2 · It installs what you keep","<code>harness-sync.sh</code>, pinned to a version; your own rules stay yours, listed as overrides")
 +card("decide","3 · You stay in charge","every rule can be switched off; updates come as a sync you review, never a silent change")
 +'<p class="note">Works with any agent that reads AGENTS.md: Claude Code, Codex, Cursor, Gemini CLI, Copilot, Aider.</p>'))
P.append(white(3,"End to end","From an empty repository<br>to merged work",
 card("repo","Bootstrap the repository","AGENTS.md and CLAUDE.md rules, labels by axis, issue and PR templates, a living README with its architecture diagram, one local check that replays the CI")
 +card("checks","CI and security","a tiered baseline: nothing costly on drafts, the expensive jobs only when ready and only if their paths changed; secrets, SAST, dependencies; a timeout on every job")
 +card("decide","Collaboration","issues with intent, claims, a ledger in each PR, an orchestrator that routes the work, stewards for docs and issues")
 +card("risk","Delivery","a merge gate (CI green, threads resolved, verdicts traced), versioned releases, a flow dashboard, lessons fed back")))
steps=[("person","Intent","user story, error cases, done, out of scope"),("decide","Ready issue","labels: type, priority, difficulty → model tier"),
 ("decide","Claim and branch","/claim on the issue, one agent, one branch"),("repo","Lot in TDD","test red, code, green; local check before every push"),
 ("agents","Adversarial review","another model, fresh context: intent + diff only"),("agents","Compliance review","GDPR, ISO 27001, PCI… when the project enables it"),
 ("checks","Ready PR and CI","every verdict traced; one automatic code review per ready head"),("risk","Merge gate","CI green on the head, threads resolved"),
 ("infer","Measure","problem PRs, loops, cost on the dashboard"),("person","Lesson","a sourced lesson, or a check that enforces it")]
loop=''.join(f'<div class="st"><span class="num" style="border-color:{C[k][0]};color:{C[k][0]}">{i+1}</span><div><b>{h}</b><small>{t}</small></div></div>' for i,(k,h,t) in enumerate(steps))
P.append(white(4,"The loop","Ten steps, every change",f'<div class="loop2">{loop}</div><p class="note">Bounded: 3 review rounds and 6 CI-tested pushes at most, then a human decides.</p>'))
P.append(white(5,"Collaboration","Many agents, many developers,<br>many models",
 card("agents","Many agents","one task, one agent: claims on issues, a ledger in each PR, an orchestrator that keeps one State and wakes on events, never polls")
 +card("repo","Many developers","the same issues, the same rules in the repository: any developer's agent can pick up the next ready issue and finds the context where the last one left it")
 +card("infer","Many models","difficulty decides the tier (fast, solid, strong, frontier), from any provider; the reviewer is never the author's model, ideally another vendor's")))
rows=[("CI on every push","nothing costly on drafts; CI when the PR is ready"),("Jobs hung for 6 hours","a timeout on every job, checked in CI"),
 ("Review ping-pong","3 rounds at most, then escalate to a stronger model or a human"),("Pushing to see if CI passes","the local check first; 6 CI-tested pushes at most"),
 ("The biggest model for everything","the model the task needs"),("Agents re-reading everything","state in issues and PRs, short briefs"),
 ("Flaky jobs re-run in silence","the dashboard names them")]
tab=''.join(f'<div class="bad">{a}</div><div class="good">{b}</div>' for a,b in rows)
P.append(white(6,"Less waste","Where agent work burns money,<br>and the guard for each",
 f'<div class="tab"><div class="th" style="color:{C["risk"][0]}">Burns money</div><div class="th" style="color:{C["checks"][0]}">Belayline</div>{tab}</div>'))
def vendor(n,kick,brand,name,url,does,keep,diff,note=''):
    return white(n,kick,f'Not tied to one<br>company\'s playbook',
     f'<div class="vend"><div class="brand">{brand}</div><div class="vname">{name}</div><div class="vurl">{url}</div>{note}</div>'
     +f'<div class="cols"><div><div class="lab">What it does</div><p>{does}</p><div class="lab">What we keep</div><p>{keep}</p></div>'
     +f'<div class="us2"><div class="lab">What Belayline does differently</div>{diff}</div></div>')
P.append(vendor(7,"Versus Google","Google","Elephant–Goldfish Model","github.com/google/elephant-goldfish-model · Apache 2.0",
 "An assistant that keeps the context (the elephant) drafts a design; reviewers without the earlier conversation (goldfish) examine it before you approve.",
 "The fresh-context reviewer, who never sees the author's conversation.",
 "<ul><li><b>The context lives in the repository</b>, shared by every agent and every developer, not in one assistant</li><li><b>The reviewer is another model</b>, ideally another vendor</li><li><b>The whole change, to merge</b>: code, CI, review, release, not only the design</li></ul>",'<div class="vnote">Hosted on Google\'s GitHub; "not an officially supported Google product", says its README.</div>'))
P.append(vendor(8,"Versus Anthropic","Anthropic","Claude Code advisor","code.claude.com/docs/en/advisor · github.com/anthropics/claude-code",
 "A stronger Claude model consulted at decision points, reading the whole conversation of the main Claude model.",
 "Escalate hard decisions to a stronger model, at the right moments.",
 "<ul><li><b>Any provider</b>: a model per task, chosen by difficulty</li><li><b>An independent reviewer</b> that never reads the author's reasoning</li><li><b>Rules in your repository</b>, not in one vendor's settings</li></ul>"))
P.append(white(9,"Tested on real work","Where it is tested",
 '<div class="bigs"><div class="big"><span style="color:#2f9e44">113</span><small>contributors to LightCraft in 30 days</small></div><div class="big"><span style="color:#1971c2">1,412</span><small>pull requests opened there in 30 days</small></div></div>'
 +card("repo","LightCraft","open-source, clean-room photo editor in Rust, built with agents")
 +card("repo","iOS apps","native Swift, agents in the cloud and on a Mac")
 +card("repo","Corporate projects","in a group of 100,000 people and 15,000 developers")
 +'<p class="note">Built from years of running platforms and products.</p>'))
P.append(f'''<div class="s n"><div class="cov low"><div class="kick">Free · open source · MIT</div><h1 class="m">Start your next project<br>by asking your agent:</h1>
<p class="q">“Check Belayline and take<br>what is useful for me.”</p><p class="url">github.com/francoisgn/belayline-agentic-harness</p></div>
<div class="foot dark"><span>Belayline 0.4.0</span><span class="pg">{N}/{N}</span></div></div>''')
css=f'''@page{{size:1080px 1350px;margin:0}}*{{box-sizing:border-box}}body{{margin:0;font-family:Inter,sans-serif}}
.s{{width:1080px;height:1350px;position:relative;overflow:hidden;page-break-after:always;padding:110px 80px 120px}}
.n{{background:linear-gradient(135deg,#10182c,#202c48);color:#f5f0e6}}.w{{background:#fff;color:{T}}}
.compass{{position:absolute;right:-50px;top:60px;width:420px;height:383px}}
.cov{{position:absolute;left:80px;right:80px;top:440px}}.cov.low{{top:360px}}
.kick{{font-size:30px;letter-spacing:.05em;color:#8aa0c0;margin-bottom:20px}}
h1{{font-size:72px;line-height:1.04;font-weight:800;letter-spacing:-2px;margin:0}}h1 em{{font-style:normal;color:#42d5e3}}h1.m{{font-size:64px}}
.sub{{font-size:30px;line-height:1.35;color:#dfe3ea;margin:26px 0 22px}}
.toc{{margin:0;padding-left:44px;font-size:29px;line-height:1.42;color:#f5f0e6}}.toc li::marker{{color:#e8a94e;font-weight:700}}
.q{{font-size:52px;line-height:1.2;color:#42d5e3;font-weight:700;margin:56px 0}}.url{{font-size:30px;color:#dfe3ea}}
.wk{{font-size:28px;letter-spacing:.08em;text-transform:uppercase;color:{K};margin-bottom:14px}}
h2{{font-size:58px;line-height:1.06;font-weight:800;letter-spacing:-1.4px;color:{INK};margin:0 0 34px}}
.card{{border:4px solid;border-radius:20px;padding:20px 26px;margin:0 0 20px;font-size:29px;line-height:1.32}}.card b{{font-size:33px;display:block;margin-bottom:4px}}
.prompt{{font-size:46px;font-weight:800;color:{INK};border-left:10px solid {INK};padding:6px 0 6px 28px;margin:0 0 34px;line-height:1.2}}
code{{font-size:27px;background:#f1f3f5;padding:1px 8px;border-radius:6px}}
.note{{font-size:29px;color:{G};margin-top:22px;line-height:1.35}}
.loop2{{display:grid;grid-template-columns:1fr 1fr;gap:22px 30px}}.st{{display:flex;gap:16px;align-items:flex-start}}
.st b{{font-size:31px;display:block}}.st small{{font-size:28px;color:{G};line-height:1.3;display:block}}
.num{{flex:none;width:56px;height:56px;border:4px solid;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:800}}
.tab{{display:grid;grid-template-columns:1fr 1.25fr;border-top:3px solid #dee2e6}}.th{{font-size:28px;font-weight:800;text-transform:uppercase;letter-spacing:.06em;padding:16px 10px}}
.bad,.good{{font-size:29px;line-height:1.3;padding:18px 10px;border-top:2px solid #e9ecef}}.bad{{color:{C["risk"][0]};font-weight:700}}.good{{color:{T}}}
.vend{{border:4px solid {INK};border-radius:22px;padding:22px 28px;margin-bottom:28px}}.brand{{font-size:72px;font-weight:800;color:{INK};line-height:1}}
.vname{{font-size:40px;font-weight:700;color:{INK};margin-top:8px}}.vurl{{font-size:28px;color:#1971c2;margin-top:8px}}.vnote{{font-size:28px;color:#868e96;margin-top:8px;line-height:1.3}}
.cols{{display:grid;grid-template-columns:1fr 1.1fr;gap:28px}}.cols p{{font-size:29px;line-height:1.32;margin:6px 0 18px}}
.lab{{font-size:28px;color:{K};text-transform:uppercase;letter-spacing:.06em}}
.us2{{border-left:8px solid #2f9e44;padding-left:22px}}.us2 ul{{margin:8px 0 0;padding-left:26px;font-size:29px;line-height:1.32}}.us2 li{{margin-bottom:14px}}
.bigs{{display:flex;gap:56px;margin-bottom:26px}}.big span{{display:block;font-size:120px;font-weight:800;line-height:1}}.big small{{font-size:29px;color:{G}}}
.foot{{position:absolute;left:80px;right:80px;bottom:50px;display:flex;align-items:center;gap:12px;font-size:28px;color:{INK};font-weight:700}}
.foot .pg{{margin-left:auto;font-weight:400;color:{K}}}.foot.dark{{color:#8aa0c0;font-weight:400}}'''
open(sys.argv[1],'w').write('<!doctype html><meta charset="utf-8"><style>'+css+'</style>'+''.join(P))
