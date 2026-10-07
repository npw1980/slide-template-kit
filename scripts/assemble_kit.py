#!/usr/bin/env python3
"""Assemble the HTML template kit: manifest.json, README.md, gallery.html, thumbnails.

Idempotent. Safe to re-run after every stream; skips existing thumbs unless --force.
"""
import json, os, re, subprocess, sys, html as htmllib
from collections import defaultdict

ROOT = '/home/nathan-white/new projects/deck-research/html-templates'
CHROMIUM = os.environ.get('CHROMIUM', '/home/nathan-white/.local/bin/chromium')
FORCE = '--force' in sys.argv

def load_entries():
    entries, seen = [], {}
    p = os.path.join(ROOT, 'manifest.jsonl')
    for line in open(p, encoding='utf-8'):
        line = line.strip()
        if not line: continue
        try: d = json.loads(line)
        except Exception: continue
        if d.get('id') and d['id'] not in seen:
            seen[d['id']] = d
            entries.append(d)
    # probe template 'cover' built before manifest convention existed
    if 'cover' not in seen and os.path.isdir(os.path.join(ROOT, 'cover')):
        manual = ''
        try: manual = open(os.path.join(ROOT,'cover','MANUAL.md')).read()
        except Exception: pass
        entries.append({
            'id':'cover',
            'title':'Full-bleed cover, firm mark bottom-right',
            'family':'cover-standalone',
            'path':'cover/index.html',
            'source':'accenture__accenture_the_nbn_effect (cover p00) + kpmg__kpmg_kpmg_2021_ceo_outlook (cover p00 variant)',
            'slots':[],
        })
    return entries

