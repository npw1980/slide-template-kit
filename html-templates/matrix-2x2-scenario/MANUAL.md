# matrix-2x2-scenario — Real-Axis Scenario Matrix (1280×720)

WHEN: Two-binary-axis framework page. Use when a decision reduces to *two* opposing conditions and every cell needs its own argument — scenario / demand-path grids, "ways to play", BCG-style selectivity grids. Not for four parallel themes with no axes: that is `matrix-2x2-panels`. It is a real diagram: both axes carry names, the cells carry numbers, and the emphasis is an argument rather than a palette. Provenance: PwC *E-Mobility in India: market paradigms and ways to play* (ACMA, 2021) p13; frame convention from Umbrex S1765-70.

ANATOMY (numbered slot map, 1280×720 stage px):
1. `kicker` — x64 y40, 12/14 bold, uppercase, letterspaced 1.8; the section marker `02 | Scenarios & demand outlook` (accent on the numeral).
2. `title` — x64 y66, width 1152, 31/42 bold, 2-line box (max-height 84).
3. `lead-in` — x64 y160, 13/16 bold with a 2px accent underline; the exhibit's own caption line.
4. `matrix` — x64 y196, **1152 × 450**. Grid = `96 / 1fr 1fr` columns × `54 / 1fr 1fr` rows, `gap:2`, background `--rule` shows through the gutter as the cross-lines.
   4a. `axis-name` — corner cell (col 1 / row 1), 10px uppercase gray, right-aligned: `Sourcing footprint →`.
   4b. `col-1`, `col-2` — column headers, row 1, height 54, ink fill white text (col 2 one step lighter, `--gray-3`).
   4c. `row-1`, `row-2` — rail cells, column 1, width 96, `writing-mode:vertical-rl; rotate(180)` so text reads bottom-up.
   4d. each `cell-NN` is **526 × 196**.
   4e. `cell-11` (col 2/row 2), `cell-21` (col 3/row 2), `cell-12` (col 2/row 3), `cell-22` (col 3/row 3). Each = `.q-head` pill + `.q-icon` 44×44 hairline box at x+~467,y+13 + `.q-body` bullets.
5. `axis-note` — x64 y652, 10/13 gray: reading instruction + the examined/not-examined legend (2 swatches, right-aligned).
6. `source` — x64 bottom 22, 10/13 gray, max-width 640, with `<sup>1</sup>` for the methodology claim.
7. `deck-tag` — centered `Point of View | E-Mobility`; `page` — bottom-right, bold gray-2.

SLOTS (name — limit — what makes it good / bad):
- `kicker` — 46 chars — a section marker, not a subtitle. Wall-of-text kickers are the corpus flaw.
- `title` — **≤15 words, 2 lines** — an assertion with a number or a consequence ("Four scenarios decide how quickly e-mobility scales"); a topic title ("EV scenarios in India") is a fail.
- `lead-in` — 18-24 chars — names what the exhibit shows ("Different scenarios"), never repeats the title.
- `axis-name` / `axis-note` — 30 / 120 chars — say how to read the grid; the axis labels alone do not tell a reader whether cells are segments, scenarios or options.
- `col-1`, `col-2`, `row-1`, `row-2` — 11-24 chars each — **polar opposites on one measured dimension** ("Localized" vs "Import-dependent"). Two unrelated categories on one axis is what turns this into SmartArt.
- `cell-NN-head` — 15-32 chars — the cell's *thesis* (economics + behaviour), not the axis label again.
- `cell-NN-points` — 3 bullets, ≤13 words each, ≥1 bullet carrying a number — the cell must argue something the other three cannot.
- `source` / `deck-tag` / `page` — always present; superscript footnote marker where the grid is a model output.

FILL (build order, plus resizing):
1. Replace `title`, `lead-in`, `kicker`. Then swap the four axis labels first — every cell text is written *against* those two axes, so the axes are the contract.
2. Cell text: edit the 4 × `.q-head` and the 4 × `.q-body` lists. Bullets are plain `<li>` with one `<b>` lead-in each; the marker square is CSS (`::before`), do not add glyphs.
3. Emphasis: exactly the cells that carry the argument get class `hl` (accent fill, inverted pill). `dim` = examined-but-unresolved or out-of-scope: gray-4 fill, gray-3 type. **Dim, never delete** — a missing cell reads as "the axis does not go there".
4. Icons: 4 inline SVGs (stroke 1.4, `currentColor`). Keep one glyph per cell; a glyph set of 4 unrelated metaphors is decoration. Replace by editing the paths, keep the 26×26 viewBox and the hairline box.
5. **Add a third column (x-axis gains a pole):** copy the `col-1` header block, set `style="grid-column:4;grid-row:1"`; copy the two cells in column 3 (`cell-21`, `cell-22`), set `grid-column:4`, `grid-row:2` / `3`. Then change `.matrix` to `grid-template-columns: var(--rail) 1fr 1fr 1fr`. Cell width reflows 526 → **350**; nothing else changes, no coordinates to recompute. If a 4th pole is needed, shorten it to one word — 1fr cannot shrink below the glyph.
6. **Add a third row (y-axis gains a stage):** copy a `.rail`, set `grid-column:1;grid-row:4`; copy the two cells of row 3, set `grid-row:4`; set `grid-template-rows: var(--head) 1fr 1fr 1fr`. Cell height 196 → **131**: drop the 4th bullet, icon box stays 44.
7. **3×3 grid** (both): cell **350 × 131**, 3 bullets max per cell. That is the ceiling — under ~131px of cell height three 11.5px bullets plus a pill do not fit, and a 4×4 on this stage is unreadable; make two pages instead.
8. **Remove a column or row:** delete the cells (and its header/rail), then renumber `grid-column`/`grid-row` on everything to the left/below it. Grid gaps do not renumber themselves; the symptom is a trailing 2px orphan line, and a cell sitting in the wrong row.
9. **Leave one cell blank-but-real:** keep the DOM node, add `dim`, set head to `Not applicable`, bullets to one line saying why. Do not remove it — 3-of-4 leaves the grid's axis honesty broken.
10. Accent change: recolor `--accent` (and `--accent-2` if used) only; the header band is `--ink`, not accent, so a warm brand does not turn the grid orange-on-orange. For the PwC house variant, see the comment block at the end of `index.html` (`--accent:#E2192A`, serif title): white on that red measures 4.8:1.

