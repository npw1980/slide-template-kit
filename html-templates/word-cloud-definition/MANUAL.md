# word-cloud-definition — Concept-Definition Word Cloud

WHEN:
Defining a fuzzy concept (strategy, resilience, partnership) by surrounding the 4–5 words that actually constitute it with dozens of casually-misused buzzwords — size IS the argument. Derived from `Forvis Mazars "Strategic Planning"` corpus slide S0007 (`corpus/sheets/sheet_001.jpg` frame 7, row 2 col 2; corpus tag 4890). Catalog note: "giant overlapping words; full-width word cloud, word-cloud typography device."

ANATOMY (1280×720 stage):
1. kicker  `left:64 top:48`     — 12px uppercase, .14em tracking, gray-1
2. title   `left:64 top:74 w:640` — 30px/1.15 bold, claim title
3. cloud   `SVG layer, stage-wide viewBox 0 0 1280 720` — three <g> tiers:
   `g#tier-anchor` (5 words, 76–96px, teal), `g#tier-core` (18 words, 36–42px,
   soft accent + gray-1), `g#tier-filler` (46 words, 17–19px, gray ramp).
   Usable cloud rect: x 64..1216, y 170..668, EXCLUDING the title pocket
   (x<560 AND y<170) and footer strip (y>668).
4. footnote `left:64 top:656`  — 10.5px gray-1, carries the ¹ definition
5. footer  rule `top:678`; source `left:64 bottom:18`; `4 | DEFINITIONS` `right:64 bottom:18`

SLOTS:
- `kicker` — one line. "Strategy, defined" / "Terms of reference". No wall of text.
- `title` — the claim the cloud illustrates, not a topic. Gate ≤15 words / 2 lines at 30px/1.15. Good: "Strategy is a set of choices about what not to do — not a wish list". Bad: "What is strategy?".
- `anchor.N` (5) — the actual definition words: each must be one word the claim could stand on alone. If a candidate is two words, it isn't an anchor; demote it to core.
- `core.N` (18) — supporting attributes (adjectives of discipline: deliberate, coherent, boundaries…). On rows 215/250/605, ~150px apart.
- `filler.N` (46) — the buzzword haze (aspiration, OKR, north star, pivot…). 17px `f` = gray-1, 19px `f2` = gray-2 (gray-2 only ≥18px — 3.1:1 floor).
- `footnote` / `source` / `pageno` — required; ¹ marks the definition claim.

FILL:
1. Title/kicker/footnote/source/runhead: plain text nodes. Replace in place.
2. SWAP A WORD: edit the inner text of one `<text>` line. Nothing reflows — this is the whole point of the three-group design; words are absolutely painted, overlap is legitimate layering, not collision.
3. REMOVE a word: delete its `<text>` line (1 line = 1 word). A hole in a tier row is invisible — fillers/core leave gaps by construction.
4. ADD a word — pick its weight first:
   - is it part of the definition? → copy an `<text class="a|a2|a3">` line in `g#tier-anchor`, set x = neighbour x ± (half your width + half theirs); keep ≤ 6 anchors (the 96px ladder gets crowded past 6).
   - is it an attribute? → copy a `.c`/`.c2` line in `g#tier-core` onto the row (y = 215 / 250 / 605) whose gap fits: word width ≈ 0.55 × font-size × chars (40px font → ~22px/char). If no row has room, drop it to filler.
   - is it just vocabulary? → copy a `.f`/`.f2` line in `g#tier-filler` onto any filler row y (195,234,275,315,355,415,455,500,540,580,645); same width rule (17px → ~9.4px/char).
   Hard bounds: no word's painted box may enter x<560 & y<170 (title pocket) or y>668 (footer strip); keep right edge ≤ 1216.
5. RE-THEME ACCENT: `--accent` (teal `#0E6B70`) drives anchors + `--accent-soft` drives core — change together (soft must stay ≥3:1 for its 38–42px bold words). Keep the grays; the source's green/purple 3-hue cloud is deliberately NOT reproduced (DON'T list).
6. TITLING VARIANT: this page has no kicker box or exhibit frame — the cloud sits directly under the title band. If the concept deserves a legend (anchors = definition, grey = buzzwords), add one 12px key line right-aligned under the title; never box the cloud.

CHART RECIPE (the cloud IS the figure):
- Encoding = word size ∝ definitional weight: 5 tiers of relative size, not pixels: anchor ≈ 96/88/80px, core 36–42px, filler 17–19px. Never let two filler words sit bigger than a core word — the size ladder carries the argument.
- Colour encodes tier, not data: anchors teal, core soft-accent/gray-1, filler grays. One hue.
- text-anchor:middle everywhere; x is the center, y the baseline.
- Overlap rule: anchors at fill-opacity .92 layer like the source; do not "fix" overlaps — a word cloud with no overlap is a bullet list.

VERIFY:
- [ ] title ≤ 15 words, ≤ 2 lines at 30px/1.15 (as shipped: 12 words, 2 lines)
- [ ] source line bottom-left with ¹; `4 | DEFINITIONS` bottom-right; footnote present
- [ ] one emphasis hue only (teal) + gray ramp; ≤ 3 hues including ink
- [ ] every text ≥17px clears 3:1 on white (gray-2 #899296 = 3.1:1 — 19px+ only)
- [ ] no word in the title pocket or footer strip; nothing clipped at stage edge
- [ ] page still reads if you squint: 5 anchor words legible first

DON'T:
- 3-hue clouds (green/teal/purple, the source habit) — size + one hue + grays is the kit rule.
- Anchors that are marketing nouns ("synergy") — anchors must be the claim's load-bearing words or the page argues nothing.
- Kicker walls of text, topic titles ("Strategy" / "What's a Strategy?" — the source's own titles are topic-style; the kit demands a claim).
- Centered everything / radial spiral layout: keeps re-adding words a nightmare. Row + baseline = reflow-free editing.
- Retaining lorem: the corpus page's filler words are real vocabulary or the size satire falls flat.

SOURCE:
Forvis Mazars, "Strategic Planning" deck, corpus slide S0007 — read on `corpus/sheets/sheet_001.jpg` frame 7 (5col×2row row-major) and `corpus/pdfpages/4890_49c9_a1ee_77b0f75a86c7_St_-07.png` (tag 4890; [pdfpage 4890]). Catalog `catalog_1-20.csv` row S0007 ("giant overlapping words; full-width word cloud"). No reviews/*.md file exists for this deck, so palette hexes are eyeball-sampled from the sheet — stated in the index.html header. Screenshot QA: `qa/word-cloud/word-cloud-definition.png`.
