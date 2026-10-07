# survey-question-exhibit-battery-matrix — Question battery as a response matrix, bars-in-cells

WHEN: A battery (one stem, 5–7 statements, same response scale) is being reported.
One row per statement, one column per response option, and a bar *inside* every cell so
the reader can compare column widths without hunting for numbers. The right rail gives
the top-box and the prior-wave delta, so the row answers "so what" without a second
chart. From two firms' practice: Accenture's "percentage matrix tables with colored
column bars" (`accenture__accenture_2019_accenture_global_financial_services_consumer`
p23 lower half / p34 / p55) and PwC's claim-bearing figure caption over a bordered
action matrix (`pwc_strategy__pwc_navigating_the_payments_matrix_charting_a_course_amid_ev`
Figure 8, p20–p22).

ANATOMY (1280×720 stage; `html{font-size:min(100vw/1280,100vh/720)}` = 1rem per stage px):
1. question stem kicker — x 64, y 34, w 1152, 15px, 1–2 lines, sup 1
2. claim title — x 64, y 60, w 1152, 29px/700 Georgia serif, line-height 35, hard cap 70px (2 lines)
3. rule-top — y 146, 1px `--ink` at .85 (the firm prints a dark rule here, not a grey one)
4. assertive lead — x 64, y 158, 16px/700 `--accent-ink`, 1 line
5. figure caption — x 64, y 184, 14px serif "Figure N." + claim-bearing descriptor
6. column headers — y 198, 11px/700 grey, at each `colX`; rail head right at x 1100, w 116
7. header rule — y 212, full width
8. matrix body — row pitch 56, row i top edge = 228 + 56*i (i 0..5)
   statement block x 64 (item code y +16, statement y +34)
   response col j: `colX = 456 + 164*j` (j 0..3), track 156 wide at y +18 h 14,
   bar at y +22 h 6, width = value × 1.58 (158px = 100%), value text y +16
   right rail: circle pill centre (1130, +26) r 19; prior-wave value at x 1156 y +22;
   delta at x 1156 y +36
   row rule y +52; zebra band (`--band`) on rows 1, 3, 5
9. base line — x 64, y 592, 11px, sup 2 — "Base: … n = …"
10. methodology note — x 64, y 620, 11px, 2 lines (scale type + comparability)
11. footer — y 696: source left; `Number of responses`, `2 | SECTION` running head, bold page right

SLOTS:
- `kicker` (stem) — 150 chars / 2 lines. Good: the stem as asked, "Which of the following…" + sup.
  Bad: "Switching intent" (topic).
