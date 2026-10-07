# scenario-forecast-split-line — Actual-solid / forecast-dashed line with widening uncertainty band (1280×720)

WHEN: A "where is this metric heading, and how sure are we" page — one market/quantity
series with observed history plus a modelled projection, and the reader must see exactly
where fact stops being fact. From PwC Strategy&, Copernicus Market Report 2019, p24
(sw_sheets/pwc_strategy__pwc_copernicus_market_report_2019_s02.jpg, sheet floor(24/10)=2,
row 1 col 5): "line forecast (Big Data market)", blue line + grey area, left text /
right chart, dashed-border % callout; p86 (s08 row 1 col 2) is the second exemplar with
a 2-line title and a line run long past the decision year. The EV Sales Review p16
(s01 row 2 col 2) supplies the axis habit: post-today years carry an "F" suffix.

ANATOMY (1280×720 stage; the inline SVG uses the same numbers as px):
1. kicker      — 64,36, 1152 wide, 15px grey, bold navy lead-in + unit/period + sup marker.
2. title       — 64,64, 1010 wide, 28px/36px Helvetica bold, max-height 72px (2 lines = MBB gate).
3. rule-top    — 64,146, 1152×1px hairline.
4. lead        — 64,172, 310 wide, 15px bold navy, 3–4 lines. The "so what".
5. points      — 64,268, 310 wide, 3 bullets, 12.5px grey with accent squares; one bold accent number per bullet.
6. callout     — 64,472, 310 wide, DASHED 1.5px accent border; big "2.7× — ~15% CAGR" + method sentence + sup.
7. chart       — ONE inline SVG, viewBox 0 0 1280 720:
   - plot box: x 470→1186 (15 points, x(i)=470+i×51.143), y 565 (=$0) → 190 (=~26 $B), y(v)=565−v×13.393
   - gridlines every $5B; year ticks every 2 years, forecast years "F"-suffixed in accent
   - today/model-start hairline: vertical dashed grey at x(7)=828 (2023)
   - band polygon (light blue #A8C8E8 @40%) around the forecast leg, widening per bandPct
   - ACTUAL polyline: ink navy #1F3864, 2.5px, points 0..7
   - FORECAST polyline: accent #1E5A90, 2.75px, DASHED 7/5, points 7..14
   - end marker: hollow circle r≈4.5 at line end; value labels end-of-line + at hairline only
8. source      — 64, bottom 26, 1010 wide, 11.5px grey, methodology sentence + sup.
9. running head— right 64, bottom 26, bold navy "PAGE | SECTION".

SLOTS:
- title: ≤15 words / 2 lines. Must state the path in numbers ("2.7× path to $22.8B by 2030F"), not "market outlook". The em clause is the whole argument.
- kicker: metric + unit + period + model + sup; never restates the title.
- lead: one sentence connecting history to projection — "revenues compounded from X to Y; the model projects…".
- points: exactly 3, each with one bold number. Long filler here means the chart is too small — cut, don't shrink the chart.
- callout: the CAGR/summary claim as ONE number phrase. Max ~110 chars of sub-text. This box IS the forecast's headline — if it reads like boilerplate, the page failed.
- bandPct: the uncertainty range; 3–15% widening across the horizon. A constant band or ±1% band means you have not thought about the range.
- value labels: 2 max (line end + baseline). Bold $ value over grey year sub-label.
- source: names the model + calibration date; sup must match the kicker's sup.

FILL:
1. Replace the three data arrays in the HTML header comment AND the two polylines:
   actual (points 0..7 → line class .line-act) and forecast (points 7..14 → .line-fc).
   For each forecast point compute ( x(7+i), y(v) ) with x(i)=470+i×51.143, y(v)=565−13.393v.
2. Band: recompute the .band polygon points = bandUp forward then bandLo reversed;
   bandUp/Lo = ( x(7+i), y(forecast[i]×(1±bandPct[i]/100)) ).
3. Gridline labels: if the new peak needs more than $26B, change the y scale factor and every
   y1 coordinate, the 6 gridline y-values, and the $-axis labels together (they all derive from one formula).
4. Axis years: edit the 8 .xlab texts; every year after the hairline keeps its F suffix and .f class.
5. Move the .today hairline x1/x2, the .line-fc start, the polygon first point and the
   "$8.5B/2023" pair together — they are the SAME moment (today/model start).
6. Callout + title + kicker: new CAGR must be derivable from the two endpoints you plotted;
   check: end/start^(1/Y−1) − 1. If the chart and the % disagree, fix the chart.
7. Recoloring for another firm: change --accent and --band (+ --accent-deep for heads). The
   actual line keeps --ink navy so solid-vs-dashed contrast survives any single-hue swap.

CHART RECIPE:
- Scale: zero-based linear, unit = $B (or the domain's own unit stated once on the plot,
  "$ billions" top-left). No dual axes here; the band already encodes uncertainty, so a
  second axis for "growth %" is redundant — put growth in the callout instead.
- Scales honest: the forecast leg shares the exact gridline family with the actual leg;
  no break marks, no compressed post-2023 segment (the corpus sin: compressed-forecast bars).
- Line roles (one accent + gray, per the PwC two-hue discipline): history = ink navy solid,
  forecast = single accent dashed, band = one lightness step of that accent at low opacity.
  Nothing else takes hue; grey is reserved for axis/labels/hairlines.
- Value-label placement: end-of-line only ("$22.8B" bold over "2030F" grey, anchored end at
  the last point) plus the baseline value at the today hairline. Mid-point labels forbidden —
  they become chart-junk on the forecast leg where points are close.
- Forecast marking — exactly three cues, all three required: dashed stroke; "F"-suffixed axis
  years after today (accent-colored ticks); the vertical today hairline + the "MODEL FORECAST"
  caption above the band. A fourth cue (a "PROJECTED" box, a shading of the whole right half
  with a second hue) is over-signalling — pick one system.
- Band rule: starts at ZERO width at the today hairline and widens monotonically to the end
  (~±1–3% first year → ~±12–17% last year). Band is a range, not a second series: no band line
  stroke, no band labels, the center line carries the numbers.
- One callout per page (the dashed box), one arrow/claim max on the chart itself.
- Axis/unit: years right-anchored every 2nd tick with F suffix; y ticks every $5B labelled
  "$N"; dollar sign appears on every y tick once.

VERIFY:
- [ ] Title ≤15 words, ≤2 lines at 28px (the max-height clips — if clipped, your title is wrong).
- [ ] Source line present bottom-left, ends with sup that matches kicker sup.
- [ ] Running head "NN | SECTION" bottom-right.
- [ ] Exactly one accent hue on the page (#1E5A90); orange/negative hue unused.
- [ ] Forecast leg dashed + F-suffixed ticks + hairline all present and consistent.
- [ ] Band touches the line at the hairline (zero width) and widens.
- [ ] CAGR in callout recomputed from plotted endpoints — agrees to 1pt.
- [ ] Text over accent/white passes 4.5:1 (all text is ink or grey on white here; value labels stay ink/accent — never light blue text).
- [ ] Page number = running head.

DON'T:
- Topic titles ("Big Data market forecast") — this is a CLAIM template.
- A forecast line that silently continues as a solid line (the #1 corpus failure — reader
  assumes fact).
- A band drawn as a second solid series, or one filled with a rainbow/hatched pattern.
- More than two value labels on the line; more than one callout; legends for two lines
  where position + stroke style already say which is which.
- Wall-of-text kicker/lead that competes with the 310px column; if the bullets run long,
  the argument is the bullets' page, not a forecast page.
- Trailing decimal noise: "$22.83719B" — one decimal max.

SOURCE: PwC Strategy& — Copernicus Market Report 2019, pages 24 (sw_sheets/pwc_strategy__
pwc_copernicus_market_report_2019_s02.jpg, row 1 col 5) and 86 (s08.jpg, row 1 col 2);
Strategy& Electric Vehicle Sales Review Q4 2022, page 16 (sw_sheets/pwc_strategy__strategy_
electric_vehicle_sales_review_q4_2022_2023_s01.jpg, row 2 col 2) for F-suffix + callout-arrow
habits. Analyzed in reviews/pwc_strategy__pwc_copernicus_market_report_2019.md (colour:
navy #1F3864 / mid-blue #1E5A90 / light #A8C8E8, grey, two-hue discipline) and
reviews/pwc_strategy__strategy_electric_vehicle_sales_review_q4_2022_2023_slides.csv (row p16).
