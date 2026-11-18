# -*- coding: utf-8 -*-
"""Build the Spotlight 6 "Irregular Verbs by Groups" section into <repo>/verbs/.
Run from src/:  python3 vg/build_vg.py
Emits: verbs/index.html (hub), verbs/01..04.html (groups), verbs/all.html (all verbs).
Grade 6, Past Simple only — no ОГЭ.
"""
import html, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from data import GROUPS, ALL, SAY

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # repo root
SECTION = os.path.join(ROOT, "verbs")
os.makedirs(SECTION, exist_ok=True)
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@600&family=Nunito:wght@400;700;800&display=swap" rel="stylesheet">')
BRAND = "Чемоданчик учителя английского"
e = html.escape
alts = lambda f: [x.strip().lower() for x in f.split("/")]
problems = []

def verb_obj(t):
    v1, v2, v3, i1, i2, i3, ru, s1, tr1, s2, tr2 = t
    allforms = alts(v1) + alts(v2) + alts(v3)
    sents = []
    for s, tr in ((s1, tr1), (s2, tr2)):
        m = re.findall(r"\*([^*]+)\*", s)
        if len(m) != 1:
            problems.append(f"{v1}: sentence needs exactly one *target*: {s}")
        elif m[0].lower() not in allforms:
            problems.append(f"{v1}: target '{m[0]}' is not a form of the verb")
        sents.append([s, tr])
    o = dict(v=[v1, v2, v3], ipa=[i1, i2, i3], ru=ru, sents=sents)
    if v1 in SAY: o["say"] = list(SAY[v1])
    return o

def expand_story(g):
    by = {t[0]: t for t in g["verbs"]}
    def rep(mt):
        base, ans = mt.group(1), mt.group(2)
        t = by.get(base)
        if not t:
            problems.append(f"group {g['id']}: story base '{base}' not in group"); return mt.group(0)
        forms = [t[0], t[1], t[2]]
        hit = [f for f in forms if ans.lower() in alts(f)]
        if not hit:
            problems.append(f"group {g['id']}: story answer '{ans}' not a form of {base}"); return mt.group(0)
        full = hit[0] if base != "be" else ans
        return f"[[{base}|{full}]]"
    return re.sub(r"\[\[([^|\]]+)\|([^\]]+)\]\]", rep, g["story"])

def page(title, body, extra_head=""):
    return f"""<!doctype html><html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>{FONTS}<link rel="stylesheet" href="assets/style.css">{extra_head}</head>
<body><div class="wrap">{body}
<div class="foot">© {BRAND} · Неправильные глаголы по группам · Spotlight 6, 6 класс</div></div></body></html>"""

# the "all" page trains every verb from every group
ALL["verbs"] = [t for g in GROUPS for t in g["verbs"]]
# every V2 form in the whole set — distractor pool for "choose the form"
ALLV2 = sorted({t[1].split("/")[0].strip() for g in GROUPS for t in g["verbs"]})

# order of the trainer pages, for prev/next navigation
SEQ = [g for g in GROUPS] + [ALL]

def group_page(g):
    i = SEQ.index(g)
    prev = SEQ[i-1] if i else None
    nxt = SEQ[i+1] if i+1 < len(SEQ) else None
    data = dict(id=g["id"], pattern=g["pattern"], title=g["title"],
                verbs=[verb_obj(t) for t in g["verbs"]])
    if g.get("story"):  # only groups with 3+ verbs carry a story
        data["story_title"] = g["story_title"]
        data["story"] = expand_story(g)
    nav = ('<nav class="top-nav"><a href="index.html">← Все группы</a><span>'
           + (f'<a href="{prev["id"]}.html">‹ {e(prev["example"])}</a> ' if prev else "")
           + (f'<a href="{nxt["id"]}.html">{e(nxt["example"])} ›</a>' if nxt else "")
           + "</span></nav>")
    pos = "Все глаголы" if g["id"] == "all" else f"Группа {int(g['id'])} из {len(GROUPS)}"
    body = f"""{nav}<header class="hero"><div class="brand">{BRAND} · {pos}</div>
<span class="pattern">{e(g['pattern'])}</span><h1>{e(g['title'])}</h1>
<div class="example">{e(g['example'])}</div><p class="rule">{g['rule']}</p><div class="tip">{g['tip']}</div></header>
<p class="scroll-hint">↓ Листай вниз — упражнения идут одно за другим.</p><div id="panels"></div>
<script>window.ALLV2={json.dumps(ALLV2, ensure_ascii=False)};
window.GROUP={json.dumps(data, ensure_ascii=False)};</script><script src="assets/app.js"></script>"""
    with open(os.path.join(SECTION, f"{g['id']}.html"), "w", encoding="utf-8") as f:
        f.write(page(f"{g['example']} — неправильные глаголы (Spotlight 6)", body))

for g in GROUPS:
    group_page(g)
group_page(ALL)

# ---- hub (index)
total = sum(len(g["verbs"]) for g in GROUPS)
cards = "".join(f"""<a class="gcard" href="{g['id']}.html"><div class="n">Группа {int(g['id'])}</div>
<div class="p">{e(g['pattern'])}</div><div class="e">{e(g['example'])}</div><div class="cnt">{len(g['verbs'])} глаг. · {e(g['title'])}</div></a>""" for g in GROUPS)
cards += f"""<a class="gcard" href="all.html"><div class="n">Всё вместе</div>
<div class="p">Все глаголы</div><div class="e">{total} глаголов</div><div class="cnt">перемешать и проверить себя</div></a>"""
dist = ""
for g in GROUPS:
    rows = "".join("<tr>" + "".join(f'<td><span class="f c{i+1}">{e(t[i])}</span><span class="ipa">[{e(t[i+3])}]</span></td>' for i in range(3)) +
                   f'<td class="ru">{e(t[6])}</td></tr>' for t in g["verbs"])
    dist += f"""<h3><a href="{g['id']}.html">{int(g['id'])}. {e(g['pattern'])} — {e(g['title'])}</a></h3>
<p class="lead">{g['rule']}</p><table class="vt"><thead><tr><th>V1</th><th>V2</th><th>V3</th><th>Перевод</th></tr></thead><tbody>{rows}</tbody></table>"""
body = f"""<nav class="top-nav"><a href="../index.html">← Spotlight 6: все темы</a></nav>
<header class="hero"><div class="brand">{BRAND} · 6 класс</div><h1>Неправильные глаголы по группам</h1>
<p class="rule">{total} неправильных глаголов из нашей таблицы, разложенных на {len(GROUPS)} групп по <b>одному чередованию</b>: в каждой группе глаголы меняются одинаково.
Учить «семьями» легче, чем по алфавиту: запомнил одну модель — знаешь всю группу.</p>
<div class="tip">В каждой группе: таблица с озвучкой, карточки, три формы по переводу, диктант на слух, выбор формы, предложения, а в больших группах — короткий текст.</div></header>
<h2>Выбери группу</h2><div class="grid">{cards}</div>
<section class="panel active dist"><h2>Все глаголы по группам</h2>
<div class="legend"><span class="c1">● V1 — начальная</span><span class="c2">● V2 — Past Simple</span><span class="c3">● V3 — третья форма</span></div>{dist}</section>"""
with open(os.path.join(SECTION, "index.html"), "w", encoding="utf-8") as f:
    f.write(page("Неправильные глаголы по группам — Spotlight 6", body))

print(f"{len(GROUPS)} groups + all, {total} verbs")
if problems:
    print("PROBLEMS:"); [print(" -", p) for p in problems]; sys.exit(1)