def thumb(entry):
    tid = entry['id']
    outdir = os.path.join(ROOT, 'gallery'); os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, f'{tid}.png')
    src = os.path.join(ROOT, entry.get('path', f'{tid}/index.html'))
    if not os.path.exists(src):
        return None
    if os.path.exists(out) and not FORCE and os.path.getmtime(out) > os.path.getmtime(src):
        return out
    cmd = [CHROMIUM, '--headless=new', '--disable-gpu', '--no-sandbox',
           '--hide-scrollbars', '--force-device-scale-factor=1',
           '--window-size=1280,720', f'--screenshot={out}', 'file://' + src]
    try:
        subprocess.run(cmd, timeout=45, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        return None
    if os.path.exists(out):
        # downscale for gallery size
        subprocess.run(['python3', '-c',
            f"from PIL import Image; im=Image.open(r'{out}'); im.thumbnail((760,428)); im.save(r'{out}')"],
            timeout=30)
        return out
    return None

def build_readme(entries):
    fams = defaultdict(list)
    for e in entries: fams[e['family']].append(e)
    lines = ["# Consulting HTML Template Kit\n",
             "Every template is one self-contained `index.html` (1280×720 stage, inline CSS/SVG, zero network "
             "calls) plus a `MANUAL.md` build manual. Rules and extraction evidence: "
             "`../DESIGN_PLAYBOOK.md` (design principles) and `../TEMPLATE_SPEC.md` (kit spec). "
             "Layout-family provenance: `../TEMPLATE_HARVEST.json`.\n"]
    lines.append(f"Templates: {len(entries)} across {len(fams)} layout families. "
                 "All extracted from visually-reviewed firm decks and report pages "
                 "(4,867 slides reviewed — see the playbook's method).\n")
    lines.append("| Family | Template | Source (evidence pages) |")
    lines.append("|---|---|---|")
    for fam in sorted(fams):
        for e in sorted(fams[fam], key=lambda x: x['id']):
            src = (e.get('source') or '—')
            lines.append(f"| {fam} | [{e['id']}]({e['path']}) + [MANUAL](<manual.md>) | {src[:120]} |".replace('(manual.md)', f"({e['id']}/MANUAL.md)"))
    open(os.path.join(ROOT,'README.md'),'w').write('\n'.join(lines)+'\n')

def build_gallery(entries, thumbs):
    fams = defaultdict(list)
    for e in entries: fams[e['family']].append(e)
    ordered = sorted(fams, key=lambda f: (-len(fams[f]), f))
    esc = lambda s: htmllib.escape(str(s))
    nav = '\n'.join(f'<a class="navrow" href="#{f}"><span class="nf">{f}</span><span class="nc">{len(fams[f])}</span></a>' for f in ordered)
    sections = []
    for f in ordered:
        rows = []
        for e in sorted(fams[f], key=lambda x: x['id']):
            t = thumbs.get(e['id'])
            img = f'<a href="{e["path"]}" class="shot"><img src="gallery/{e["id"]}.png" alt="" loading="lazy"></a>' if t else f'<div class="shot pending">render pending</div>'
            slots = ''.join(f'<span class="chip">{esc(s)}</span>' for s in (e.get('slots') or [])[:8])
            rows.append(f'''<article class="entry">
      {img}
      <div class="meta">
        <h3><a href="{e['path']}">{esc(e.get('title') or e['id'])}</a></h3>
        <code class="id">{esc(e['id'])}</code>
        <p class="src">{esc(e.get('source') or '—')}</p>
        <p>{slots}</p>
        <p class="links"><a href="{e['path']}">template</a><span></span><a href="{e['id']}/MANUAL.md">build manual</a></p>
      </div></article>''')
        sections.append(f'''<section class="fam" id="{f}">
      <h2>{esc(f)}</h2>
      <p class="count">{len(fams[f])} template{'s' if len(fams[f])!=1 else ''}</p>
      {''.join(rows)}
    </section>''')
    doc = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Slide Template Index</title>
<style>
  /* Read-mode specimen index: paper + ink, one navy accent, editorial serif display.
     Theming of browser surfaces (selection, scrollbar, focus) comes from the palette. */
  :root {{
    --paper:#FAF8F5; --card:#FFFFFF; --ink:#171512; --ink-2:#4A453E; --ink-3:#6E675F;
    --rule:#E6E0D6; --accent:#1D3A63; --accent-soft:#EEF2F8; --danger:#8A2822;
  }}
  * {{ box-sizing:border-box; }}
  html {{ scroll-behavior:smooth; }}
  body {{ margin:0; background:var(--paper); color:var(--ink);
    font:15px/1.55 Georgia,"Times New Roman",serif; }}
  ::selection {{ background:var(--accent); color:#fff; }}
  ::-webkit-scrollbar {{ width:12px; }}
  ::-webkit-scrollbar-track {{ background:var(--paper); }}
  ::-webkit-scrollbar-thumb {{ background:#CFC8BC; border:3px solid var(--paper); border-radius:9px; }}
  a {{ color:var(--accent); text-decoration:none; text-underline-offset:3px; }}
  a:hover {{ text-decoration:underline; }}
  a:focus-visible {{ outline:2px solid var(--accent); outline-offset:2px; }}

  header.masthead {{ max-width:1180px; margin:0 auto; padding:64px 40px 40px;
    border-bottom:2px solid var(--ink); }}
  header.masthead h1 {{ font-size:clamp(2rem,4.5vw,3.4rem); line-height:1.05; margin:0 0 14px;
    font-weight:700; letter-spacing:-0.01em; }}
  header.masthead p.dek {{ margin:0; color:var(--ink-2); font-family:"Helvetica Neue",Arial,sans-serif;
    font-size:15px; max-width:62ch; }}
  header.masthead p.facts {{ margin:18px 0 0; font-family:"Helvetica Neue",Arial,sans-serif;
    font-size:13px; color:var(--ink-3); }}
  header.masthead p.facts b {{ color:var(--ink); font-weight:600; }}

  .wrap {{ max-width:1180px; margin:0 auto; padding:0 40px 120px; display:grid;
    grid-template-columns:280px 1fr; gap:56px; align-items:start; }}
  nav.fams {{ position:sticky; top:24px; padding:10px 0 4px; }}
  nav.fams .navhead {{ font-family:"Helvetica Neue",Arial,sans-serif; font-size:11px;
    letter-spacing:.08em; text-transform:uppercase; color:var(--ink-3); margin:0 0 10px; }}
  nav.fams a.navrow {{ display:flex; justify-content:space-between; padding:5px 8px 5px 10px;
    font-family:"Helvetica Neue",Arial,sans-serif; font-size:12.5px; color:var(--ink-2);
    border-left:2px solid var(--rule); }}
  nav.fams a.navrow:hover {{ background:var(--accent-soft); color:var(--ink); border-left-color:var(--accent);
    text-decoration:none; }}
  nav.fams .nc {{ color:var(--ink-3); font-variant-numeric:tabular-nums; }}
  .howto {{ margin-top:26px; padding:14px 16px; background:var(--card); border:1px solid var(--rule);
    border-radius:12px; font-family:"Helvetica Neue",Arial,sans-serif; font-size:12.5px; color:var(--ink-2); }}
  .howto b {{ color:var(--ink); }}
  .howto a {{ display:block; margin-top:6px; }}

  section.fam {{ padding-top:56px; }}
  section.fam + section.fam {{ margin-top:12px; }}
  section.fam h2 {{ font-size:1.55rem; letter-spacing:-0.01em; margin:0; }}
  section.fam .count {{ margin:4px 0 22px; font-family:"Helvetica Neue",Arial,sans-serif;
    font-size:12px; letter-spacing:.06em; text-transform:uppercase; color:var(--ink-3); }}

  article.entry {{ display:grid; grid-template-columns:minmax(0,560px) 1fr; gap:28px;
    align-items:start; padding:26px 0; border-top:1px solid var(--rule); }}
  a.shot, div.shot.pending {{ display:block; border:1px solid var(--rule); border-radius:10px;
    overflow:hidden; background:var(--card); box-shadow:0 1px 0 rgba(23,21,18,.03); }}
  a.shot img {{ display:block; width:100%; height:auto; }}
  a.shot {{ transition:box-shadow .18s ease-out, transform .18s ease-out; }}
  a.shot:hover {{ box-shadow:0 10px 26px rgba(23,21,18,.14), 0 2px 6px rgba(23,21,18,.08);
    transform:translateY(-2px); text-decoration:none; }}
  div.shot.pending {{ aspect-ratio:16/9; display:flex; align-items:center; justify-content:center;
    color:var(--ink-3); font-family:"Helvetica Neue",Arial,sans-serif; font-size:12px; }}
  article.entry .meta h3 {{ margin:2px 0 6px; font-size:1.05rem; line-height:1.3; }}
  code.id {{ font-family:"SF Mono",ui-monospace,Menlo,Consolas,monospace; font-size:11.5px;
    background:var(--accent-soft); color:var(--accent); padding:2px 7px; border-radius:6px; }}
  p.src {{ margin:10px 0 8px; font-size:13px; color:var(--ink-2); max-width:38ch; }}
  .meta .chip {{ display:inline-block; margin:2px 6px 2px 0; font-family:"Helvetica Neue",Arial,sans-serif;
    font-size:11px; padding:2px 8px; border:1px solid var(--rule); border-radius:999px; color:var(--ink-2); }}
  p.links {{ font-family:"Helvetica Neue",Arial,sans-serif; font-size:12.5px; margin:6px 0 0; }}
  p.links span {{ display:inline-block; width:10px; }}
  footer.colophon {{ max-width:1180px; margin:0 auto; padding:26px 40px 60px; border-top:2px solid var(--ink);
    font-family:"Helvetica Neue",Arial,sans-serif; font-size:12.5px; color:var(--ink-3); }}
  @media (max-width:960px) {{
    .wrap {{ grid-template-columns:1fr; gap:24px; }}
    nav.fams {{ position:static; display:flex; flex-wrap:wrap; gap:6px; }}
    nav.fams .navhead,.howto {{ display:none; }}
    nav.fams a.navrow {{ border:1px solid var(--rule); border-radius:999px; }}
    article.entry {{ grid-template-columns:1fr; }}
  }}
</style></head>
<body>
<header class="masthead">
  <h1>Slide Template Index</h1>
  <p class="dek">Buildable page templates extracted from visually-reviewed consulting decks and
  market-research reports. Each entry ships a self-contained HTML page on a 1280×720 stage and a
  build manual that says exactly how to fill and resize it.</p>
  <p class="facts"><b>{len(entries)} templates</b> · {len(fams)} layout families · extraction rules
  in TEMPLATE_SPEC.md · design rules in DESIGN_PLAYBOOK.md · every template cites its source pages</p>
</header>
<div class="wrap">
  <nav class="fams" aria-label="families">
    <p class="navhead">Families</p>
    {nav}
    <div class="howto"><b>How to use</b>
      Open a template, copy its files, replace the marked slots per its MANUAL.md.
      Palettes and chart rules follow DESIGN_PLAYBOOK.md.
      <a href="../README.md">README index</a><a href="../TEMPLATE_SPEC.md">kit spec</a>
    </div>
  </nav>
  <main>
    {''.join(sections)}
  </main>
</div>
<footer class="colophon">Extracted from a corpus of 4,867 visually reviewed slides across firm decks
(Accenture, Deloitte, EY, KPMG, L.E.K., PwC Strategy&) and vetted template archives. Fonts in the
templates are honest stand-ins for the firms' licensed faces; manuals label every substitute.</footer>
</body></html>'''
    open(os.path.join(ROOT,'gallery.html'),'w').write(doc)

def main():
    entries = load_entries()
    print(f"entries: {len(entries)}")
    thumbs = {}
    for i, e in enumerate(entries, 1):
        t = thumb(e)
        thumbs[e['id']] = t
        if i % 10 == 0: print(f"thumbs {i}/{len(entries)}")
    done = sum(1 for v in thumbs.values() if v)
    print(f"thumbs done: {done}/{len(entries)}")
    json.dump(sorted(entries, key=lambda x: (x['family'], x['id'])),
              open(os.path.join(ROOT,'manifest.json'),'w'), indent=1)
    build_readme(entries)
    build_gallery(entries, thumbs)
    print("manifest.json / README.md / gallery.html written")

if __name__ == '__main__':
    main()
