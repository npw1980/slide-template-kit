# line-trend-multi — Multi-Series Trend Line Chart, End-of-Line Value Labels

WHEN: A "how a metric moved over time, and who is driving it" analysis page: 2–4 series
on one time axis, one focus series in the accent colour, all others in the grey ramp, and
the series identified by END-OF-LINE VALUE LABELS instead of a legend. From KPMG Venture
Pulse Q3 2024 p8/p9/p24 (kpmg__kpmg_venture_pulse_q3_2024_2024, sw_sheets/..._s00.jpg row
2 — "median deal size by stage" panel), where the review's chart conventions note
*"multi-series line charts … annotated with end-of-series value labels rather than
legends"* and forecast years are flagged `2024*`. PwC 23rd CEO Survey (p07 multi-line
time series) and PwC 21st CEO Survey (3-series + circle markers) show the identical
convention at another firm, so this is a house pattern, not one firm's quirk. Use when the
argument is *trajectory + gap between segments*; if the page only tells a single story
curve, use line-trend-response.

ANATOMY (1280×720 stage):
1. kicker    — 64,36, 940 wide, 15px grey; bold navy lead-in + unit/period + n + sup. Footnote sup is required where the source claims methodology.
2. title     — 64,64, 1000 wide, 28px/36px, ≤15 words / 2 lines (max-height 72px clips overflow — that is the gate). Line 2 = operative clause in `em` (accent).
3. nav strip — right 64,34; 5 chips (Global | US | Americas | Europe | Asia); active chip solid `--accent`, rest grey on hairline border. KPMG's region-rail device; omit or swap for any "view" tab set the deck actually has.
4. rule-top  — 64,138, 1152×1px `--rule` under the title zone.
5. chart     — ONE inline SVG, viewBox 0 0 1280 720, 1 unit = 1 stage px:
   - plot box: x 110→1050 (10 x-points, x(i)=110+i×104.44), y 197→565 (linear 0%→80%)
   - horizontal gridlines every 10% (`--rule`), y-axis line + baseline `--axis`
   - one polyline per series: solid leg points 0..7 + DASHED forecast leg points 7..9
   - end markers: hollow circles r≈4 at x=1050 + two-line value labels at x=1062
   - annotation: dashed leader line + claim box (one per page max)
6. source    — 64, bottom 26, 1010 wide, 11.5px grey, methodology sentence + sup marker.
7. running head — right 64, bottom 26, bold navy "PAGE | SECTION".
NO legend element exists — the value labels ARE the legend (keep it that way).

SLOTS:
- title: ≤15 words / 2 lines. Must contain a number or comparative (the gate fails a bare topic line). The em clause is the finding.
- kicker: names the metric, unit, period, n, and the forecast asterisk — ≤160 chars. "Share of respondents using AI…" is good; a kicker restating the title is bad.
- series: 2–4. EXACTLY ONE focus series (accent stroke, 3px); all context series grey ramp (`--s1` darker = more important context). Max 2 grey series: a third grey line at 2px competes with gridlines.
- value labels: bold % over 11px grey series name, right of the end marker; label the LAST point of each series only. Never label mid-points.
- forecast: the * on axis + dashed last leg (points 7..9) is the ONLY forecast flag; if you need a "projected" box that's a second device — pick one.
- annotation: one claim box + dashed leader onto the anomaly (one per page). Box width ≤340, text 12.5px, max 2 lines.
- nav strip: 3–6 chips; active = current view. If deck has no views, delete the strip and widen the title to 1152.
- source: must name waves/method and the sup marker that matches the kicker sup.

FILL:
1. Replace the header-comment DATA ARRAYS (years, focus, context1, context2). Values are %; geometry does not change if you keep the axis at 0–80%.
2. For each series recompute the two polylines:
   x(i) = 110 + i×104.44 ; y(v) = 565 − v×4.6
   solid leg = points 0..7, dashed leg = points 7..9 (last 3 x-points).
   If your value range is very different, rescale y: pick step px = (plot height)/(axis max/step), redraw gridlines/labels, never stretch one series' stroke.
