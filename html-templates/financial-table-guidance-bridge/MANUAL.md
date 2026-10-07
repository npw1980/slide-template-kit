# financial-table-guidance-bridge — Prior vs. current guidance table with change pills

WHEN: A page that reports guidance (or a plan) TWICE — an old number and the
current one — and the exhibit's whole job is to show what moved on each
financial measure. For investor-update pages, mid-plan revisions, "we raised
guidance" moments, and P&L / KPI re-forecasts where the ranges and the
qualifiers matter more than a curve. Extracted from the Accenture Investor &
Analyst Conference 2022 deck, p11 "Continued Strong Momentum" (sheet
`sw_sheets/accenture__accenture_accenture_investor_analyst_conference_2022_s01.jpg`,
pages p11-p20, p11 = row 2 col 2), with the same highlighted-column device on
p17 of that deck; `reviews/accenture__accenture_accenture_investor_analyst_conference_2022.md`
line 21 calls this "the deck's core device" (4 occurrences) and line 18 gives
the colour semantics (purple = own figures, gray = comparator, box = the
number to remember).

Distinct from `financial-table-step-up`: that template has ONE derived
last-column difference (per-cell magenta boxes); THIS one compares two dated
guidance vintages side by side and encodes the change as a per-row pill
(▲ / ▼ / unchanged), with the current column framed by one tall panel.

ANATOMY (1280×720 stage, `rem` = 1 stage px; one inline SVG viewBox 0 0 1280
720, 1 user unit = 1 px):
1. title (claim, violet, no kicker) — x64 y48, 1152×76, 30px regular display
2. claim-sub (what the comparison is + markers) — x64 y118, 1152×22, 16px gray
3. header captions — two lines y166/y184, centered over each column
   (prior center x666, panel center x952, pill center x1158)
4. emphasis panel — rect x832 w240 y140 h386 rx4, violet 8% fill + violet
   stroke: the CURRENT column is highlighted as a column, not cell by cell
5. prior column — x520→x816, values right-anchored x792; hairline under its
   header x520→x816 at y200 (neutral gray, since the panel frames its side)
6. current column — values right-anchored x1030, bold `--ink`, inside the panel
7. detail sub-lines — same anchor as their value, baseline +18, 11px gray
   (max 3 of 5 rows; where a qualifier is genuinely needed)
8. change pills — rect x1112 w84 h24 rx12 at row baseline−17, text centered
   x1158 11.5px (▲ tinted/stroked violet; unchanged = gray fill, no glyph)
9. data rows — 5 rows, pitch 60px, first baseline y240; row i =
   `<g transform="translate(0, 60*i)">`; panel + captions live outside them
10. footnote block — x64 bottom:56, 10.5px, ≤2 paragraphs with ¹ ² markers
11. source line — x64 bottom:24, 11px; running head + page number bottom-right

SLOTS:
- `title` — ≤15 words / 2 lines. Names what moved and what did NOT
  ("FY26 guidance raised on four of five measures; cash generation is held").
  A flat "Guidance update" wastes the page's whole comparison.
- `claim-sub` — ≤130 chars: both vintages with their dates + the delta
  definition marker. It states the comparison basis so the reader cannot
  assume "same plan".
- `rows[].label` — ≤32 chars. Exactly ONE row is bold + ink (the measure the
  delta commentary names); all others stay `--ink-soft`.
- `rows[].prior` / `rows[].now` — range strings "x to y" in words, or
  "At least $x" for minimums. Same precision both sides. Never mix a point
  value against a range on one row.
- `rows[].detail` — optional qualifier under the current value, ≤38 chars
  ("21% to 23% adjusted YoY growth"). ≤3 rows.
- `rows[].delta.dir` — "up" | "down" | "flat". "flat" is a result, not an
  omission: keep the pill gray so "unchanged" is visible rather than silent.
- `rows[].delta.txt` — the computed change with unit ("+4 pts", "+20 bps",
  "+6.7%", "+$0.8B", "unchanged"). 8 chars/1 line — it must fit the 84px pill.
- `footnotes` — ≤2 paragraphs: guidance basis (ranges are mid-points or
  minimums) + non-GAAP definitions.
- `source-line` — ≤170 chars: which call/filing/plan, plus who computed the change.

FILL:
1. Replace `title` then `claim-sub`. The title drives which row gets bolded —
   if it names a measure, that row is `bold:true`.
2. Swap the four value strings per row. Coordinates never change; if a string
   is longer than the column, shorten the wording ("At least" → "≥" is NOT
   allowed here — spell the qualifier, it is the honest-uncertainty device) or
   move to "x to y" with 1-decimal precision.
