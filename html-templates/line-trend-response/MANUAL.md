# line-trend-response — Single-Curve Response Chart + Numbered Key-Insight Rail

WHEN: A "how returns behave as you spend more / keep improving" page: ONE curve
(spend→response, price→volume, effort→quality), a grey linear-reference to show what the
curve is arguing against, two marker thresholds, and a right-hand rail of three CIRCLED-
NUMBER key insights that correspond 1:1 to the circles on the curve. From Accenture
Moneyball Canada p18 (illustrative response curves + annotation callout, honestly tagged
"ILLUSTRATIVE") and p19 (same curves + 3 circled-number "Key insights" column) —
accenture__accenture_the_moneyball_moment_for_marketing_in_canada_2019,
sw_sheets/..._s01.jpg rows 2–3; review calls out both the curve+annotation form and the
red/black/grey semantic encoding this template keeps. Use when the argument is *shape of
returns* (where does more stop being better); for trajectory-over-time across segments,
use line-trend-multi.

ANATOMY (1280×720 stage):
1. kicker    — 64,36, ≤1000 wide, 15px grey; bold dark lead-in + units + n + sup + the ILLUSTRATIVE tag (dark-red chip, inline). The honesty flag is part of the device, not decoration.
2. title     — 64,64, 1152 wide, 28px/36px, ≤15 words / 2 lines (max-height 72px clips). Line 2 = operative clause in em (accent).
3. rule-top  — 64,138, 1152×1px --rule.
4. chart     — inline SVG (viewBox 0 0 1280 720): plot box x 130→830 (spend $0–100M), y 170→560 (index 0–100).
   - shaded "below threshold" band x 130–270 (`--zone`), dashed accent vlines at $20M (x=270) and $85M (x=725) with white PILL labels above the plot
   - grey dashed LINEAR REFERENCE from origin to the curve's endpoint — the assumption
   - THE CURVE: 3.5px accent stroke, 21 points (every $5M)
   - circles ① ② ③ (r13, accent fill, white number) sit ON the curve at x=$15M/$50M/$85M
5. insight rail — x 890→1216: "KEY INSIGHTS" head + 3 blocks; each = circled number (r14) + bold claim (15px) + 2-line explanation (12.5px grey). Numbers must equal the curve markers.
6. source    — 64, bottom 26, 11.5px grey; method + honesty clause + sup marker.
7. running head — right 64, bottom 26: "18 | EFFECTIVENESS" pattern "N | SECTION".

SLOTS:
- title: ≤15 words / 2 lines; carries the curve's *conclusion* (threshold + direction), not a topic ("TV spend response" is a kicker).
- kicker: metric pair + units + n + the ILLUSTRATIVE (or "MODELLED", "10-YEAR AVG") chip. Chip text ≤45 chars. If your data IS measured, drop the chip but never swap it for marketing filler.
- curve: ONE curve. Second series only as grey dashed reference (linear) or grey "other market" at ≤70% of response; never a second hue.
- thresholds: exactly two — floor (threshold) + ceiling. A third dashed line turns the page into a picket fence.
- pills: rounded 11px labels above the plot naming the two thresholds in units. ≤16 chars each ("threshold: $20M").
- circled numbers: 2–4. If 4, the rail shrinks and explanations must shrink to 1 line each.
- rail claims: each is a sentence with a number ("$20M–$85M is the effective band"). Explanation ≤135 chars/line × 2 lines.
- source: must state what the curve is calibrated from; the honesty tag + sup go here too.

FILL:
1. Replace curve parameters in the header comment (RMAX, TAU) and the polyline: px x = 130 + 7×x, px y = 560 − 3.9×r(x) for x = 0..100 step 5. If your axis ranges differ (e.g. spend to $40M, response to 1.2), change the px formulas and the tick label lists TOGETHER — the px gridlines/labels come from (plot_span / value_span).
2. Move the threshold vlines: x = 130 + 7×threshold ($M); pill x = vline x − 56..+70; shaded band width = threshold px − 130.
3. Circled numbers: cx from x = 130 + 7×spend, cy = curve y at that point (round to 1 decimal). Keep them ON the curve line or the numbering lies.
4. Rail: rewrite 3 claims + explanations inside the rail SVG; the circle y-centres sit at 240/350/460 — do not renumber if you drop to 2 insights, delete the third block and spread the other two to y=295/455.
5. Recolouring: swap --accent/--accent-deep only. Keep --light/--gray-1/--zone grey; the linear reference and bands are "context" roles, not brand.
6. No forecast here — if the curve itself is modelled rather than measured, say so in kicker chip (MODELLED/ILLUSTRATIVE), not with dashes.

