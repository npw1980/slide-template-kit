# process-flow-pathway — Pathway Summary (lane map + milestone callouts + duration ribbon + stage chevron band, 1280×720)

WHEN: Whole-of-pathway "this is what the route actually looks like" pages — the summary exhibit that opens a chapter or closes a process section: an actor-lane process map, the dated milestones that mark it, how long each stage takes, and the stage names as a footer band. From the Deloitte Accelerated Access Review "pathway summary" pages p15–p17 (`reviews/deloitte__deloitte_accelerated_access_review_uk_mapping_2015.md`, callout 3: "swimlane pathway maps with time ribbons"). Where the other member of this family (`process-flow-stage-matrix`) compares alternative models, this one maps ONE route.

## ANATOMY (slot map, stage px)
1. `kicker` — x64 y36, 12/1 bold uppercase ls .18rem, `15 | …` (numeral in accent).
2. `title` — x64 y56, 27/35 bold ink, width 1152, ≤2 lines; `<sup>` marker where a figure is modelled.
3. `lead` — x64 y100, 13/17 bold, width 1152, 2 lines; the message line (in the source deck this is the argument-bearing subhead).
4. `lanes` — SVG, 3 actor bands, band dividers y=265 / y=395 (x64→x1216). Node rows: lane 1 y182–218, lane 2 y312–348, lane 3 y442–478. Lane chips x64 w118 h24, centred on lanes (y188 / 318 / 448).
5. `nodes` — `<g class="nd" translate(x,y)>`, 124×36 box, label centred (62,22). Node x-centres used: 275 / 531 / 787 / 1043 (stage columns are 288 wide from x64).
6. `links` — connectors behind nodes: horizontal `M{rightEdge} cy H{leftEdge}` with `marker-end="url(#ar)"`; cross-lane elbows `M{cx} {yBottom} V{yTop}` (vertical) or `V{y} H{xEdge}`.
7. `milestones` — `<g class="ms" translate(x,555)>`: circle r5.5 + name (y15, 10 bold) + cumulative months (y26, 9 grey); its dashed leader line is one of the `<g id="drops">` lines (x553→170) drawn behind the map. Baseline is fixed at y=555.
8. `durations` — `<g class="brk" translate(stageX,602)>`, one per stage column: double-ended arrow line (x12→W−12) + centred range label y19. Same column x's as the stage band.
9. `stageband` — `<g class="chev" translate(x,632)>` y632–676 (h44): grey ramp stages 1–3, last stage accent; white text on dark fills, ink on light fills. Tip/notch depth t=14.
10. `ornament` — four small stage-coloured chevrons x1060–1190 y38–54 (the source deck's recurring top-right section indicator).
11. `source` — x64 bottom14, 10 grey-3, sup markers; `pageno` — right64 bottom14, bold grey-2.

## SLOTS (name — limit — good/bad)
- `title` — **≤15 words, ≤2 lines** — a claim ("adds no step … only time"), not a topic. The page is evidence FOR the title; if the title is "Medical devices pathway" the page has no argument.
- `lead` — ≤2 lines — names the comparison and the dimension that differs (duration, not steps). Never restates the title.
- `lanes` — 2–4 — the actors whose hands touch the route (Manufacturer / Regulator / Payer). A lane with no nodes is a lie — merge or delete it.
- `ndl` (node) — ≤22 chars — a state, not a task family: "Technical file + UDI", not "Documentation". Present-tense noun or past-participle ("submission", "published").
- `msn` (milestone) — ≤20 chars — an event the client can verify exists ("HTA submission"); `msx` — one number, cumulative months (or "n/a" honestly).
- `durT` (duration) — ≤11 chars — a RANGE ("4 – 18 mo."), never a point: single-point durations claim false precision on a pathway page.
- `cvt` (stage name) — ≤15 chars — the stage as the client's own vocabulary names it.
- `source` / `pageno` — always; sup after n=, modelled ranges, timelines.

## FILL (build order + resizing)
1. Replace kicker / title / lead, then stage names + durations (they define the columns), then lanes, nodes, milestones — the column model constrains everything downstream.
2. **Stage count — the master reflow.** Columns: `W = (1152 + 28·(N−1)) / N`; stage i `translate(64 + i·(W−28), 632)`; chevron polygon `0,0 {W−14},0 {W},22 {W−14},44 0,44 14,22` (first stage flat-left: drop the `28,22` tail point). Duration brackets sit at the same x with `x2 = W−12`, text at `W/2`. For **3 stages**: W=404 → x = 64 / 468 / 872, arrows 12→392, text x=202. For **5 stages**: W=243.2 → x = 64 / 307.2 / 550.4 / 793.6 / 1036.8. Copy one `<g class="chev">` and one `<g class="brk">` per added stage. The last stage keeps `fill="var(--accent)"` (the destination), earlier stages step down the grey ramp `#262B30 → #565E65 → #E9ECEF → …` — with 5 stages make stage 2/3 both mid-grey and the extra stage grey-4.
3. **Add / remove a process node.** Copy a `<g class="nd" translate(x,y)>`, set x to a free column centre (275 / 531 / 787 / 1043 / 1171 within lanes) and y to its lane row (182 / 312 / 442), then add its connectors: horizontal `M{x+124} {cy} H{next−124}` or the vertical transfer to the lane below/above. Max **3 nodes per lane** (column width 288, node 124 + 2×20 arrow run). Remove = delete the group + its connector paths; renumber nothing (nodes carry no numbering here).
4. **Critical path (the one emphasis).** Three nodes carry `class="nd crit"` + an accent `rect.wash`, two `path.lk.crit` connectors carry `marker-end="url(#arA)"`. Move it by moving those classes — exactly one path per page.
5. **Add a milestone.** Copy `<g class="ms" translate(x,555)>`, copy BOTH the `ms` group and its line in `g#drops` (same x), choose x under a real event (avoid <70px spacing from the neighbour, avoid crowding the next label), write name + cumulative months. Leader lines span y553→170 and paint behind the node boxes (white fills cover them) — shortening or extending one changes only that line's `y2`; the circle/label never move.
6. **Add a 4th lane.** Extend one divider `y` (e.g. 265/395 → 265/395/505), shift the lane-3 row to y525+ and re-space — the band is tight; a 4th actor usually means the page wants to be a swimlane detail map (`p23` in the source deck), i.e. two summary pages.
7. **Recolour house:** swap `--accent`; keep ink. Ink-on-lime is ~7:1, white-on-#262B30 ~14:1; if the new accent is LIGHT (e.g. a sky), the last stage's label stays ink (fine) but check node wash contrast is irrelevant (wash is decorative) and the ornament keeps `fill="var(--accent)"`.

## DIAGRAM RECIPE (how the figure encodes)
- Three encodings stacked: lanes = WHO, node chains = WHAT (in order), milestone row + duration ribbon = WHEN, chevron band = the stage vocabulary. Same four questions Deloitte answers with p15–p17.
- One accent: the critical path (nodes, wash, arrows). Everything else is grey + the stage band ramp (grey is the series colour here, lime is "the goal state").
- Drop-lines are DASHED on purpose: they are leader lines, not process arrows — never give them markers.
- Durations are per-stage ranges, drawn as double-ended arrows across the stage's own column so the eye can read "column 2 is the bottleneck" without numbers.
- Cumulative months under milestones (13 / 33 / 51 / 67 / 118) give the page a monotone time axis; label the unit once ("mo.").

## VERIFY (against the render)
- [ ] Title ≤15 words / 2 lines; sup markers after n= and modelled figures.
- [ ] One accent (critical path + last stage + ornament tail); ≤1 extra hue total; every grey fill from the ramp.
- [ ] White text only on #262B30/#565E65/#23262B-class fills; ink text everywhere light (ink-on-lime ≈ 7:1, ink-on-grey-4 ≈ 12:1).
- [ ] Every drop-line lands on a milestone that marks a real event (name it as of this file); no dots without a story.
- [ ] Duration ranges sum in the same units and roughly agree with the milestone months (sanity, not arithmetic).
- [ ] Chevron band right edge lands exactly at x1216; stage band columns and duration brackets share boundaries.
- [ ] Source line bottom-left, pageno bottom-right, ornament present (page signature).
- [ ] Resize proof: added a 5th stage via FILL 2 without editing any node or milestone.

## DON'T (corpus failure modes)
- Topic title under a fully detailed map — the source deck's own green topic-label style, which reads as contentless in a kit page that already carries the lead-in line.
- One dot per stage (uniform 4-dot timeline) = SmartArt; milestones must sit where events are, unequal spacing is the point.
- Point durations ("12 months") — ranges only, and never a range wider than the whole journey.
- Rainbow stage band (cyan/green/grey/yellow copied straight) — the source's stage hues carry semantic colour code across the deck; in a standalone kit page that palette is decoration, so grey + one accent.
- All-crossing connector spaghetti (the source p23 detail map earns 20+ crossings by being a reference map; this summary page caps at ~10 connectors).
- Node text >2 lines or 8px notes inside boxes.

## SOURCE
Deloitte — *Accelerated Access Review, UK mapping* (2015), pages 15–17 "pathway summary", read in `sw_sheets/deloitte__deloitte_accelerated_access_review_uk_mapping_2015_s01.jpg` (bottom row, cells p15–p20; viewed cells p15/p16 at `k_mapping_2015 p16/p17`). Structural analysis: `reviews/deloitte__deloitte_accelerated_access_review_uk_mapping_2015.md` (colour-system section: stage-colour semantics; callout 3: swimlane maps + time ribbons; title/lead style "scannable green topics + argument-bearing subheads"). Brand anchor: Deloitte green, rendered `#86BC25` — same anchor already used in sibling `agenda-contents-tracker` (real deck face is Calibri/Frutiger-family; the Helvetica/Arial stacks here stand in for it). The four-stage semantic colouring of the source is collapsed to grey-ramp + one accent per the kit rule (see DON'T).
