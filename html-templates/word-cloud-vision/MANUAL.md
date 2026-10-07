# word-cloud-vision — Full-Bleed Vision-Statement Word Cloud

WHEN:
Presenting a survey/analysis of statements (vision statements, manifesto pages, ESG claims) as raw vocabulary: every subject word sized by frequency, the claim title floating in a cleared pocket, cloud bleeding to all stage edges. Derived from `Forvis Mazars "Strategic Planning"` corpus slide S0016 (`corpus/sheets/sheet_002.jpg` frame 6, row 2 col 1; corpus tag 4890). Catalog note: "dense multicolored words, full-bleed word cloud."

ANATOMY (1280×720 stage, cloud under everything, text on top):
1. cloud   SVG layer `inset:0 viewBox 0 0 1280 720`, three <g> tiers:
   `g#tier-anchor` (8 horizontal words 82–130px + 1 rotated edge word
   `class="aV"`), `g#tier-core` (18 words 36–40px), `g#tier-filler`
   (~55 words 17–19px). Only two banned bands: title block (x 48..650 AND
   y<150) and footer strip (y>668). x 70..1210 otherwise; words may touch
   stage edges — that bleed is the device.
2. kicker  `left:48 top:34`  — 12px uppercase .14em gray-1
3. title   `left:48 top:58 w:600` — 32px/1.15 bold claim (usually a question)
4. footnote `left:64 top:672` — 10.5px: states what word size encodes
5. footer  rule `top:690`; source `left:64 bottom:10`; `17 | VISION` `right:64 bottom:10`

SLOTS:
- `kicker` — "Higher ed · Vision statements". One line.
- `title` — the claim the cloud proves. Gate ≤15 words / 2 lines at 32px/1.15. A question is legitimate here ("Do vision statements actually inspire strategy?") because the cloud is the evidence, not the subject. Topic titles still banned.
- `anchor.N` (8–10) — the most frequent real words. One may be rotated 90° on the right edge (`class="aV"`) to echo the source's vertical word; that's ONE per page max.
- `core.N` (18) — second-frequency tier, two families: `c` soft-accent bold, `c2` gray-1.
- `filler.N` (~55) — the haze. 17px `f` gray-1 / 19px `f2` gray-2 (19px floor: gray-2 is 3.1:1).
- `footnote` — required, because size=frequency is a methodology claim; it states whether overlap is measured co-occurrence or illustrative.

FILL:
1. Text slots (kicker/title/footnote/source/runhead): replace in place. Title may be 2 lines — the pocket is 650px wide, words must stay clear of it.
2. REMOVE a word: delete its `<text>` line. Holes are invisible by design; full-bleed means gaps read as breathing space.
3. ADD a word by weight:
   - most frequent → copy a `.a*` line in `g#tier-anchor`. Size ladder 130/114/100/88 is relative-frequency, not type: if you add a 9th/10th anchor, give it 88px and push, don't re-scale the others. Pair words (the source's "become graduates" as two same-tier adjacent texts, ~30px gap) count as ONE concept — keep the pair on one baseline band.
   - second rank → copy a `.c`/`.c2` line onto any core baseline; width rule ≈ 0.5 × font-size × chars (38px → ~19px/char), check neighbours' half-widths on that row.
   - haze → copy a `.f`/`.f2` line; fillers tolerate overlap with everything behind anchors and are cheap; row pitch ≥ 38px so haze stays separable.
   - rotated word: copy the `aV` line and change its rotate center `rotate(-90 1250 470)`: x stays ~1250, y moves it up/down the edge. Max one.
   Hard bounds: no word enters (x<650 AND y<150); nothing below y>668; right edge ≤ ~1210 except the rotated word.
4. RE-THEME: `--accent` teal drives anchors; `--accent-soft` drives `c` words — move as a pair, soft must stay ≥3:1 (its words are 36px+). Grays stay; source's green/teal 2-hue is deliberately collapsed per kit rule.
5. DENSITY: this template tolerates ~80 words. Under ~50 it looks like a poster, over ~100 the haze stops reading as haze and becomes mud — drop fillers first, never core.

CHART RECIPE (the cloud IS the figure):
- Size ∝ frequency: anchors ×2 core × core 114/100/88, core 36–40, filler 17–19. One step down = a real drop in frequency, don't resize to fill space.
- Colour encodes tier: teal anchors, soft-accent/gray core, gray haze. Exactly one hue + ramp.
- text-anchor:middle; overlap = layering; anchors at .92 opacity keep their edges readable over anything behind.
- No axis, no legend — the footnote carries the encoding. Squint test: if you can't name the 5 biggest words first, the frequency ranks are wrong.

VERIFY:
- [ ] title ≤ 15 words / 2 lines, clear of all cloud words (as shipped: 8 words, 2 lines)
- [ ] source bottom-left, `17 | VISION` bottom-right, ¹ footnote present (size=frequency claim)
- [ ] one emphasis hue (teal) + gray ramp; ≤ 3 hues total
- [ ] all text ≥ 3:1 on white (gray-2 filler used at 19px+ only)
- [ ] title pocket and footer strip word-free; nothing clipped off-stage (rotated word is the only edge-touch)
- [ ] pair words (e.g. become graduates) read as TWO words, not one mash

DON'T:
- 2-hue (green+teal) or 3-hue source clouds — kit rule is one accent + grays.
- Box the cloud, frame it, or put it "in an exhibit" — the bleed is the point; a boxed cloud is the `content-action-title` page with a wasted frame.
- Centering the cloud with a hole around it: off-centre anchors (education low-left-heavy here) carry the tension; centred = corporate screensaver.
- Two rotated words, or a rotated filler (only ≥36px edge words read).
- Letting "an inspiring" / "transformative"-style adjectives take anchor size unless frequency says so — nouns first.
- Lorem — every word must be real statement vocabulary or the frequency argument is fake.

SOURCE:
Forvis Mazars, "Strategic Planning" deck, corpus slide S0016 — read on `corpus/sheets/sheet_002.jpg` frame 6 (S0011-S0020 row-major 5col×2row) and `corpus/pdfpages/4890_49c9_a1ee_77b0f75a86c7_St_-17.png` (tag 4890; [pdfpage 4890]). Catalog `catalog_1-20.csv` row S0016 ("dense multicolored words, green/teal cloud, full-bleed word cloud, word-cloud typography device"). No reviews/*.md exists for this deck; palette hexes are eyeball-sampled from the contact sheet (stated in index.html header). Sibling template: word-cloud-definition (bounded-cloud variant, S0007). Screenshot QA: `qa/word-cloud/word-cloud-vision.png`.
