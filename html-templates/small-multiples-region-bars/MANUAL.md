# small-multiples-region-bars — Ranked horizontal-bar panels: Global + regions

WHEN: A survey-driven argument that must show one claim holds EVERYWHERE — the
same ranked category list re-run across Global + N regions in one glance.
Comes from PwC 23rd Annual Global CEO Survey Exhibit 6 ("Uncertain economic
growth is a top ten threat around the world", deck p15/p17) where ranking, not
axis, carries the story. Use it when the point is "same #1 in every segment",
not "who is bigger overall" (that is one ranked bar, not eight).

ANATOMY (1280×720 stage, all coords px):
1. kicker — (64, 38) w860: question phrasing, bold, with footnote marker.
2. title — (64, 63) w900, 28px/35px display, 2-line slot; `em` = operative clause in --accent-deep.
3. chart layer — SVG overlay, 8 panels, origins x = 64/286/508/730, y = 150/406; panel w ~206, h ~246.
4. panel titles — 11.5px bold, baseline y+13 inside each panel.
5. bars — bar x = panelX+6, rows start y+30 (abs 180/211/242/273/304/335 row 1, +256 row 2), step 31, height 9.
6. question sidebar — (976, 150) w240 tinted box: QUESTION label + full survey question + base line.
7. source — (64, 681) w1020.
8. page number — (1216, 681): "12 | CEO SURVEY".

SLOTS:
- title: ≤15 words, ≤2 lines (slot clips at 71px — if it clips, your title is wrong). Must be a QUANTITATIVE POSITION CLAIM ("…top-ten threat in every region"), not a topic label ("Threats").
- kicker: one line, ≤160 chars — the survey question, not background.
- question sidebar: verbatim survey question, ≤170 chars; base line ≤80 chars incl. n=.
- panel titles: region/segment names, ≤21 chars each (they clip around 26).
- category labels: ≤28 chars. "Uncertain economic growth" is the long case; longer needs wrapping — avoid.
- value labels: integer %, one per bar. Never show 2 decimals.

FILL (replace text + numbers, never geometry):
1. Swap kicker/title/`<div class="qbox">` texts (keep tag structure).
2. Per panel, edit the 6 value texts (e.g. "33%") and re-order their whole
   `<text>/<rect>/<text>` triples so each panel is SORTED DESC by value.
3. Re-size each bar: width = round(value × 3.36). If width ≥ 110, move the
   value INSIDE the bar end: `x = barX+width-6 text-anchor="end"` class
   `valin` (bold ink — never white); below 110 keep outside, class `val`/`valf`.
4. Focus category: keep class `barf` + `catf` + `valf` on the SAME category in every panel; others `bar`/`cat`.
5. To retarget the segment count: panels are 4×2; a 3×2 grid keeps panel x = 64/286/508. Don't invent a 5th column — width dies at ~205/panel.
6. Different accent: recolor `--accent` (+ `--accent-deep` for ink-weight text); bars, focus text and running head follow the tokens.

CHART RECIPE:
- Encoding: length = % share, ZERO baseline, all bars one fixed height (9px),
  sorted descending within each panel. Sorting is the device: readers see the
  #1 of every panel in the same position row-by-row.
- Scale: SHARED ABSOLUTE across all panels — width = v × 3.36 px, 50% ≈ full
  bar (168px). No axis ticks, no gridlines, no unit axis; value labels on the
  bars replace the entire y-axis logic (PwC practice: "negative-space bar
  labels"). If your max value > 50%, change the 3.36 factor to
  168/maxvalue (documented once in the header comment).
- Emphasis: exactly ONE category is the claim — accent #ED8B28 (PwC orange) in
  every panel; context bars a single gray #C9CED3. No color-per-category, no
  region tinting, no second hue. If you want a gray "ramp" (e.g. older cohorts
  lighter), alternate #C9CED3/#DDE1E4 only among context bars.
- Labels: value at bar end (inside when long, outside when short); category
  above the bar (this frees bar-end space — the PwC page itself uses
  left-rail labels; the above-bar variant is the legible-at-grid-scale choice
  and is stated so the swap is honest). Focus row: ink-bold category, deep-
  orange value; context rows: gray label, ink value.
- Panels: whitespace + two hairline dividers (255/510-ish x-lines per row),
  NOT boxes. Panel title names the segment; nothing else.
- Units: % only (or "share of respondents"); put n= and question in the
  sidebar/source, never on the canvas.

VERIFY:
- title ≤15 words / 2 lines, and it asserts the cross-panel pattern (one claim, eight panels).
- every panel sorted descending; one (and only one) accent color #ED8B28; focus category identical in all panels.
- value label on every bar; no axis line, no ticks, no legend (panels + labels are the legend).
- question sidebar present + source line bottom-left + "N | SECTION" bottom-right.
- inside-bar value labels use class `valin` = bold INK text (#1A1A1A) on the accent/gray bar fill — ink on #ED8B28 clears 4.5:1 (~5:1) and on gray #C9CED3 too; never white inside (ink-on-orange is the legible pick, and gray-bar-white is invisible on context bars).

DON'T:
- topic titles ("Regional threat rankings") — the title IS the finding.
- recoloring the #1 bar differently per panel — that breaks "same claim everywhere" and doubles the palette.
- legends, tick marks, 3D bars, shadows; kicker walls of text (one line max).
- unsorted panels or value labels inside short bars (gray-on-white ghost text).
- more than 8 panels; a 12-panel grid needs 160px panels and label death.

SOURCE: pwc_strategy__pwc_23rd_annual_global_ceo_survey_navigating_the_rising_tide
— Exhibit 6, deck p15/p17 (sw_sheets/…rising_tide_s01.jpg, sheet index
floor(17/10)=1); "Question sidebar / direct labels over legends / negative-
space bar labels / two-ranking bar forms" from reviews/pwc_strategy__pwc_23rd_
annual_global_ceo_survey_navigating_the_rising_tide.md §forms+§axis. Orange
hexes sampled from that review (#F08300/#ED8B28/#D93F00).