3. End markers + value labels: circle cy = y(last value) per series; label y = cy−5 (value) and cy+9 (name). Sort label blocks by cy so they never overlap — if two ends land closer than 22px apart, order labels by value and stagger ±11px.
4. Swap x-axis year labels; keep the * on forecast years and add the "see methodology note" clause in the source line.
5. Recolouring for a different brand: change `--accent`/`--accent-deep` only. The grey ramp (`--s1`, `--s2`) is the "context series" role and must stay grey — do not tint them or you lose the one-accent rule.
6. If the series has no forecast, delete the `.fc` polylines entirely (do not leave a floating dash).

CHART RECIPE (chart template — follow exactly):
- SCALES. Linear, zero-based on both axes. x: year ticks evenly spaced (no time-proportional x unless periods are uneven — then state the break with a "//" rule). y: %/index/$ per respondent, ticks at round steps (here 0–80% step 10), labels right-aligned to x=98. NO dual axis. NO log axis — if a curve looks exponential, that is the story and it should be stated in the title, not hidden by the scale.
- EMPHASIS. One accent: the focus series only (3px solid `--accent`). Context series = grey ramp, 2px (`--s1` then `--s2`). The focus series gets a slightly bigger end marker (r4.5). No third hue, no red/green "winners/losers" scheme — colour is segment identity, not good/bad.
- VALUE LABELS. At line ends only, right of the hollow end marker: bold % (15px, ink; focus series in accent) over grey series name (11px). Labels never sit on gridlines or inside another series' line — if the last points are vertical-crowded, stagger ±11px (keep the vertical order = line order at that x).
- FORECAST. Dashed last leg (dasharray 5 4) + `*` axis flag + source-line clause. Same colour as the series — a dashed leg is the same story, not a different one. Do not add a shaded "forecast zone" as well; that's double-flagging.
- ONE ANNOTATION MAX. Dashed leader + rounded claim box pointing at the anomaly; text is a claim sentence (12.5px, ≤2 lines), not a caption. Anything else that needs saying goes in the kicker or title.
- AXIS/UNIT RULES. Unit appears once on the y tick labels ("0%…80%") and once in the kicker. x years plain, forecast years italic-flagged with *. Baseline `--axis` slightly darker than gridlines. No vertical gridlines. No axis titles ("Share of respondents") — the kicker owns that.

VERIFY:
- [ ] Title ≤15 words / 2 lines at 28px, with the operative clause in accent.
- [ ] Exactly ONE accent stroke on the whole page (the focus series + its em clause). Context series grey.
- [ ] Value labels present on every series end; none overlap gridlines or each other.
- [ ] Forecast leg dashed + `*` + methodology clause in source line.
- [ ] Source line present bottom-left with superscript matching kicker sup; running head "N | SECTION" bottom-right.
- [ ] Text on accent (nav chip active) is white ≥4.5:1 contrast (KPMG blue passes; check any recolour).
- [ ] Zero network calls: page renders identically offline.

DON'T:
- Topic titles ("AI adoption trends") — that's what the kicker is for. The title is the claim.
- Legend boxes — the corpus deck itself has none; end labels replaced them. A legend box is chart junk here.
- 3+ context series or one context series in accent-adjacent hue (blue-family + violet-family = the KPMG review's "over-wide palette" complaint).
- Forecast shown both dashed AND in a tinted zone box.
- Value labels on every point (that's the paired-bars style, not lines) or mid-series.
- Kicker walls: kicker ≤160 chars, no two-sentence micro-essay.
- Dual axis / twin charts that silently change the scale between panels.
- Adding markers to every point because "there might be reading error" — one hollow end marker per series is the whole marker budget.

SOURCE: Extracted from kpmg__kpmg_venture_pulse_q3_2024_2024 p8 (left panel "Global median deal size ($M) by stage", 2018–2024*; cross-checked p9/p24 same grammar) read in sw_sheets/kpmg__kpmg_venture_pulse_q3_2024_2024_s00.jpg row 2 — analysed in reviews/kpmg__kpmg_venture_pulse_q3_2024_2024.md §4 (palette table: navy #0A1F3A, blue #1E49E3, cyan #00B8F6) and §5 (line-chart conventions, end-label rule). Convention corroborated on pwc_strategy__pwc_23rd_annual_global_ceo_survey_navigating_the_rising_tide p07 (sheet s00) and pwc_strategy__pwc_21st_ceo_survey_the_anxious_optimist_in_the_corner_offic p03 (sheet s00), whose reviews describe 3-series lines with circle markers + end %.
