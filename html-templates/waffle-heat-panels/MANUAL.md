# waffle-heat-panels — Cohort waffle panel page (hero 10×10 waffle + per-cohort mini-grids)

WHEN: A survey finding is a single share (1 dot = 1%) and the argument lives in *which group* carries it. Built from the PwC Global Workforce Hopes & Fears survey grammar — the p13 page "65% of employees have discussed social/political issues" pairs a 10×10 waffle with cohort bars — and the KPMG AI report's blue Figure-5 page of 12 dot-matrix mini-grids (each 10×5, fill = share). Use when the exhibit must show "one number, and who it comes from" without any axis.

ANATOMY (1280×720 stage):
1. Kicker / chapter tab — 64,44, up to 900×20, uppercase 11px + 46px accent underline.
2. Claim title — 64,82, 980 wide, 31px/1.22 bold, ≤2 lines; sup-marker `1` for the methodology claim.
3. Hero exhibit (left) — 64,196, 580×420: caption at top; giant numeral 92px at 64 relative y≈44; 10×10 waffle SVG (29×29 pitch, cell 26px, rx 3.5) right of the numeral; unit note below ("1 cell = 1%").
4. Cohort panel (right) — 700,196, 516 wide, 4 rows at relative y = 36/138/240/342 (96px each): 5×10 dot grid (16px pitch, dot r 3.6), cohort name 15px + descriptor 12px, right value 34px bold, delta "±N pts vs overall" 12.5px.
5. So-what kicker band — 64,646, full width −128, 34px tall, 3px accent left rule, 14.5px bold sentence.
6. Source line — 64,bottom 16, 9.5px gray; page running head — 64 right at bottom 16 (`NN | SECTION`).

SLOTS:
- kicker — ≤70 chars, "Chapter · Sub-theme", one tab not a wall.
- title — quantitative claim, ≤15 words / 2 lines. "Ethnic-minority employees discuss social issues 5 points above the workforce average" — a topic title ("political issues at work") is a failure.
- HERO.value — one integer %, no decimals.
- COHORTS[] — 3–5 groups; name ≤21 chars, desc ≤24, value integer %, exactly one `hot: true` (the argument group).
- kickerbox — ≤110 chars, one imperative "so what", no numbers it doesn't need.
- source — question + n + geography, 2 lines max.

FILL:
1. Replace `HERO.value` (the whole-population %, drives the hero grid and all deltas).
2. Replace `COHORTS` name/desc/value for each row. Nothing else is manual — grids, delta text and colors recompute.
3. If a cohort exceeds 50×2% precision needs, keep the 5×10 grid (round to nearest dot) — never change dot geometry per row.
4. Different firm: recolour `--accent` (and keep `--accent-soft` one lightness lighter, `--accent-text` a darker text-safe variant). Inactive cells keep `--gray-2`.
5. Page number: edit `.page`.

CHART RECIPE:
- Scale: hero is exactly 100 cells; 1 cell = 1%; fill = `Math.round(value)` cells read row-major left→right, top row first. Mini-grids are 50 dots; 1 dot = 2%; fill = `Math.round(value/2)` dots. Never mix two scales inside one figure; if the audience needs finer resolution, switch the HERO grid, not the minis.
- Value labels: the giant `68%` numeral sits beside the hero grid (92px, `--accent-text`); each cohort shows its % as a 34px numeral at the right of its row, plus a signed delta vs overall (`+5 pts vs overall`, `−4` uses a real minus glyph). No axis, no gridlines, no legend — the unit note "1 cell = 1%" is the legend.
- Emphasis: ONE accent. The argument group's dots use `--accent`; every other cohort fills with gray `#AEB2BA` (inactive dots stay `--gray-2`), so the page still reads one hue + gray. Hero cells: accent filled / gray empty. Never colour cohorts by "identity" — colour is emphasis, not category.
- Axis / unit rules: none allowed; percentages to integers; the question + n belong in the footnote line, never inside the picture. Base is weighted and named in the source line.
- Rounding rule: row-major fill, remainder dot left gray (never "last row centered"); state "cells filled represent a weighted average — not exact people counts" if challenged.

VERIFY:
- [ ] Title ≤15 words, ≤2 lines at 31px.
- [ ] Exactly ONE `hot: true` cohort; only one saturated hue on the page.
- [ ] Hero fill matches HERO.value to the cell (row-major count).
- [ ] Delta signs use `+`/`−` and reference "vs overall" consistently.
- [ ] Source line present with n, question, weighting; sup 1 marker on title.
- [ ] Page running head bottom-right.
- [ ] Text on accent areas ≥4.5:1 (accent is only used for numerals/graphic fills on white — check white-on-accent if you invert).

DON'T:
- Don't colour each cohort differently (10-hue pie disease in waffle clothing).
- Don't write topic titles ("workforce discussions").
- Don't keep legends or axis ticks on a waffle — they're chart-junk here.
- Don't let cohort names run to two lines; wrap is off by design.
- Don't show more than 5 cohorts; the panel stops fitting honestly.

SOURCE: PwC Strategy&, `pwc_strategy__pwc_global_workforce_hopes_and_fears_survey_2022_2022`, p13 (waffle + cohort matrix, "65% have discussed…") measured on `sw_sheets/pwc_strategy__pwc_global_workforce_hopes_and_fears_survey_2022_2022_s01.jpg` (sheet 1, row 1); grey waffle-cell values (#BFBFBF/#D9D9D9) and crimson-family waffle fill (#E30345→#EC008C) from `reviews/pwc_strategy__pwc_global_workforce_hopes_and_fears_survey_2022_2022.md` §color table + p13 description. Second witness: KPMG, `kpmg__kpmg_ai_in_financial_reporting_and_audit_navigating_the_new_`, Figure-5 blue waffle page (10×5 dot-matrix grids, fill=%) per `reviews/kpmg__kpmg_ai_in_financial_reporting_and_audit_navigating_the_new_.md` §color/chart inventory. Accent set to crimson #D62246 with darker text-variant; firm-neutral tokens otherwise.
