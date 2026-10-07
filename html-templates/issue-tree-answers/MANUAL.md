# issue-tree-answers — Question Tree with Answer Panels (1280×720)

WHEN: Two-level question tree where the right-hand column is the register of what each branch *answered* — stat, claim, and answered/largest/set-aside status. Use when the page's job is "we decomposed the question and here is the answer to each part" — the readout of a hypothesis-driven week. It is the answer-panel widening of Umbrex S1752 ("Template — Hypothesis Tree", 2-level navy/cornflower/grey scaffold, `corpus/sheets/sheet_176.jpg` row 1 panel 2); the discipline (numbering, one focus, dim the set-aside) is from `reviews/umbrex_patterns.md` §4. For a 3-level tree that ends in evidence leaves, use `issue-tree-hypothesis`.

## ANATOMY (slot map, stage px)
1. `kicker` — x64 y36, 12/1 uppercase ls 1.8, `NN | Section`, numeral in accent.
2. `title` — x64 y58, w 1152, 28/36 bold navy; the claim answers the root question; `<sup>` on modelled figures.
3. `lead` — x64 y138, 13/16.5 bold; names the convention; 56px accent underline below (must stay short — the branch column starts at x430).
4. `tree` — SVG overlay, stage-sized. Rows = branch + panel **sharing one centre line**, centres **170 / 360 / 550** (pitch 190):
   4a. `root` — x64, **236 × 112**, navy, centred on row 2 (y360). Label 9px + question 12.5/18 × 3 lines.
   4b. `branch-1..3` (sub-questions) — x430, **250 × 76** (y = centre−38), white fill, rule stroke; focus branch teal 2.5 stroke. Number badge r 11.5 on left edge; question 11.5 bold + scope note 9.
   4c. `panel-1..3` (answers) — x786, **430 × 104** (y = centre−52). Head `WHAT WE FOUND — n` 8.5 ls; stat 23 bold (x16); chip 16px-tall top-right (x316..396); claim 10/14 × 2 lines right of the stat (x116). Focus panel: teal 2 stroke + 5px teal left bar, `LARGEST` teal chip. Set-aside row: `dim` class + `stroke-dasharray="4 3"`, chip outline style.
   4d. `links` — root elbows `M300 360 H356 V{rowY} H430`; branch→panel one straight segment `M680 {rowY} H786`. Focus links teal 2.2.
5. `legend` — x64 bottom 34: the three chips with their swatch dots. `source` x64 bottom 14; `pageno` right 64 bottom 14.

## SLOTS (name — limit — good/bad)
- `title` — **≤15 words / 2 lines** — answers the root question in the title itself ("All three answers point to cost, not price…"). A title that restates the question duplicates the root box.
- `root-q` — ≤18 chars/line × 3 lines — one measurable question; if you can't phrase it, the decomposition isn't ready.
- `branch-q` — ≤28 chars — a question, not a category. "Are unit costs breaking?" (open) is the genre; "Costs" is a tab.
- `branch-note` — ≤30 chars — what evidence was looked at ("labour, shrink, freight") so scope is auditable.
- `panel-stat` — ≤8 chars — one headline number per answer, in the root question's units. "—" is allowed for not-yet-answered.
- `panel-claim` — **2 lines × ≤37 chars** — what the answer asserts, with one number inside. More than two lines is an overflow, not a layout.
- `chip` — 1 per row, ≤9 chars: ANSWERED / LARGEST / SET ASIDE (add OPEN if a live branch exists — grey outline chip).
- `legend` / `source` / `pageno` — always; footnote sups where figures are modelled.

