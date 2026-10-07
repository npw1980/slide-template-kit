# cover-standalone-band — Field Cover + Full-Width Value Band

WHEN: The report's page-1 cover when the cover stands on type AND wants a dedicated emphasis
zone — a brand-color field carries the title stack and a full-width accent band across the lower
third carries the value line and one headline stat. No photo, no diagram. Use it over
`cover-standalone-flat` when the cover has a quantitative takeaway worth a band rather than an
inline subtitle. Evidence: KPMG *Global Tech Report 2022*, cover p1 — solid brand field with the
type lifting off a lower accent-blend zone and a faint numeral texture behind it; the one brand
accent does real work as a band, not just a corner chip.

ANATOMY: numbered slot map, px coords on the 1280×720 stage (measured against the file):

1. `kicker` — 64, 56 · chip 26×8 (`--accent`) + eyebrow. Height 20.
2. `lockup` — right 64, 54 · ~150×26. Three white bars + wordmark "YOURCO®". Above the band.
3. `title` — 64 → 1064 (width 1000), 260 · 2-line block. 54px bold / 1.08, −0.6 tracking, white on field.
4. `band` — 0 → 1280, 520 → 640 (120 tall). Full-width `--accent`→`--accent-edge` gradient. This is the emphasis device.
5. `bandtext` — 64 → 1000 (right 280), 556 · value line, dark ink `--band-ink` on the band.
6. `bandstat` — right 64, 546 · big numeral 44px tabular + caption, dark ink, right-aligned.
7. `bandrule` — 64 → 1216 @ 616, 1px, `--rule-band` (dark hairline inside band).
8. `meta` — 64, 658 · date (white bold) · home · url, light ink — sits on the FIELD below the band.
9. `page` — right 64, 494 · bare "1", sits on the field just above the band.
10. `watermark` — right 40 / top −40 · giant translucent section numeral "1", opacity .055 (decorative, not an editable slot).

SLOTS: name → limit → good / bad.

- `title` → ≤15 words, ≤2 lines. 1000px @ 54px bold −0.6: ~115 chars / ~15 words over 2 lines. GOOD: a claim with a number/scope. BAD: topic label ("2026 Tech Report"). 3 lines = cut the clause, don't shrink.
- `kicker` → 1 line, ≤50 chars, uppercase ≤5 words. BAD: a 2-line eyebrow wall.
- `bandtext` → 2 lines, ≤205 chars. GOOD: what the study proves + n= + markets, carrying the `sup 1` marker. BAD: restating the title, or a value line that duplicates `bandstat`.
- `bandstat` → big number ≤4 chars (e.g. `64%`) + caption ≤34 chars. GOOD: the single headline stat, and it should be a DIFFERENT number than any in `bandtext` (here `bandtext` narrates the barriers list, `bandstat` isolates the governance figure). BAD: two competing headlines, or the same figure shown twice at the same weight.
- `meta` → 3 items: date (bold ≤18), scope (≤10), url (≤34). BAD: an address block or "draft" boilerplate.
- `page` → single digit. This family carries a bare page number (on the field, above the band), not `1 | SECTION`.
- `lockup` → wordmark ≤8 chars; replace text only. Placeholder "YOURCO" is honest — not another firm's brand.

FILL (text nodes; band geometry is layout, not data):

1. Title: edit `h1.title`. Keep `<em>` only for one tinted emphasis word (`--accent-edge`, same hue); delete it if there is nothing to stress.
2. Band value line: edit `p.bandtext`; keep `<b>` on the quantitative anchors and `<span class="sup">1</span>` only if a footnote is carried.
3. Band stat: edit `.bandstat .big` and `.cap`. This is the slot's whole reason for existing — one number, biggest weight. If you delete it, widen `.bandtext` right 64 and center the value line.
4. Recolor: change only `:root`. Field `--bg` + band `--accent` are one hue pair; text on the band MUST be dark (`--band-ink` / `--band-sub`), never white. To go the violet (Accenture) variant: `--bg:#2E0B66 --accent:#7B1FF0 --accent-edge:#A45CF0 --tint:#E7D9F8 --gray-1:#E7DEF7 --gray-2:#CBBAEC` — but keep dark ink on the band; on a dark violet band white text is fine, so that variant can flip `--band-ink:#FFFFFF --band-sub:#E7DEF7` instead. The rule is text-band contrast, not a fixed color.
5. Watermark numeral: edit the `1` in `.watermark` to the section/cover number; keep opacity low enough that the title over it stays ≥4.5:1 (5.5% is safe).

VERIFY: checklist (measured, not asserted):
- [ ] Title gate ≤15 words / 2 lines at 1000×54. Placeholder passes.
- [ ] Contrast on the FIELD (#00338D): white `--ink` ≈12.9:1, `--tint` #CFEEFB ≈11.3:1, `--gray-2` #A9C4E6 ≈4.9:1 — all ≥4.5:1.
- [ ] Contrast ON THE BAND (#00AEEF→#31C6FF, worst end the lighter #31C6FF): `--band-ink` #001E3C vs #31C6FF ≈7.6:1, `--band-sub` #0A3A5C ≈5.4:1 — all ≥4.5:1. White text on this azure would be ≈2.4:1 and FAILS — that is exactly why the band carries dark ink, not white. Do not swap to white body text on the band.
- [ ] One emphasis hue: blue family + achromes; the band is that hue expressed as a surface, not a second color.
- [ ] `sup 1` contract: if present in `bandtext`/`bandstat` cap, the cover has no separate note line — delete the markers if you are not shipping a methodology footnote elsewhere, or add a one-line `.note` above the bandrule. Never leave a dangling marker.
- [ ] No page-number-in-band: page number sits on the field (right 64 / 494), a bare digit, not `1 | SECTION`.
- [ ] Self-contained: `grep -o -E "https?://" index.html` returns nothing (the url anchor is `href="#"`, no host). `grep -o -c "<script\|<link\|<img\|<iframe\|@import"` → 0. Inline CSS + divs/gradients (no SVG element, no webfonts).
- [ ] Fonts: display `"Helvetica Neue", Arial, Liberation Sans`; body Arial/Calibri stack. House sans substitute, not a brand face.

DON'T:
- Don't paste white body text onto the azure band (2.4:1 fail) — dark ink only; the violet variant may flip to white only if the band goes dark.
- Don't show the same figure twice (bandtext + bandstat) at the same weight; isolate one number in the stat.
- Don't add a photo — this is the type-only band subtype.
- Don't stack a kicker wall, don't run a second hue for category, don't let the watermark climb into a legibility risk over the title.
- Don't shrink the title to force a 3-line story into 2 — cut the clause.

SOURCE: extracted from the live render of the cover, not prose alone —
`/home/nathan-white/new projects/deck-research/sw_sheets/kpmg__kpmg_kpmg_global_tech_report_2022_2022_s00.jpg` (cover = p1, frame 1: solid brand field, left-aligned white display title, lower accent blend lifting the value line, faint brand texture, wordmark lockup, bare page marker). Analyzed in
`reviews/kpmg__kpmg_kpmg_global_tech_report_2022_2022.md` (color section: KPMG navy/blue ground ≈#00338D, azure #00AEEF / #31C6FF, one-hue-per-section, cover anatomy). Harvest family `cover-standalone`, exemplars `kpmg__kpmg_kpmg_global_tech_report_2022_2022__p14` ("display-only title page") + deck cover p1. Spec: `TEMPLATE_SPEC.md`.
