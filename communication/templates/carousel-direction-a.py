import re,sys
SP=open(sys.argv[2]).read()
# compass only: crop the social preview to the compass, drop texts, transparent background
comp=re.sub(r'<text[^>]*>.*?</text>','',SP,flags=re.S)
comp=re.sub(r'<rect width="1194" height="597" fill="url\(#(bg|halo)\)"/>','',comp)
comp=re.sub(r'viewBox="[^"]*"','viewBox="590 50 570 520"',comp,count=1)
comp=comp.replace('<svg ','<svg class="compass" ',1)
INK="#10182c"; T="#1e1e1e"; K="#868e96"
C=dict(person=("#f08c00","#fff3bf"),agents=("#1971c2","#a5d8ff"),repo=("#2f9e44","#b2f2bb"),checks=("#e8590c","#ffd8a8"),
       infer=("#0c8599","#c3fae8"),decide=("#6741d9","#d0bfff"),risk=("#e03131","#ffc9c9"))
chip=f'''<svg width="44" height="44" viewBox="0 0 44 44"><circle cx="22" cy="22" r="19" fill="none" stroke="{INK}" stroke-width="3"/><circle cx="22" cy="22" r="9" fill="none" stroke="{INK}" stroke-width="3"/><path d="M22 6 L26 22 L22 38 L18 22 Z" fill="{INK}"/></svg>'''
def white(n,title,body):
    return f'<div class="s w"><h2>{title}</h2>{body}<div class="foot">{chip}<span>Belayline</span><span class="pg">{n}/8</span></div></div>'
def card(kind,head,text):
    s,f=C[kind]; return f'<div class="card" style="border-color:{s};background:{f}55"><b style="color:{s}">{head}</b><br>{text}</div>'
pages=[]
pages.append(f'''<div class="s n">{comp}<div class="cov"><div class="kick">Belayline 0.4.0 · free · open source · MIT</div>
<h1>A harness for<br>coding agents,<br><em>in your repository.</em></h1></div><div class="foot dark"><span>github.com/francoisgn/belayline-agentic-harness</span><span class="pg">1/8</span></div></div>''')
pages.append(white(2,"Your repository,<br>ready for agents",
  card("repo","Rules every agent reads","AGENTS.md, conventions, lessons from real projects")+
  card("repo","Labels and templates","issues and pull requests that carry their intent")+
  card("checks","A CI that runs when needed","nothing on drafts, the costly jobs only when it matters")))
steps=[("person","Intent","what the user gets, the error cases"),("repo","Tests first","red, then the code, then green"),
       ("agents","Review by another model","fresh eyes, never the author's reasoning"),("risk","Merge","when the checks and the review agree")]
loop=''.join(f'<div class="step"><span class="num" style="border-color:{C[k][0]};color:{C[k][0]}">{i+1}</span><div><b>{h}</b><br><small>{t}</small></div></div>' for i,(k,h,t) in enumerate(steps))
pages.append(white(3,"One loop<br>for every change",f'<div class="loop">{loop}</div><p class="note">Lessons feed the next intent.</p>'))
pages.append(white(4,"Agents that<br>work together",
  card("decide","One agent per task","a claim on the issue, a ledger of who does what")+
  card("decide","The right model for each task","an orchestrator routes the work, from any provider")+
  card("agents","Stewards","keep the docs and the issues true after every merge")))
big=lambda n,t,k: f'<div class="big"><span style="color:{C[k][0]}">{n}</span><small>{t}</small></div>'
pages.append(white(5,"Less waste",
  '<div class="bigs">'+big("3","review rounds at most","checks")+big("6","CI-tested pushes at most","checks")+'</div>'+
  card("checks","A timeout on every CI job","no runner held for hours by a hung test")+
  card("risk","A dashboard that flags","stuck runs and jobs that pass only on a re-run")))
