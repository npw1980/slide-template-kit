# waffle-heat-matrix — Adoption heat matrix (paired in-cell bars + 5-step status ramp, "waffle" of cells)

WHEN: A survey needs *many* percentages shown at once — items × respondent cohorts with a change-direction signal per row — and the honest encoding is a matrix of cells, not a bar race. Built from L.E.K.'s signature in-cell bar heat matrices: APAC hospital deck p11/p24/p25 (departments/journey stages × geographies, paired bars + green/red status arrows + "not included" graying) and the Deloitte New Mexico staffing study p13 (colored numeric-cell matrix). Use when the exhibit's job is "who is ahead, and moving which way".

ANATOMY (1280×720 stage):
1. Claim title — 60,40, 950 wide, 27px/1.25 bold green `--accent-deep`, ≤15 words / 2 lines: "SEA hospitals are outpacing China and India on digital adoption — and the gap is widening".
2. Section chip — right 56, top 42, 24px tall, white bold caps in green pill `NN · SECTION`.
3. Matrix table — 60,118, 1160 wide. Header row 2px accent underline. Group bands (journey stage) 26px gray rows with caps green label. Item rows 57px: label 378px | paired-bar cell 336px | per-geography numerals 132px | status 96px.
4. Status legend — right 56, top 118, 206 wide: 5-step ramp list + series key (SEA / China-India / n/a swatches).
5. So-what kicker band — 60,586, full width −120, 38px, gray fill + 4px accent left rule.
6. Footnote block — 60,640, 9.5px: Question / Base / Source with bold lead-ins.
7. Page stamp bottom-left (`NN | CONFIDENTIAL — DRAFT`), running head bottom-right, diagonal green/lime logo notch bottom-right corner.

SLOTS:
- title — comparative quantitative claim ("outpaced… and the gap is widening"), ≤15 words / 2 lines.
- chip — `section-number · Section Name`, ≤24 chars.
- ROWS[] — 6–9 items in 2–3 stage groups. item ≤46 chars + optional 11px parenthetical example; `sea`/`chi` integer % (null = not asked → renders "not included"); `delta` signed pts vs baseline (null when baseline missing).
- kickerbox — ≤115 chars.
- foot — question verbatim, base n per cohort, source + fieldwork window.

FILL:
1. Swap `ROWS` — each `item`, `sea`, `chi`, `delta`. Bars auto-length (track = 0–100% linear on 308px), status arrow auto-selects from thresholds.
2. A cohort not in the sample = `chi: null` (renders gray track + "not included" + dash arrow) — never delete the row.
3. Thresholds live in `STATUS[]`: ≥+15 pts dark green up / +3…14 green up / −2…2 flat gray / <−2 red down. Adjust only with the same semantic ladder.
4. Recolouring for another firm: change `--accent` and keep the ramp as `--accent-deep` (darker) / `--accent-soft` (lighter) / grays. The 5 status colors are *semantic*, not palette: keep up=dark-accent/green, down=red, flat=gray.
5. Group bands: one `<tr class="group">` per stage; keep groups ≤3 (they stack vertically, height is fixed).

CHART RECIPE:
- Scale: single shared 0–100% scale on every bar track (308px) across all rows — a 29% bar is the same physical length anywhere on the page; that is the point of the matrix. No axis: values print at the bar's right end inside the track (10px bold) and again in the "by geography" column for cross-reading.
- Paired series: SEA = `--accent` solid; China-India = `--accent-soft` (one lightness of accent). The second series is never a second hue. The "rest" (n/a) is `--gray-2`. This is the "one accent + gray ramp" rule — the page is green + gray + red-for-declining + the flat-gray marker.
- Status encoding (the "heat" part): each row's *change* is a 5-step ramp — dark green / accent green / gray flat / red down / gray dash. Red is allowed as the fourth semantic color ONLY for decrease; it is not decorative. The legend defines every step with a threshold range; the reader never guesses.
- Value-label placement: inside the bar end for bars ≥ ~12%, else right of the track; geography column is right-aligned with cohort labels in gray. Status arrow is vertically centred in its 96px column.
- Sorting: group by the analytic sequence (patient journey = time order here), then items descending within a group if no natural order — never alphabetical.
- Emphasis: the one accent is the home cohort; comparison series sits one lightness back so the eye reads lead/lag before reading numbers. No bold borders around cells, no shadows.
- Axis / unit rules: all bars are "% of respondents currently using" — stated once in the header; integers only; base n per cohort in the footnote with the question quoted verbatim.

VERIFY:
- [ ] Title ≤15 words / 2 lines, comparative not topical.
- [ ] One accent hue; red appears only in decreasing-status arrows.
- [ ] Bars share the same px scale row to row (spot-check two rows).
- [ ] Every row has an arrow; null-delta rows render the dash + "not included", not 0%.
- [ ] Legend lists all 5 steps with ranges; series key present.
- [ ] Footnote has Question / Base / Source; fieldwork window named.
- [ ] Page stamp + running head present; ≤7px rows never carry in-bar text that overlaps.
- [ ] White-on-green chip text ≥4.5:1; green `--accent` used for large text/titles passes.

DON'T:
- Don't rainbow the matrix (each stage another hue) — L.E.K.'s discipline is green+gray, arrows do the talking.
- Don't give "not included" a 0% bar — it reads as a failure, not a gap in the question.
- Don't put delta arrows inside the bars; they live in the status column with a legend.
- Don't re-sort alphabetically and don't add a trendline — this is a snapshot, not a time series.
- Don't exceed ~9 data rows; below ~10px bar height, value labels go off-bar.

SOURCE: L.E.K. Consulting, `l-e-k-consulting__l_e_k_2023_apac_hospital_insights_survey_findings_for_health`, p24 (and sibling heat matrices p11/p25/p26) measured on `sw_sheets/l-e-k-consulting__l_e_k_2023_apac_hospital_insights_survey_findings_for_health_s02.jpg` (sheet 2, row 1); green+gray + arrow semantics and "not included grayed / N-per-country / question-quoted" discipline from `reviews/l-e-k-consulting__l_e_k_2023_apac_hospital_insights_survey_findings_for_health.md` §color system / §signature exhibits. Secondary witness: Deloitte, `deloitte__deloitte_new_mexico_state_university_staffing_study_opportun`, p13 colored numeric-cell matrix, `sw_sheets/deloitte__deloitte_new_mexico_state_university_staffing_study_opportun_s01.jpg` (sheet 1, row 1), per its review's diverging-cell-matrix notes.
