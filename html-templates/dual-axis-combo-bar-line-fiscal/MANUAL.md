# dual-axis-combo-bar-line-fiscal — Fiscal-Year % Bars (left) + Money Line (right), Actual/Estimate/Budget qualifiers

WHEN: A policy/budget "the ratio is rising and so is the money" page in the PwC
Namibia idiom — crimson % columns with printed labels + a black currency line, on a
fiscal-year axis whose years carry Actual/Estimate/Budget qualifiers (source:
pwc_strategy__pwc_namibia_national_budget_2024_25_for_our_humanity_now_s_t, p05/p06
"Interest Repayment" exhibit; sw_sheets/pwc_strategy__..._s00.jpg). Review palette:
crimson ≈ #C4172C–#D6006C dominant series, amber #E87722 / yellow #F8C820 highlight,
charcoal #3E474D; footer convention "deck tag left; month + page number right";
triangle motif cluster top-right. Use when one metric is a SHARE/PERCENT and the
second is its ABSOLUTE money twin — the dual-axis justification is that both are
the same underlying fact read two ways; for two unrelated metrics prefer
dual-axis-combo-column-line.

ANATOMY (1280×720 stage):
1. kicker    — 64,36, 1000 wide, 15px; crimson bold lead-in, BOTH axis assignments named inline, nominal-basis sup.
2. title     — 64,64, 1080 wide, 28px/36px, ≤15 words / 2 lines (max-height 72px = gate). Line 2 operative clause in crimson.
3. brand echo — right 64,36; three 11×14 triangles (grey / crimson / amber) — the firm's motif cluster, pure decoration, no meaning.
4. rule-top  — 64,138, 1152×1px `--rule`.
5. chart     — ONE inline SVG, viewBox 0 0 1280 720, 1 unit = 1 stage px:
   - plot box: x 110→1130 full width (no commentary rail — the chart IS the page), y 205→565
   - bars w=64 centred cx(k)=174+k×127.5 (8 fiscal years)
   - LEFT axis 0→16% step 2%, tick labels with % suffix (unit lives in ticks here, as the firm does it); RIGHT axis 0→16,000 N$m step 2,000 + axis head "N$ millions"
   - crimson bars = actual years; amber bars = Estimate/Budget years (fill flag, same series)
   - black line w=2.6 with hollow white dots; ink end label "15,900 / N$m" above the last dot
   - ONE annotation: grey dashed leader + 2-line claim above the 2021/22 step
   - legend row at y≈648: crimson chip "(left axis)", black line chip "(right axis)", amber swatch "Estimate / Budget years"
6. fiscal qualifiers — second x-line under each year: "Actual" grey-italic / "Estimate|Budget" amber-italic. This line is load-bearing, not decoration.
7. source    — 64, bottom 26, 960 wide, 11.5px grey, appropriation-source + basis + estimate/budget caveat.
8. footer    — right 64, bottom 26: "PwC Namibia · <Month Year> | <page>" — deck tag + month + page per firm convention (no section running head on this variant).

