# vbar-delta-arrows — Vertical Columns + Benchmark Line + Directional Delta Arrows

WHEN: A "one clear winner against a benchmark" page: single-series vertical columns (one
per item/channel/option) compared to a stated reference level, with the finding's margin
shown as a block arrow. From the Accenture Moneyball marketing-effectiveness deck p16
(accenture__accenture_the_moneyball_moment_for_marketing_in_canada_2019,
sw_sheets/..._s01.jpg row 2), where the claim "the SALES ROI OF TV INCREASED BY 23%" is
carried by one red column, a dashed benchmark line and gain/loss arrows. Use when the
argument is *level vs. benchmark*, not distribution across segments (that's
vbar-grouped-tints).

ANATOMY (1280×720 stage):
1. title   — 64,36, 1152 wide, 2 lines 30px; line 2 in accent (the deck's red-clause device)
2. kicker  — 64,118, 15px bold grey all-caps figure caption + units + footnote marker
3. chart   — inline SVG 1280×720; baseline y=598 (58→1222); 7 column slots of 164.57px,
             centres x = 100 + i×164.57; benchmark dashed line across full plot width
4. arrows  — 56×50 block-arrow group above each non-reference bar, centred on its x
5. spend row — bold share % centred under each bar (y≈666) + "MEDIA SPEND:" gutter label
6. note    — 64, bottom 36, 1112 wide, methodology line with superscript marker
7. footer  — source bottom-left, "16 | SECTION n" bottom-right

SLOTS:
- title: ≤15 words / 2 lines; the operative clause goes in accent colour; both lines carry
  numbers (one absolute margin, one spread) — no bare topic.
- kicker: caption names the unit ("USD per incremental sales dollar") — this page type's
  credibility lives in the unit line. ≤150 chars.
- bars: 5–8 columns. Exactly ONE focus bar (accent). Reference "Overall" is dark grey,
  context bars light grey.
- value labels: "$14.34" inside the bar top, white on dark/accent, ink on light grey.
  2 decimals if <20 units, else integers.
- delta chips: "+22%" / "−15%" (real minus sign, not hyphen); one per non-reference bar
  max; if a delta would read >±50%, sanity-check the benchmark.
- spend row (optional): share of total per column — turns the chart into "where the money
  is vs. where the returns are". Column labels ≤16 chars.
- note: one line, methodology + superscript that matches the footer marker.

FILL:
1. Swap the header `bars = [...]` array: for each value, height = round(value×19),
   rect y = 598−height, inside label y = y+21. The Overall bar sets the benchmark:
   move the two `.bench` line y to 598 − Overall×19 and update its text.
2. Per non-reference bar, set delta text and choose the arrow: positive → tip-up path
   (rotate 180 about the head, as in cols 2/5), negative → tip-down path (cols 3/4/6).
   Fill = .up-accent ONLY for the focus bar, else .down-dark class (grey).
3. Title/kicker/note/footer text per SLOTS. If the brand isn't Accenture, recolour
   --accent/--accent-deep only; keep --dark grey — it's the benchmark role, not decoration.

CHART RECIPE (page type — follow exactly):
- SCALE. Linear, zero-based, vertical: height_px = value × 19 ($15 ≈ 285px) on the
  stage; plot baseline y=598, arrow zone consumes ~60px above the tallest bar so title
  never collides. If swapping units (%, index), choose the multiplier so the tallest bar
  lands 280–300px, keep zero-based.
- BENCHMARK LINE. A dashed rule (#7D7D7D, 1.6px, dash 6 5) across the ENTIRE plot at the
  reference value's height, labelled once at the right end ("Benchmark = $11.79 (…)").
  No y-axis line, no ticks, no gridlines — the inside-bar labels + benchmark carry scale.
- VALUE LABELS. Inside the bar top, centred, 13px bold — colour depends on the bar:
  white on focus/accent and dark grey, ink (#1A1A1A) on light grey. Never a label that
  floats outside and collides with an arrow.
- DELTA ARROWS. Direction = sign (+ up, − down), fill = emphasis (only the focus bar's
  arrow may take the accent hue; all others dark grey). Tip sits 10px above the bar;
  chip is a 56×30 rect with a 20px head; delta text white centred. This is the whole
  argument device — if the deltas aren't the point, delete the arrows, don't dim them.
- ONE ACCENT + GREY RAMP. Exactly one hue (red here): focus bar + focus arrow. Everything
  else lives on the grey ladder: #4D4D4D reference, #BFBFBF context, #7D7D7D text.
  moneyball painted every positive arrow red — that's their brand habit; the kit keeps
  single-accent discipline so the focus bar still reads as THE finding.
- ORDER. Reference first (left), focus second, remaining columns by value or by spend
  share — state the sort in the kicker if not obvious.

VERIFY:
- [ ] Title ≤15 words / 2 lines at 30px; operative clause is in accent colour.
- [ ] Source line bottom-left + "n | SECTION" bottom-right; methodology sup matches footer sup.
- [ ] Exactly ONE bar and ONE arrow carry the accent hue; rest grey ladder.
- [ ] Delta sign ↔ arrow direction consistent everywhere (spot-check each chip).
- [ ] Inside-bar labels legible: white only on dark/accent fills (4.5:1 holds for
      #fff-on-#D8112B and #fff-on-#4D4D4D; ink text on light bars).
- [ ] Benchmark dashed line spans full width and is labelled once.
- [ ] No y-axis/ticks/gridlines; bars zero-based (a truncated column bar is a lie).
- [ ] Zero network requests.

DON'T:
- Repainting every positive delta in the accent hue (source habit; kills the focus).
- Up-arrows drawn pointing down or vice-versa — the rotation math is the one bug class.
- More than one benchmark line / a benchmark above the tallest bar with no room.
- Deltas that don't recompute from the printed values (11.79→14.34 is +21.6%, so "+22%"
  not "+23%" — moneyball's own page fails this; the template shouldn't).
- Truncated value axes, 3D bars, drop shadows.
- Both a benchmark line AND a per-bar delta chip AND a trend line — pick one device.

SOURCE: firm = Accenture. Page p16 of
accenture__accenture_the_moneyball_moment_for_marketing_in_canada_2019 (2019), viewed from
sw_sheets/accenture__accenture_the_moneyball_moment_for_marketing_in_canada_2019_s01.jpg
row 2 col 1. Palette/arrow semantics from
reviews/accenture__accenture_the_moneyball_moment_for_marketing_in_canada_2019.md
(colour system: red = the finding, dark grey = comparison, directional arrows encode
gain/loss; title device: one red clause). Same grammar cross-referenced in the
harvest's catalog (Moneyball "grouped bars by segment + delta arrows").
