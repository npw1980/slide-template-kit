# before-after-state-pair — Before/After Transformation (two state panels + matched metric rows + centre arrow + two-numeral KPI band, 1280×720)

WHEN: "What we changed, and what it did" pages — the transformation reveal that closes a process/operations chapter: the same N operating metrics shown twice (the old state, the new state), joined by one programme arrow. From EY ARC *Analytics Mindset* p12–p21, the deck's strongest device: "before/after chart pair — same figure shown twice, cleaned version vs bad version" (`reviews/ey__ey_ey_academic_resource_center_mission_2019.md`, recurring layout archetype 2); the two-numeral callout band is the PwC Namibia budget device (`reviews/pwc_strategy__pwc_namibia_budget_on_a_plate_2019_2020_2019.md`). Use it when the *metric set is shared* across states; when each state is a whole chart, use `before-after-item-bars` instead.

## ANATOMY (slot map, stage px)
1. `kicker` — x64 y36, 12/1 uppercase ls .18rem, `17 | …` (numeral in `--accent-ink`).
2. `title` — x64 y56, 27/35 bold ink, width 1152, ≤2 lines.
3. `lead` — x64 y100, 13/17 bold, width 1152, 2 lines; the mechanism sentence.
4. `kpiband` — two numeral callouts: `k1` x64 y154 (40px numerals, unit 20px grey) + captions `kcap` y196 (10.5/13 grey-2, 288rem wide); slot pitch 324px. Right: `chip` x952 y156 w264 h36 (scope tag, uppercase 10.5).
5. `panels` — SVG: `rect.panel` x64 y226 w508 h380 and x708 y226 w508 h380, rx6, grey-5 fill. Headers: swatch 11×11 (grey / yellow-with-ink-edge) + 11.5 uppercase label, y~255. (Lead sits y134 under the 2-line title — the stack is title→lead→KPI→panels.)
6. `rows-before` / `rows-after` — `g.row` translate(64 or 708, rowY). rowY = 278 + i·P, i=0…N−1, default **P = 85** → 278/363/448/533; the ceiling is P ≤ floor(270/(N−1)) (N=3→135, N=5→67, N=6→54). Row block local: `mname` (11.5 uppercase grey-2) x32 y14, `val` (17 bold ink) anchor-end x476 y15, track `rect` x32 w410 h14 y24 rx7, fill rect x32 same y w=fill, note/pill y40.
7. `arrow` — fixed centre block arrow (x588→678, y392–432, tip right) + label above (10.5 uppercase) + constraint note below (9.5 grey-3), centred x633.
8. `source` — x64 bottom14, 10 grey-3, sup markers; `pageno` — right64 bottom14, bold grey-2.

## SLOTS (name — limit — good/bad)
- `title` — **≤15 words, ≤2 lines** — the claim is the *change*, with a magnitude: "cut order-to-cash by half — without new systems or added heads". A topic title ("Order-to-cash transformation") fails: the panels already show change, the title must say what it's worth.
- `lead` — ≤2 lines — the mechanism: *why* the states differ. Never restates the title.
- `kpi` numerals — 2 max — headline numbers that a reader could verify from the row data (−47% cycle time must equal the row-1 pair; 2.7× is the productivity restatement). Three numerals = wall; the chip carries the scope instead.
- `kcap` — ≤48 chars/line — numeral + what it measures; second line = baseline definition.
- `chip` — ≤28 chars — scope (network size, window). Not a claim.
- `mname` — ≤24 chars per panel row — metric names must be *identical* in both panels (same row = same metric, that's the page's whole logic).
- `val` — ≤7 chars incl. unit — three significant digits max; align on the anchor-end rail x476.
- `dl` (before note) / pill (after delta) — before: one honest baseline word ("FY18 actual"), after: signed delta with unit (`−47%`, `+51 pts`). Percent-vs-percentage-points discipline: % for ratios of a stock/flow, **pts** for ratio-of-ratios.
- `source` / `pageno` — always; sup after sample sizes, self-reported claims, modelled ranges.

