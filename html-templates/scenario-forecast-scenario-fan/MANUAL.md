# scenario-forecast-scenario-fan — One history, three diverging paths to 2031F, with assumption strip (1280×720)

WHEN: A "how much depends on the assumptions" page — one observed series that splits into
named scenarios (upside / base / downside) with each path's end value and likelihood visible.
From PwC Strategy& — Copernicus Market Report 2019, p86 (sw_sheets/pwc_strategy__
pwc_copernicus_market_report_2019_s08.jpg, sheet floor(86/10)=8, row 1 col 2: line projections
run long past the decision year, blue line + grey, 2-line title) and Strategy& EV Sales Review
Q4 2022 p16 (s01.jpg, row 2 col 2: wide single-panel forecast, F-suffixed years, ONE arrowed
% callout on the chart, disciplined single-figure annotation). The three-path fan is this
family's signature device; the corpus rule it enforces is one accent — likeliest solid,
alternatives grey.

ANATOMY (1280×720; SVG numbers == stage px):
1. kicker      — 64,36, 1152 wide; bold navy lead + unit + "three cases" + sup.
2. title       — 64,64, 1010 wide, 28px/36px, 2-line max-height gate.
3. rule-top    — 64,146, 1152×1px.
4. chart       — ONE inline SVG, viewBox 0 0 1280 720, occupying x 98→1216, y 185→596:
   - plot box: x 110→1060 (14 points, x(i)=110+i×73.077; 2018..2031F), y(0)=575, y(36$B)=200,
     y(v)=575−v×10.4167; gridlines every $6B
   - "today" hairline: dashed vertical at x(5)=475.4; axis years 2024F..2031F F-suffixed in accent
   - fan fill: polygon = upside path forward + downside path reversed, grey #9AA3AF @10%
   - history polyline: ink navy solid 2.75px, points 0..5
   - UPSIDE: grey dashed 7/5 2px · BASE: accent solid 3px, drawn last · DOWNSIDE: lighter grey dotted 2.5/4
   - endpoint markers: hollow circles at x=1060 (base r=4.5 accent, others r=4 grey) + solid dot at the split
   - right-edge labels x=1075: NAME / $VALUE bold / "N% CAGR · N% likelihood" — one group per path
   - one arrowed annotation inside the fan (the EV-p16 device), ≤3 lines
5. strip       — 110,612, three scenario-assumption cards (1106 wide, 16 gap): left-border
   colour-coded (base = accent, alternatives = grey), name + one-sentence condition.
6. source      — 64, bottom 26, methodology + likelihood basis + sup.
7. running head— right 64, bottom 26, "PAGE | SECTION" bold navy.

SLOTS:
- title: ≤15 words / 2 lines, names the swing factor and the base outcome: "Scenario paths split
  on capacity timing — base case lands at $25.1B by 2031F". A title that merely says "scenarios"
  is a topic, and this template dies on topics.
- kicker: metric, unit, horizon, "three cases", sup.
- paths: EXACTLY three. Two is a before/after (use the split-line template); four is a hedge.
- base path: must be labelled "BASE — LIKELIEST" and wear the accent; it is the anchor the
  other two read against. Likelihoods must sum to 100 (15/60/25).
- endpoint labels: one per path; value + CAGR + likelihood. The CAGRs must recompute from the
  plotted endpoints (start 2023 value, end 2031F value): e.g. 10.2→25.1 over 8y = 12%.
- strip cards: one sentence each — the CONDITION that opens that path, not a restatement of
  the value. 110 chars max per card.
- annotation: the spread in one readable ratio ("base is 36% below upside…"). One per page.
- F-suffix on all axis years after today; today dot solid, path endpoints hollow.

FILL:
1. Replace arrays in the header comment + the four polylines:
   history (points 0..5 → .line-hist) and the three scenario paths (points 5..13 → .line-alt,
   .line-alt2, .line-base LAST). x(i)=110+i×73.077; y(v)=575−10.4167v. All three paths must
   share the split point (475.4, y(start value)) — that is the whole point of the fan.
2. Fan fill: rebuild the .fan polygon as upside-forward + downside-reversed using the NEW
   path coordinates.
3. Scale: if a new upside peak exceeds $36B, re-derive the y factor AND all gridline y-values
   AND the $-axis labels from one formula (y(v)=575−(375/vmax)·v); never stretch one line alone.
4. Right-edge labels: move with endpoints; keep the base label visually centred between the
   other two; likelihood numbers live ONLY here and in the kicker's "three cases" — not on the lines.
