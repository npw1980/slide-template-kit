# scatter-bubble-before-after-arrows — Per-item change arrows on a scatter, before/after state pairs

WHEN: An argument about CHANGE in two variables — "X moved a lot here, Y didn't move" — where
each item has a past position and a present position, and the arrow (direction + length) IS the
story. Items sit at their "now" (x, y) coordinates; an arrow from a hollow "before" marker to the
solid "now" marker carries the delta, labeled once per item below the pair. From Accenture's nbn
value report: `accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o` p13
(right panel: before/now circle pairs with dashed transfer arrows + "(142% increase)" labels,
bubble-size key = empty circle per 1M, axis break) — read from
`sw_sheets/accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o_s01.jpg` sheet
row 1, cross-checked with the same device's description in
`reviews/accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o.md`.

ANATOMY (numbered slot map, stage px on 1280×720; SVG user units are 1:1 with stage px):

1. `band` — 0,0 → 1280×104. Deep-violet gradient claim band. Title 64,16 → 1152 wide, 25px bold,
   2-line cap, white.
2. `sub_kicker` — 64,118 → 1152×17. Bold violet panel line ("Work-related activities — weekly
   hours before vs now¹").
3. `sub_line` — 64,139 → 1152×15. Grey line stating both units + arrow meaning + size encoding.
4. `rule_top` — 64,158 → 1152×1. Hairline.
5. `legend_pair` — upper-right, two 11px markers + labels "Before COVID-19" (open ring) /
   "Now" (solid dot) at 916/1030, y 184; size-key note right-aligned 1160,211.
6. `plot` — figure lives at x 120→1160 split by a break, y 254→544. Left segment 0–9 hrs
   (120→772, 72.4 px/hr), break 772→812, right segment 16–17 hrs (812→1160, 348 px/hr). y = 0–65%
   (290px, 4.46 px/%). Gridlines every 10% only (gray ~35%); the break is drawn as a pair of
   slashes at 779/795.
7. `pairs` — 5 `<g class="pair">` groups (Web browsing, Emails, LinkedIn, Conference calls, Work
   tools). Each: `circle.ring` (before, white fill + gray stroke 2.4), `circle.filled` (now,
   gray fill, ink stroke 1), `line.arrow` + gray arrowhead marker (both edges trimmed by the
   radii — geometry rule in FILL), item `name` centered above the pair midpoint (11px, ink),
   `delta` label below at midpoint+30 ("(+7% hours increase)"), `data-delta` attr.
8. `axis_x_title` / `axis_y_title` — bottom-right + rotated left, bold violet.
9. `twin_boxes` — 64/656,612 → 560×60 each, tint-filled: takeaway headlines (title 12.5px bold
   violet + 12px grey line).
10. `footer` — 64→1216, bottom 14: `sup` footnote + source line left, `14 | SURVEY FINDINGS`
    right.

SLOTS:
- `band_title` → ≤15 words / 2 lines. GOOD: names the big movers AND the non-movers
  ("Time spent on work services grew most for conferencing and work tools — enjoyment was
  unchanged"). BAD: "Before vs after: hours spent" (that's a caption, not a claim).
- `sub_line` → must say what the ARROW means (hours change) plus both units + size encoding.
- `pairs[]` → 3–6 items, each = (before x,y / now x,y / millions / signed delta%). Both states
  sit on the SAME y usually (this chart's y is "who enjoy %" and rarely moves — if y is flat,
  arrows are horizontal; that's fine and common).
- `delta` → one line per pair "(+142% hours increase)" — the % is the headline number; ≤ ~28
  chars. No signed deltas without a following "… increase/decrease" word.
- `twin_boxes` → 2 boxes max, ~7 words title + 25-word line; one "where it moved" + one "where
  it didn't" (a contrast pair, not two unrelated notes).
- `legend_pair` → exactly 2 states ("Before/Now"); a 3-state change chart is a different story
  (use the dots version in scatter-bubble-quadrant-cluster or split into two panels).

FILL:
1. Swap band/kicker/subline text; keep `sup 1` markers (the delta methodology is survey-derived,
   so it needs its footnote).
2. For each `<g class="pair">`: set `data-xb,data-yb` (before coords in plot units) and
   `data-xn,data-yn` (now coords) plus `data-m` (millions) and `data-delta`. Radius rule
   `r = 7*sqrt(m)`; both markers of a pair share r (the base is constant per item, only position
   moves). If your base changes, draw two different radii and mention it in the sub-line.
3. The arrow: `line` x1 = ring center + r + 4 toward now, y1 = yb; x2 = now center − r − 4, y2 =
   yn, `marker-end=url(#ah)`. For long arrows draw dashed grey 1.4; the arrowhead triangle is the
   only solid element. No arrow if xb≈xn and yb≈yn (then draw a single point with a "flat"
   annotation instead).
4. Position labels at `(xb+xn)/2` (name 16px above the higher of the two markers, delta 30px
   below the lower) — midpoint of the PAIR, not of the arrow, so they never collide with the
   shaft. If two pairs overlap (LinkedIn/Conference calls here), nudge labels apart by ±14px in y.
5. Axis break: when your x range has a big empty gap, split the axis as here (short linear
   segments + double slashes + restated ticks); if the range is continuous, delete the break
   group and stretch segment 1 across the full plot width.
6. Recolor with tokens: state pair is gray (`--gray-1` fill on `filled`, `--gray-2` stroke on
   the ring) — color is reserved for the arrow/ink story. Set `--accent`/`--accent-ink` for the
   claim band + titles; swap to another violet-family pair, never green/red for "change".

CHART RECIPE:
- **Scales.** Both axes linear, zero-based, rounded headroom over data (x 0→17 hrs via the break,
  y 0→65%). Plot x splits 120→772 for 0–9, 812→1160 for 16–17; y 290px over 65 points = 4.46
  px/%. Gridlines only on the y ticks (horizontal rules carry the % reading); x gets ticks +
  numbers but no vertical rules, keeping the arrows on the cleanest canvas. A break must be
  explicit (double slashes + tick relabel), never implied by stretching.
- **Value-label placement.** The only per-item numbers are the deltas "(+142% hours increase)",
  centered below the pair, grey 11px — never on the arrow shaft. Item names sit above the pair
  (11px, ink, 2-line max). No value for x/y positions: position is the value; the reader reads
  both states off the gridlines. Leaderless floating labels = chart-junk; everything belongs to
  a pair group.
- **One accent + gray.** Before/after states read by SHAPE not hue: open ring = before, solid
  fill = now, both gray. The hue budget goes to the claim band and the axis titles (one violet
  family, ≤3 lightnesses on the white field). If you must encode a category, split into two
  side-by-side panels rather than tinting pairs by class — tinting pairs kills shape-legibility
  of before/now.
- **Arrow rules.** One arrow per item, arrowhead points to NOW. Label the arrow exactly once
  (below, per-item). No arrow bundles, no "all items flow to one target" spaghetti, no arrows
  with numbers on the shaft. If >5 items have real movement, the page becomes a movement map,
  not a change chart — split items across a twin-panel or two pages.
- **Axis/unit rules.** Units stated in sub-line AND axis titles; hours numbers without "hrs"
  suffix, percents with "%". The % on the delta line is hours-change %, which is a THIRD unit
  and must be named in words ("hours increase"), because "(+142%)" alone could read as either
  axis. Superscripts ¹ for survey-derived deltas; NOTE line says so.
- **Emphasis:** the change chart gets zero extra emphasis devices — no callout box, no shaded
  region, no accent bubble. The arrows are the emphasis. The only permitted additions are the
  two takeaway boxes (each ≤60px tall), which sit OUTSIDE the plot.

VERIFY:
- [ ] Title ≤15 words / ≤2 lines, claims a mover + a non-mover.
- [ ] SOURCE line bottom-left, NOTE + `¹`; `NN | SECTION` stamp bottom-right.
- [ ] Exactly one hue + gray; before/now distinguished by shape (ring vs solid).
- [ ] One arrow per item, labeled once below the pair; no shaft labels; no arrow crossing a
      legend or another arrowhead.
- [ ] Axis break drawn explicitly if used (slashes + relabeled ticks); otherwise continuous.
- [ ] 4.5:1+ text contrast; no legend collision (size note stays top-right, pairs stay inside
      plot bounds).
- [ ] Twin-box takeaways: one "moved" + one "didn't", ≤30 words each.

DON'T:
- Color the before/now states (green→red "traffic light" or violet→orange) — shape carries the
  state; hue carries the category elsewhere. The corpus rejects multi-hue "change" charts.
- Put the delta number ON the arrow or above every bubble; one number per item, one place.
- Add a callout box or shaded region — this variant's emphasis is the arrow set already.
- Fake the axis break: stretching one axis to make 14 hrs look like 16 breaks scale honesty.
- Let names collide with the arrow (LinkedIn/Conference-calls risk zone): labels go mid-pair with
  the ±14px nudge, never centered on the shaft.
- Topic titles ("Before vs now, hours spent"); the claim band names the movers.

SOURCE: `reviews/accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o.md` +
`sw_sheets/accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o_s01.jpg`
(sheet 2 row 3 = slide p13 right panel; cross-checked against p12/p22/p24 descriptions in the
same review). Firm fonts: GT/Eurostile-family custom — `"Helvetica Neue", Arial` display stack
stands in; body Arial/Calibri (see TEMPLATE_SPEC.md font clause). Hexes #7B1FF0/#6E00C9/
#C9A9E9/#7D7D7D from the review's color system, not invented.
