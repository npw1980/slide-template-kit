# data-table-numeric-matrix — Dense numeric matrix with one highlighted row + summary bars

WHEN: A survey/fieldwork page whose exhibit IS the table — entity rows (banks, markets, peers) × metric columns, plus a weighted-average line. For "the numbers themselves argue" pages: bank-level detail, market share matrices, survey cross-tabs with an outlier to point at. From EY IFRS 9 banking survey p12 ("bank-level data matrix; raw table; summary bars", sheet `sw_sheets/ey__ey_ey_ifrs_9_impairment_banking_survey_2018_s01.jpg`) with EY European Banking Barometer p5 (boxed crosstab) and KPMG Our Impact Plan p23 (region × metric grid + footnote markers) as secondary evidence.

ANATOMY (all coords on the 1280×720 stage, rem = 1 stage px):
1. kicker — x64 y36, 14px uppercase, gray-1 (section breadcrumb)
2. title (claim) — x64 y60, 28px bold display, max 2 lines @1050px width
3. claim-sub (table description + superscript marker) — x64 y106, 16px gray-1
4. header band — x64 y160, 1126×52px fill gray-4; group captions y183, column captions y201; baseline rule y212
5. data rows — 36px pitch, first baseline y268; row = one `<g transform="translate(0,36*i)">`; label x80 (left), numbers right-anchored at x505 / 610 / 715 / 862 / 990; mini-bar band x1015..1190 with baseline hairline
6. total row — translate(0,252), rule 13px above, bold values, no mini bar
7. highlight — 4×24px accent bar at x64 + bold row values + accent mini bar (never a tint block)
8. so-what band — x64 y540, 1126×58px accent fill, headline y562 + detail y582, near-black text
9. footnotes — y628 / 643 / 658, 10.5px gray-1, tspan-bold markers
10. source line — x64 bottom:24, 11px; running head + page stamp right:64 bottom:24

SLOTS:
- `kicker` ≤ 60 chars — section + sub-section + detail marker; not a sentence.
- `title` ≤ 15 words / 2 lines — a quantitative claim that survives reading the table ("Three banks carry more than triple the sample-median stage-2 exposure"), not "Stage allocation by bank".
- `claim-sub` ≤ 120 chars — what the columns mean + methodology superscript.
- `rows[].*` — 7 entity rows: label ≤ 18 chars (anonymised "Bank A" is honest when the deck does that); s1/s2/s3 one decimal; pd integer; d signed "+x.x"/"−x.x".
- `total` — one line, bold, labelled "Weighted avg. (n=7)" — state the weighting, never "Total" if it is not additive.
- `highlight-row` exactly ONE (the `hl:true` row); the so-what band restates it in plain language ≤ 2 lines.
- `footnotes` ≤ 3 — definitions the claims need (rounding, PD horizon, n).
- `source-line` ≤ 150 chars — survey, date, n, analysis provenance.

FILL (step-by-step):
1. Replace kicker / title / claim-sub text nodes. Title first — if it breaks 2 lines, shrink the wording or widen to `width:1100rem`, never shrink below 26px.
2. Swap the `rows` array (documented in the index.html comment). Per row, change only: the label text, the five number texts, and the bar `<rect width>` = pd × 1.1. Keep one row `hl:true` and delete the left `rect` pair + bold attrs from the previous one.
3. Total row: five numbers only. If row count changes, adjust the total-row `translate(0, 36*count)` and its rule line is relative (`y="-13"`), so it follows automatically; if >8 rows, drop the so-what band to `y = 56 + 36*(rows+1)`.
4. So-what band: swap the two text lines; the band stays 58px — two lines max.
5. Footnotes and source line last.
6. Recolor: swap `--accent` (yellow → #EAF1FD for KPMG blue, hexes in the token comment); `--accent-ink` must stay near-black or dark-navy so text ON the band clears 4.5:1.

CHART RECIPE:
- This is a table, not a picture: the encoding is position (row/column) + one visual check bar. No cell shading, no zebra banding, no icons.
- Scale: columns have no axis — each column is a closed scale defined by its caption unit ("% of book", "bp, 1-year horizon", "pp"). Print precision is fixed per column (1 decimal / integer / signed 1-decimal) so decimals line up on the right anchor; that is the whole axis discipline.
- Value labels: none needed — the cell IS the label. Right-align (text-anchor:end at the column edge); never center numeric columns.
- Mini-bar: linear, width = value × 1.1px inside a fixed 175px band; baseline hairline per row, no tick marks, no category repeats. It exists so the eye sees the PD distribution; the exact number lives in the column. One bar accent = the `hl` row; all others gray-2.
- One accent + gray ramp: gray ramp does everything (text ink #1A1A1A, secondary #7A7A7A, hairlines #D9D9D9, bars #B8B8B8); the accent (#FFE600 EY yellow) appears exactly twice — the left marker of the highlighted row and the so-what band. Never fill cells with the accent.
- Emphasis is data-driven: highlight whatever row the claim names. If two rows compete, there is no single claim — rewrite the title.
- Totals: separated by a 1.4px ink rule, bold, never shaded.

VERIFY:
- [ ] title ≤ 15 words, ≤ 2 lines at stage width (MBB gate)
- [ ] numbers right-anchored, decimals lining up, per-column precision constant
- [ ] exactly ONE accent color (yellow), text on it ≥ 4.5:1 (ink on #FFE600 ≈ 12.4:1)
- [ ] ≤ 4 hues total (accent + ink + gray ramp)
- [ ] one highlighted row, matching what the title claims
- [ ] source line present bottom-left; `SECTION · 1` stamp bottom-right; superscripts match footnote count
- [ ] render passes in headless chromium at 1280×720, nothing clipped

DON'T: topic titles ("Bank-level detail"); highlight by row position instead of by claim; shade the whole highlighted row in yellow (band + bar is enough — block fills turn the table into a poster); zebra-stripe rows; put `<sup>` inside SVG `<text>` (chromium silently drops everything after it — use ¹ ² ³ or tspan); "Total" for a weighted average; footnotes longer than 3 that repeat the caption.

SOURCE: EY — `ey__ey_ey_ifrs_9_impairment_banking_survey_2018` p12 (sheet `sw_sheets/ey__ey_ey_ifrs_9_impairment_banking_survey_2018_s01.jpg`, row 1 col 2), page viewed directly; secondary: `ey__ey_european_banking_barometer_2015_2015` p5, `kpmg__kpmg_kpmg_our_impact_plan_2023` p23 (`..._s02.jpg`). Colour rules from reviews `ey__ey_ey_ifrs_9_impairment_banking_survey_2018.md` (line 25: two-colour system, yellow ~#FFE600) and `kpmg__kpmg_kpmg_our_impact_plan_2023.md` (lines 41-45 for the blue-house swap). Real fonts: EY uses EYWeb/Helvetica family — the Arial/Helvetica stack stands in.
