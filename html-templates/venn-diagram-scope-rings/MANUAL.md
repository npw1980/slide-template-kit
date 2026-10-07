# venn-diagram-scope-rings — Coverage Rings per Component (1280×720)

WHEN: Scope / coverage pages for assurance, compliance, due-diligence, program governance: "we audited this much of that, reviewed this much, the rest is out of scope." The ring is the honest cousin of the overlap diagram — when the claim is *how much* of each component the work reaches (coverage per component, not three-set intersection). Provenance: PwC *Annual Report 2017-2018* p103 (`sw_pages/pwc_strategy__pwc_pwc_annual_report_2018/pg-103.png`). The harvest and slide CSV tag p103 as "venn-diagram / red-gray overlapping circles"; read at 1:1 the page actually draws three **non-overlapping** coverage rings with a review wedge — this template reproduces that exactly, and the sibling `venn-diagram-triad` is for real overlap claims.

ANATOMY (numbered slot map, 1280×720 stage px):
1. `kicker` — x64 y38, 11.5 uppercase letterspaced, red tick.
2. `title` — x64 y58, width 1152, Georgia 30/43 bold, 2-line box (max 86); a numeric in red inside the sentence is allowed (4.6:1). `<sup>1</sup>` for the methodology claim.
3. `caption` — x64 y130, Georgia italic 13.5/17 — the figure's own lead line ("For clarification purposes we show our scope…"), one sentence.
4. `ringfield` — x64 y156, 1152 × 264 svg, viewBox 0 0 1152 264, three `<g class="ring">` at translate(pitch·(i+½), 140), pitch = 1152/N = 384 for N=3. Each ring group, locally:
   4a. `ring-N-label` y−92, Georgia bold red 13 — the component / slice name.
   4b. ring at (0,0): base track circle r=74 stroke-26 `--gray-4` = not-in-scope; a second circle (stroke `--gray-2`, the review wedge) and the accent arc circle, both `pathLength="100"` with `rotate(-90)` so coverage starts at 12 o'clock.
   4c. `ring-N-pct` 21 bold in the hole + `ring-N-sub` 9.5 gray under it.
   4d. `ring-N-note` y+112 gray 10 — "16 of 22 statutory components".
5. `legend` — centered row y426: red square "Audit procedures", gray square "Not in scope" (the review wedge is explained in band-p4, not in the legend — the ring is already busy).
6. `band-rule` — 2px red hairline y462 across the canvas (the p103 editorial divider).
7. `band` — two columns from y478 (grid 1fr 1fr, gap 54, Georgia 11.5/16.5 charcoal, red serif h3s): the so-what: how coverage moved, what the gray residual means.
8. footer — `source` 10/13 gray-3 bottom-left, `page` bold + running head bottom-right.

SLOTS (name — limit — good / bad):
- `title` — **≤15 words / 2 lines** — quantitative: a coverage figure or a delta ("reaches 71%, six points above FY17"); "Scope of work" fails the MBB gate.
- `caption` — ~120 chars — states what the rings *are*, one sentence.
- `ring-N-label` — 34 chars max — component or slice name, consistent construction across rings ("Group Audit — divided into X" pattern).
- `ring-N-pct` / `ring-N-sub` / `ring-N-note` — the number triple: headline %, "of component scope", count form "16 of 22 components". All three must be consistent: pct == dasharray number == the "X of N" numerator's own reading.
- `band-title` / `band-title2` — 46 / 40 — assertions, not "Observations".
- `band-p1..p4` — 150–260 chars each — why coverage moved and what residual means. This is where the page stops being a picture.
- `source` / `page` — always present; footnote superscript where the scope map is methodology.

FILL (build order, plus resizing — the diagram must be editable, not a picture):
1. Text first: `kicker`, `title`, `caption`, three `ring-N-*`, band headings, then footer. All editable nodes carry `data-slot`.
2. Per-ring numbers are in **three synced places** per ring — (a) the `ring-N-pct` text, (b) the accent arc `stroke-dasharray="71 100"` (the number IS the coverage %; because pathLength=100 no arc math), (c) the review wedge `stroke-dasharray="17 100" stroke-dashoffset="-71"` (its offset = coverage %; its dash length = review %, the remainder is the visible gray track). Change coverage: edit (a)+(b); review-only share: (c). If audit+review exceed 100, the wedges will overlap visibly — that IS the error check.
3. Accent change: recolor `--accent`; also update the `band-rule` background and red `h3` fills (all read the token — a single variable change suffices, plus optionally `--accent-tint` for the hatched "not in scope" wash if you add one).
4. **Add a ring (N → 4):** copy one `<g class="ring">` wholesale, change `translate(cx,140)` to cx = pitch·(i+½) with pitch = 1152/N (for N=4: pitch 288, cx 144/432/720/1008). All inner geometry is local to the group — label centering via `text-anchor:middle` reflows free. Nothing else reflows: svg width, band and legend stay put.
   - **Remove a ring:** delete the `<g>` and re-pitch the remaining cx values the same formula (e.g. 2 rings → cx 288 / 864, pitch 576). Keep N ≥ 2 or the single ring stops being a comparison and belongs on a donut-claim page instead.
