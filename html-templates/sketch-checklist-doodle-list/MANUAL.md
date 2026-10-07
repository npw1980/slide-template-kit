# sketch-checklist-doodle-list — MANUAL

Hand-drawn stick figure (left) beside a blue-check habit list (right). One page, one message:
process guidance delivered with a candid, human voice. The figure is decoration with a job — keep the
checklist scannable.

## WHEN
- Process/habit pages, closing pages, and "how we work" asides where an earnest, human-sketch register
  beats a polished SmartArt diagram. Works as a two-column figure-plus-list content page.
- Evidence: corpus S0042 (2017 Gartner conference material, catalog_1-20.csv; rendered from
  corpus/sheets/sheet_005.jpg) — stick-figure doodle left, four+checkmarks right, "black ink plus
  blue checks", "checkmarks right; doodle left". That slide's own register is deliberately rough;
  this template keeps the roughness but imposes firm-grade text discipline.

## ANATOMY (all coords px on the 1280×720 stage)
1. **Kicker** — (64, 64), 11.5px bold, 1.8px tracking, gray-2.
2. **Claim title** — (64, 106) + (64, 146), 30px bold display, navy `--ink`; one word may carry
   `class="em"` (teal-deep) for emphasis.
3. **Figure column** — x 80–255, y 160–445. One group `g#figure`; the stick figure is a head (two
   overlapping rough ellipses at ~168,196), a lopsided smile, torso, two raised arms ending in
   mitten loops, two splayed legs ending in shoe ellipses. Caption `figure-label` at (170, 440).
4. **Checklist rows** — each row is `g.row` translated to **(360, 222 + k·82)**, k = 0..4. Inside a
   row: check glyph at local (0,8)–(25,17), text at local x=32, two lines at y=17 and y=43
   (so text starts at stage x=392). Last row may use the **open** state: hollow circle instead of
   check, `class="item dim"` text.
5. **Footer** — source line (64, 700), page number (1216, 700) right-anchored "N | SECTION".

## SLOTS
- **kicker** — ≤55 chars, ALL CAPS. Good: "THE FINAL STEP — DRAW IT, DON'T POLISH IT". Bad: any
  longer phrase (wraps) or sentence case.
- **title** — max 15 words across exactly 2 lines, ≤44 chars per line. Good: "Imperfection is the
  feature: five habits / that make rough strategy sketches land". Bad: 3 lines (shrinking the font
  below 30px breaks the display scale; instead cut words).
- **figure** — one doodle, no max length; keep strokes ≥3px so the wobble filter doesn't erode them.
  Optional caption ≤30 chars.
- **item.lead** (bold opener) — ≤30 chars. Good: "Iterate first, polish last."
- **item lines** — 1–2 lines ≤68 chars each (text area is 784px: x 392→1176). Good: plain sentences.
  Bad: three+ lines in one row — that's a different page.
- **row count** — 5 rows fit at step 82 (last row baseline block ends ≈593, footer at 700). For 6
  rows use step 76; for 7, step 70; ≥8 do not fit — split the page.
- **open row** — exactly one, last. Marks "not started"; the check color is reserved for done.

## FILL (step-by-step)
1. Replace kicker text (`text.kicker`), title (`text.title` ×2, keep the `tspan class="em"` on the
   emphasized word), footer source line and page number.
2. Per row: keep `<path class="check" .../>`; replace the `<tspan class="lead">…</tspan>` opener
   and both following `text.item` lines. If a row is one line, delete the y=43 text node and leave
   y=17 where it is (do not re-center).
3. **Remove a row:** delete its whole `<g class="row">…</g>`, then change each following row's
   `transform="translate(360, Y)"` to Y−82 (the block re-flows upward by hand; nothing auto-reflows).
4. **Add a row:** copy the last `g.row`, change its translate y to last+82, paste. For the new open
   state, replace the `<path class="check" ...>` with
   `<circle class="open" cx="12" cy="12" r="10"/>` and give the text `class="item dim"`.
   If that pushes past row 5, re-step ALL rows: translate y = 222 + k·76 (6 rows) or ·70 (7 rows).
5. **Move/resize the figure:** everything is inside `g#figure` — change its `translate` (e.g.
   `translate(40,-10)`) or add `scale(0.9)`; do not edit individual coordinates. If the figure gets
   too small (<0.8×) drop the two `thin` face strokes so the face doesn't clot.
6. **Recolor:** checks take `--accent-deep`; change it once in `:root` to recolor every check.
   Figure ink follows `--ink`. The faint face dots use `fill:var(--ink)`.
7. **The wobble:** `filter="url(#sk)"` is on stroke paths only (doodle, checks) and NEVER on text —
   text inherits strokes from class groups unless `.annot/.item` sets `stroke:none`; if you add
   paths inside a class with a stroke, set `stroke:none` on any text you nest.

## VERIFY
Title ≤15 words ≤2 lines · source line present · one emphasis color (teal-deep for checks/em word)
· ≤3 hues total (navy, teal family, gray) · check strokes 4.5:1-ish on white · page number set.

## DON'T
- Do not apply the wobble filter to text (displacement eats small glyphs) or stack one text node on
  another — S0042's legibility comes from generous line spacing.
- Do not add a second doodle, arrows from the figure, or shadow/rainbow fills — SmartArt energy in
  sketch clothing.
- Do not check the "open" row with a ✓ (the open state IS the message); do not let two rows run to
  3 lines.

## SOURCE
- Firm/corpus: Gartner conference material style, slide S0042, catalog_1-20.csv
  ("sketch plus checklist"; "check bullets; stick figure"; "black ink plus blue checks").
  Sheet: /home/nathan-white/new projects/deck-research/corpus/sheets/sheet_005.jpg (S0042).
- Font note: deck corpus uses Garamond/Calibri-family office fonts; the Helvetica Neue/Arial stack
  stands in for firm display type. Sketch strokes are drawn, not a font.