5. Strip cards: rewrite conditions when scenarios change (they are the page's actual argument
   surface — if the conditions are vague, the deck will not survive the client meeting).
6. Annotation text + arrow: recompute the ratio from endpoints, move the arrow's path/lines to
   point at the upside line between x≈900-1000.
7. Recolor: swap --accent (+ --accent-deep). Upside/downside stay grey — recoloring them to
   green/red is the one edit that breaks the kit (a third and fourth hue enter the page).

CHART RECIPE:
- Scale: zero-based linear on one axis, unit stated once ("$ billions" top-left). All three
  paths share it — scenario comparison IS the comparison, so unequal scales are fatal.
- Encoding per path: BASE = solid accent 3px (likeliest; reads first even under the fan),
  UPSIDE = dashed grey (gray-2), DOWNSIDE = dotted lighter grey (gray-3). Identity comes from
  line STYLE + right-edge labels, never from green/amber/red weather colours.
- Fan fill: grey between upside and downside only, 10% opacity, no stroke — it says "the
  plausible envelope", not "another series". Do not add a second fan for confidence bands.
- Value labels: endpoints only (right edge), each group exactly: NAME over $VALUE over
  "CAGR · likelihood". No mid-path labels; the paths are 1-2cm apart mid-chart and labels collide.
- Forecast marking: shared split dot + today hairline + "F" axis suffix. The fan start IS the
  forecast divider; do not also shade the right half.
- Axis/unit: y gridlines every $6B with "$N" ticks; x ticks every 2 years, forecast years accent-tinted.
- One arrowed callout inside the fan (≤3 short lines) stating the spread as a ratio; it must
  land on a real geometric gap (upside vs base), not empty space.
- Likelihood math honesty: 15+60+25=100 shown twice (labels) is a cross-check — if you change
  one, change the kicker/strip story to match (e.g. base condition weakened ⇒ base likelihood down).

VERIFY:
- [ ] Title ≤15 words / 2 lines (max-height gate clips — re-write if clipped).
- [ ] Three paths, one solid accent (base), two grey dashed/dotted; zero extra hues.
- [ ] All three paths share the split point at today; endpoint dots present.
- [ ] CAGRs recomputed from endpoints; likelihoods sum to 100.
- [ ] Fan touches both boundary lines exactly (its edges ARE upside/downside polylines).
- [ ] Right-edge groups: 3, non-overlapping, base between the others.
- [ ] Assumption strip: 3 cards, base card has the accent left-border, ≤110 chars each.
- [ ] Source line + matching sup; running head present; text contrast on white ≥4.5:1.
- [ ] Exactly one arrow annotation; no legend (line styles + end labels are the legend).

DON'T:
- Green/upside, red/downside — that is weather, not a scenario model, and it injects 2-4 hues.
- A "fourth line" for policy/aspiration — if needed, it is a dashed line out of scope of this page.
- Endpoint values that don't match the CAGRs printed under them, or likelihoods that don't sum to 100 (client will spot it; it reads as a guess).
- Topic title or bare "scenarios" kicker — the swing factor (launch cadence / capex / policy) belongs in the title.
- Shading the fan with hatch/rainbow, or adding confidence-band stripes; grey fill only.
- Failing to define the base's likeliness: an unlabeled "base" invites the client to discount it.
- Mid-chart labels and more than one arrow callout — the chart-junk failure mode of the 10-hue pie pages.

SOURCE: PwC Strategy& — Copernicus Market Report 2019 p86 (sw_sheets/pwc_strategy__
pwc_copernicus_market_report_2019_s08.jpg row 1 col 2) for long-horizon line projection with
blue+grey stack; Strategy& EV Sales Review Q4 2022 p16 (sw_sheets/pwc_strategy__strategy_
electric_vehicle_sales_review_q4_2022_2023_s01.jpg row 2 col 2) for F-suffixed wide forecast,
single arrowed callout, legend row discipline. Analysed in
reviews/pwc_strategy__pwc_copernicus_market_report_2019.md (palette anchors #1F3864 /
#1E5A90 / #A8C8E8, orange-only-for-negatives rule) and
reviews/pwc_strategy__strategy_electric_vehicle_sales_review_q4_2022_2023_slides.csv row p16.
Palette is the same PwC Strategy& two-hue system; the scenario-fan geometry (shared split point,
envelope fill) is kit standard, verified against the exemplar chart pages rather than invented.
