# three-horizons-curves — Three growth horizons as rising curves on a value × time stage

WHEN: The "where does growth come from, and when" page — a portfolio or growth
strategy claim that the core is running out of runway and a second (and third)
business line has to take over on a schedule. Drawn from the Umbrex three-horizons
template (corpus slide S1782): a Value×Time stage, three column bands NOW / NEW /
NEXT, three rising curves each captioned inside the plot. The kit's replacement for
"SmartArt staircase + three bullet columns".

ANATOMY (stage 1280×720, all numbers px; one full-stage SVG viewBox 0 0 1280 720;
`html` font-size maps 1rem = 1 stage px, so the coords below are literal):
1  kicker           x64 y34    "N | SECTION" (index in accent)
2  claim title      x64 y56    2-line slot, clip-gated (3rd line clips)
3  lead             x64 y150   one sentence, exactly one accent span
4  band arrow       line x190→1200 y171 + arrowhead; caps NOW x350 / NEW x735 /
   NEXT x1043 at y190. Column separators = dashed verticals x590, x880 (y206→520).
5  axes             y-axis x112 (y520→186, arrow), x-axis y520 (x112→1206, arrow).
   TIME  x112 y558 · state note right-aligned x1206 y558.
6  gridlines        dashed y417 / y315 / y210 with 2 / 4 / 6 axis labels.
7  SERIES GROUPS    #h1 / #h2 / #h3 — one <g> per horizon (the unit you copy).
8  crossover ring   #crossover: ring on the intersection + leader + 2-line note.
9  readout table    3 columns x110 / x474 / x838, width 348 each: 3px rule y576,
   caps y598, name y616, 3 metric rows y634 / y648 / y662 (label left, value
   right-aligned at column x+348).
10 hairline y682 · source line x64 bottom · page stamp bottom-right.

SCALE MATHS (the two formulas the whole geometry derives from):
  x = 155 + (FY − 24) × 145        FY24 155 · FY26 445 · FY29 880 · FY31 1170
  y = 520 − value_bn × 51.667      0 bn 520 · 2 bn 417 · 4 bn 315 · 6 bn 210

SLOTS (name, max, good/bad):
- kicker: "N | SECTION", ≤ 4 words after the pipe.
- title: action title ≤ 15 words / ≤ 2 lines. GOOD: the shown claim (15 words,
  states who overtakes whom and by when). BAD: "Three horizons" — a topic label;
  the column caps below already say "horizon".
- lead: 1–2 lines, exactly one accent span, carries the unit (EUR bn) and the
  plan's headline number.
