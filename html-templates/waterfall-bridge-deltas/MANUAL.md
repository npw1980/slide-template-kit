# waterfall-bridge-deltas — From/To Value Bridge with Floating Delta Bars

WHEN: One page that walks a reader from an opening value to a closing value through a handful of named drivers ("what moved the number and how"). Comes from EY-Parthenon *Generative AI in retail and commercial banking* (2023), p9 — where accent-blue highlight bars + a grey ramp, value labels on the bars, and a dashed outline for the immaterial bar carry the whole argument. Use it whenever the story is "A became B because of +x, +y, −z"; not for ranked bars with no shared start/end (use vbar/hbar then).

ANATOMY (px on the 1280×720 stage):
1. Claim title — left 64, top 34, width 1152, two lines of 29px/37px, second half carries `.em` accent span.
2. Kicker — left 64, top 112, 14px all-caps letter-spaced, with superscript footnote mark.
3. Chart SVG — full stage viewBox 0 0 1280 720. Plot area: baseline y=600 (zero), bars from x 122–1158, six column centres at x = 170 + i×188 (i=0..5), bar width 96.
4. NET pill — rect 566,158 w148 h28 rx14, accent fill, centred over the columns; drop-lines at 170/1110.
5. Legend — three 12px chips at y=196, x 768/872/986 (uplift / erosion / totals).
6. Methodology note — left 64, bottom 34, 10px; explains the dashed-outline dagger.
7. Footer — source line bottom-left (left 64, bottom 14), `PAGE | SECTION` bottom-right.

SLOTS:
- title — ≤15 words / 2 lines. GOOD: a quantified claim naming the net direction ("+1.9pp to 23.9%"). BAD: "EBITDA margin bridge" (topic, not claim). The numbers in the title must equal the numbers the bars actually add to.
- kicker — figure caption + methodology hook (basis, scope). ≤12 words + footnote mark. BAD: restating the title.
- steps — 4–6 driver columns for legibility (plus opening/closing totals). Each label ≤2 lines × ~18 chars. GOOD labels are named economic levers ("Pricing & discounts", "Cost of delivery"), not "Other" piles; every material movement gets its own column, one "Other/Net residual" bar is honest but must be small.
- delta labels — signed (+3.1pp / −2.4pp), one decimal. BAD: unsigned bars — reader must guess direction.
- note — 1–2 lines for the dagger/dashed device (uncertainty ranges, unaudited scope).
- source — institution + dataset + period + reconciliation ("bridge reconciles to board plan v4").

FILL (step by step):
1. Replace the DATA ARRAY comment at the top: `start`, `steps[]` with `{label, sub, delta, kind, dashed?}`, `end`, `net`. Check `end = start + Σdelta` before touching SVG — if it doesn't tie, the page lies.
2. Recompute running totals rᵢ (r₀ = start, rᵢ = rᵢ₋₁ + deltaᵢ). For each float column i: `y = 600 − max(rᵢ₋₁,rᵢ)×11`, `height = |deltaᵢ|×11`, `x = centre−48` (centres: 170, 358, 546, 734, 922, 1110). Swap only `y`/`height` on that `<rect>` and the two text lines under it.
3. Start/end total bars: `height = value×11`, `y = 600 − height`; update the white inside-labels and the % inside.
4. Connectors: five `<line>`s at y = 600 − rᵢ×11 between adjacent columns (218→310, 406→498, 594→686, 782→874, 970→1062).
5. Delta labels: positive text above float (y = bar top − 11), negative below float (y = bar bottom + 20); colour `#1B96E0` for positive, `#4A4E55` for negative.
6. NET pill text `NET ±N.Npp` = end − start; update title span to match.
7. For an approximate driver: keep `dashed:true` — draw the extra dashed rect (`x=centre−54, y=barTop−5, w=108, h=bar+10`, `stroke-dasharray="4 3"`) and append `†` to its delta label; describe it in the note slot.
8. Recolour for another brand: set `--accent` to the brand hue and `--neg-stroke`/`--neg` to two greys of that ramp; totals stay neutral grey (they are anchors, not the finding).