CHART RECIPE (chart template — follow exactly):
- SCALES. Linear, zero-based, both axes. x = the lever you control (spend/effort), y = the outcome (index/%/$). Choose tick values so the curve ends inside the plot with ~5% headroom. Label every 20 index units and every $20M — the argument needs readable thresholds. No dual axis; if the response is $ not index, change the y labels and unit phrase only.
- THE CURVE IS THE ARGUMENT. 3.5px accent — the single stroke emphasis on the page. Everything that is not the curve is grey ladder: linear reference `--light` dashed, gridlines `--rule`, annotations `--gray-1`. Never outline the curve, never gradient-fill under it.
- LINEAR REFERENCE. Grey dashed (7 5) straight line from origin to the curve's ENDPOINT. This is what makes diminishing returns visible without a caption. Label it once in italics below the line. If your story is not "against the linear assumption", replace it with the measured/comp-avg curve in grey — but one reference only.
- THRESHOLDS. Two dashed accent vlines (opacity .55) with white pill labels ABOVE the plot (pill = white fill + light stroke, 11px dark text — pills are the only white-fill objects allowed on the chart). Shade the dead zone under the threshold (100–15% tint of grey). This encodes "there is a floor and a ceiling" — if your claim is one threshold, show one.
- NUMBERED MARKERS. r13 accent discs with white bold digits, centred on the curve. The digit is the ONLY place the number appears outside the rail — no duplicated "1" labels along the axis. Circles order left→right = rail order.
- VALUE LABELS. This page type labels NOTHING with end-of-line % (no % to put). The units live on axes + pills. If one absolute number must appear (e.g. "$60K per $1M"), it goes inside the rail explanation, not floating on the curve.
- ONE ACCENT + GREY RAMP. One hue (red). Focus = curve, markers, emphasis clause. All context = #BFBFBF/#D9D9D9/#7D7D7D/#4D4D4D ladder + #F3F4F6 band. Two accent uses max per element (marker fill, claim circle) — same hue, never adjacent intensity pairs.

VERIFY:
- [ ] Title ≤15 words / 2 lines at 28px; operative clause accent.
- [ ] Curve is the only solid accent stroke; reference line grey dashed; no second hue anywhere.
- [ ] Both threshold vlines have pill labels above the plot, in units.
- [ ] Circled numbers 1:1 between curve and rail; rail claims contain numbers, not adjectives.
- [ ] ILLUSTRATIVE/MODELLED tag present if data isn't measured (and absent if it is).
- [ ] Source line + sup marker present bottom-left; "N | SECTION" running head bottom-right.
- [ ] Text on accent chips/rail circles: white on #D8112B / #9B0B20 ≥4.5:1.
- [ ] Renders identically offline — zero network calls.

DON'T:
- Topic title ("Media spend response"). The conclusion belongs in the title; the topic belongs in the kicker.
- More than one curve with color-coded "market A/B/C" — multi-series trend is line-trend-multi's job; here multiple coloured curves destroy the single-curve argument.
- Circled numbers without the matching rail (mystery markers = the corpus's "lazy annotation" failure).
- Duplicating axis values inside pills AND on the baseline ("$20M" on pill and x-axis tick is fine; "$20M" ALSO as a mid-plot floating text is not).
- Gradient area fills under the curve or 3D axes — chart-junk the reviews flag everywhere.
- Shaded band + pill + arrow for the same threshold (one threshold = band + one pill).
- Marketing chip text ("KEY TAKEAWAYS", "INSIGHTS!!!") where the honest tag belongs; if measured, use no chip.

SOURCE: Extracted from accenture__accenture_the_moneyball_moment_for_marketing_in_canada_2019 p18 (response curves + annotation, "ILLUSTRATIVE" tag praised in review §chart discipline) and p19 (curves + circled-number Key insights column, review item 10), read in sw_sheets/accenture__accenture_the_moneyball_moment_for_marketing_in_canada_2019_s01.jpg (row 2/3); analysed in reviews/accenture__accenture_the_moneyball_moment_for_marketing_in_canada_2019.md — red/black/grey semantic encoding, grey-reserved rule, honest-tagging lesson.
