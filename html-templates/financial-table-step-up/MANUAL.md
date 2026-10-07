# financial-table-step-up — Fiscal-year financial table with one derived step-up column boxed

WHEN: A page whose exhibit IS a small financial table — fiscal-year columns
plus a "what changes" column — so the reader sees the step-up the claim is
about without a chart. Purpose: justify an investment or guidance step-up in
one page ("we're spending more and here is what it buys"). Extracted from the
Accenture Investor & Analyst Conference 2022 deck, p2 and p3 (sheet
`sw_sheets/accenture__accenture_accenture_investor_analyst_conference_2022_s00.jpg`,
pages p1-p10: p2 = row 1 col 2, p3 = row 1 col 3), plus the same deck's p11/p17
variants on `..._s01.jpg`. The review that called this the deck's core device:
`reviews/accenture__accenture_accenture_investor_analyst_conference_2022.md`
line 21 ("highlighted financial tables — plain row-label/column table with one
column wrapped in a magenta box; the deck's core device").

ANATOMY (1280×720 stage, `rem` = 1 stage px; every element on the stage plane,
table drawn in one inline SVG whose viewBox maps 1 user unit = 1 px):
1. title (claim, violet, no kicker) — x64 y56, 430×114, 30px regular display
2. header captions — baselines: single-line y196; two-line y172/y188; the
   row-label column carries no caption
3. header accent rule — x580→x1216 at y198, 2.0px, violet mid-tone
4. data rows — 6 rows, pitch 44px, first text baseline y240; row i = one
   `<g transform="translate(0, 44*i)">`
5. row labels — right-anchored at x606 (they hug the numbers, as in p2)
6. numeric columns — right-anchored at x780 / x926 / x1072
7. step-up column — boxed cells: rect x1100 w116 h30 rx2 at baseline−23, fill
   `--highlight`, value white bold 17px centered at x1158
8. closing hairline — x580→x1216 at y504, 1px `--rule`
9. footnote block — x64, bottom:56, 10.5px, up to 3 lines with ¹ ² ³ markers
10. source line — x64 bottom:24, 11px; running head + page number bottom-right x1216

SLOTS:
- `title` — ≤15 words / 2 lines at 430px width. A quantitative claim that
  states the step-up AND the result ("Stepping up investment by $0.9B adds
  4.8 pts of revenue growth"), not "Investment overview" or "Our plan".
  If it wraps to 3 lines, cut words — do not drop below 26px.
- `rows[].label` — ≤34 chars. One row is the claimed metric (bold); "of which:"
  sub-rows are gray, 13px, and inherit the parent's unit.
- `rows[].a / b / c` — three fiscal-year figures. Right-anchor means the value,
  not the label, is what lines up. Same precision down the column.
- `rows[].box` — the derived step-up. One per row, no exceptions. Format:
  sign + value + unit ("+$36.5B", "+4.8 pts", "+55 bps").
- `rows[].bold` — exactly ONE row true (the metric named by the claim); bold is
  the only second emphasis mark, the box fill never changes per cell.
- `units` — printed once per row in the label ("($B)", "bps") or on the column
  header; never repeated inside every cell.
- `footnotes` — ≤3. Required wherever a figure is illustrative/non-GAAP or a
  step-up is a derived difference; each carries its marker in the row or header.
- `source-line` — ≤170 chars: filing/plan, page, and who did the calculation.

FILL:
1. Replace the `title` text node. Title first — everything else keys off its
   numbers. Width slot is 430rem; two lines at 30px is the gate.
2. Swap the numbers in the `rows` array documented in the index.html comment.
   Per row change ONLY: the four `<text>` values (label stays at x606) and the
   boxed value text. Never move an `x` coordinate.
3. Recompute every `box` value from `c − b` with the row's unit; if the derived
   number is negative, print "−$X" (the box text is white on magenta either
   way) and consider whether the claim is still "step up".
4. Row count: rows sit on a 44px pitch from baseline 240. A 7th row is
   `translate(0,264)`; then move the closing hairline from y504 to y548 and
   check the footnote block (starts ~y604) is clear. >8 rows means the page has
   no single claim — split it.
5. Columns: if you need FY24/FY25/FY26/FY27 actuals instead of
   actual/actual/illustrative/step-up, drop the boxes and keep three right
   edges; do not re-add a fifth column inside 636px of table width.
6. Recolour: swap `--accent` / `--accent-mid` (KPMG navy: #123B96 / #16419E;
   Deloitte green: #0F8A66 / #34A184). `--highlight` may stay magenta or move
   with the accent family — never introduce a third hue. Text printed ON the
   box must stay #FFFFFF; check the box fill keeps ≥4.5:1 (a lighter fill
   requires dark `--ink` text instead).

CHART RECIPE:
- This is a table, not a picture. The encoding is position (row × column) plus
  one fill. No bars inside cells, no zebra banding, no icons, no sparklines.
- Scale discipline: there is no axis. Each column is a closed scale defined by
  its caption ("FY24/FY25 = actual, FY27 = illustrative plan"). Print
  precision is FIXED per column (currency $x.x / % x.x / bps integer) so that
  decimals align on the right anchor — alignment is the axis.
- Value-label placement: numbers are the labels, right-anchored; the derived
  step-up column is boxed so the eye lands on it last (left→right reading of
  actual → actual → plan → change). Never center-align a numeric column.
- Units: stated once — in the row label's parenthetical or the header caption.
  Never inside cells, never "≈", never two units for one metric.
- One accent + gray ramp: violet does structure (title, header rule, footnote
  markers); every non-emphasis number is ink/gray ramp; magenta appears ONLY in
  the step-up boxes and nowhere else on the page. Emphasis is one row bold +
  one column boxed — two marks maximum.
- Emphasis follows data: bold the row the claim names. Two bold rows = the
  claim is really two claims.
- Superscripts: methodology claims carry ¹ ² ³ in the text; the footnote block
  restates each. Illustrative or guidance figures get a marker by rule —
  a number without a source marker on this system reads as fabricated.
- Column derivation: the highlighted column is computed from the other columns.
  It must be possible to check it visually in one second.

VERIFY:
- [ ] title ≤15 words and ≤2 lines at stage width (MBB gate)
- [ ] source line present bottom-left, page number bottom-right
- [ ] exactly one emphasis hue family; magenta only in the step-up boxes
- [ ] white-on-box contrast ≥4.5:1 (box fill #A34E98 passes: 6.0:1)
- [ ] right-anchored numerals line up; fixed precision per column
- [ ] step-up box values equal (illustrative − last actual) for every row
- [ ] footnote markers appear in rows/headers and in the block below
- [ ] no cell fills outside the step-up column, no fourth colour

DON'T:
- Topic titles ("Investment summary", "Guidance update") — the claim is the
  device; without a number in the title the page is a spreadsheet.
- Boxing two columns, or filling cells with the accent to "show" a delta.
- A legend for the box: it means one thing. Legends belong to multi-series charts.
- Per-cell units ($58.1B $72.4B …) or mixed precision (11% / 15.75%).
- Zebra row shading, drop shadows, or the source deck's silver-gradient ground
  (brand scenery; this kit renders on white with real hairlines).
- Silent derivations — the step-up column needs a footnote naming the
  subtraction and its provenance.
- Adding a fifth year-column to the same table (636px of table width fits four
  columns' right edges and no more).

SOURCE: `accenture__accenture_accenture_investor_analyst_conference_2022`,
slides p2, p3 (and p11/p17 variants) of the deck, extracted from
`sw_sheets/accenture__accenture_accenture_investor_analyst_conference_2022_s00.jpg`
(rows 1 col 2 and col 3) and `..._s01.jpg`; analysed in
`reviews/accenture__accenture_accenture_investor_analyst_conference_2022.md`
(architecture §1 "highlighted financial tables", palette line 18, footer-band
discipline line 12). Palette hexes: no hexes are listed in that review, so the
values in `index.html` are sampled from the p2 render crop (violet ~rgb(147,116,192),
magenta ~rgb(180,115,181), numerals ~rgb(16,22,38)) and deepened for white-stage
contrast as documented in the file header. Real fonts in the source deck:
Accenture House grotesque (single family, three registers) — the
Helvetica Neue/Arial stack stands in, per kit rule (no webfonts).