CHART RECIPE (how this figure encodes):
- Encoding = position on two named binary axes → 4 cells. No sizes, no areas, no bubbles; nothing is scaled, so there is no scale to defend and no axis units. State that in the `axis-note` if a reader might expect quantities.
- Emphasis rule: 1-2 cells accent-filled (one diagonal pair = the two end-states; one cell = the recommended play). Never all four; the page then says nothing. Everything else is gray ramp + white.
- Dimming rule: gray-4 fill + gray-3 text = "we looked and did not carry this". Keep the head pill so the cell still reads.
- Direct labels only: the argument lives in the pill and the bullets. No legends, no callout balloons, no key on the side.
- Text-on-accent: white 11.5-12.5px on `--accent` (5.7:1) or on the inverted pill. Do not put 10px gray-3 notes inside an accent cell.

VERIFY (run against the render):
- [ ] Title ≤15 words, ≤2 lines (`h1.title` box is 84 tall; a third line is an overflow, not a layout).
- [ ] Both axis names state one measured dimension and their poles are genuinely opposed.
- [ ] One emphasis color in the frame (accent + grays only, ≤2 hues total).
- [ ] Every examined cell has ≥1 numeric bullet; the source line is present with a footnote marker where the grid is modelled.
- [ ] Text on accent clears 4.5:1 (white on #2251FF = 5.7, on #E2192A = 4.8).
- [ ] `axis-note` explains how to read the cells; page number bottom-right.
- [ ] Resize proof: adding a column per FILL 5 reflows cells to 350px with no manual coordinate edits.

DON'T (failure modes seen in the corpus):
- Four boxes with no axis labels — the SmartArt "quadrant" that says nothing about what separates them.
- Both axes as adjectives ("high"/"high") without stating *what* is high; the reader has to guess the measurement.
- Same bullet text repeated across cells because the copy was written first and the axes later.
- Topic titles ("Scenario analysis"), 10-15 word kicker walls above the grid, 4-5 bullets/cell.
- Arrows or speech-pointers between cells when no flow exists (the PwC boardroom p35 quad does this; the review flags "arrows imply interaction but no diagram semantics").
- Gray-on-gray body text (the Accenture IAC 2x2 message-grid page is cited in DESIGN_PLAYBOOK as the low-contrast flaw) — gray-3 belongs to source lines, not bullets.
- A second hue for "the other stakeholder" (amber in the source deck) — that is a color argument, and this frame has one accent.

SOURCE: extracted from `sw_pages/pwc_strategy__pwc_e_mobility_in_india_market_paradigms_and_ways_to_play_20/pg-13.png` (sheet `pwc_strategy__…20_s01.jpg`, row 1) — read as a full page: ink column-header band, vertical rail labels, 4 quadrant cells with pill + boxed icon + 3-4 bullets, opposite corners in house red #E2192A on gray. Supporting page: `sw_pages/pwc_strategy__pwc_boardroom_agenda_2022/pg-35.png` (2×2 quad, arrow-pointer device, deliberately not ported). Catalog: `reviews/pwc_strategy__pwc_e_mobility_in_india_market_paradigms_and_ways_to_play_20_slides.csv` (archetype "scenario matrix", charts "2x2 matrix") and `reviews/pwc_strategy__pwc_boardroom_agenda_2022_slides.csv` (p35 "2x2 icon quad"). Analysis: `reviews/pwc_strategy__pwc_e_mobility_in_india_market_paradigms_and_ways_to_play_20.md` — color section (near-black #1A1A1A, grays #F2F2F2/#D9D9D9/#9AA0A6, accent #E2192A / maroon #7A0F1F), typography (Georgia-class serif titles ≈16-18pt page titles, Arial-class 9-10pt body, bold lead-in + regular continuation), devices ("no SmartArt-generic pages — every shape device is data-labeled, incl. the 2×2 scenario matrix"), palette ruling "1 accent + neutrals, color never decorative". House tokens from `DESIGN_PLAYBOOK.md` §palette ruling (navy #051C2C + one accent + 2D2D2D/464646/7D7D7D/DEDEDE).