SLOTS:
- title: ≤15 words / 2 lines, a ratio claim with a number ("15 cents of every rand") + the consequence clause. Topic titles fail (the deck's own titles were graded as failing wholesale — this slot fixes that).
- kicker: names which axis each series reads AND the basis (nominal, fiscal year). One sentence ≤200 chars.
- bars: 8 fiscal years max (labels collide beyond that at 1280 wide). One series. If you have two % series this is the stacked/share family, not this page.
- line: one money series whose unit cannot be a % (currency, tonnes, FTE). That unit difference is the entire license for the right axis.
- bar labels: printed INSIDE the bar top in white bold 11.5px (final bar 14px) — on a dual-axis page where the line rides above the bars, printed-above labels collide with it; inside-the-bar is the clean side of the house habit (PwC prints inside dark columns too). Emphasis is size/weight, colour stays white.
- projected years: fill amber + italic amber qualifier word; the boundary year is stated once in the legend, once in the x-qualifier. Do not also dash the line or shade the plot — that triple-flags.
- line label: last point only ("15,900 N$m"). Mid-point labels are allowed ONLY where the annotation references a value (then 13px ink, not bold).
- fiscal qualifiers: exactly the words Actual / Revised Estimate / Budget (or "Estimate"); any other qualifier vocabulary ("Projected", "Outlook") is the deck's business, keep them consistent across the whole deck.
- brand echo: three triangles max; deleting them is fine for other firms (that flag exists nowhere else).
- footer month = the publication month, not the fieldwork date.

FILL:
1. Header DATA ARRAYS: `fyears`, `bars` (%), `line` (N$m). Geometry: bar y = 565 − pct×22.5 (height = 22.5×pct); line y = 565 − $mn×0.0225.
2. Rescale when ranges differ: pick round axis maxes (left: step 2–4%; right: round thousands). px per unit = 360/max, redraw gridlines + BOTH tick label columns at the same 9 y-positions — gridlines belong to both axes jointly, never draw separate sets.
3. Projection boundary: set `class="bar proj"` (amber) from the first Estimate/Budget year onward AND flip that year's qualifier to `class="xq proj"`. Both together or the flag is ambiguous.
4. Different brand: swap `--accent`/`--accent-deep` (bars) and keep the line `--ink` — do NOT recolor the line; it is an axis reading. Amber stays "projected" or is deleted.
5. Non-fiscal x-axes (quarters/months): replace the year strings; the qualifier line is optional but then delete the legend's amber swatch too if nothing is projected.
6. Emphasis dial: for a denser data person, grey labels + one bold end bar; for exec skims, delete all grey labels and keep the two bold ones. Numbers, not colours, absorb the audience.

CHART RECIPE (dual-axis combo — the exact swap contract):
- SCALES. Both linear, zero-based, ONE shared gridline set (y = 565 − v×360/axis_max — a gridline is valid on both sides simultaneously: 2% on the left is N$2,000mn on the right). Left: the bar %, tick labels suffixed "16%". Right: the money line, thousands-separated "16,000", axis head "N$ millions" top-right. Never put the money unit inside every tick.
- AXIS/UNIT RULES. The unit each series reads lives in exactly two places: its tick side (or axis head) and the legend phrase "(left axis)" / "(right axis)". Colour-codes: % labels are printed ON the bars in grey/crimson (bar = left), the line's number is ink (line = right). If a reader must ask "which axis?", the template is broken — check before shipping.
- EMPHASIS (one accent + grey). Crimson is the only hue (bars + title clause + brandmark). Amber is a STATE FLAG (projected years), not a series — it may cover at most the projected tail, same value heights. Line is near-black #141A1E = neutral axis reading. Grey ramp everywhere else. Data-hue count: 1.
- VALUE-LABEL PLACEMENT. Bars: white 11.5px bold centred 17px below bar top (inside the column — this keeps labels clear of the right-axis line, which passes just above most bar tops; printed-above labels WILL collide with it, which is the whole reason for inside placement). Final bar: 14px, same white, emphasis by size. Line: last point only, 15px bold ink centred above the enlarged dot, no unit word (the axis head owns the unit).
- ONE ANNOTATION MAX. Grey dashed leader + 2 lines of claim text (12.5px) pointing at the step change. Claim sentence, not caption.
- DUAL-AXIS HONESTY. The two series here are the SAME fact twice (% and its N$ source), so comparing "which curve is higher" is meaningless — state the ratio story in the title instead ("takes 15 cents of every rand"). Never adjust either axis max so the curves visually meet; that's the standard dual-axis lie. If your two series do NOT share an underlying fact, say so in the kicker and consider whether the deck really needs this page.
- AXIS-QUALIFIER RULE. Projected/estimated years are flagged in words on the x-axis line (primary) + fill (secondary). A bare "2024/25" with an unlabeled amber bar is a lie by omission — the qualifier line is required whenever fill is amber anywhere.

VERIFY:
- [ ] Title ≤15 words / 2 lines with the ratio number.
- [ ] One data hue (crimson); amber appears only as projection fill/flag text.
- [ ] Both axes zero-based with round ticks; each unit stated twice max.
- [ ] Projected years: fill + qualifier words agree; legend has the flag swatch.
- [ ] Line label on last point only (unless annotation cites a value).
- [ ] One annotation max; leader grey, not brand.
- [ ] Source names appropriation + basis + estimate/budget caveat; sup matches kicker.
- [ ] Footer = deck tag + month + page bottom-right.

DON'T:
- Topic title ("Interest Repayment") — that is the page label, not a claim; the corpus scores these pages down for exactly this.
- A second coloured series (red bars + blue line) or a coloured line — one hue, line is ink.
- A "growth" second line on the right axis — right axis belongs to the money twin only; a third metric belongs on a companion page.
- 3D bars, gradient fills, exploded pies (the corpus's Excel-default sins — flat fills, straight strokes).
- Amber on mid-series bars "to highlight momentum" — amber is projection-only, full stop; emphasis is weight/size.
- Both a dashed forecast line AND amber AND qualifier words — two flag devices max, three is noise (keep fill + words).
- Tiny 6pt source text (the deck's other ding): source stays 11.5px.

SOURCE: pwc_strategy__pwc_namibia_national_budget_2024_25_for_our_humanity_now_s_t, "Interest Repayment" exhibit p05/p06 (sw_sheets/pwc_strategy__pwc_namibia_national_budget_2024_25_for_our_humanity_now_s_t_s00.jpg). Palette roles + "N$ left, % right", axis-qualifier convention, footer block, triangle motif: reviews/pwc_strategy__pwc_namibia_national_budget_2024_25_for_our_humanity_now_s_t.md (charts §, palette §, footer convention, weaknesses: Excel-default furniture, value-label-heavy, action-title failures — corrected by slots/recipe above). Same combo pattern seen KPMG-side (dual-axis column+line, reviews/kpmg__kpmg_venture_pulse_q3_2024_2024.md §Charts) and in kpmg__kpmg_kpmg_our_impact_plan_2022_update_2022 p13 (column + red dual-axis line + table) — see sibling dual-axis-combo-column-line.