3. Recompute every pill from the mid-points of the two ranges
   (`(x+y)/2` both sides) so the change is checkable on the page. Sign, unit
   per row, direction → the pill style table in the header comment.
4. Row count: pitch is 60px from baseline 240; a 6th row is `translate(0,300)`
   and the panel `height` becomes 386+60=446 (bottom 586 — check it clears the
   footnotes at ~y604). >6 rows: the comparison is a table, not a bridge.
5. Detail sub-lines: only where a qualifier exists; delete both `<text>` for
   the row if not needed. Never a sub-line on every row.
6. Colours: `--accent`/`--accent-mid`/`--accent-tint` move together for another
   firm (KPMG: #0F2E8C / #16419E / #EAF1FD; Deloitte: #0F7B5F / #17997A /
   #E6F5F1). Keep the panel fill light enough that bold `--ink` numerals stay
   ≥7:1 on it.

CHART RECIPE:
- Not a chart: two closed scales side by side. The comparison is
  position (row) × vintage (column) + the pill. No connectors, no arrows
  across the page, no waterfall — the delta lives in one small place.
- Scales: the columns are NOT plotted, so "axis rules" here are precision and
  alignment rules: ranges print "x to y" in words, right-anchored so the two
  vintages align on their right edge and the eye reads the range, not the
  slope. A point value is printed with the same decimal count as its partner.
- Value-label placement: value on the value line, qualifier on the line below
  and one step lighter, so no cell repeats the number. The panel's right edge
  is the visual "current" boundary — do not put the pill inside the panel.
- Units: stated once per row in the label or in the value string (bps vs pts
  is a real distinction — never collapse "bps" into "%"). "At least" is
  spelled out: the qualifier is data.
- One accent + gray ramp: violet does the panel, its captions, the "up" pill.
  Gray does everything else, including the flat pill, which MUST be gray so
  the unchanged rows read as deliberately held, not forgotten. `--highlight`
  (magenta) is deliberately unused in this template: with a panel already
  marking the current column, a second filled colour is a third emphasis.
- Emphasis rules: one bold row + one panel + one pill per row. Never bold two
  rows, never box a second column, never colour a pill green/red — direction
  is a glyph plus the sign, not a new hue.
- Change derivation is footnoted (mid-point to mid-point), so a reader can
  redo it. Ranges are not subtracted as ranges; minimums are not averaged.

VERIFY:
- [ ] title ≤15 words, ≤2 lines at stage width (MBB gate); names moved + held
- [ ] both vintages dated in `claim-sub` (an undated comparison is a fabrication)
- [ ] source line bottom-left, page number bottom-right
- [ ] one emphasis hue family: violet panel/pills + gray ramp, no third hue
- [ ] bold `--ink` numerals on the panel fill clear 4.5:1 (they pass ≥7:1 here)
- [ ] every pill value = mid-point(prior) → mid-point(current) with correct sign
- [ ] exactly one bold row; unchanged rows shown as gray pills, not blank cells
- [ ] all ranges in "x to y" words; qualifiers spelled; precision matches per row

DON'T:
- Green/red up-down colouring (introduces a fourth hue and a trading-desk
  register the kit does not use).
- Silent "no change" cells: an omitted pill looks like missing data. Print the
  gray "unchanged" pill.
- Detail sub-lines on every row — a wall of qualifiers kills the comparison.
- Arrow glyphs inside the value cells, connector lines, or arrows spanning the
  table (those belong to waterfall/bridge templates).
- Topic titles ("2026 guidance overview") or an "FY26 vs FY25" mislabel —
  these are two vintages of the SAME fiscal year, not two years.
- Mixing point values with ranges on the same row, or "x–y" en-dash ranges
  (read as subtraction).
- Re-plotting the same numbers as a line chart below the table: the table IS
  the exhibit, and this page's argument is the revision.

SOURCE: `accenture__accenture_accenture_investor_analyst_conference_2022`,
slide p11 ("Continued Strong Momentum") extracted from
`sw_sheets/accenture__accenture_accenture_investor_analyst_conference_2022_s01.jpg`
(5-col × 2-row sheet, p11 = row 2 col 2), with the sibling device on p17 of the
same deck; analysed in
`reviews/accenture__accenture_accenture_investor_analyst_conference_2022.md`
(architecture §1, palette semantics line 18, footnote/footer discipline line
12). The review lists no hexes, so token values come from pixels sampled in
the p2/p11 render crops (violet ≈ rgb(147,116,192), numerals ≈ rgb(16,22,38))
and are deepened for the white stage — the source deck's silver-gradient
ground is replaced by white, a documented deviation. Real fonts in the source
deck: Accenture House grotesque, single family in three registers; the
Helvetica Neue/Arial stacks stand in (no webfonts allowed).