- series-h1/h2/h3: the curve arrays. Each horizon is 6–8 points (one per fiscal
  year); GOOD: 3.1 → 3.4 → 3.6 → 3.4 → 3.1 → 2.6 (the core peaks then declines —
  that decline is the page's argument). BAD: three monotonically rising curves;
  that says nothing about the trade-off and the title has nothing to claim.
- horizon caps: "HORIZON 1" etc., placed inside the plot under the curve. No
  legends, no colour key.
- val (end labels): one number per curve, 1 decimal. Everything else stays clean.
- readout row labels: ≤ 28 chars, and the value right-aligned in the column:
  45% / COO + 6 GMs / < 5.0 $bn. The worst plausible fill is shown (long owner
  string "Ventures + CFO", long exit rule "No gate at 18m").
- crossover note: a 5–6 word claim + one line of evidence. The ring is the only
  decoration, and it marks a fact (the year the curves cross), not a look.
- source-line: basis + n + footnote markers (sup) where methodology claims.

FILL (step by step):
1. HEADER: replace kicker / h1.title / p.lead; keep the <span class="em">.
2. MOVE THE STAGE: the plot needs 112→1206 px of width and 186→558 px of height.
   To widen or narrow the window, change ONLY the two scale constants above;
   every point, tick, gridline, label and band separator is a derived number.
   Ticks: x = 155 + (FY−24)×145. Gridlines: y = 520 − bn×51.667.
3. ADD A HORIZON (a fourth, or a second curve inside a band): COPY an existing
   `<g id="h…">` wholesale — it is a self-contained unit holding one <path>, the
   per-point <circle> dots, one caps <text> and one <text class="val">. Paste it
   after #h3. Nothing else reflows, because these are absolute-positioned series
   on a shared stage. Then edit inside the copy:
     · path: `M x0,y0 C x0+58,y0 x1−58,y1 x1,y1 C …` (58 = 0.4 × the year step;
       keep the segment endpoints exactly equal to the dots, or the curve and the
       markers drift apart);
     · dots: one <circle> per point at the same coordinates;
     · swap the colour class: `c1` (solid accent) → `c2`/`c3` (grey step / grey
       dashed) and the matching `dotN`. A 4-series page may use accent +
       accent-mid + two grey steps (solid / dashed) — never a fourth hue.
   REMOVE a horizon: delete its whole <g>; no reflow anywhere. Then delete its
   column in #readout (below).
4. ADD/REMOVE A READOUT COLUMN: columns are <g class="col"> blocks at
   x110 / x474 / x838 (pitch 364 = 348 wide + 16 gutter). Copy a block and move it
   one pitch right/left, or for a different N re-space:
   x(k) = 110 + (k−1) × (1186 − 110)/N, width = same − 16. Column text is
   anchored start at x and end at x+348, so nothing else needs touching. The
   readout column order MUST match the curve order (H1 left, H3 right).
5. BANDS: separators are 2 lines (x590, x880) and the caps are 3 texts centred
   between them. To add a 4th band, add a separator line and re-centre the caps:
   cap x = midpoint of the band. Bands must stay aligned to fiscal years, or the
   page stops being a chart and becomes a schematic.
6. CROSS-OVER: ring cx/cy = the intersection you computed from the two arrays;
   if the curves do not cross on your numbers, DELETE #crossover entirely rather
   than move the ring somewhere decorative.
7. EMPHASIS: accent lives in exactly one place per page — the emphasis curve's
   `.c1` class plus its readout rule + caps. Moving emphasis = moving that class
   pair, nothing else.
8. FOOTER: source line + page stamp; keep sup markers on the claims they back.

CHART RECIPE: Position on two real axes — x is time (fiscal years, monotone,
equal spacing), y is incremental revenue in one unit (bn), both labelled on the
axis, not in a legend. One accent: exactly one curve is solid accent (the one the
title is about); the other series render in grey ramp + one lightness of accent
(#h2 `c2` = accent-mid, #h3 `c3` = grey-2 dashed) so they are readable as
hierarchy, not palette. Value labels sit at the curve ends in ink bold — the last
point is the only one labelled. No axis shadows, no gradient fills, no markers
except 3.2px dots at each year. Gridlines dashed grey-3 and behind everything.
The dashed vertical band separators are furniture, not data — they must not read
as a threshold line (that role belongs to a solid rule with a label, if needed).

VERIFY: title ≤ 15 words / 2 lines (clip gate); source line present + sup markers;
exactly one accent hue + greys, no more; end value labels present on every curve;
axis unit stated once ("INCREMENTAL REVENUE, EUR BN"); page stamp present; each
series group survives the copy-paste test; readout column count = curve count.

DON'T: topic title ("Three horizons of growth"); a fourth hue or a red/green
"delta" palette; a legend box (labels go on the curves); a bar chart instead of
curves (the shape of the S-curve is the argument); curves that all rise forever;
numbers painted on the axes' interior that repeat the readout table; kicker as a
wall of text; letting a metric value run long enough to break its right alignment.

SOURCE: corpus slide S1782 — Umbrex "Template — Three Horizons" (tag umbrex:umb),
read on corpus/sheets/sheet_179.jpg frame 2 (S1771–S1780 row-major 5col×2row);
catalog row catalog_umbrex.csv S1782 ("blue curves on axes · Now/New/Next columns
with growth curves · genuine horizon captions: Maintain core 1–3 yrs / Foster
emerging / Seed future"). Observed at the sheet level: value/time arrows, three
captions inside the plot with year ranges, "Your logo here | Source: ___"
footer. The value axis, the FY tick scale, the crossover annotation and the
readout table are kit additions (the corpus page is a blank template with "XXX"
placeholders) built to the DESIGN_PLAYBOOK rules; the shape, the three-band
columns and the in-plot captions are the corpus's. Screenshots:
qa/three-horizons/three-horizons-curves.png.
