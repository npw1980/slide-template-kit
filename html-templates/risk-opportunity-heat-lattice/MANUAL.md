# risk-opportunity-heat-lattice — Likelihood × Consequence Grid + Response Rail

WHEN: The page that answers "how much of this register actually matters." A 5×5 grid plots
each risk as a bubble whose AREA is annualised exposure and each opportunity as a hollow
diamond on the same axes, with a response rail (exposure + owner + response) down the right.
Use it where the register has been screened, not just collected — board risk sections, EBITDA
"exposures at risk" pages, post-workshop heat maps. Evidence:
`kpmg__kpmg_genai_survey_2024_key_insights_2024` p9 (risk ranking drawn as ranked bars over
grey tracks, one value numeral per item — `sw_sheets/kpmg__kpmg_genai_survey_2024_key_insights_2024_s00.jpg`),
`kpmg__kpmg_kpmg_2022_ceo_outlook_2022` p5 (numbered risk list, one value numeral per item,
"Source:" line under every exhibit, single blue hue — `sw_sheets/kpmg__kpmg_kpmg_2022_ceo_outlook_2022_s00.jpg`
row 1 col 5), and `pwc_strategy__pwc_boardroom_agenda_2022` p26 (the "Risks/opportunities
identified over short/medium/long term" block — `sw_sheets/pwc_strategy__pwc_boardroom_agenda_2022_s02.jpg`,
row 1 col 5) read against that deck's documented weakness: colour assigned by layout, not
meaning. Here grey = risk and ONE hue = exposure/upside, always.

ANATOMY: numbered slot map, px on the 1280×720 stage (1rem = 1 stage px; the SVG overlay maps
`0 0 1280 720` so user-units are the same px):
1. `kicker` — "05 | Risk & opportunity — exposure map", x:64, y:36.
2. `title` (h1) — claim, x:64, y:56, w:752, 27/33px navy; trailing `sup`.
3. `strip` — three roll-up figures right-aligned to x:1216, y:56 (`18 register entries` /
   `$7.0M plotted exposure` (accent) / `3 funded responses`).
4. `lead` — so-what line, x:64, y:136, w:1152, 13px bold, with a 56px accent underline.
5. `grid` — 25 rects, 80px cells, ORIGIN (150,200) → occupies x 150..550, y 200..600. Cell
   class IS the severity ramp: `s1` light (<10), `s2` mid (10–19), `s3` deep (≥20) — computed
   as likelihood × consequence, never as a hue ramp.
6. `band` — the critical zone: impact 4–5 × likelihood 4–5 = rect x:390 y:200 w:160 h:160,
   filled `--accent-1` with an accent outline, plus the `band-label` caps above it.
7. `axis` — consequence ticks (5..1) left of x:150; likelihood ticks (1..5) under y:600; both
   axis titles (the vertical one rotated −90° about (112,400)); baseline rule y:600 from
   x150→550 (ends at the grid edge — do not run it into blank canvas).
8. `opp` markers — hollow diamonds, same coordinate space as risks. One `<g class="opp">` each.
9. `marker` bubbles — filled circles, id inside. One `<g class="marker">` each.
10. `rail` (HTML) — x:692, y:196, w:524. Header row + one `.rrow` per risk (rank chip, name,
    exposure, owner/response), then a `rail-note`.
11. `legend` — x:692, bottom:118 — the encoding is stated ON the page (area = $, diamond =
    upside, grey ramp = severity).
12. `footrule` y:676 / `source` bottom-left / `pageno` bottom-right.

COORDINATE MODEL (manual-checkable, no hidden maths):
  cell = 80px, origin = (150,200)
  x = 150 + 80 × (likelihood − 1) + 40      likelihood 1..5, left → right
  y = 200 + 80 × (5 − consequence) + 40      consequence 1..5, bottom → top
  So L1·I1 → (190,560) and L5·I5 → (510,240); L4·I4 → (430,320). The marker's `translate` IS
  that pair. Bubble radius is the only other number you set.

