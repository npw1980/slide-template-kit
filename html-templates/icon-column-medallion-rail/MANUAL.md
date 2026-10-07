# icon-column-medallion-rail — Commitment block with a five-disc gradient medallion rail

WHEN: Use when a page must show "what we are on about" as a set — programme pillars, commitments,
capability areas — under a title, with the set legible at a glance from the back row. The device is a
blue title with a magenta hairline, dash-bullet commitment blocks, and a rail of filled circular
medallions carrying white pictograms and captions. Evidence:
kpmg__kpmg_kpmg_our_impact_plan_2022_update_2022 p37 ("Our commitments"), read in
`sw_sheets/kpmg__kpmg_kpmg_our_impact_plan_2022_update_2022_s03.jpg` (row 2, frame 2). The same disc
device recurs on p38 (three violet→blue discs) and p39 (three blue discs on the ESG tree) of the same
sheet, so it is a house component, not a one-off.

ANATOMY: numbered slot map on the 1280×720 stage (`rem` == stage px):
1. `slot-kicker` — 56,38. Uppercase 11px, .13em, gray-2.
2. `slot-title` — 56,56 → max-width 1120. 28px bold print blue `#0049C0`, ≤2 lines.
3. `rule` — 56 → 1224, y 118, 2px magenta `#E6007E`. The deck's title signature: a thin rule, not a bar.
4. `slot-lead` — 56,133 → max-width 900. 12.5px / 1.5, one bold phrase, one footnote marker.
5. `slot-h2-1` + bullets 1–4 — x 56, y 214, width 560. Theme 1.
6. `slot-h2-2` + bullets 1–4 — x 664 (left:608 + padding), y 214, width 560 → right edge 1168. Theme 2.
7. `slot-rail-label` — 56,432. Small uppercase line above the rail, with a magenta phrase. A 1px hairline
   (`.rail-rule`, y 410) separates the commitment blocks from the rail; keep it, otherwise the rail
   floats and the band above it reads as dead space.
8. `slot-cap-1..5` / `slot-sub-1..5` — five equal cells from x 56 to 1224 (each 233.6 wide), 96px
   disc centred in its cell at y 456–552, caption 12px bold print blue 12px below, sub-line 10.5px gray.
9. `source` — 56, bottom 26 → max-width 1010. Superscript markers.
10. `pagestamp` — right margin, bottom 26: "p. 37 | OUR IMPACT PLAN".

SLOTS:
- `slot-title` — action title, HARD GATE ≤15 words / ≤2 lines. The source deck's habit is a statement
  with the statement device elsewhere; here the statement is the title, so make it count: number the
  set ("Five commitments…") when the count is real, otherwise say what changes.
- `slot-lead` — ≤330 chars / 3 lines. Explains how the set is organised or bounded. Bad: a second
  title, or a wall that repeats the bullets.
- `slot-h2-1`, `slot-h2-2` — ≤34 chars. Theme names, noun phrases, not sentences.
- `slot-b1-1..4`, `slot-b2-1..4` — ≤110 chars / 2 lines each. One dash bullet = one commitment with a
  date, an amount, or a measure where one exists; `em` renders the honest caveat. Bad: adjectives
  ("excellent", "world-class") where a number belongs.
- `slot-cap-1..5` — ≤34 chars. Programme name. If a caption needs 3 lines the rail is too crowded —
  drop to four discs.
- `slot-sub-1..5` — ≤46 chars. Optional one-line gloss. If all five glosses are the same shape, delete
  them; they add nothing.
- `slot-rail-label` — ≤60 chars. Optional; delete if the title already names the set.
- `source` / `pagestamp` — required.

FILL:
1. Text nodes: title, kicker, lead, two `h2`s, eight bullets, five captions + five sub-lines. Delete a
   bullet block wholesale if the theme has nothing to say — three bullets is fine, four filler is not.