pages.append(white(6,"Two choices<br>that make it different",
  '<div class="cmp"><div class="lab">Context</div><div class="them">Elephant–Goldfish (Google): held by one long-lived agent</div>'
  f'<div class="us" style="border-color:{C["repo"][0]}">Belayline: in the repository, shared by every agent and every person</div>'
  '<div class="lab">Models</div><div class="them">Claude advisor: two Claude models in one conversation</div>'
  f'<div class="us" style="border-color:{C["agents"][0]}">Belayline: a model per task, any provider, reviewed by another</div></div>'))
pages.append(white(7,"Tested on real work",
  card("repo","LightCraft","open source, more than 100 contributors in 30 days")+
  card("repo","iOS apps","native Swift, agents in the cloud and on a Mac")+
  card("repo","Corporate projects","in a group of 100,000 people and 15,000 developers")+
  '<p class="note">Built from years of running platforms and products.</p>'))
pages.append(f'''<div class="s n"><div class="cov low"><div class="kick">Try it</div><h1 class="m">Start your next project<br>by asking your agent:</h1>
<p class="q">“Check Belayline and take<br>what is useful for me.”</p><p class="url">github.com/francoisgn/belayline-agentic-harness</p></div>
<div class="foot dark"><span>Free · open source · MIT</span><span class="pg">8/8</span></div></div>''')
css=f'''@page{{size:1080px 1350px;margin:0}}*{{box-sizing:border-box}}body{{margin:0;font-family:Inter,sans-serif}}
.s{{width:1080px;height:1350px;position:relative;overflow:hidden;page-break-after:always;padding:150px 90px 150px}}
.n{{background:linear-gradient(135deg,#10182c,#202c48);color:#f5f0e6}}.w{{background:#fff;color:{T}}}
.compass{{position:absolute;right:-60px;top:110px;width:640px;height:584px;opacity:.95}}
.cov{{position:absolute;left:90px;right:90px;top:720px}}.cov.low{{top:330px}}
.kick{{font-size:30px;letter-spacing:.06em;color:#8aa0c0;margin-bottom:24px}}
h1{{font-size:84px;line-height:1.05;font-weight:800;letter-spacing:-2px;margin:0}}h1 em{{font-style:normal;color:#42d5e3}}h1.m{{font-size:64px}}
.q{{font-size:52px;line-height:1.2;color:#42d5e3;font-weight:700;margin:60px 0}}.url{{font-size:30px;color:#dfe3ea}}
h2{{font-size:68px;line-height:1.08;font-weight:800;letter-spacing:-1.5px;color:{INK};margin:0 0 56px}}
.card{{border:4px solid;border-radius:24px;padding:26px 32px;margin:0 0 28px;font-size:32px;line-height:1.3}}.card b{{font-size:38px}}
.loop{{display:flex;flex-direction:column;gap:30px}}.step{{display:flex;gap:28px;align-items:center;font-size:32px;line-height:1.3}}
.step b{{font-size:40px}}.step small{{font-size:30px;color:#495057}}.num{{flex:none;width:76px;height:76px;border:4px solid;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:38px;font-weight:800}}
.note{{font-size:32px;color:#495057;margin-top:44px}}
.bigs{{display:flex;gap:60px;margin-bottom:40px}}.big span{{display:block;font-size:150px;font-weight:800;line-height:1}}.big small{{font-size:30px;color:#495057}}
.cmp{{display:grid;grid-template-columns:1fr;gap:18px}}.lab{{font-size:30px;color:{K};letter-spacing:.08em;text-transform:uppercase;margin-top:20px}}
.them{{font-size:32px;color:#495057;padding:0 4px}}.us{{font-size:36px;font-weight:700;border-left:8px solid;padding:10px 0 10px 24px;color:{INK}}}
.foot{{position:absolute;left:90px;right:90px;bottom:60px;display:flex;align-items:center;gap:14px;font-size:28px;color:{INK};font-weight:700}}
.foot .pg{{margin-left:auto;font-weight:400;color:{K}}}.foot.dark{{color:#8aa0c0;font-weight:400}}'''
open(sys.argv[1],'w').write('<!doctype html><meta charset="utf-8"><style>'+css+'</style>'+''.join(pages))