## FILL (build order + resizing)
1. Replace kicker / title / lead, then the two KPI numerals + captions (they fix the story), then metric rows, then verify the numerals reconcile against the rows.
2. **Metric count — the master reflow.** A metric = one `g.row` in `#rows-before` AND its twin in `#rows-after` (same id suffix, same rowY). Copy the pair, set rowY = 278 + i·P, edit names/values/pills, set each fill width = `round(value / scaleMax × 410)` where scaleMax is the per-row comment (40 / 45 / 100 / 100) — pick scaleMax just above the LARGER of the two values so neither panel bars hit the track edge. Both panels keep identical row order — the eye walks straight across. Delete = remove both row groups; nothing else moves (rows are independent translates, the page never reflows horizontally).
   - N range: **3–6** rows. N=6 → P=54 < block 58: shift the pill/note baseline from y52 to y46 first; bars stay 14 tall.
3. **Add a KPI.** HTML only: copy `.kpi .k2` + `.kcap .c2` pattern, next slot left = previous +324rem; widen each `.kcap` to 260rem if N=3; the `chip` then moves left by 324rem (or delete the chip — scope goes into the source line).
4. **Panels** never resize with row count — they are fixed 508×380 at y226; the row block must end above y606 (278 + (N−1)·P + 58 ≤ 606).
5. **Recolour house:** swap `--accent` + `--accent-ink` together (ink-on-yellow is ~16:1; if your accent is dark, set `.filla` white-on-accent only for the pills and keep bars on the fill). Before-bars stay grey-3 unconditionally — grey is the *old state*, never dimmed further, never tinted.

## CHART RECIPE (how the figure encodes)
- Two matched panels = the comparison is the layout, not the legend: left is always the past. One metric per row, bars share the row's own scale, so the two bars in a row are directly comparable *and* cross-row you read "which lever moved".
- One accent: every AFTER bar + the delta pills. The whole before column is one grey. Never yellow-outline the before side.
- Delta pills sit under the after bar, same x as the bar start — they read as the row's verdict.
- No axes, no gridlines: values label the bars (17px ink), units live in the metric name. Chart-junk rule of the source pages (the EY deck's own pedagogy): no axes on paired-state bars.
- Arrow is decorative-simple: it means "this window" — no programme-step detail inside the arrow (that belongs on a process page).

## VERIFY (against the render)
- [ ] Title ≤15 words / 2 lines; both panels have identical row labels in identical order.
- [ ] KPI numeral reconciles with its row pair (−47% ↔ (18.2−34.5)/34.5); units consistent (pts vs % discipline kept).
- [ ] One emphasis colour: after-bars + pills; before-bars all grey-3; ≤1 extra hue total.
- [ ] No white-on-yellow anywhere (pills/numerals/notes use ink or `--accent-ink`).
- [ ] Bars inside tracks (fill ≤ 410 px), scaleMax > larger value.
- [ ] Source line present with sup markers on n= and self-reported figures; page number present.

## DON'T (corpus failure modes)
- Topic title under a full before/after grid — EY's own pages carry the same title 4× ("competency framework") and read as contentless; the kit title is the claim.
- A third "mid" panel (before → pilot → after) — that's a journey page; two states is this page's contract.
- Rainbow before-palette (the EY before-chart's rainbow bars are deliberately *bad-practice samples* — never inherit them).
- Equal-length bars because "both are impressive" — if after isn't longer/shorter where it should be, the metric pair is wrong; pick metrics that actually moved.
- Yellow with white small text (contrast fails) — the source deck only uses yellow fills + black text.

## SOURCE
EY Academic Resource Center, "Analytics Mindset" curriculum deck — `ey__ey_ey_academic_resource_center_mission_2019`, before/after chart pairs p12–p21 (`reviews/ey__ey_ey_academic_resource_center_mission_2019.md`, archetype 2 "before/after chart pair with red-arrow corrections"; red annotation replaced by the single kit accent). Read in `sw_sheets/ey__ey_ey_academic_resource_center_mission_2019_s01.jpg` (5×2 sheet, p12 = row1 col2). Two-numeral callout band: PwC Namibia budget review `pwc_strategy__pwc_namibia_budget_on_a_plate_2019_2020_2019` p3 (`sw_sheets/…_s00.jpg` row1 col3; review file: palette read as orange/burgundy/grey — the kit takes only the *device*, one accent). Accenture NBN Effect p14 (icon-cards with paired before/after bars) supports the per-metric pairing idea: `reviews/accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o.md` / `..._slides.csv`. Palette anchor: EY yellow `#FFE500` pixel-sampled (histogram mode of `sw_sheets/…_s01.jpg` p12 region); grey ramp per DESIGN_PLAYBOOK. Real brand type: EY House Sans — the Helvetica Neue/Arial stack stands in.
