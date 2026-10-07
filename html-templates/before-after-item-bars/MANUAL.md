# before-after-item-bars — Per-item before/after paired bars + ringed highlight + callout (1280×720)

WHEN: "Step by step: what changed and what didn't" pages — the reduction is uneven and you want the reader to *see* which of several items moved and which stayed. Unlike `before-after-state-pair` (same metric twice, whole-page reveal), this template compares N items inside one chart, each item carrying its own before/after pair, with exactly one pair ringed + called out as "the fix that worked" — EY's red-arrow correction device (`reviews/ey__ey_ey_academic_resource_center_mission_2019.md`, before/after chart pairs p12–p21), recoloured to the single kit accent. Per-item paired bars as a reading pattern come from Accenture NBN Effect p14 (`reviews/accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o.md`).

## ANATOMY (slot map, stage px)
1. `kicker` — x64 y36, 12/1 uppercase ls .18rem, `21 | …`.
2. `title` — x64 y56, 27/35 bold ink, width 1152, ≤2 lines.
3. `lead` — x64 y134, 12.5/16.5 bold, width 1100, 1–2 lines. (Title runs 2 lines to y~116; lead clears it. If your title is 1 line, you may pull lead to y100 and the chart is unchanged.)
4. `legend` — fixed: two 11×11 swatches at x986 / x1148 y167 + 9.5 labels; `unit` note x64 y181.
5. `baseline` — line x64→1216 y600 (the page floor of the chart; no y-axis, no gridlines).
6. `items` — N `<g class="item" transform="translate(cx,0)">`, cx = 172 + i·216 (N=5 → 172/388/604/820/1036). Item-local: before bar x−52 w44 (grey-3), after bar x+8 w44 (grey-1, or `.h` accent if highlighted), value labels at x∓30/+30 y=barTop−8, delta pill (`.dp` 66×18 rx9) centred on cx at y=barTop(max)−30…−12, category x0 y626, sub x0 y641.
   Bar height = value / scaleMax × 400, baseline y600. (scaleMax=40 days in the placeholder.)
7. `annotate` — optional, anchors to the ONE highlighted item: ring `ellipse` centred over the pair (cx ±76 / bar span, cy 485, rx76 ry118 in placeholder), leader path + dot from ring edge to callout box, callout `rect` x96 y196 w510 h74 rx5 + eyebrow (9.5 uppercase `callK`), 11/16 two text lines (one bold lead-in).
8. `source` x64 bottom14 w980 (sup markers); `pageno` right64 bottom14 "21 | …".

## SLOTS (name — limit — good/bad)
- `title` — **≤15 words / 2 lines** — carries the *unevenness* verdict: "One fix removed half the cycle time — four of five steps still run as before". Good = number the unchanged ones; bad = "Cycle time before and after" (describes the chart, not the finding).
- `lead` — ≤2 lines — measurement frame: what, where, window.
- `item.cat` — ≤17 chars, UPPERCASE — process steps / regions / product lines. All items must be the *same kind of thing* (steps × steps yes, steps × "other" no).
- `item.sub` — ≤20 chars — the volume behind the bar ("1.2k orders/day"), with `sup` if it's a daily average.
- `val` labels — ≤3 chars + unit in the unit note / sub — integers preferred at this bar size.
- `delta pill` — signed % (−42%, +51 pts). The highlighted pair's pill gets `.h` (accent-tint + accent-ink text). If a pair is 0% change, keep the pill as "±0" in grey — *show* no change, don't erase the pair.
- `callout` — ≤118 chars/line × 2 — one sentence naming the fix + its scope caveat (pilot sites). The ring is *not* the callout's scope: the callout says which fix, the ring says which pair.
- `unit` note — the metric + n, one line, `¹/²` sup markers.