## FILL (build order + resizing)
1. Root question first, then branch questions (MECE, parallel phrasing), then the paired panel (stat + claim + chip), row by row — the panel is not separate content, it is that row's verdict.
2. **Status swap (the maintenance edit):** each row's chip is one rect + one text; set-aside look = `class="node dim"` on BOTH groups of the row + `stroke-dasharray="4 3"` on the two rects + outline chip (white fill, rule stroke, gray-3 text). Answered = gray-4 chip. Largest = teal chip + teal strokes, and that's also what moves when the recommendation shifts. Exactly one LARGEST per page (or zero, pre-readout).
3. **Add a 4th row:** copy `node-q1` + `panel-1` + both of that row's link paths; then set centres by the row formula **centre(i) = 170 + i × (380 / (n−1))** — for n=4: 170 / 296.7 / 423.3 / 550. Per row you change: branch `translate(430, centre−38)`, panel `translate(786, centre−52)`, both link paths' `V{centre}` / `H` endpoints (the two `V` in the root elbow and the straight segment), the panel head number, and the elbow `M300 360` stays put. n=4 clears (pitch 127 vs panel 104); **n=5 is the cap** and only by shrinking panels to `height="87"` (claim to one line) — past that use `issue-tree-hypothesis`'s leaf form or two pages.
4. **Remove a row:** delete its two `<g>`s + the two paths, renumber rows/heads, re-centre survivors with the same formula. Keep the removed question as a dimmed row if it was examined — dimming is the house "we looked" marker.
5. **Add a sub-sub-question:** this form has no third level; either collapse (the claim absorbs it) or switch templates. Don't cram a child node between branch and panel — the straight link is what makes the answer column readable.
6. **Accent change:** swap `--accent`; teal→any lighter accent, keep ink-colored text on chips (teal under navy text measures ≈7:1 here). `--ink` stays navy; do not recolor the root box, the focus is the accent's job. Palette anchors (navy #1F2A65, teal #00D4C8) from `reviews/umbrex_patterns.md`; real deck faces were Calibri/Arial (stock template typefaces) — the CSS stacks stand in.
7. Stat/claim typography is fixed at x16/x116 — long claims wrap inside the 37-char budget; never push stat and claim into one line.

## DIAGRAM RECIPE (how the figure encodes)
- Encoding: horizontal containment (question splits) + a verdict column (row = question↔answer pair). No scales; the only numbers are the answers themselves.
- Emphasis rule: exactly one LARGEST row carries teal (strokes, bar, chip, links). Everything else is gray ramp + white.
- Dimming rule: set-aside rows keep full content at 0.78 opacity + dashed stroke — visible so the MECE set reads complete, quiet so the live rows lead.
- Chip legend is mandatory here; chips are the only symbols the reader didn't already have.
- Text-on-accent: navy on teal (≈7:1); white numerals on gray/teal badges, never gray-3 on teal.

## VERIFY (against the render)
- [ ] Title ≤15 words/2 lines and *is* an answer, not the question.
- [ ] Exactly one teal row (or zero); one chip per row; legend explains all chips.
- [ ] Stat + claim fit without touching the chip zone (x316..); claim ≤ 2 lines.
- [ ] ≤2 hues total; dimmed row still legible (check claim at 0.78 gray-3: ≥3:1 large text — if not, darken note fill, not opacity).
- [ ] Numbering 1/2/3 matches panel heads "WHAT WE FOUND — n".
- [ ] Source + page number present; sup markers on modelled figures.
- [ ] Resize proof: FILL 3 run end-to-end — 4th row lands without overlapping panels.

## DON'T (corpus failure modes)
- Answer panels with just a % and no claim — the number without the sentence is why SmartArt decks get "so what?" back.
- Chips as decoration (one on every row saying ANSWERED when one is clearly open) — status is data.
- Four "answered" rows and one teal — if everything is largest, nothing is; pre-readout decks ship zero LARGEST legitimately.
- Question categories instead of questions ("Price" as branch) — the branch must be answerable.
- A third level squeezed under panels (see FILL 5) — the corpus's own answer is a second page.
- Panel claim as a third paragraph wall: two lines is the genre.

## SOURCE
Umbrex template deck S1752 ("Template — Hypothesis Tree") read in `corpus/sheets/sheet_176.jpg` row 1: navy root box, two cornflower mid boxes, grey side-leaf boxes on elbows — side leaves widened into answer panels here. Status/dimming discipline: `reviews/umbrex_patterns.md` §4 + palette line (navy ~#1F2A65, teal ~#00D4C8, cornflower ~#6E93C4). Placeholder content (NorthCo retail turnaround) is invented; no client meaning in any name or figure.
