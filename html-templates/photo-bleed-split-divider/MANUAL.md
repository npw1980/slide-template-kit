# photo-bleed-split-divider — White text field + right-edge photo bleed

WHEN: A chapter opener / "you are here" page inside a survey or ranking report:
one claim, a short lead, and at most three numbered highlights — set against a
photograph that bleeds down the right edge instead of covering the whole page.
Source: PwC Strategy& *Global Top 100 companies by market capitalisation* (2023)
p03 — the review records it precisely: "large black double-quote glyph + serif
chapter name on a white left panel, right panel full-bleed stock photo"
(~55/45 split). Use `photo-bleed-narrative-overlay` instead when the photograph
must be the whole stage.

ANATOMY (1280×720 stage; `index.html` uses `1rem = 1 stage px`, zero JS):
1. photo — `figure.photo`, left 704, width 576, top 0, height 720: bleeds to the top, right and bottom canvas edges only. SVG `preserveAspectRatio="xMidYMid slice"`.
2. seam — right 0, width 4, height 720: 4px brand-orange seam binding the photo page to the rest of the system.
3. glyph — left 64, top 24, 150px serif `&#8220;`: the divider's signature device (decorative, aria-hidden).
4. kicker — left 64 (field x), below glyph: 26×3px orange tick + 10.5px caps, .18em.
5. claim title — 40px serif bold, field width 560, 1–2 lines; ONE keyword in `--accent-deep`. THIS IS THE GATE.
6. lead — 14px/1.6, max-width 520, ≤3 lines.
7. highlight list — `ol.points`, top border 1px, rows separated by 1px hairlines; each row = 15px serif orange numeral + 13px/1.5 text with `<strong>` figures and `sup` markers.
8. footer rule — 1px `--rule` above; source line left (9.5px gray, `sup` markers) + page stamp right (`PAGE | SECTION`, serif page number, caps section).
9. credit line — 8px gray under the footer: photo provenance.
10. placeholder badge — inside the photo, left 12 / bottom 12.

SLOTS:
- `kicker` — 1 line ≤34 chars. Good: `Chapter 2 · The ranking` — it names the section, the way the deck's chapter openers do. Bad: a hashtag or the deck title.
- `title` — **≤15 words, ≤2 lines** (40px serif × 560px ≈ 26 chars/line). Good: a quantitative claim with one emphasised keyword ("The top twenty *own more* of the list than last year"). Bad: "Highlights" / "Supplementary analysis" — the review flags exactly this deck for letting divider and ranking pages drop to topic labels.
- `lead` — ≤3 lines × 62 chars. Good: one sentence of mechanism + a promise of what follows. Bad: restating the title (then the page says the same thing twice).
- `point_1..3` — ≤2 lines each, and each row needs at least one `<strong>` figure. Good: number + what moved + comparison. Bad: three rows that are just labels, or a fourth row (the hairline block stops fitting).
- `source_line` — ≤2 lines with as-of date, universe, restatement note; `sup` markers map to back-matter.
- `page_stamp` — `PAGE | SECTION`, 1 line.
- `credit_line` — 1 line. Good: library/licence + grade. Bad: blank.
- `photo` — one landscape image, subject weighted to the LEFT third of the frame so faces/objects sit where the text field can't reach.