## FILL (build order + resizing)
1. Set kicker/title/lead + unit note; then the data: for each item two numbers (before, after). Pick **scaleMax** = the smallest round number ≥ max(all values) (40 for max=31 here); write it as a comment on the item block.
2. **Add/remove items — the master reflow.** One `<g class="item">` per item; copy any item block and change `translate(172 + i·216, 0)` — everything inside the item block is item-local, nothing else moves (no global reflow by design; deleting = remove the block; the baseline is fixed 64→1216 so pairs keep standing on it).
   - The pitch **216** holds 4–6 items. N=4 → translate 216 + i·232; N=6 → 150 + i·178, and shrink bar width to 40 (x−48 / x+8) with value labels x∓28/+28. N>6 → split across two pages (the ring/leader geometry is sized for 5).
3. **Per-item numbers, four coupled values** (the only edits that require arithmetic): bar height h = round(v/scaleMax×400), bar y = 600−h; value label y = barTop−8. Delta pill y = (barTop of the TALLER bar) − 30; pill text = signed %. The **pill y, both label ys** all derive from bar heights — change a value and its three derived y's must move (the pill never floats into the value above it).
4. **Move the ring/callout to another item:** change ring `cx` to that item's cx (keep cy485/rx76/ry118 — sized for one pair's bar span), move the leader's start point to (cx+46, 386), flip its curve toward the empty upper-left/upper-right quadrant, and re-anchor the callout rect (place it in the *emptiest* half of the band y185–280, clear of legend x≥980). Only ever one ring + one callout.
5. **Recolour house:** swap `--accent`/`--accent-ink` together. Non-highlighted after-bars stay `.fa` (grey-1); before-bars `.fb` grey-3 always — the old state is grey unconditionally.

## CHART RECIPE (how the figure encodes)
- Paired columns on a shared baseline: the *pair* is the comparison, the item is the row you walk across. Bars in a pair must be visually adjacent (44 wide, 16 gap) — wider gaps turn pairs into separate series.
- One emphasis: accent only on the highlighted pair (after bar + tinted pill + ring). Everything else is grey ramp (grey-1 after / grey-3 before / grey-2 text).
- Delta pills above each pair make the page read top-down even without an axis; value labels above the bars keep pills and values from fighting over the same vertical slot.
- Ring + leader + callout = EY's "corrections" annotation: dashed, low fill, never a filled blob; leader line starts on the ring edge (a 3px dot) so it reads as attached, not floating.

## VERIFY (against the render)
- [ ] Title ≤15 words / 2 lines and it names what didn't change as well as what did.
- [ ] Every bar sits on the baseline (y = 600−h), none taller than ~415px (would hit legend band).
- [ ] Pills clear value labels above them (pill y = barTop(max)−30, never higher than −12 into a label).
- [ ] One ring, one callout, callout text ≤2 lines and ≤118 chars/line; leader visually connects ring→box.
- [ ] Grey logic intact: before grey-3, after grey-1, highlight accent — never two accents, never white text on yellow (accent-ink for pill text).
- [ ] Source line + sup markers + pageno present; sup ¹² match the source text.

## DON'T (corpus failure modes)
- Ringing two pairs "because both matter" — the ring is a spotlight; a second one is a second page.
- Inheriting EY's before-chart rainbow (the EY deck's own bad-practice sample) — before side is grey.
- Equal bars + equal pills = a "everything improved" page; the device is only credible if some items visibly didn't move (that's why the title names the four that didn't).
- Delta pills inside bars or below baseline — they belong above the pair, aligned to the tallest bar.
- Annotating the callout on a non-highlighted item (callout claims a fix, ring points to the pair — if they point apart, readers can't connect them).

## SOURCE
EY Academic Resource Center "Analytics Mindset" — `ey__ey_ey_academic_resource_center_mission_2019`, before/after chart pairs p12–p21 (`reviews/ey__ey_ey_academic_resource_center_mission_2019.md`; device: same chart twice + red-arrow corrections on the cleaned version — kit: one chart, ringed pair + leader instead of per-bar arrows). Second anchor: Accenture NBN Effect p14, per-item paired bars (`reviews/accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o.md`). Sheet: `sw_sheets/ey__ey_ey_academic_resource_center_mission_2019_s01.jpg` (p12 = row1 col2). Accent `#FFE500` pixel-sampled from the EY sheet (dominant (255,229,0)); greys as per kit tokens. Real brand type: EY House Sans — Helvetica Neue/Arial stands in.
