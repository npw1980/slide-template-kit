# framework-named-option-scorecard — Option Comparison Scorecard (1280×720)

WHEN: Decision page that closes the "which option, why" question: every candidate laid down as a
row, scored on Risk / Benefits / Cost, each row carrying an explicit verdict — the option-comparison
table, the device consulting teams actually ship when a recommendation needs to survive a council/
board room. From Deloitte "Town of Tillsonburg IT Strategic Review" p15 (`reviews/deloitte__…upd.md`
§devices #4: "the deck's strongest single device"), with scorecard-table density discipline from
PwC Annual Report 2017-18 p26. For narrative option prose instead of a scored grid, use a
content-action-title page, not this.

ANATOMY (slot map, stage px; `1rem = 1 stage px` via the html rule):
1. `kicker` — x64 y36, 12/1 bold uppercase ls .15em, `07 | Options appraisal` (numeral in accent).
2. `title` — x64 y58, width 1152, 30/38 bold navy, 2-line box: the RECOMMENDATION as a claim, not "Option Analysis".
3. `lead` — x64 y106, 13/18 bold one line naming the scoring basis + `<sup>1</sup>` methodology marker.
4. `table` — x64 y158, width 1152, table-layout fixed. Column widths live on the `<col>` elements:
   opt 300 / risk 104 / ben 302 / cost 288 / dec 158 — the five numbers ARE the frame; change
   them there, nowhere else.
   4a. `thead` — navy (var(--ink)) band, white 11/1 bold caps ls .10em, height ~37. One `<th>` per column.
   4b. `tbody tr` — 4 rows × 110px, zebra: even rows `--gray-6`, bottom hairline `--rule` per row.
5. per row: `opt-lead` (12 bold + circle number badge 16px) + `opt-note` (10.5/14 gray, 1-2 lines);
   `pill` in the risk column (9.5 bold caps, the gray ramp as the scale); `cell-text` in benefits
   and cost (10.5/14.5 gray-1); `dec-text` (11 bold) + `dec-fine` (9.5 regular) in the verdict column.
6. `tr.reco` — the recommended row: accent 4px left-border on its `td.dec` + verdict text in accent.
   This is the ONLY place the accent appears inside the table.
7. `foot-src` x64 bottom, 9.5 gray-3 with method strings + dates + `<sup>1`; `foot-page` bottom-right `07 | OPERATING MODEL`.

SLOTS:
- `title`: the verdict sentence — ≤15 words / ≤2 lines. Good: "Fully in-house IT is the recommended
  operating model". Bad: "Option Comparison" / "Options Analysis" (topic title — the whole point of the page vanishes).
- `opt-lead`: option name ≤34 chars, noun phrase ("County contract + governance"); `opt-note`: one line of mechanism, ≤110 chars.
- `pill`: exactly one of Low / Moderate / High per row per rated column — same word list everywhere.
  Dark fill = High, mid = Moderate, light = Low; never fill by decoration, never "Low/Moderate".
- `cell-text`: benefits and cost must each carry a NUMBER or a named mechanism (61% of volume,
  $1.4M/yr, 3-yr commitment, single-source exposure). Two full lines is the expected worst-case
  fill — the layout is built for it; do not "help" by shortening to bullet fragments.
- `dec-text` / `dec-fine`: verdict (2-4 words: Recommended / Fallback / Not viable / Not short-term)
  + one fine line giving the condition or date ("Revisit at FY30 county contract renewal"). A verdict
  without a condition line invites "why not?" as the only question.
- 3-5 rows is the discipline; 4 is comfortable. Under 3 the comparison isn't a decision.

FILL:
1. Replace text nodes column-first: opt-lead/opt-note, pill word (see 5), cell-text, dec-text/dec-fine. No coordinates move.
2. REMOVE A ROW: delete one whole `<tr>…</tr>`; nothing reflows (row heights are fixed `tr{height:110rem}`),
   remaining rows keep their zebra because it's `:nth-child(even)` — check parity flips and just accept
   the stripe change or reorder.
3. ADD A ROW: copy any `<tr>` block, change the badge number and all five cells' text. Then (a) set the
   `tr{height}` down from 110rem so 410+110n stays under the footer (table must end above y≈664):
   5 rows → ~98rem, 6 rows → ~86rem; (b) if text starts clipping, drop `.cell-text`/`.opt-note`
   10.5rem → 10rem before touching widths; (c) more than 6 rows is past the device's honest limit —
   move to a `data-appendix` page with a "see appendix" verdict.
4. ADD A SCORING DIMENSION (e.g. "Time to implement"): add `<th>` + one `<td class cell-text/pill>` per
   row, add a `<col>` and re-width the five `<col>` rules so they still sum to 1152rem (shave benefits
   and cost first — prose columns tolerate 240/250 more than option/decision do). The `td.dec`
   left-border of `tr.reco` is a column boundary, not a divider — keep the verdict column last.
5. Accent for a different brand: change `--accent` only (e.g. PwC red #D60A2C). The rating ramp is
   grays by design (see RECIPE) so it survives any accent swap.
6. Zebra/stripes: automatic via `:nth-child` — do not add inline classes to rows except `reco`.

CHART RECIPE (table encoding rules):
- The rating scale is encoded as GRAYS (light `#F1F3F5` → mid `#C9CFD4` → dark `#464646`, white text
  on dark = 8.6:1): Deloitte's semantic traffic-light fills reproduced hue-cheap. The single accent
  is spent entirely on the recommendation (verdict text + 4px bar), so the reader's eye lands on
  "which row wins" in under a second.
- Option column is the reading spine: numbered badge + bold lead, so rows survive being quoted as
  "option 2" in the room.
- Verdict column is visually separated by its left border line (and the accent bar on the chosen row)
  — the table always ends with a decision, never with "and the client decides".
- Header band: ink fill, white caps — same banding device as the deck's other boxed tables (p6/p8).

VERIFY:
- [ ] Title ≤15 words / ≤2 lines and IS the recommendation (the placeholder is 8 words).
- [ ] Every row has exactly one rating per rated column, same word list, ramp fills correct (dark=High).
- [ ] Accent only on recommended row; contrast white-on-gray-2 8.6:1, accent-on-white 6.3:1.
- [ ] ≤5 rows, table bottom above the footer rule; no cell clipping.
- [ ] Source line with method + dates + sup marker; running head `NN | SECTION` bottom-right.
- [ ] Two hues total: ink navy + one accent, everything else grays.

DON'T: topic titles; RAG fills painted as decoration on cells that aren't ratings; hedged ratings
("Low/Moderate"); verdict-less tables ("for discussion" rows); 10+ rows (that's an appendix, not a
decision page); arrows or shading connecting rows (the table speaks by adjacency, not flow); an
accent left-painted onto non-recommended rows — one winner, one accent bar.

SOURCE: Deloitte Town of Tillsonburg IT strategic review p15 — image read in
`sw_sheets/deloitte__deloitte_town_of_tillsonburg_it_strategic_review_council_upd_s01.jpg`
(floor(15/10)=1, row-major 5×2, p15 = row 1 col 5); analyzed in
`reviews/deloitte__deloitte_town_of_tillsonburg_it_strategic_review_council_upd.md` §devices
(#4 option-comparison table, color-coded ratings) and §palette (navy band dominant, RAG as
semantic-only). Row-level density / bold-figure discipline cross-cited to PwC AR2017-18 p26 —
`sw_sheets/pwc_strategy__pwc_pwc_annual_report_2018_s02.jpg` (floor(25/10)=2; note cell offset:
the sheet's row-1 col-5 cell renders p25, p26 lands one cell later — read there) and
`reviews/pwc_strategy__pwc_pwc_annual_report_2018.md` §color/§type. Fonts: Deloitte GT America /
PwC house colophon faces unlicensed here — Helvetica Neue / Arial stacks stand in (noted per spec).