SLOTS:
- `title` — max 15 words / 2 lines and it must be checkable against the drawing: "Five items
  move EBITDA this year; three carry a funded response" is falsifiable by counting. Never a
  topic title ("Risk heat map"). If it wraps to 3 lines, cut words.
- `strip.fig` — roll-up counts (18 / $7.0M / 3). The accent one is the dollar figure, because
  the page's argument is money, not count.
- `lead` — ≤30 words. Says what the grid means, including what is deliberately NOT drawn.
- `marker.r` — the ONLY data number per risk: exposure tier 18 (≥$3M) / 13 ($1–3M) / 10
  ($0.3–1M) / 7 (<$0.3M). Radius is scaled by area, not radius, because area is what the eye
  compares. Set r only — never scale the circle with `transform`.
- `marker.id` — R1/R2… inside the bubble (`.mid`); 2 glyphs; the rail uses the same code. This
  is what stops "which dot is which" being a guess.
- `marker.mk-val` — the $ figure beside the dot (`.mk-val`, ink/accent). One per dot. It must
  also appear in the rail; if it doesn't, delete it.
- `opp.o-lab` — "O2 · +$1.1M": code + upside figure in one label. Diamonds carry no id inside
  because they are hollow — the label is their only identity.
- `.rrow` — 5 fields max: rank chip, name (1 line + a 9.5px `sub` explaining it), exposure
  figure + "exposure" caption, owner + response. The response text says either "funded — <move>"
  or "no priced response" / "monitor monthly"; that binary is the honest part of this slot.
- `dim-note` — one italic line inside the low-severity corner naming what sits below the cut
  line. Present on purpose: an all-filled grid is the tell of a decorative heat map.

FILL (build order — resizing is the whole point of this page):
1. HTML first: `kicker`, `title`, three `strip` figures, `lead`.
2. ONE RISK = ONE `<g class="marker" id="rN" transform="translate(x,y)">` —
   copy that group and change exactly two things: the `translate` pair (use the coordinate
   model above) and the `<circle class="bub" r="13">` value. Its children (`.mid` id, `.mk-val`)
   inherit position from the group. Do NOT add per-child x/y: absolute coordinates are what make
   the diagram impossible to grow.
   TO ADD A RISK: copy a `.marker`, set translate to its cell centre, set r to the exposure tier.
   Nothing reflows — the grid is a fixed scale, not content, so 5 or 9 or 15 risks all sit in
   the same 25 cells. Two risks that land in the same cell: jitter the second by ±14px on x or
   y so both bubbles and both value labels stay legible.
   TO REMOVE A RISK: delete the whole `<g>`. If the rail still has its row, delete that too.
   Then check the claim title still counts correctly — it may have said "five", and that is
   now wrong (this is the failure mode of the whole family).
3. ONE OPPORTUNITY = ONE `<g class="opp" id="oN" transform="translate(x,y)">` — same rule,
   plus the diamond path `d="M0 -11 L11 0 L0 11 L-11 0 Z"` (11 = half-diagonal; the focus
   diamond uses 13). Diamond size is NOT the exposure tier here: opportunities are ranked by
   their +$ label, not by geometry, so keep one size for all unless you want to encode size too.
4. GRID: leave the 25 rects alone. The severity class `s1/s2/s3` is recomputed from the
   likelihood×consequence product when you change the band definition — do not recolour cells
   individually.
   TO CHANGE THE SCALE (e.g. 4×4 or 3×3 bands): keep cell = 80, change the count of rects, and
   change the coordinate model's multipliers consistently — 4 bands means x = 150 + 100×(n−1)+50.
   Update BOTH axis title strings and the tick labels in the same edit, or the grid lies.
   TO MOVE THE CRITICAL BAND: edit the single `.band` rect (x:390 y:200 w:160 h:160) and the
   `band-label` — everything else, including which markers sit inside it, follows from the
   coordinate model.
