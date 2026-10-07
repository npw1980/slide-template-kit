# cover-standalone-flat — Flat-Field Display Cover (Type-Only)

WHEN: The report's page-1 cover when the cover must stand on type alone — one solid brand
field, a left-aligned display title, an eyebrow chip, a subtitle line, and a date | home | url
footer. No photo, no diagram, no collage. Use it for insight reports whose cover is a plain
"publication title page" rather than a duotone photo. Evidence: KPMG *Global Tech Report 2022*,
cover p1 (flat brand-blue field, white left title stack, subtitle kicker, tiny footer run
"September 2022 | home | kpmgtechreport2022", wordmark lockup). Re-sighted on KPMG *Our Impact
Plan 2023* cover. It is a sibling of the full-bleed `cover` template — pick this when there is
no hero image and the title is doing all the work.

ANATOMY: numbered slot map, px coords on the 1280×720 stage (measured against the file):

1. `kicker` — 64, 56 · chip 26×8 (`--accent`) + eyebrow text. Height 20.
2. `lockup` — right 64, 54 · ~150×26. Three brand bars + wordmark "YOURCO®". Top-right counterweight to the chip.
3. `title` — 64 → 1104 (width 1040), 288 · 2-line block. 56px bold / 1.08 line-height, −0.6 tracking.
4. `subtitle` — 64 → 1064 (width 1000), 486 · ~57 high (19px / 1.5). One value line, 2 lines max.
5. `hairline` — 64 → 1216 @ 634, 1px, `--rule`.
6. `meta` — 64, 656 · date (bold white) · home (azure) · url (tint, underlined) run.
7. `page` — right 64, bottom 26 · single "1". Tabular numerals.
8. `device` — decorative concentric-ring arc, right:0/bottom:0, 360×360, opacity .10 (not a slot — decorative only).

SLOTS: name → limit → good / bad.

- `title` → ≤15 words, ≤2 lines. 1040px wide at 56px bold −0.6: two lines hold ~118 chars / ~15-16 words. Placeholder is 63 chars and fills 1.5 lines; the slot caps at 2 lines by design. GOOD: a claim with a number and scope ("Digital Investment Held Steady, but Maturity Gaps Cap the Payoff"). BAD: a topic label ("2026 Tech Report"). If it wants 3 lines, cut a clause — never drop the font size.
- `kicker` → 1 line, ≤50 chars, uppercase ≤5 words. GOOD: "Global Technology Report 2026". BAD: a 2-line eyebrow wall.
- `subtitle` → 2 lines, ≤215 chars. GOOD: what the study proves + n= + markets, with the `sup 1` marker where methodology is cited. BAD: restating the title, or a boilerplate "Confidential draft".
- `meta` → 3 items separated by dots: date (bold, ≤18 chars), scope word (≤10), url (≤34 chars). GOOD: fieldwork/publication date + market + report url. BAD: an address block, or "draft for discussion".
- `page` → single digit; covers in this family carry a bare page number bottom-right, not a section name.
- `lockup` → wordmark ≤8 chars; replace text only, keep the bars and the top-right position. (Placeholder "YOURCO" is honest — swap to the real wordmark, not another firm's.)

FILL (replace text nodes; no SVG numbers here, this cover has no chart):

1. Title: edit `h1.title`. Keep `<em>` only for the one tinted emphasis word (same hue as the field, only lightness differs) — delete `<em>` if there is no single word to stress.
2. Kicker: edit `.eyebrow`. The `.chip` is brand chrome; recolor it via `--accent`, do not resize.
3. Subtitle: edit `p.subtitle`; keep `<b>` on the quantitative anchor and the `<span class="sup">1</span>` only if you carry a footnote. This cover carries no footnote line, so if you keep `sup 1` you must either add a `.note` line above the hairline or delete the marker — never leave a dangling superscript.
4. Meta: edit `.meta` spans; set the url `href` to the real report path (the `#` is a placeholder; still zero network, it is inert).
5. Wordmark: `.lockup .word` → real wordmark. Swap the `.bars` `<svg>`-free divs for the brand lockup if it differs; keep position (right 64 / top 54).
6. Recolor: change only `:root`. Field is one hue (`--bg`); `--accent` is the only chroma; white/azure/greys carry everything else. To go the violet (Accenture) variant set `--bg:#2E0B66 --field-deep:#211139 --accent:#7B1FF0 --tint:#E7D9F8 --gray-1:#E7DEF7 --gray-2:#CBBAEC --rule:rgba(231,217,248,.30)` and leave everything else.

VERIFY: checklist (measured values, not asserted):
- [ ] Title gate ≤15 words / 2 lines at 1040×56. Placeholder passes; your text must too.
- [ ] Contrast on `--bg` #00338D: white `--ink` ≈12.9:1, `--gray-1` #D6E4F5 ≈7.0:1, `--gray-2` #A9C4E6 ≈4.9:1, `--tint` #CFEEFB ≈11.3:1 — all ≥ 4.5:1. Re-run after any field-hue swap; the gradient stops at `--bg` (flat) so there is no bright band to hide behind.
- [ ] One emphasis hue total: blue family + achromes. Grey only ever means "the other thing".
- [ ] No page section running head — this family puts a bare page number bottom-right, not `1 | SECTION`.
- [ ] Self-contained: `grep -o -E "https?://" index.html` returns nothing (the url anchor is `href="#"`, no host). `grep -o -c "<script\|<link\|<img\|<iframe\|@import"` → 0. Inline CSS + inline SVG only, no webfonts.
- [ ] Fonts: display/titles `"Helvetica Neue", Arial, Liberation Sans`; body Arial/Calibri stack. The real cover type is a house sans; this stack is the honest substitute, not the brand face.

DON'T:
- Don't paste a photo — this is the type-only subtype. A photo belongs to the `cover` / `photo-bleed` templates.
- Don't add a second hue for category coding; the whole cover is one hue + achromes.
- Don't stack a kicker wall or run a 6pt footer; eyebrow is one line, footer is three short items.
- Don't leave a dangling `sup 1` without a note line.
- Don't shrink the title to force a 3-line story into 2 — cut the clause.

SOURCE: extracted from the live render of the cover, not from prose alone —
`/home/nathan-white/new projects/deck-research/sw_sheets/kpmg__kpmg_kpmg_global_tech_report_2022_2022_s00.jpg` (cover = p1, frame 1; flat blue field, left-aligned white display title, subtitle kicker, footer run "September 2022 | home | kpmgtechreport2022", wordmark lockup, faint page marker). Analyzed in
`reviews/kpmg__kpmg_kpmg_global_tech_report_2022_2022.md` (color section: KPMG navy/blue ground ≈#00338D, azure #00AEEF, one-hue-per-section mapping, cover anatomy). Cross-referenced with KPMG *Our Impact Plan 2023* cover (same flat-field pattern). Harvest family `cover-standalone`, exemplars `kpmg__kpmg_kpmg_global_tech_report_2022_2022__p14` (arch "display-only title page") and the deck cover p1. Spec: `TEMPLATE_SPEC.md`.
