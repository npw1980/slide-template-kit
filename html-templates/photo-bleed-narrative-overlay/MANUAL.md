# photo-bleed-narrative-overlay — Full-bleed photograph with floating copy panel

WHEN: A page whose argument is a short piece of narrative (study design,
approach, "why we did this") that needs atmosphere as well as text — the
photograph IS the page and the copy sits in an opaque panel on top of it.
Source: PwC Strategy& *IAB Podcast Ad Revenue Study* (2017) p04, where a
sunlit photo bleeds edge-to-edge and a cream panel carries three justified
paragraphs under a serif-italic "Overview". The same grammar recurs on PwC
narrative-photo pages (`..._pwc_global_family_business_survey_2018` p23/p36,
`..._consumer_insights_pulse_survey` p01). Use it to open or bridge a section;
for the quote-glyph divider sibling use `photo-bleed-split-divider`.

ANATOMY (1280×720 stage; `index.html` uses `1rem = 1 stage px`, zero JS):
1. photo — `figure.photo`, inset 0, 1280×720, bleeds to all four edges; inline SVG `preserveAspectRatio="xMidYMid slice"` so a swapped real image cover-crops identically.
2. scrim-top — left 0, top 0, 1280×96: faint dark wash so white kicker/title stay legible over bright skies.
3. scrim-bl — left 0, bottom 0, 660×120: gradient wash behind the source line.
4. kicker — left 64, top 66 — 11px accent square + 10.5px white caps, .16em, one line.
5. title — left 64, top 92, width 600 — 38px serif bold-italic white, ONE keyword in accent amber; ≤2 lines. THIS IS THE GATE.
6. copy panel — left 664, top 196, width 552, height 456, opaque `--panel` + 1px `--panel-edge` + drop shadow.
   6a. panel head — h2 "Overview" 19px serif italic maroon, right-aligned 9.5px caps label, 1px rule under.
   6b. panel body — 12.5px / 1.56 justified, 3 paragraphs, `<strong>` maroon phrase, `<sup>` markers.
   6c. panel foot — 1px rule + running head, right-aligned.
7. source line — left 24, bottom 20, width 600 — 9.5px white on the scrim, with `sup` markers.
8. credit line — left 24, bottom 8 — 8px 62%-white photo credit.
9. running head — inside the panel foot: 7px accent square + `PAGE | SECTION`, page number near-black.
10. placeholder badge — `figure.photo .stamp`, right 14, bottom 12: "PHOTO PLACEHOLDER" so a mock is never mistaken for licensed imagery.

SLOTS:
- `kicker` — 1 line ≤34 chars. Good: section tag + a marker (`Study design · 01`). Bad: a sentence, or a brand hashtag repeated.
- `title` — **≤15 words, ≤2 lines** (38px × 600px ≈ 33 chars/line). Good: a directional claim whose keyword is the accent word ("Published estimates were *too wide to be reliable*"). Bad: a topic label ("Overview", "Background") — the deck puts topic labels in the panel head, not in the title.
- `panel_head` — ≤12 chars. Good: "Overview" / "Approach" / "Contacts" — exactly the deck's own serif-italic panel heads. Bad: repeating the kicker.
- `panel_label` — ≤14 chars, caps. Good: fieldwork window or section. Bad: a date range that also appears in the source line.
- `para_1` — 3–4 lines. Good: the scene-setting fact with one pulled `<q>` line. Bad: throat-clearing.
- `para_2` — 4–5 lines and must contain the ONE `<strong>` maroon phrase — that bold phrase is where the argument lives. Bad: two bold phrases (then nothing is emphasised).
- `para_3` — 4–5 lines, method/close. Good: what was actually done (scan → interviews → n=20) so the page is falsifiable. Bad: a conclusion that duplicates the title.
- `source_line` — ≤2 lines including `n=` and the fieldwork window; every `sup` needs a back-matter entry.
- `credit_line` — 1 line. Good: the real picture library or client's own shoot. Bad: blank (that is the failure mode the review calls "bulk without argument").
- `running_head` — `PAGE | SECTION`, 1 line.