5. RAIL ROWS (HTML): copy or delete a whole `<div class="rrow">…</div>`; the rail reflows by
   itself, no coordinates. Mark exactly one `class="rrow focus"` (accent rank chip + accent
   exposure) to tie the rail to the focus bubble in the grid.
6. EMPHASIS: `class="marker focus"` + `class="opp focus"` + `class="rrow focus"` — all three
   must name the SAME item (R1 in the shipped placeholder). That is the only accent geometry on
   the page; the critical band is a fill, not emphasis.
7. RECOLOR: set `--accent`. Blue→PwC orange = `--accent:#D04800; --ink:#333333`; the band uses
   `--accent-1`, so give it the client's 15%-lightness tint (orange tint ≈ #F7D9CC), otherwise
   the band goes invisible. Greys stay.

CHART RECIPE: Two encodings on one scale. Axes are ordinal 1..5 bands, stated in the axis title
("Likelihood of occurrence, next 24 months" / "Consequence — EBITDA at risk") — never "low/med/
high" with no definition, and the cut line must be defined somewhere (the footnote says which
bands qualify). Risk = filled circle, AREA ∝ annualised $ exposure; the tier table lives in the
legend line so the reader can convert dot→dollars without a caption. Opportunity = hollow
diamond: hollow is the honest mark, since upside is a claim not a measured loss. One accent hue:
it means "the one item this page is about" (focus bubble + its band-rail twin), and the band is
the single tint. No gridline clutter, no 3-D, no red. If you need to show response coverage, do
it in the rail's response column, not with ring outlines around the bubbles. Never plot a marker
whose exposure figure is absent from the rail.

VERIFY: title ≤15 words AND ≤2 lines AND its count matches the number of markers drawn (recount,
don't trust); every bubble's $ appears once as `mk-val` and once in the rail; one accent hue +
grey ramp (≤3 values: navy, blue, greys); `--accent-1` used only for the band; bubbles do not
overlap (jitter cells with ≥2 risks); text contrast — `.mk-val` ink #002478 on #EFF1F4 ≈ 11:1 ✓,
`mk-lab`/`.ax` #6E767F on white = 4.6:1 ✓; axis line ends at the grid edge (x550); `dim-note`
present if any risk is below the cut line; source bottom-left with footnote sup; `NN | SECTION`
bottom-right.

DON'T: 10 hues (the PwC boardroom deck's documented failure — six risk triggers in six colours,
colour by layout not meaning); bubble size by radius instead of area (a "2×" dot reads as 4×);
red-for-risk (adds a second hue and makes the page a traffic light); filling every cell with
"risks" until the grid says nothing — draw the cut line and name what's excluded; 25 markers
(caps ~9 — beyond that the dots overlap and the rail stops being readable; aggregate into
categories instead); SmartArt arrows between cells; opportunity diamonds sized/coloured as if
they were measured losses; 3-D or gradient cells; lorem; webfonts.

SOURCE: KPMG `kpmg__kpmg_genai_survey_2024_key_insights_2024` (2024) p9 and
`kpmg__kpmg_kpmg_2022_ceo_outlook_2022` (2022) p5 — ranked risk presentation over grey with
one value numeral per item, single blue hue; PwC Strategy `pwc_strategy__pwc_boardroom_agenda_2022`
(2022) p26 — risks/opportunities as numbered blocks. Cells resolved from `sw_sheets/` contact
sheets (5 col × 2 row, row-major). Palette: `reviews/kpmg__kpmg_kpmg_2022_ceo_outlook_2022.md`
(royal blue #243CE4, deep navy #002478, greys #333/#4A4A4A/#999, canvas #F8F8F8/white) and
`reviews/pwc_strategy__pwc_boardroom_agenda_2022.md`, whose §colour note — "Colour is
decorative, not semantic" — is the reason this template hard-codes the semantic mapping
(grey ramp = severity band; one accent = the item under discussion) instead of inventing a ramp.
Fonts: KPMG Sans / PwC custom faces are the real systems; `"Helvetica Neue", Arial` is the
stand-in, with a Calibri-class stack for body text.
