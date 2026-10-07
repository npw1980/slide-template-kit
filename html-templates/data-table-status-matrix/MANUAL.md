# data-table-status-matrix — Grouped heat-cell verdict matrix

WHEN: A landscape page where the exhibit is a matrix of qualitative verdicts, not numbers — players/markets/segments (rows) × capability or value-pool dimensions (columns), grouped into band rows by one headline metric, with the problem cells loud. Built from Accenture Post & Parcel Industry Trends 2023 p10 — four CAGR band headers, players under each, colour-coded cells + legend strip (sheet `sw_sheets/accenture__accenture_2023_post_parcel_industry_trends_2023_s00.jpg`, page p10 row1 col5, viewed directly). Secondary: Deloitte Digital Transformation 2018 p7 (5-coloured-header matrix), EY Infrastructure Barometer Italy 2020 p8 (comparison matrix).

ANATOMY (1280×720 stage, rem = 1 stage px):
1. kicker — x64 y36, 14px uppercase gray-1
2. title (claim) — x64 y60, 28px bold, ≤ 2 lines @1080px
3. claim-sub — x64 y104, 15px gray-1; states the grouping metric + what cells mean + superscript
4. header chips — full-width band x64 y198 h34, deep-accent fill, white column captions (label col left, verdict cols centre-anchored, numeric col right)
5. group bands — x64 w1126 h26, gray-4, 11.5px uppercase letterspaced captions (the banding metric + threshold)
6. player rows — 36px pitch inside each group; label x92 13.5px; four verdict cells 124×24px centred on x520 / 660 / 800 / 940; numeric column right-anchored x1160
7. highlighted row — 4px accent bar x64 + bold label; cell fills unchanged
8. legend strip — right-aligned y608, four 70×20 chips (Strong/Stable/Weak/n.e.); one line of legend text left-aligned x64
9. footnotes — y652/666, 10.5px gray-1, tspan-bold markers
10. source line x64 bottom:24; running head + page stamp bottom-right

SLOTS:
- `title` ≤ 15 words — a count + consequence claim ("Two of seven players sit on double-weak economics before the 2024 price round"); must be readable off the cells alone.
- `claim-sub` ≤ 170 chars — grouping rule, CAGR basis, "cells state the verdict, not the score".
- `group bands` 3–4 — each names the banding metric + numeric threshold ("MID-TIER — VOLUME CAGR 0 TO 5%"); bands must be mutually exclusive.
- `rows[].p` ≤ 26 chars — anonymised players are fine pending client release.
- `rows[].v[0..3]` — verdict word only: strong/stable/weak/ne. No numbers in cells, no scores, no 5-point scales.
- `rows[].cagr` — signed one-decimal %; a row whose CAGR contradicts its band is an error — re-band.
- `highlight` exactly ONE row (hl:true), footnote ² says why.
- `legend` — 4 chips; keep the "n.e." chip even if unused once, it declares the evidence boundary.

FILL (step-by-step):
1. Text nodes: kicker/title/claim-sub. If the claim-sub goes to 3 lines, drop the em-dash clause, not the font size.
2. Swap the `groups` array (in the index.html comment). Per row change: label text, the four cell fill colors + words + glyphs (they swap as a TRIPLE — fill, word, glyph together), and the CAGR text. Cell geometry never changes.
3. Verdict → styling triple, fixed: `strong` → fill `--accent-tint` + "▲ Strong" (ink text); `stable` → `--gray-3` + "● Stable"; `weak` → `--accent` + "▼ Weak" (white bold); `ne` → white fill + dashed gray-2 outline + "n.e." gray.
4. Highlighting a different row: move the two small rects (`x64 y-12 w4 h24`) + bold attrs — the bar's colour is `--accent` (weak-row semantics) or `--accent-2` (strong-row marker; see group 1). No row gets a fill band.
5. Add/remove rows: rows are `translate(0, centreY)` groups at 283/317/400/434/468/531/565 — keep the pattern (+36 per row, +126 after each group band) and keep the legend/footnotes below. >8 rows → shrink group bands to 22px and pitch to 32px.
6. Recolour for another house: set `--accent` (e.g. KPMG #0F2E8C) and `--accent-tint` (pale tint of it) together so the ramp stays one hue; header chips and weak cells share `--accent`, text on them must clear 4.5:1.

CHART RECIPE:
- The matrix encodes ordinal verdicts: strong > stable > weak, plus an "n.e." hole for missing evidence. Encode as ONE-ACCENT SILENCE RAMP: problem cells take the full accent (that is the page's purpose — the eye lands on weaknesses first), mid sits on the gray ramp, strong stays pale. Never red/green traffic lights (the source's habit, rejected here — see DON'T).
- Cell = word + glyph: ▲ (up/favourable), ● (flat), ▼ (deteriorating/negative) — redundant encoding so the page survives greyscale print and colour-blind reading. Word text is always the same 12.5px; emphasis comes only from fill + white text on weak cells.
- No numeric axis exists by design: the band headers + the CAGR column give the quantitative spine. If you need exact numbers in cells you picked the wrong template — this is `data-table-numeric-matrix`.
- Group bands ARE the scale: thresholds stated in the caption, bands sorted high→low growth, never mixed.
- Legend is the contract: every fill must appear in it; if a state stops being used, remove its chip, don't let the legend drift.
- One accent + gray ramp: hues on the page = purple accent (+ its tint) + gray ramp + ink = ≤ 3 hues. Group band headers/legend are gray, header chips are the single deep accent value.

VERIFY:
- [ ] title ≤ 15 words / 2 lines and true from the cells alone
- [ ] every fill used in cells also appears in the legend strip
- [ ] weak cells: bold white text on full accent, contrast ≥ 4.5:1 (white on #6E00C9 = 6.7:1)
- [ ] no red/green anywhere, ≤ 3 hues
- [ ] one highlighted row with a footnote stating why
- [ ] verdict cells are word+glyph (not scores, not arrows-only)
- [ ] source line + page stamp present; superscripts ≤ 2
- [ ] headless-chromium render at 1280×720 shows no clipped bands, rows inside groups

DON'T: 5-point scales or +/++ ratings (verdicts, not scores); red/green traffic lights (kit is one-accent — the accent IS the warning colour); 10+ hue heatmaps; group bands without thresholds; more than one highlighted row (then nothing is highlighted); numbers inside verdict cells; a legend that only partially covers the fills; "so what" boxes duplicating the title (the cells carry it here).

SOURCE: Accenture — `accenture__accenture_2023_post_parcel_industry_trends_2023` p10 (sheet `sw_sheets/accenture__accenture_2023_post_parcel_industry_trends_2023_s00.jpg`, viewed directly; review `reviews/accenture__accenture_2023_post_parcel_industry_trends_2023.md` items 7 + steal-list "grouped heat-cell table with CAGR band headers + legend strip"). The p10 red/green cell convention was deliberately converted to the kit's one-accent silence ramp — deviation documented above and in the index.html header comment. Secondary: `deloitte__deloitte_digital_transformation_2018` p7, `ey__ey_ey_infrastructure_barometer_italy_2020` p8 (via catalog). Real fonts: Accenture Source Sans family — the Arial/Helvetica stack stands in.