FILL:
1. Swap the photograph: delete the `<svg>` inside `figure.photo` and paste either a base64-embedded raster inside the same SVG (`<image href="data:image/jpeg;base64,…" width="1280" height="720" preserveAspectRatio="xMidYMid slice"/>`) or the exported picture layer (Figma/PPTX place, same crop). Delete the `.stamp` span the moment licensed imagery is in. Keep a subject off-centre to the left — that is what keeps the right half free for the panel.
2. Re-tune scrim if the photo is dark: the two `linear-gradient` stops in `.scrim-bl` / `.scrim-top`; raise the first stop's alpha toward `.72` for pale photos. Never raise the panel's transparency — opaque is the load-bearing rule.
3. Recolour for a different client: `--accent` (kicker square, title keyword, sup markers, foot square), `--accent-deep` (panel head + bold phrase), `--panel` (panel ground). One accent hue; the maroon is a dark tint of it. For a monochrome house style set `--accent-deep: var(--accent)` and drop the keyword colour to white.
4. Panel size: the panel is 552×456. Body copy at 12.5px/1.56 holds ~47 lines; if your text runs to 4 paragraphs, cut text — do not grow the panel past 500 tall or it collides with the running head.
5. Footnotes: `sup` 1/2 in body map 1:1 to `sup` in the source line; body-only markers with no source entry are wrong.
6. Real font: PwC Strategy& uses a transitional serif display face (Georgia/PT-Serif-like per the review) with a grotesque body. Georgia stands in for the display stack, Arial/Calibri for the body stack; nothing here is a webfont.

CHART RECIPE: n/a — the photograph is the exhibit. If a small figure is added, put it in the panel under the body at ≤500px wide, keep the series to one accent + gray ramp, and never overlay a chart on the photo itself.

VERIFY:
- [ ] title is ≤15 words and renders in ≤2 lines at 600px (gate) — the panel head carries the topic word, not the title.
- [ ] exactly one emphasis hue: orange appears in exactly 4 places (kicker square, title keyword, sup + bold phrase, foot square).
- [ ] body text sits on the opaque panel and clears 4.5:1 (`--ink-soft` #404040 on `--panel` #FAF9F7 ≈ 10:1); white text over the photo appears only with its scrim.
- [ ] white source line over the scrim: check the photo's darkest corner — if it reads below 4.5:1, darken `.scrim-bl`.
- [ ] page number sits on panel ground inside the foot (near-black), not floating on the photograph.
- [ ] photo bleeds to all four edges with no letterbox; subject is left-of-centre so the panel never lands on a face.
- [ ] "PHOTO PLACEHOLDER" badge removed once licensed imagery is in place.

DON'T (corpus failure modes):
- Do not let the photo page be decoration. The review's criticism of the deck is that "photo/divider pages add bulk without argument" — the title must be a claim, not a mood.
- Do not make the panel translucent to show more of the photo; 12.5px justified text over a busy image fails on projection.
- Do not put the page number over the photograph; put it on panel ground where contrast is guaranteed.
- Do not run a third bold phrase or an italic body run — bold = maroon, italic = the pulled `<q>` only.
- Do not stack two photo pages: the deck's own photo pages alternate with exhibit pages for a reason.
- Do not letterbox the photo; "full bleed" is the whole contract.

SOURCE: firm PwC Strategy& · deck `pwc_strategy__pwc_iab_podcast_ad_revenue_study_an_analysis_of_the_largest__` · page 4 measured on `sw_sheets/pwc_strategy__pwc_iab_podcast_ad_revenue_study_an_analysis_of_the_largest__s00.jpg` (sheet 0 = pages 1–10, tile 4 of row 1) — full-bleed warm photograph + opaque right-hand copy panel + white source line on the image + serif-italic "Overview" panel head with a 1px rule and small caps label; page number bottom-right. Subtype cross-check (same family, different geometry): `pwc_strategy__pwc_global_top_100_companies_by_market_capitalisation_2023` p03 = 55/45 white/bleed-photo split divider (`sw_sheets/..._s00.jpg` tile 3) → built as `photo-bleed-split-divider`; KPMG 14th Five-Year Plan p11 (`sw_sheets/kpmg__kpmg_the_14th_five_year_plan_sector_impact_outlook_2021_s01.jpg` tile 1) is a photo-accompanied sector page with kicker pill + figure/table stack, not a new geometry. Palette hexes quoted from `reviews/pwc_strategy__pwc_iab_podcast_ad_revenue_study_an_analysis_of_the_largest_.md` §Color system (orange #E87722 / #ED8B2F, maroon #71301D / #71301D, grays #595959 / #404040) and §Quality tier (serif-italic titles, uniform footer); typography facts (serif bold-italic titles with an orange keyword, four-tier size hierarchy, small sans body) from §Typography of the same review.