2. Medallion count: `.rail` is `display:flex` with `.item{flex:1 1 0}`, so deleting an `<div class="item">`
   auto-rebalances the remaining cells to full width. Three to five discs is the tested range; six
   pushes a caption under 150px.
3. Glyph swap: inside each `<svg>`, the `<g class="glyph" transform="translate(28,26)">` group is
   drawn in a 40×40 field. Replace only `d`/`cx`/`cy`; white is applied by `.glyph`
   (`stroke:#FFFFFF`, width 1.9) so any new path inherits it. Do not scale the group — 96px disc /
   40px glyph is the proven ratio.
4. Recolour: the discs read `--accent` (mid blue) to `--accent-d` (deep blue) across the gradient
   stops `#4A86F5 → #0049C0`. For a different brand hue rewrite all five `<linearGradient>` stop pairs
   in one pass and keep the deepest stop as the `--accent-d` value used for caption text. The magenta
   appears in exactly three places — the title rule, one phrase in the rail label, and the emphasis
   caption — replace all three or none.
5. Emphasis: the last `.item` carries `class="item emph"`, which turns its caption magenta. Move that
   class to whichever programme is the page's point; never to more than one.

CHART RECIPE (the rail is a categorical, not quantitative, figure):
- Encoding is identity, not magnitude: five equal cells, equal discs, so nothing claims a ranking the
  data does not support. A bigger fifth disc would be a lie — the only permitted size signal is the
  `emph` caption colour.
- Ramp rule: tints are one lightness family of the accent (25% / 45% / 70% / 100%), no second hue, so
  the rail reads as one system with the brand blue.
- Label placement: caption centred under the disc, max-width 186px so a long programme name wraps in
  its own cell rather than crossing the neighbour. Never put captions inside the disc.
- White glyph on the mid-to-deep blue stop clears 4.5:1; the palest stop (`#8FB6FA` on `g4`'s light
  edge) is used because a 1.9px white stroke on that disc reads as texture, not text. If you lighten a
  gradient, thicken the stroke, do not darken the glyph.

VERIFY:
- [ ] Title ≤15 words / ≤2 lines at 28px within 1120px.
- [ ] One hue family (blue) + magenta in at most three places; no cyan/red data colours ported in from other KPMG pages.
- [ ] Every white glyph on a disc — check by zooming to 100%: a glyph that disappears is a stop that went too light.
- [ ] Dash bullets: 4+4 max, each with a number, date or a stated dependency.
- [ ] Source line with superscripts bottom-left, page number bottom-right, magenta rule under the title.
- [ ] Contrast: caption text `#0049C0` on white ≈ 8:1, body `#333B44` ≈ 11:1, lead same.

DON'T:
- Ten discs, or a disc per bullet — the rail is the set, not a bullet-point ornament.
- Gradient text or gradient-filled titles. The gradient lives on the discs only.
- Topic titles ("Our commitments", "Programmes") — that is the kicker's job; the title is the claim.
- Data-colour contamination: the review lists cyan `#25C8E8` and red `#E4262C` for chart series on other
  pages of this deck. On a text page they belong to nobody.
- Putting the whole argument in the kicker: kicker walls are the corpus failure mode this schema names.

SOURCE: kpmg__kpmg_kpmg_our_impact_plan_2022_update_2022, deck "KPMG Our Impact Plan — 2022 update" —
p37 ("Our commitments", `sw_sheets/kpmg__kpmg_kpmg_our_impact_plan_2022_update_2022_s03.jpg` row 2
frame 2), with the recurring disc device from p38–p39 (same sheet, row 2 frames 3–4). Palette hexes and
title/rule habit from `reviews/kpmg__kpmg_kpmg_our_impact_plan_2022_update_2022.md` §Color system
(#1565F0 / #0049C0 / #E6007E / #DCE6F5 / #333B44) and the "dash bullet" + "oversized stat numeral"
devices noted in that review's recurring-devices list.
