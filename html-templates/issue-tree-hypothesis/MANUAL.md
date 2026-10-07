# issue-tree-hypothesis — 3-Level MECE Issue Tree (1280×720)

WHEN: Decomposition page for a single big question: key question on the left, MECE hypotheses, evidence leaves underneath each. The workhorse of real issue work — the page that says "we split the problem properly and we know which branch we're pulling." From Umbrex template-deck S1753 ("Template — Issue Tree", read in `corpus/sheets/sheet_176.jpg`), with the numbering + dimming discipline from `reviews/umbrex_patterns.md` §4. For a 2-level tree whose leaves carry the answers themselves, use `issue-tree-answers`.

## ANATOMY (slot map, stage px)
1. `kicker` — x64 y36, 12/1 bold uppercase ls 1.8, `NN | Section` (numeral in accent).
2. `title` — x64 y58, width 1152, 28/36 bold navy, 2-line box; `<sup>` marker on the modelled number.
3. `lead` — x64 y138, 13/16.5 bold; names the split (never wraps into the tree); 56px accent underline rule below it.
4. `tree` — the SVG overlay, whole stage. Real boxes:
   4a. `root` — x64 y322, **252 × 116**, navy fill, "KEY QUESTION" 9px + question 12.5/18 white, centred on the middle branch (y 380).
   4b. `branch-1..3` — x440, **258 × 84**, centres y = **206 / 380 / 554** (pitch 174). Number badge (r 11.5) sits on the left edge, half in/half out. Head 12/15 + value-note 9.5. Branch 2 is the focus node: teal 2.5px stroke, 5px teal left bar, teal badge, `IN FOCUS` pill 88×17 above. Branch 1 is dimmed (gray-4 fill).
   4c. `leaves` — x812, **260 × 46**, three per branch, centres = branch centre −57 / 0 / +57. "x.y" numbering in 9.5 bold, right-aligned at x804. Focus leaves: white fill + teal 4px left bar; examined-then-set-aside leaves: gray-5 fill, gray-2 text.
   4d. `links` — elbow paths behind everything. Root→branch: `M316 380 H372 V{branchY} H440`. Branch→leaf: `M698 {branchY} H754 V{leafY} H812`. Focus paths teal 2.2px, dimmed paths opacity .75.
5. `legend` — x64, bottom 34, 9.5 gray-3: what Q / 1–3 / x.y and grey mean.
6. `source` — x64 bottom 14, 10 gray-3, footnote markers; `pageno` — x64-right bottom 14, bold gray-2.

## SLOTS (name — limit — good/bad)
- `title` — **≤15 words, ≤2 lines** — a claim with a number ("Cost — not price — explains 70% of …"). A topic title ("Margin issue tree") is a fail: the tree itself is the content, the title is the finding.
- `lead` — 18-30 chars — names the exhibit (the split), never restates the title and never becomes a second paragraph. Long lead-ins collide with the tree columns by construction — the kit genre is short.
- `root-q` — ≤46 chars/line × 3 lines — one measurable question (what/why/how), no compound "and".
- `branch-h` — ≤25 chars — the hypothesis as a domain noun ("Price & mix", "Cost base"); the MECE promise. Three vague branches read as a mind-map, not an issue tree.
- `branch-note` — ≤32 chars — attribution in the model's own units ("−160 bps · largest driver") — this is what makes the tree quantitative.
- `leaf-h` — ≤34 chars — the evidence item, not the metric family ("Shrink & outbound logistics", not "logistics KPIs").
- `leaf-note` — ≤30 chars — one number per leaf or an explicit "no change" negative result.
- `legend` / `source` / `pageno` — always; footnote sup after any modelled figure.

