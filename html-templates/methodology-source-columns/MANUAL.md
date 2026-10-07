# methodology-source-columns — "Methodology:" band + icon-circle source columns

WHEN: The methodology/closing page of a research deck that used several distinct evidence
streams (surveys, client data, secondary sources). Extracted from Accenture's "The nbn Effect"
(2021), methodology pages p30–p31 — one column per data source under a single full-bleed purple
claim band. Use when the reader must see *where every number came from*, one column per source,
not a wall of prose.

ANATOMY (1280×720 stage):
1. Full-bleed title band — 0,0 → 1280×96, `--accent` fill, white claim title inside
   (h1 at left padding 56, 28px, 2 lines max) and a small `1 | SECTION` running head pinned
   right inside the band.
2. Icon-circle source columns — 56,132 → 1168×150 to ~480; 4 equal columns, 36px gutters.
   Each column: icon circle 76px at top-left, caption under it (min-height 2 lines to hold the
   row baseline), 1px divider, bold `Source` label + one sentence, bold `Information` label +
   3–4 bullets.
3. Lavender pointer inset — 56, bottom:104, 370px wide: italic pointer to the detailed appendix
   pages, light `--tint` field.
4. Fieldwork strip — 444, bottom:110 → right 56: 4 label/value pairs under a 2px `--accent`
   rule (window / mode / total sample / weighting), superscript markers on claims.
5. Footer — chevron glyph bottom-left (14px, accent), source line bottom-left of it (max ~1090px
   wide, 10.5px `--gray-2`), page number bottom-right.

SLOTS:
- title — 2-line claim inside the band, ≤15 words ("Methodology:" prefix is part of the label;
  the rest must be a claim, not the topic word "Methodology" alone).
- running-head — "1 | SECTION" style, ≤18 chars.
- src-caption ×4 — source name, ≤2 lines / ~15 chars.
- src-source ×4 — one factual sentence, ~110 chars. What makes it good: names the instrument,
  the provider and a date; bad: "NBN Co" alone.
- src-bullets ×4 — ≤4 per column, ~75–90 chars each, each carrying one verifiable fact
  (population size, coverage, field dates). Good: three-digit sample sizes and exact dates.
- inset — pointer sentence, ≤2 lines.
- field-value ×4 — one short phrase each (dates / mode / n / weighting method).
- source-line — full provenance sentence, 2 lines max; footnote definitions inline after it.
- pageno — deck page, right aligned.

FILL:
- Replace every text node; the geometry does not change. If a fifth source appears, set
  `main.cols` to `grid-template-columns:repeat(5,1fr)` — then shrink `src-bullets` to 3 per
  column (28px min line-height means ~11 text lines per column is the hard ceiling).
- Bullets use a gray square marker (::before), not an icon font. Icons are inline SVG circles —
  swap only the inner path per source, keep `fill:var(--accent)` on the circle.
- Recolor for another firm: set `--accent` (band, circles, fieldwork rule, chevron) and
  `--accent-2` (labels) to the brand pair; keep the white body. For a blue firm (e.g. KPMG
  #00338D) that single swap is the whole rebrand.
- The footnote markers in the source line (¹²³) must match the superscripts used in the field
  strip and inset — add/remove together.

VERIFY:
- [ ] Title ≤15 words and ≤2 lines at the band's 1090px cap (the h1 max-width enforces it).
- [ ] "Methodology:" label prefix present; rest is a claim sentence.
- [ ] Source line bottom-left present, with every methodology claim footnoted.
- [ ] One emphasis color (`--accent`) + gray ramp only — bullets must NOT be colored.
- [ ] Text on the purple band clears 4.5:1 (white on #6E0A8F ≈ 8:1; do not lighten the band).
- [ ] Page number bottom-right; running head in band.

DON'T:
- Don't let captions/fields run long enough to break column baseline alignment (caption slot is
  sized for 2 lines — that's the gate).
- Don't add more than 4 bullets or a second sentence per Source block; that is the difference
  between a scannable page and the "wall of methodology text" the corpus decks get punished for.
- Don't replace circles with SmartArt-style clip icons — draw real SVG shapes, per the source
  deck's custom iconography.
- Don't leave the lavender inset as boilerplate ("see appendix") — it must name pages.

SOURCE: Accenture — "The nbn effect: how the nbn network adds value to…"
(accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o), p30 read in
sw_sheets/accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o_s03.jpg
(p31 frame; 5-col × 2-row sheet), archetype "methodology-iconrow" per
TEMPLATE_HARVEST.json; pattern + palette + footer contract (chevron / page / source) from
reviews/accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o.md
(§Color system, §Copy — band height 10–12% cap, 2-line white claim, lavender tint tokens).
The review flags p30's layout as near-SmartArt boilerplate and tells builders to keep its real
Source/Information content but not mine the shape — this template keeps the content discipline
and tightens the shapes (custom SVG icons, real fieldwork strip, footnoted provenance).