CHART RECIPE (the encoding, in words a data person can rebuild):
- **Scale**: linear, ZERO-BASED. `y(v) = 600 − v × 11` px. Never truncate the axis on a bridge — a floating bar must be comparable to the full-height totals or the eye over-reads the delta.
- **Bar placement**: totals (start/end) sit on the baseline at full height; drivers "float" — the bar's bottom/top edge starts exactly where the running cumulative lands, so bar bottom = min(rᵢ₋₁,rᵢ), bar top = max(rᵢ₋₁,rᵢ). Connectors are thin (1.4px) horizontal rules linking column edges at running-total levels.
- **Value labels**: inside the totals (white 700, 14px, bar top+22); drivers get a SIGNED delta label outside — above positive bars, below negative bars, 13px bold, direction-coloured. Never label both the float and its cumulative; one number per bar.
- **Emphasis — one accent + grey ramp**: positive movement = `--accent` (EY azure #1B96E0); erosion = light grey #B9C1C9 with a #6E747C stroke (thin bars need the stroke or they vanish); opening/closing totals = neutral grey #59616B. The accent is the *finding*, and the story is the NET direction — if the net is negative, flip `--accent` onto the negative columns and grey the positives (swap fills + label colours, geometry unchanged). Max 1 hue + greys.
- **Uncertainty device**: a driver that is directional, not modelled, keeps its normal float but gains a dashed 4-3 outline + `†` + one note line. This is the EY p9 habit — honest about materiality instead of hiding the bar.
- **Axis/units**: % axis labels every 5pp down the left, unit spelled once in the kicker ("PERCENTAGE POINTS OF REVENUE"); deltas signed `±N.Npp` with ONE decimal.

VERIFY:
- [ ] title ≤15 words / ≤2 lines, and title numbers = bar arithmetic (start+Σdeltas=end)
- [ ] source line bottom-left present; `N | SECTION` bottom-right present; superscript mark on the kicker if methodology caveats exist
- [ ] exactly one hue + grey ramp (check: positive/negative fills differ ONLY in hue per the rule above; totals neutral)
- [ ] NET pill matches end − start; pill text clears 4.5:1 (accent fill + white text passes at #1B96E0 only because it's 700-weight 13px — verify brand swaps)
- [ ] baseline at zero, gridlines ≤5, no shadow/3D/gradient on bars
- [ ] if a dashed bar exists, the note slot explains it (dagger is not decorative)

DON'T:
- topic title ("Margin bridge FY24-FY26") — this page only earns its space if the title states the finding;
- >8 drivers: past ~6 columns labels collide at 188px pitch — roll small ones into "Net other" and say so in the kicker;
- 4-colour "up/down/other/unallocated" rainbow — grey + one hue is the whole kit rule;
- connectors that jump columns at the wrong level (classic PowerPoint-bridge bug: bar height and connector y computed independently and drifting);
- dashed outlines everywhere — it's a materiality flag, ~1 bar max;
- letting "Other" exceed the named drivers: then the honest chart is a 2-bar chart.

SOURCE: EY-Parthenon *Generative AI in retail and commercial banking* (2023), slide p9 (`sw_sheets/ey__ey_generative_ai_in_retail_and_commercial_banking_2023_s00.jpg`, row 2 col 4) — accent + grey ranking bars with in-bar value labels and the dashed-outline marker; palette/emphasis ("azure = the finding, grey = comparison", "dashed outlines group bars visually") from `reviews/ey__ey_generative_ai_in_retail_and_commercial_banking_2023.md` (Color system, Chart discipline sections). The from/to bridge frame itself is standard MBB practice; this template pins its geometry to that deck's colour and label discipline. Placeholder numbers (22.0→23.9 EBITDA bridge) are invented but arithmetically true.
