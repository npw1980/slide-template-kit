# process-flow-stage-matrix — Operating-Model Flow Matrix (stage chevrons × model rows, 1280×720)

WHEN: "The same work, three different ways" — compares two or three alternative operating models (or two routes / two target-states) across a fixed set of stages, showing which steps each model drops, owns, or outsources. This is the consulting answer to SmartArt: a stage-column matrix with icon swim-rows and long skip-arrows that carry the argument. From Accenture's post-parcel trends deck p17 ("chevron journey band over icon swimrows" — `reviews/accenture__accenture_2023_post_parcel_industry_trends_2023.md`, COPY list). Use `process-flow-pathway` instead when there is ONE route to show.

## ANATOMY (slot map, stage px)
1. `kicker` — x64 y36, 12/1 bold uppercase, `04 | …` (numeral accent).
2. `title` — x64 y56, 27/35 bold ink, ≤2 lines.
3. `subclaim` — x64 y114, 13/18 **accent**, 1–2 lines. This is the deck's signature: the so-what line, in the hue, not in black.
4. `corner` — 132×38 cell at (64,150), grey-5 wash, "Operating model" header.
5. `stages` — chevron columns x210→x1170 (960 wide), h38 at y150. Tip t=12; `W = (960 + 24·(N−1))/N`; stage i `translate(210 + i·(W−24), 150)`. N=4 → W=258, x = 210/444/678/912. Fills: dark grey → grey-3 → grey-4 → LAST = accent (the stage where the models all converge, or where the insight bites).
6. `guides` — dashed vertical column guides at stage left-edges −12 (432/666/900/1134) from y192→y590; matrix floors = hsep lines y192/326/458/590.
7. `rows` — three blocks, block height 132 (y192/324/456): `rowlab` block x64 w132 (grey-1 / accent / tint — the model identities, one hue three lightnesses) + `r-chain` (icon nodes, axis y = blockY+146 abs) + `r-hops` (one path per hop) + `r-end` rail.
8. `chain` — node pitch 112 from x254, cap 7 nodes (254+112·6=926, last caption lands inside the stage band); node = `<g class="cnode" translate(cx,146+blockY?) — inside a row group use translate(cx,138)>`; icon centred at (0,0) ≈ 22×22, caption 10px bold below (y+26), sub-caption 8.5 grey (y+36).
9. `hops` — horizontal `M{cx+17} {cy} H{nextcx−17}` + `marker-end="url(#ar)"`; a COLLAPSED pair of stages is one `long` hop (254→685 style: x1=383, x2=685) — that arrow IS the finding "no own sort". Emphasis: model-under-test hops use class `a2` + `arA`.
10. `end rail` — per row: B2C house glyph x1158 + B2B tower x1196 (x1148…1216 strip); 8.5 bold labels below.
11. `legend` — y630: two sample arrows (own op / under test). Only if collapsed arrows exist.
12. `insight` — bottom-right above footer, x1216 anchor, 11.5 bold ink, 2 lines, sup marker — the page's money sentence.
13. `source` x64 bottom14; `pageno` right64 bottom14.

## SLOTS (name — limit — good/bad)
- `title` — **≤15 words / 2 lines** — a claim naming the variable that differs ("network depth, not fleet size"); the matrix proves it.
- `subclaim` — ≤180 chars — the mechanism in one sentence, accent colour. Bad: a topic gloss ("Overview of models").
- `stages` — 3–6 names, ≤11 chars each — stage vocabulary shared by ALL rows (the invariant); if a model renames a stage, the comparison is broken.
- `rowlab` — ≤2 lines ×14 chars — model archetype name; `rowsub` — 4–18 chars, the model's defining trade ("owns every step" / "no own sortation") — it must name the step the arrows actually skip.
- `cnn` (node caption) — ≤19 chars, one noun — the OPERATION ("Origin sort", "Linehaul partner"), not company names.
- `cns` (sub-caption) — optional one word ("in-city") — only where the node deviates from the row above.
- `endlab` — "B2C"/"B2B" only; if an end state changes, the strip re-draws (see FILL 4).
- `insight` — ≤90 chars — quantitative, with sup; it may repeat what the arrows show, it must not introduce a fifth fact.
- `source` / `pageno` — always.