- `title` — ≤15 words / 2 lines. Good: a quantified limit ("65% would trade providers for a
  bundle — but only two services deep"). Bad: the survey objective restated.
- `lead` — 85 chars / 1 line: the recommendation, not another number.
- `figure-cap` — 70 chars. This is the PwC convention: the caption *is* allowed to carry the
  claim and is the honest place for "top-box and change since 2018".
- `rows[i].q` (5 chars) + `.text` (60 chars / 1 line at 13px in this slot). Good: the statement
  respondents rated, kept as asked. Bad: a summary rewrite — the code (Q12a…Q12f) does the labelling.
- `columns[j]` labels — 11 chars each. Copy them from the questionnaire verbatim; if the scale is
  "Definitely / Probably / Not really / Don't know", do not rename mid-deck.
- `rows[i].v` — 4 numbers; `rows[i].top` = v[0]+v[1]; `rows[i].y18` prior wave.
- `base-line` / `note` / `source-line` / `runhead` / `pageno` — required furniture.

FILL:
1. Text first: kicker, title, lead, caption, the 6 item codes + statements, column headers,
   base line, source. Caps above; the row slot fits exactly 2 text lines per row.
2. Cells: edit `rows[i].v` (the only source of truth). For every changed value re-derive:
   - bar `width = v * 1.58`, clamp 158; `x = colX(j)` never changes — bars always start
     at the column's left edge so one column is one shared 0–100 scale
   - value text `x = colX(j)`, `y = rowTop + 16` (already placed, only the digits change)
   - pill number = `v[0] + v[1]`; delta = `top - y18`, printed `+N` / `−N`
   - if a column is dropped (3-option scale), delete the whole `<g>`'s third track+bar pair
     and re-space columns: `colX = 456 + 218*j` with track 210 wide
3. Rows: 6 is the design (336px of body). 5 rows: end the body at 508 and let whitespace hold.
   7+ rows: this template is wrong — split to a second page or use a stacked-share template.
4. Prior wave: `y18` must be the *same question wording*. If the wording changed, delete the
   rail's prior value and print "n/c" (not comparable) in grey, and say so in note 2.
5. Recolour: `--accent` (bars col 1 + pill stroke). Columns 2–4 are `--gray-1`, `--gray-2`,
   `--gray-3` and must stay grey. To echo the firm's amber header band, set `--band`
   to `#F7A11D` for the header strip only — then keep all four bars on the grey ramp.
6. Fonts: the real PwC face is a Freight/Source-Serif class serif with Arial-ish body;
   Georgia/serif stands in for the display role, Arial stack for the table. Do not let the
   matrix go serif — digits need the sans stack to align.

CHART RECIPE:
- **Encoding.** Two encodings on purpose: the printed value (exact) and a bar inside the
  cell (relative magnitude). Every bar is anchored left on its column's x, so a column is
  a single 0–100% scale and cross-column comparison is only valid because the scale is
  shared. Cell width 156px ↔ 98.7pp of displayable range; 1.58px per pp.
- **Scale.** Linear 0–100% of respondents, no baseline truncation, no per-column scaling
  (that is the classic matrix failure: each column quietly normalised so everything looks equal).
- **Label placement.** Value label above its bar, left-aligned on the column edge, 12px;
  the first column's values bold in `--accent-ink` because that column is what the page argues.
  Never place values inside a 6px bar. Never centre-align — alignment on the column edge is
  what makes the matrix scannable.
- **One accent + grey ramp.** Column 1 = `--accent`; columns 2–4 = grey ramp, getting
  progressively lighter toward "Don't know", so the reader reads intensity not category colour.
  The right rail's pill and delta use the same accent. Total hue count: 1 (+greys).
- **Emphasis rules.** Emphasise a *column*, not scattered cells. If the finding is about one
  statement, invert that row's statement text to `--ink`+bold and leave everything else grey;
  do not add a fourth colour.
- **Axis / unit rules.** Unit is percent of respondents, integer, `%` on every value. The
  right rail prints raw points without `%` inside the pill and `vs. 2018` in the header so the
  comparison is labelled. Deltas between two top-boxes are **pp**. No secondary axis anywhere.
- **Rounding discipline.** Row values should sum to 100; if they sum to 99/101 that is a
  rounding artefact and note 1 must say so. Multiple-response batteries (select-all-that-apply)
  are allowed only if note 1 is replaced by "columns do not sum to 100 — multiple response".
- **Base rule.** Base line carries both the total n and the sub-base the row is filtered to;
  a matrix row computed on a different base must be footnoted per row, not averaged into the base line.

VERIFY:
- [ ] title ≤ 15 words / 2 lines; caption present above the exhibit (firm convention)
- [ ] source line bottom-left, running head + bold page number bottom-right
- [ ] one hue only: accent on col 1 + pill; cols 2–4 grey; no red/green/blue traffic-light shading
- [ ] contrast: `--accent` #D9105A on white = 5.0:1, safe for 11–12px bold text; grey 12px on white ok
- [ ] every row's `v` sums to 100 (or the note says why it cannot)
- [ ] base line names total n and the sub-base; prior-wave comparability addressed
- [ ] bars anchored left, no column quietly re-scaled

DON'T:
- Traffic-light green/amber/red fills — that is a dashboard, not a consulting exhibit, and it
  replaces the argument with a third hue.
- Per-column max-normalisation, which makes 17% look like 71%.
- A kicker wall: the stem is 2 lines, the rest belongs in the note.
- Topic title over the matrix while the caption does the arguing — the caption convention is
  PwC's, and here the title still has to carry the claim.
- More than 4 response columns in one matrix: merge the "neither" middle or split the battery.
- Printing a trend without saying whether the question is the same. Print "n/c" instead.
- Using SmartArt / a PowerPoint table shape with bars bolted on; this whole page is one SVG.

SOURCE: matrix device from `accenture__accenture_2019_accenture_global_financial_services_consumer`
p23 (lower half: the statement rows × persona columns with coloured column bars), also p34/p55
per `reviews/accenture__accenture_2019_accenture_global_financial_services_consumer_.md` line 37
("percentage matrix tables with colored column bars") — read on
`sw_sheets/accenture__accenture_2019_accenture_global_financial_services_consumer__s02.jpg`.
Caption / footer / serif-sans pairing and the bordered action matrix from
`pwc_strategy__pwc_navigating_the_payments_matrix_charting_a_course_amid_ev` Figure 8, p20–p22,
read on `sw_sheets/pwc_strategy__pwc_navigating_the_payments_matrix_charting_a_course_amid_ev_s02.jpg`;
convention and approximate hexes (`#E4146E` / `#D9105A`, `#F7A11D`, `#9AA0A6`) from
`reviews/pwc_strategy__pwc_navigating_the_payments_matrix_charting_a_course_amid_ev.md`
§4 colour system and §5 figure-caption/footnote rules ("Figure N:" captions above the chart,
"Source: PwC analysis", 6–7pt footnotes). Placeholder values are invented for the slot.
