# kpi-numerals-hero — purple claim title + section word + row of giant near-black KPI numerals with keyword captions (footnoted)

WHEN: Stakeholder-value / impact-pages where 3–4 oversized figures speak in one row, each with a tiny caption whose keywords carry the brand colour, plus methodology footnotes — no chart, no boxes, lots of air. From Accenture's 2022 investor-analyst-conference deck, pages 14–16 ("Highlights of our 360° value…": Diversity / People / Communities & Sustainability), where the review's type section pins the device: "giant KPI numerals ≈50–60pt near-black with a micro-caption beneath".

ANATOMY (1280×720 stage; all coords in stage px):
1. title        — x76 y40 w1104, 28px regular display, brand violet `--accent`, line-height 1.18 (2 lines max).
2. section      — x76 y152 w220, 23px regular ink, the one-word section label (Diversity / People / …) sitting left of the numeral row.
3. row (container)— x316 y148 w888 h206: one leading wide column (flex 180) + three equal columns (≈236); 1px `--rule` dividers between columns.
4. num-1..4     — inside each column: 58px bold near-black, letter-spacing −1.6px, white-space nowrap; the leading column carries a RANGE as "44% to" (26px) stacked over "47%¹" (58px).
5. caps block   — x316 y264 w888, same column flex; 11px grey captions under their numbers, dividers continuing; `--accent-ink` bold keywords, one `--magenta` keyword per page max, superscript footnote markers.
6. footnote     — x76 y640 w860, 9.5px grey, three numbered notes; rule at y672.
7. chevron      — x26 y686, violet brand chevron SVG (page-navigation signature; keep or drop).
8. source       — x76 y696, 10.5px grey long method string.
9. page         — right x1204 y695, bold numeral + " | SECTION" running head.
The zone y360–y630 is deliberately EMPTY; the silver wash (one soft radial) substitutes the deck's gradient field. Do not fill it.

SLOTS:
- title: action claim ≤15 words / 2 lines at 28px/1104px. Sentence case, regular weight, violet — weight is NOT emphasis on this system; colour is.
- section: 1–3 words (the sub-section word, "Diversity & inclusion"). Topic word allowed here — it is a label, not an argument.
- num-1..4: display numerals 3–5 chars + optional superscript ("75%¹", "$3B", "315k", "100%"). The leading slot may be a range: `pre` = "X% to" (26px) + `big` = "Y%¹" (58px); do not stack two full-size numbers.
- captions: ≤90 chars / 3 lines each. Exactly ONE keyword per caption is violet-bold; the argument word inside (e.g. "accessibility") may be the one magenta item on the page; everything else grey. Footnote markers ride inside captions like the deck (1, 2, 3).
- footnotes: ≤3 notes, ≤110 chars each, numbered; they are what makes the giant numbers honest.
- source: full method string (dashboards + audit + registry, ≤170 chars).

FILL:
1. Title first (claim gate drives the page), then the section word.
2. Numbers: replace `.num` strings; keep at most one `sup` inside; letter-spacing −1.6px keeps "100%" on one line — never let it wrap.
3. For a range in the leading column, edit BOTH spans (`.pre` and `.big`); for a plain number, replace `.pre` with nothing and give `.big` the whole string (block stays).
4. Captions: swap whole `.cc` blocks, keeping column order aligned with numbers (column flex duplication means numbers-block and captions-block must both stay 4 items in the same order).
5. Emphasis discipline: recolour `--accent`/`--accent-ink` together; `--magenta` exists for ONE word max; if a second magenta word appears, the page is wrong.
6. Chevron SVG is presentational — delete it plus nothing else if the deck has no nav signature.

CHART RECIPE: no chart — row of display numerals as encoding. Rules: (a) the four figures must answer ONE question (all "does the 360° model work?"), not four unrelated KPIs — the row is a sentence; (b) read left→right as an argument ladder (headline range → support → support → one that shows the edge, like 32%); (c) the leading range column exists to show momentum (X to Y) — never put a single number there; (d) near-black numerals only — colour on numerals would compete with the violet title, and the deck keeps numerals ink-neutral; (e) one hue (violet) + one magenta word + greys.

VERIFY: title ≤15 words / 2 lines (28px×1.18×2 ≈ 66px ends y106 — 42px above the row); numbers nowrap inside 180/236px columns (test "1,234%" fits: 58px × −1.6 tracking ≈ 130px — 5 chars max per single-num column); captions ≤3 lines and never collide with the footnote rule at y672; text on white ≥4.5:1 (violet #6A3FB5 ≈ 7:1, ink-dark violet #4B2A91 ≈ 9:1, magenta #B01769 ≈ 5:1); ONE magenta word on the page; footnote numbers match superscripts in captions/numbers; source line present; page numeral present.

DON'T:
- Filling the lower canvas with boxes, logos or a paragraph — the deck's stat rows are deliberately airy; density belongs to other templates.
- Topic title + topic captions ("Diversity: 44–47%" style restatement) — at least the title must argue.
- Colouring the numerals (brand violet/green numerals) — the review is explicit: numerals are near-black, colour lives in keywords.
- Two magenta words — emphasis is scarce here or it means nothing.
- More than four numerals, or a fifth column squeezed under 180px — it breaks the 888px row.
- Unfootnoted giant numbers — at display size an unsourced figure is the most persuasive, most misleading device in the corpus; the footnote block is mandatory if any number is survey/estimate-derived.

SOURCE: accenture__accenture_accenture_investor_analyst_conference_2022 — pages 14/15/16 read from sw_sheets/accenture__accenture_accenture_investor_analyst_conference_2022_s01.jpg (row0/col3, row0/col4, row1/col0); violet pixel band #6A40A0–#A880D8 sampled from p14/p11 title pixels (JPEG, anti-aliased) with `--accent: #6A3FB5` as midpoint — remap to the brand hex when known; device inventory (claim title, numeral row + purple micro-caption, chevron, footnote band) per reviews/accenture__accenture_accenture_investor_analyst_conference_2022.md §type/§color. Real deck face is Accenture's house grotesque; the file ships a Helvetica/Arial stand-in per spec.