FILL:
1. Swap the photograph: replace the `<svg>` inside `figure.photo` with either the base64 raster in the same SVG (`<image href="data:image/jpeg;base64,…" width="576" height="720" preserveAspectRatio="xMidYMid slice"/>`) or the exported picture layer. Crop to 4:5 portrait-ish; the crop is cover, so nothing stretches. Delete the `.stamp` span once licensed imagery is in. If the crop is wide, widen the `.photo` box (left 640 → width 640) rather than letting the crop cut a face.
2. The seam: keep the 4px orange edge; set `--accent: var(--ink)` if the client is monochrome, or delete `.seam` if the house style forbids decorative colour on photo pages (the review notes this deck's photo colour is decorative — fix that here rather than copying it).
3. Recolour: `--accent` (seam, tick, numerals, keyword), `--ink`/`--ink-soft` (type), `--rule` (hairlines). Photos in this family run COOL blue-teal (#3C679A / #12232C measured) and must stay independent of chart colours — never duotone the photo in the same hue you use for bars.
4. Title grows: 40px is the ceiling. If a claim needs more room, drop to 36px (2 lines ≈ 29 chars/line) before touching the list; the list must keep 3 rows at 15px numerals.
5. Footnotes: body `sup` 1/2 must appear in the source line and match back-matter numbering.
6. Real fonts: PwC Strategy& uses a transitional serif (Georgia/PT-Serif-like) for cover/chapter/page titles and a grotesque for body, data and footnotes. Both stacks here stand in; nothing is a webfont.

CHART RECIPE: n/a — this is a divider page; the numbers belong in the three highlight rows, not in a figure. If a spark is added, it goes under the lead at ≤300px wide, one accent line + gray, and never on top of the photograph.

VERIFY:
- [ ] title ≤15 words, renders in ≤2 lines at 560px (gate).
- [ ] one emphasis hue: orange appears in the seam, tick, keyword, numerals and nothing else; the photo's blue is photographic, not a second brand hue.
- [ ] dark ink on white: `--ink` #12232C on white is ~15:1; body `--ink-soft` #3C4A52 ~8:1; gray-1 source ~7:1. No white-on-photo text is needed here — that is the point of the split.
- [ ] photograph touches top, right and bottom edges (no letterbox), and no text is placed on it.
- [ ] exactly three highlight rows, each with a `<strong>` figure; hairlines aligned to the field width.
- [ ] page number + section present bottom-right, source line bottom-left, both on white.
- [ ] "PHOTO PLACEHOLDER" badge removed once licensed imagery is in place.

DON'T (corpus failure modes):
- Do not title these pages with a topic word. The deck's own weakness is that divider/ranking pages drop from action titles to "Highlights" / "Supplementary analysis" — the gate above is the fix.
- Do not put a fourth highlight or a paragraph-length list item; the block overflows the field.
- Do not tint the photo with brand orange or reuse the chart palette for it — the review calls the photo colour unrelated to the charts, and that is the flaw, not the feature.
- Do not stack more than two photo pages in a row; this family needs the white-field contrast on either side.
- Do not let the photograph carry the page alone: if it has no claim + no numbers, delete the page.

SOURCE: firm PwC Strategy& · deck `pwc_strategy__pwc_global_top_100_companies_by_market_capitalisation_2023` · page 3 measured on `sw_sheets/pwc_strategy__pwc_global_top_100_companies_by_market_capitalisation_2023_s00.jpg` (sheet 0 = pages 1–10, tile 3 of row 1) — white left panel with oversized black double-quote glyph + serif chapter name, right panel full-bleed cool stock photo, "PwC | Global Top 100 companies – by market capitalisation" footer line, page number bottom-right. Divider geometry + serif/sans split + footer habit from `reviews/pwc_strategy__pwc_global_top_100_companies_by_market_capitalisation_2023.md` §Section dividers / §Typography / §Colour system (measured hexes: orange #F07D2D / #ED7D31 / #D04A03, ink #12232C, grays #F2F2F2 / #EFEFEF / #595959, photo blue-teal #3C679A / #12232C) and its §Weakness notes (decorative photo colour, topic-label dividers, no figure numbering) that this template deliberately corrects. Related exemplars noted in the harvest but not new geometry: `pwc_strategy__pwc_iab_podcast_ad_revenue_study...` p04 (→ `photo-bleed-narrative-overlay`), `l-e-k-consulting__l_e_k_2023_manufacturing_survey_executive_summary_2023` p01 (diagonal chevron-clipped photo cover — cover subtype, not this template).
