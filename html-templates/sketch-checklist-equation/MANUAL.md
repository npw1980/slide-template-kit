# sketch-checklist-equation — MANUAL

Hand-sketched "A + B = C" ring diagram: three rough double-stroke circles in a row with a plus and
an equals sign, each ring carrying one concept, the result ring in the accent color. This is the
anti-SmartArt page: it argues a composition in one line across the middle of the stage.

## WHEN
- Explaining how two or three things combine into a new thing: deal structures, joint ventures,
  "our capability + their asset = the offer", organic + inorganic = the plan. Use when the equation
  IS the story; use the framework pages when the parts have more structure than that.
- Evidence: PwC / Mayer Brown "Merging with a SPAC: preparing for life as a public company",
  the bespoke ring diagram (review file says "three-circle row across page centre, caption under
  each circle", rings "blue / green / red" as a hand-sketch device).

## ANATOMY (all coords px on the 1280×720 stage)
1. **Kicker** — (64, 64), 11.5px, tracking 1.8px, gray-2.
2. **Claim title** — (64, 106) + (64, 146), 30px bold, navy.
3. **Ring row** — three `g.ringnode` groups centered at **(240, 330), (640, 330), (1040, 330)**,
   radius ≈120. Each ring = two overlapping rough ellipses (double-stroke sketch). Inside each node
   group, local coords: ring label y=−176 (all caps above the ring), two emphasis words y=−2 and 22
   (centered inside), caption two lines y=160 and 177 (below).
4. **Operators** — `g.op` at **(440, 330)** (plus, with two annotation lines at local y=52, 66) and
   **(840, 330)** (equals). Operator strokes carry the wobble filter; their annotation text must
   have `stroke:none` (see FILL step 5).
5. **Footer** — source (64, 700); page "16 | DEAL STRUCTURE" right-anchored at (1216, 700).
   The result ring alone uses the accent (`ring result`, teal-deep #006F68); input rings are gray-2.

## SLOTS
- **kicker** — ≤55 chars caps. Good: "STRUCTURE OF THE DEAL". Bad: two clauses.
- **claim title** — ≤15 words, ≤44 chars/line, exactly 2 lines. Good: "A trust pool plus an operating
  company / equals one listed successor". Bad: question form — the title states the equation.
- **ring label** (above ring) — ≤34 chars caps ("LISTED SPAC", "TARGET COMPANY"). Good: one noun
  pair. Bad: sentences — captions below already carry the sentence.
- **ring word** (inside) — 2 lines ≤22 chars, bold; result ring only gets `.result` classes.
- **caption lines** — 2 lines ≤42 chars each. Good: plain description. Bad: 3+ lines (next ring
  overlaps: ring spacing is 400px, ring diameter ~240px, so side-by-side captions collide).
- **operator annotation** — 2 lines ≤24 chars (y 52 and 66), gray-3, under the plus sign.
- **page number** — "N | DEAL STRUCTURE".

## FILL (step-by-step)
1. Replace kicker, both title lines, all ring labels/words/captions, operator annotation, source
   line, page number. Keep every `text-anchor="middle"` — centering is what keeps the sketch honest.
2. **Remove a node (3 → 2 rings):** delete the middle `g.ringnode`, change the remaining two
   translates to (440, 330) and (840, 330), move the `g.op` equals group to (640, 330) and delete
   the plus group. Reflow: ring centers must stay ≥380px apart or the two-stroke rings touch.
3. **Add a node (3 → 4 rings):** copy one full `g.ringnode` block and set the four ring centers to
   **(190, 330), (490, 330), (790, 330), (1090, 330)** — symmetric about 640 with 300px gaps.
   Put one plus `g.op` at **x=340**, one at **x=640**, and the equals `g.op` at **x=940** (each is
   the midpoint of adjacent ring centers; copy the plus markup and swap its two lines for the
   equals pair). Reflow side effects at 4 rings: shrink every ring ellipse to **rx="101" ry="97"**
   (both strokes, keeps a 98px gutter so operators don't touch ring edges), move ring labels to
   y=−150, and drop captions to 11px / ≤34 chars. Above 4 rings the equation stops reading — stop.
4. **Recolor the result:** the accent is only on `ring result` / `ringlabel result` / `ringword
   result`. Change `--accent-deep` in `:root` once — every result element follows. Keep inputs
   gray-2; do not give inputs their own hues (the corpus deck did — the review flagged that as
   decorative color; one accent is the house rule).
5. **Text safety (learned the hard way):** text inside a `g` whose class sets a stroke (`.op` is
   `fill:none; stroke:…`) inherits the stroke and small text smears into blobs. Either give it
   `stroke:none` (done for `.annot`) or place text outside the stroked group. Never apply
   `filter="url(#sk)"` to a group containing text — displacement distorts glyphs.
6. **Wobble dials:** `#sk` is feTurbulence baseFrequency 0.014 + displacement scale 5. Raise scale
   to 8 for more hand-drawn; drop to 2 for near-clean. The ring wobble also comes from the second
   offset ellipse — that pair is the sketch device; keep both strokes.

## VERIFY
Title is a claim not a question · ≤15 words ≤2 lines · source line bottom-left · page number bottom-
right · one emphasis hue (accent-deep teal) + grays only · ≥4.5:1 text contrast · the equation reads
left-to-right at a glance — squint test: you should be able to mouth "+…=" without reading.

## DON'T
- Do not add shadows, gradients, or 3D fills — the rings' roughness is the entire look; anything
  "glossy" reads SmartArt instantly.
- Do not color each ring differently "to match the reference" (the PwC rings were blue/green/red,
  decorative, and the review called that out).
- Do not stretch the equation to 5+ terms — it stops being an equation and becomes a process map
  (that's a different template).

## SOURCE
- Firm: PwC Strategy / Mayer Brown — "PwC: Merging with a SPAC, preparing for life as a public
  company", deck p15 (custom ring diagram; continuation pages p16+).
- Review: reviews/pwc_strategy__pwc_merging_with_a_spac_preparing_for_life_as_a_public_compa.md and
  the companion slides CSV (p15: arch diagram, "A + B = C figure", "bespoke hand-sketch ring
  diagram: cash trust + operating company = successor company").
- Font note: firm deck uses a light humanist sans for display; the Helvetica Neue/Arial stack here
  stands in for it; body is the standard Arial/Calibri office stack.
