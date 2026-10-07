# dual-axis-combo-column-line — Columns (left currency axis) + Count/Rate Line (right axis) with commentary rail

WHEN: The "value and volume moved differently" analysis page — the KPMG Venture
Pulse workhorse (kpmg__kpmg_venture_pulse_q3_2024_2024, p12/p13/p15; sw_sheets/
kpmg__kpmg_venture_pulse_q3_2024_2024_s01.jpg rows 2-5). Per review §5: "quarterly
column + line on two axes — columns = $ value (left), line = deal count (right),
2018 → Q3'24, with value labels printed on every bar", fixed series palette (cyan
#00B8F6 primary chart fill), partial years flagged "2024*". Review §71 gives the
skeleton: chart block left/centre, ~28–30% commentary column right, legend row
under the chart, 6pt source line. Use when two metrics share one x-axis but two
different units AND the whole point is their divergence — for one metric with one
unit, a plain vbar/line template is the honest choice (see DON'T).

ANATOMY (1280×720 stage):
1. kicker    — 64,36, 860 wide (clears the nav strip), 15px grey; bold navy lead-in + both units + restatement sup.
2. title     — 64,64, 1000 wide, 28px/36px, ≤15 words / 2 lines (max-height 72px clips = the gate). Line 2 = operative clause in cyan-deep `em`.
3. nav strip — right 64,34; 4 chips (Global | Americas | EMEA | APAC); active chip solid `--blue`. Swap for the deck's real view-switcher or delete and widen title to 1152.
4. rule-top  — 64,138, 1152×1px `--rule`.
5. chart     — ONE inline SVG, viewBox 0 0 1280 720, 1 unit = 1 stage px:
   - plot box: x 110→830 (chart block), y 205→565; bar centres cx(k)=145+k×95 (k=0..7)
   - LEFT axis US$bn 0→24, labels right-aligned to x=98, gridlines every $4bn
   - RIGHT axis deal count 0→1,000, labels left-aligned at x=842, unit head "deals" top-right
   - cyan bars w=46 (current bar filled `--accent-deep`), ink line w=2.6 with hollow dots
   - value labels: grey 11.5px above context bars, bold-ink 13.5px over the CURRENT bar; ink label at the line's last point only
   - ONE annotation: blue dashed leader + claim text (no fill box — rail is nearby)
   - legend row under chart at y≈628: cyan chip + "left axis" wording, ink line+dot + "right axis" wording, partial-year note
6. commentary rail — 930,168, 286 wide: 11px letterspaced header + 3 numbered reads (26px bold navy numeral + 13px/17px text; key figures in cyan-deep `i`).
7. source    — 64, bottom 26, 1010 wide, 11.5px grey, methodology + sup matching the kicker.
8. running head — right 64, bottom 26, bold navy "PAGE | SECTION".
NO third data element exists — legend + rail text are the only remaining marks.

SLOTS:
- title: ≤15 words / 2 lines; must carry both curves' divergence quantitatively ("value recovered, count −35%"). A topic line ("funding trends") fails the gate.
- kicker: names BOTH units and which axis each reads, period, restatement/method sup. Good: "announced deal value (US$bn, left axis) and deal count (right axis)". Bad: kicker that only names the bars.
- bars: 7–8 x-points. ONE series only (the currency/volume series). More bar series = pick the stacked-100col or grouped vbar template instead; a combo page supports exactly one column story.
- line: ONE series, unit different from bars by construction (that's why there are two axes). Count, rate, %, index — anything but the bar unit.
- value labels: default = CURRENT bar + line's last point only. KPMG prints all bars; the review scores that "decoration over data" (review §66) — you may print context bars in grey 11.5px if the audience reads numbers off charts, but never both series' full label sets.
- emphasised bar: the current/partial bar filled `--accent-deep`; its label bold-ink. Exactly one bar gets emphasis.
- annotation: one dashed leader + ≤2 lines of claim text; leader colour `--blue` (structure), never the data colours, or it reads as a series.
- commentary rail: exactly 3 numbered reads, each a sentence with ≥1 number; the rail replaces "so what" text on the exhibit. If the page has no reads to give, delete the rail and widen the chart to x=1150.
- partial-year flag: the `*` italic x-label + legend clause is the ONLY forecast marker. Solid legs everywhere (KPMG style) — no dashed leg, no shaded zone.
- source: must define restatement scope, partial-year boundary, exclusions.

FILL:
1. Header-comment DATA ARRAYS: `years`, `bars` (US$bn, left), `line` (count, right). Keep 8 points; both scales then stay valid without touching geometry.
2. Bars: y = 565 − value×15 (each rect height = 15×value); recoloring a different brand = change `--accent`/`--accent-deep` ONLY (keep the deep/light pair — light = context bar, deep = current).
3. Line: y = 565 − count×0.36 per point; edit the polyline points + dot cy. If the range differs, rescale: right-axis max must be round (1,000 here); px/unit = 360/(axis max), then move the last-point label with it.
4. Axis heads "US$bn"/"deals" and legend wording carry the units — change the three text strings, not just numbers.
5. Different partial-year flag (e.g. FY not calendar): replace "2024*" label and the legend clause "* 2024 = year to 30 Sep" together.
6. Recolour for another firm: bars keep the role (one accent hue), the line stays ink/navy — NEVER make the line a second hue; if the line is coloured, readers read two stories where there is one.
7. If there is no partial year: drop the `f` class + legend asterisk clause; the * flag is the only forecast device.

CHART RECIPE (dual-axis combo — follow exactly; this is the page a data person swaps numbers into):
- SCALES. Both axes linear, zero-based, drawn to the SAME plot box (shared gridlines — every gridline is a legitimate reference on both sides: $4bn on the left IS 111 deals on the right — never draw one gridline set per axis). Left axis: the BAR metric, tick steps at round numbers. Right axis: the LINE metric, round ticks (0/250/500/750/1,000). Choose the right-axis max so line points sit in the lower/middle band — a line riding the ceiling hides its own wiggle.
- AXIS/UNIT RULES. Each unit appears exactly twice: once as an axis head (top of that side) and once in the legend wording ("US$bn (left axis)", "(right axis)"). Tick labels carry bare numbers. The unit's horizontal position must match its colour: left labels grey right-aligned at x=98, right labels lighter-grey at x=842. No axis titles along the side, no rotated axis labels.
- EMPHASIS (one accent). Bars = the one hue (cyan #00B8F6; current bar its darker lightness). Line = ink/navy — it is an axis reading, not a second hue. Annotation leader = structure blue, third colour never touches data. Gridlines/rails = grey ramp. Total data hues: exactly 1.
- VALUE-LABEL PLACEMENT. Bar labels centred 8px above bar top (grey 11.5px; current bar bold-ink 13.5px — size+weight, not colour, carries the emphasis). Line labels: last point only, 15px bold ink just above-right of the last dot, series word ("deals") under it in grey. Never label every line point; the line's shape is its message. If a bar label and line point collide, the line label wins (drop that bar's grey label).
- EMPHASIS RULE. One emphasised bar (current period, `--accent-deep` fill) + one emphasised line dot (bigger stroke). One annotation. One number in the rail text. That's the whole emphasis budget; more than three highlight devices and the page argues with itself.
- DUAL-AXIS HONESTY. Two axes mean the eye cannot compare bar heights to line heights — say so in the title/rail by making the ARGUMENT about each series against itself (levels, not crossings). Never scale an axis purely to make the two curves touch or cross; that is the dual-axis lie. If both metrics could share one zero-based scale without lying, use a single axis and the line-trend/vbar template instead.

VERIFY:
- [ ] Title ≤15 words / 2 lines, states both curves' relationship quantitatively.
- [ ] Exactly one data hue; line is ink, not a second colour.
- [ ] Both axes zero-based, units visible once per axis side + legend.
- [ ] One emphasised bar, one annotated event, one labelled line point (max).
- [ ] Partial year flagged by * x-label + legend clause only (no extra shading).
- [ ] Source line defines restatements + partial-year cutoff; sup matches kicker.
- [ ] Page number / section running head present bottom-right.

DON'T:
- Topic titles ("Global venture funding trends") — the whole point of a combo page is the divergence; make it explicit.
- A second bar series or a coloured second line — two accents turn this into a fireworks chart; pick the right template family.
- Scaled-to-cross axis games — never tune an axis max so the curves visually intersect "for the story".
- Dashed legs / forecast shading in addition to the * flag (double-flagging; KPMG uses the solid leg + * only).
- A 10-bar value-label wall (the corpus habit the review dings — default is label-the-now only).
- A 4th rail read, or rail text without numbers (it is not an opinion column).
- SmartArt/Chart-recreated axes drawn in separate SVGs — one <svg>, one coordinate system, or the two axes drift on export.

SOURCE: kpmg__kpmg_venture_pulse_q3_2024_2024 p12/p13/p15 (sw_sheets/kpmg__kpmg_venture_pulse_q3_2024_2024_s01.jpg — pages 11–20 grid). Palette + "column + line on two axes" convention + ~28–30% commentary column: reviews/kpmg__kpmg_venture_pulse_q3_2024_2024.md §"Charts" (cyan #00B8F6 measured) and §71 (body grid), weaknesses §66 (value-label-everywhere, dual-axis comparability) encoded as the trimmed labelling rule. Chart+commentary pairing corroborated by kpmg__kpmg_kpmg_our_impact_plan_2022_update_2022 p13 (column + red dual-axis line) and pwc_strategy__pwc_namibia_national_budget_2024_25… p05 (bars + line) — see sibling template dual-axis-combo-bar-line-fiscal.