## FILL (build order + resizing)
1. Replace title / lead / kicker first; then the root question; then branch heads + notes (write them as a MECE set, not after the leaves). Then leaves.
2. **Recolour for another house accent:** swap `--accent` (and keep `--ink` navy). Text on accent must stay ≥4.5:1 — this template puts ink-colored text on teal pills (≈7:1), so a light accent is safe; a dark accent needs `fill:#fff` on the `.num`/`.chip` texts instead. The palette anchors it replaces (navy #1F2A65, teal #00D4C8, cornflower #6E93C4) come from `reviews/umbrex_patterns.md`; Umbrex's own deck sets type in Calibri/Arial (stock template faces) — the stacks here stand in for that.
3. **Add a leaf under a branch:** copy the `<g class="node" id="leaf-x-y">` block closest to it, change `transform="translate(812,{newTop})"` where newTop = leafCentre − 23, copy one `<path class="link">` from `links-b{y}`, set its final `V{leafCentre}`; set the "x.y" label text and its `y` (label y = leafCentre + 4). Three leaves per branch is the density cap on this stage (3×46 + 2×11 = 160 < 174 pitch); a 4th leaf under one branch overlaps its neighbour's row — shorten to two leaves or give the branch its own page.
4. **Add a 4th branch — usually a "make it a second page" moment.** The leaf column is shared: three leaf rows occupy ±80px around each branch centre, so adjacent branches need centre pitch ≥ 156, and 3×156 + leaf margins exceed the 135–650 tree band. **3 branches is the stage cap for this geometry** — same advice the corpus gives about 4×4 grids. If the 4th question is real, give it its own page and show the parent tree with a "carried to p.N" chip. Re-centring is otherwise: with 3 branches keep 206/380/554 (pitch 174); to shift the whole tree, move it as a unit by editing the three root elbows' `M316 {rootC}` + `V{branch}` pairs and every branch `translate` y together.
5. **Remove a branch:** delete its node group, its `links-b{y}` paths, and its root elbow — then renumber branches/leaves and (optional) re-centre the remaining rows with pitch 174 again. **Dim, not delete** is the house rule: an examined-and-set-aside branch keeps its box with the `dimmed` treatment (gray-4 fill, gray-3 badge/note, `.link.dim` paths) so the MECE set stays whole.
6. **Different fan-out (2 or 4 leaves):** keep leaf centres symmetric about the branch centre: ±d for 2 leaves (d=57 already), −1.5d/−.5d/+.5d/+1.5d with d=57 for 4 (extremes ±85.5, still inside the 174 band). The connector `V{}` value is the only number that moves.
7. `IN FOCUS` marker: exactly one per page (the recommendation branch). Moving it = move the teal stroke (`stroke="var(--accent)" stroke-width="2.5"`) and left-bar rects on the node, swap which `links-*` paths carry class `focus`, and move the pill rect+text.

## DIAGRAM RECIPE (how the figure encodes)
- Encoding = containment + hierarchy: question → MECE hypotheses → evidence. Position carries no scale — there is no axis to defend.
- Emphasis rule: one branch teal (focus), its leaves white-with-teal-bar, its links teal 2.2px. Everything else = gray ramp. One accent, ≤1 extra hue (navy is ink here, not a hue).
- Dimming rule: examined-and-set-aside = gray-4 fill + gray-3 type + 0.75-opacity links. Unexamined would be an *empty* slot with only the box — never render it.
- Numbering is the argument's address system: 0 root (none needed), 1..n hypotheses, x.y leaves. Keep it if you keep one thing.
- Text on navy: white; on teal pills: ink. No 10px gray notes inside accent shapes.

## VERIFY (against the render)
- [ ] Title ≤15 words / 2 lines; sup marker present where a figure is modelled.
- [ ] One teal branch, one `IN FOCUS` pill, teal links only along it.
- [ ] All non-accent fills from the gray ramp; ≤2 hues total.
- [ ] White-on-navy ≈ 13:1; ink-on-teal pills ≥ 4.5:1; gray-3 used for notes/dimming only.
- [ ] Numbering consistent 1, 1.1, 1.2 … / 2 … no gaps after edits.
- [ ] Source line + page number bottom; leaf numbers right-aligned at x804.
- [ ] Resize proof: added a leaf per FILL 3 without touching any other leaf's coords.

## DON'T (corpus failure modes)
- SmartArt "vertical box" clone — equal boxes, equal fonts, no numbering, no dimming. That is a org chart wearing a tree costume.
- Topic branches that overlap ("price", "customers", "cost") — the whole point of the page is the MECE claim; overlaps belong in a brainstorm.
- All three branches accented, or nothing accented — the tree must land somewhere or the page is a drawing.
- Leaf text longer than the box (11px ≤ 34 chars) — the box does not grow, the page gets dirty.
- Kicker as a paragraph; kicker walls of text are the corpus flaw.
- Ten leaves on one branch (density cap is 3, see FILL 3).

## SOURCE
Umbrex template deck, slides S1752–S1753 ("Template — Hypothesis Tree", "Template — Issue Tree"), read as the third panel of row 1 in `corpus/sheets/sheet_176.jpg` (S1753 = 3-level branch-and-leaf with navy root / cornflower mid / grey leaves). Palette + numbering + dimming conventions: `reviews/umbrex_patterns.md` §4 (S1752/S1753) and house-palette line (navy ~#1F2A65, teal ~#00D4C8, light blue ~#6E93C4). Placeholder content is invented (NorthCo retail turnaround) — figures and names carry no client meaning.