## FILL (build order + resizing)
1. Write stages first (they define columns), then model rows top-down with the INCUMBENT first and the model-under-test in row 2 (the emphasis position, next to accent block + accent hops). Insight line last.
2. **Add a stage column.** N→N+1: recompute `W=(960+24(N))/  (N+1)`; for N=5: W=211.2 → chevron x = 210 / 397.2 / 584.4 / 771.6 / 958.8 (copy `<g class="chev">` ×1, edit translate + polygon `0,0 {W−12},0 {W},19 {W−12},38 0,38 12,19`). Move every vsep to the new stage edges (x_edge−12). Then add a node to each row where the stage exists: copy a `<g class="cnode">`, `translate(254+112·k,138)`, split the spanning hop into two. **Cap check:** a row's chain must stay inside x1041 (=1134−12−81): ≤8 nodes at pitch 112, and if stages are >5, reduce pitch to 104 (254+104·k). If the new stage means every row gets a new node, the page is a 5-column matrix — captions get 2-line width (112→96), still one page.
3. **Add a model row.** Block pitch = 458−192−(N_rows−1)·12… for 4 rows: blockH=(398−3·12)/4=90.5 → translate(0,192+102.5i). Copy a whole `<g class="row">`, change its translate, re-write labels + chain; the chain axis stays blockH/2 relative (tight rows: 90/2=45…) in practice keep blockH ≥96, meaning max 4 rows; a 5th model wants its own page or a second matrix — the corpus pattern is ≤3 rows precisely because the chains need reading room). Re-place the hsep floor lines. End rail + hop y values shift with the row: they're inside the row group, so they move automatically — but check the vsep/guide bottom y590 stays the frame.
4. **Add / remove a node inside a row.** Copy one `<g class="cnode" translate(x,138)>` from the same row; shift ALL later nodes in THAT row by the freed pitch (112·slot gap) and re-time that row's hops: each hop is one path, x1 = prev node cx+17, x2 = next cx−17 — after a shift every downstream x1/x2 changes; the row group's translate stays put (rows don't reflow each other). Remove = delete node + bridge its two hops with one path (this is what "skip a stage" looks like — draw it long, don't leave a gap and hope).
5. **Re-emphasis.** Exactly ONE row carries `a2`/`arA` hops + an accent label block (the one under test). Moving it = swap rect fill + hop classes. Grey-1 block = incumbent, tint = asset-light — don't invent new hues.
6. **Recolour house:** swap `--accent` + `--tint` (one lightness of it). White label text on light accents fails 4.5:1 — flip `.rowlab`/`.cvt` (stage 4) fill to `var(--ink)`. The deck's real faces are Calibri-family; stacks here stand in (see SOURCE).

## DIAGRAM RECIPE (how the figure encodes)
- Encoding = a matrix: columns are the invariant process (chevrons), rows are alternative structures (blocks + icon chains). Position within a column = which actor performs the step; HORIZONTAL GAP = a step the model does not own — that's the whole game, skip-arrows read as "outsourced / absent".
- One hue (purple) + grey: stage band is grey ramp ending accent on the convergence stage; model blocks are three lightnesses of the SAME hue/grey; hops default grey, under-test row accent. No green/red traffic lights (that's a different Accenture pattern, p10 heat matrix — keep this page's encoding pure).
- Icons are generic line glyphs (24px grid, stroke grey-2) — they must read at 60% zoom; no photos.
- Every row ends on the same right rail: B2C/B2B — the models converge; if they don't, say so with a "—" or different glyphs and put THAT in the insight line.
- Value labels live in the INSIGHT line, not on arrows; arrows carry structure only.

## VERIFY (against the render)
- [ ] Title ≤15w/2 lines; subclaim is 1–2 lines, accent, NOT black.
- [ ] One hue family: stage ramp + block lightnesses + tint all from purple/grey; ≤1 extra hue; no accent on >1 row's arrows.
- [ ] White text only on dark fills (accent block, dark stage 1/2); ink on grey-4/tint stages. Check the swapped-accent build (FILL 6).
- [ ] Long hops pass UNDER node captions, never through them; skip-arrows land on the next real node.
- [ ] Chains align to columns: each node caption sits under its stage band (±30px).
- [ ] End rail identical across rows (unless the insight claims divergence).
- [ ] Legend present if collapsed arrows exist; insight + source + pageno present.
- [ ] Resize proof: added one node per FILL 4 inside one row without touching other rows.

## DON'T (corpus failure modes)
- 10-hue stage band or "every row its own colour" (the review's praise — semantic colouring — only survives with a legend; the kit page uses one hue + grey).
- SmartArt chevrons with filler text inside cells ("lorem in 5 boxes"): stages stay thin (38px) and captions carry the meaning.
- All-own-op arrows in every row (then the matrix says nothing — a comparison row must SKIP something, or the page collapses into a feature table).
- Company names as nodes ("Amazon sortation") — operations, then name them in notes.
- A fifth row squeezed to 80px: captions stop being legible; split pages.
- Insight line with no number — the deck convention is "~55%, 80% of which is labour", not "last mile is expensive".

## SOURCE
Accenture — *Post-parcel industry trends 2023*, p17 "Changes in ecommerce supply chains: a different network" (stage-chevron header "Collection › Sortation › Transportation › Delivery" over three purple-sidebar icon swim-rows with B2C/B2B rail and bottom-right bold insight), read in `sw_sheets/accenture__accenture_2023_post_parcel_industry_trends_2023_s01.jpg` bottom-row cell (p17). Analysis: `reviews/accenture__accenture_2023_post_parcel_industry_trends_2023.md` — COPY list names "chevron journey band over icon swimrows"; header pattern "claim title + magenta 1-line sub-claim" (subclaim slot here is that pattern); colour section "1 hue family + semantic accents", purple-dominant. Real deck faces: Calibri/Arial family; the Helvetica/Arial stacks here stand in. Palette note: the source's live violet is not hex-cited in the review, so `--accent` is the same purple family anchored at #5B1B8A (darkened from the kit's #7B1FF0 cover accent for text contrast) — recolour per FILL 6 rather than assuming the brand hex is exact.