5. **N ≥ 5:** pitch < 240 and the red `ring-N-label` (13 px) collides. Fix: shorten labels to the component name only (≤16 chars, drop the "Group Audit —" prefix, the band explains) and if labels still collide at N=6/7, raise `y=-92` to −104 and let labels stack above the ring field (270→252 field height still fits inside svg 264); past that, split the page.
6. **N = 1 or 2:** for two rings, add a faint center line at x=576 with `--rule` and shorten labels to fit. For one ring, replace the ring field with the donut-claim pattern from `donut-claim-center` (see DON'T).
7. Review wedge off: delete the second arc circle (keep the track), keep the legend square but change its key text to "Reviewed — control testing" pointing to band-p4. Not-in-scope is never explained as a wedge, it is simply the visible track.
8. **The rest of the page is independent:** the band columns are normal grid flow — adding a 4th column breaks it; keep 2 columns or replace with one full-width paragraph grid `1fr`.

CHART RECIPE (how this figure encodes):
- One arc per coverage fraction, 12 o'clock start, clockwise, arc sweep = coverage %. No areas scaled (ring width is fixed 26 px — coverage is shown by sweep, not radius: changing radius would lie).
- Review wedge is the same ring, same width, darker gray, starting where coverage ends — coverage + review ≤ 100, remainder is track gray-4.
- Emphasis: one hue (red) for "audit coverage", rest gray ramp. Never two coverage hues.
- Percentages inside the ring hole, not on the arc; the arc is qualitative, the number is authoritative.
- No value ticks, no gridlines, no "0–100%" axis — this is a part-to-whole reading, not a time series.

VERIFY:
- [ ] Title ≤15 words / 2 lines; numeric present and matches the rings it quotes.
- [ ] Dasharray pct, hole pct, "x of n" note and band prose all say the same number.
- [ ] Review offset == coverage pct on every ring (dashoffset is `-`coverage).
- [ ] One accent hue; gray ramp only elsewhere; red text only ≥13 px bold.
- [ ] `caption` is a sentence, not the title again; band h3s are assertions.
- [ ] Source line + page present; `<sup>1</sup>` for scope-map claim.
- [ ] Resize proof: delete one ring, re-pitch cx per FILL 4 — rings stay centered in 1152 field, labels don't collide.

DON'T (corpus failure modes):
- Turning this into a 3-set overlapping venn to look like a venn — the p103 page is honest about being coverage; if you need real intersection claims, build `venn-diagram-triad` and put this on a second page.
- A second "second coverage" hue for review (teal/red "audit types" variants appear in the corpus) — review is gray, only audit is red.
- Putting percent labels *on* the ring arc — 21 px text doesn't survive a 26 px stroke; labels go in the hole.
- Topic titles ("Scope of work"), kicker walls, band paragraphs longer than 4 lines each.
- Scaling ring radii by coverage (radius = component size is a *different* chart; you would need an explicit radius rule and a legend, and it fights the arc encoding).
- 6+ rings on one page.
- Putting the source line or a legend inside the ring field (the rings need their clear band).

SOURCE: extracted from `sw_pages/pwc_strategy__pwc_pwc_annual_report_2018/pg-103.png` (and sheet cell `pwc_strategy__pwc_pwc_annual_report_2018_s10.jpg` row 1 col 2) — read as full page: three donut rings each with red coverage + small gray review segment, red ring-head labels above, "■ Audit / ■ Review" key under each, two red hairline rules separating two blocks of legal text, Georgia-class serif on paper white, `103 | PwC Annual Report 2017-2018` + nav chevrons bottom. Catalog row: `reviews/pwc_strategy__pwc_pwc_annual_report_2018_slides.csv` p103 "venn-diagram / red-gray overlapping circles". Analysis: `reviews/pwc_strategy__pwc_pwc_annual_report_2018.md` — palette: "PwC brand red/crimson, single accent … ≈#D60A2C–#E1123C … lighter pinks for donut tracks … charcoals ≈#58595B … light gray table fills ≈#E6E6E6", typography: "house font system, not PowerPoint defaults", editorial rule device; colophon page confirms single-brand discipline. Kit tokens from `DESIGN_PLAYBOOK.md` (one accent + grays; paper-white ground per spec).
