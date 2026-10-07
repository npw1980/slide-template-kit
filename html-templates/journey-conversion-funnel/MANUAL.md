# journey-conversion-funnel — Stage Funnel with Retention Chips + Benchmark Rail

WHEN: A "where do people drop out" page — the same cohort followed through 3–5 journey
stages, with stage populations as proportional widths and a stage-to-stage retention number
on every gap. Straight from Accenture, *Accelerating global companies toward net zero by
2050*, p39 "G2000 SAMPLE" (a cascade of stage-definition boxes each carrying its own n=,
with the drop-off counts printed off the spine and one stage recoloured), plus catalog
funnel evidence S0018 / S0257 / S0266. Pick this when the argument is about **leakage**:
which stage is lost, how big the leak is, and whether it is worse than benchmark.

ANATOMY (1280×720 stage, coords from the CSS/SVG source; 1rem = 1 stage px):
1. kicker    — `14 | CUSTOMER JOURNEY — …` 64,34, 1152×20, 12px caps, page number + section
2. title     — claim title, 64,56, 1152 wide, 27px/35px bold, sup¹ marker
3. lead      — 64,102, 1152 wide, 13px bold, one b-tagged figure (accent)
4. funnel    — stage 1 rect x94,196 640×84 · stage 2 x334.5,300 159×84 ·
               stage 3 x392.5,404 43×84 (accent) · stage 4 x403.5,508 21×84.
               Centrefold x=414, dashed, 176→616. No ticks, no y-axis.
5. retention column — fixed x=512, one block per gap, text baselines 285/299, 389/403,
               493/507; arrow on the centrefold per gap (290/394/498 centres)
6. annotation — one block, accent tick-free, x100: title y430, body y448/462/476,
               leader line 300→390 with dot at the emphasized stage's bar
7. benchmark rail — divider x=766 (168→636); wash rect x786,168 430×468;
               rows: caption y214/324/434/544, numeral y252/362/472/582, delta y274/384/494/604;
               hairlines y292/404/514; gap-2 row has an accent wash x786,296 430×88
8. footnote  — inside the SVG, x94,y634, 9.5px — the stage-assignment rule
9. base      — 64,bottom52, 1152 wide, 10px — the population/base sentence
10. footer   — source line 64,bottom16 + sup²; running head "14 | JOURNEY" right,bottom16

SLOTS:
- kicker: page number + section only. Never a sentence.
- title: ≤15 words, ≤2 lines at 27px. Must name the lost stage or the leak size
  ("lost between consideration and trial"); a topic label ("THE FUNNEL") is wrong.
- lead: one sentence, ≤200 chars, exactly one b-tagged figure. It must not restate the title.
- stage names: ≤2 words each ("Awareness — reached" is the long form allowed). Names go
  inside bars of width ≥150, right of the bar otherwise (stages 3–4 here). Never rotate.
- stage value: 26px inside the bar if width ≥150, else right of the bar + 34px. Always
  thousands-separated, never abbreviated ("1,284,000" not "1.28M" — abbreviations hide
  the base you are arguing from).
- stage sub: one short qualifier ("24.8% of base", "1 in 31 reached adults"). ≤45 chars.
- retention chip: "24.8% retained" + loss line "−965,400 did not continue". Both lines
  live in the 20px gap at fixed x=512 — never inside the bars, never at variable x.
- rail row: caption ≤26 chars per leg ("awareness → consideration"), numeral = that gap's
  rate, name = "N moved forward", delta = "benchmark X% · ±Ypp — performing/the gap".
- base + source: present always. A funnel with no stated base is an unqualified claim.
- annotation: ONE per page max, ≤3 lines, must state a derived number, not a mood.

FILL (build a new page from this file):
1. Header comment carries the scale. The stage numbers live in the `<g>` blocks; the
   geometry is `w(i) = round(v(i)/v1*640)`, `x(i) = 414 − w(i)/2`, `y(i) = 196 + i*104`,
   `h = 84`. To swap data: replace the four `v` values, then rewrite each rect's
   `width` and `x` with the computed pair. Rect 1 is always 640 wide because stage 1 is
   the base (100%). Never edit `y`, `h`, or the pitch — 84/104 are furniture.
2. Retention: `retained(i) = v(i+1)/v(i)` as one decimal + "%"; loss = `v(i+1) − v(i)`
   with a unicode minus. Write both into the gap block (baselines gapcentre −5 / +9).
   The centrefold arrow is one `<line>` per gap with `marker-end="url(#drop)"`; the
   emphasized gap uses `stroke="var(--accent)"` and `marker-end="url(#dropA)"`.
3. Rail: for each gap add `benchmark − actual` in pp with an explicit sign, and pick
   the tail word: "the gap" (negative) or "performing" (positive/non-negative). The
   end-to-end row is `v(last)/v(1)`. Only ONE row gets the accent wash + `.hi` classes.
   If a gap's benchmark is genuinely unknown, print "benchmark n/a" and drop the delta —
   do not invent one.
4. Labels: after changing widths, re-check the inside/outside rule for every stage —
   inside if `width ≥ 150`, else right of the bar at `x(i)+w(i)+12` with 3 stacked
   lines (name / value / sub). A bar under 100px must not carry inside text.
5. Emphasis: exactly one stage keeps the `fill="var(--accent)"` rect. Everything else is
   grey fill or the single `--accent-1` tint. To move the argument, move the accent — do
   not add a second hue "to show the other stage".
6. Recolour: set `--accent` to the brand hue, keep `--accent-1` as one clear lightness of
   it, keep `--ink #051C2C` and the grey ramp (2D2D2D/464646/7D7D7D/DEDEDE) unchanged.
   Text on `--accent` must be white; text on `--accent-1` must be `--ink`/`--gray-1`.
7. Extra stages: 5 stages = pitch 84, y = 196 + i*84, and drop the annotation to a single
   line. 6+ stages belong on two pages, not a squeezed one.

CHART RECIPE (this is the page type — follow exactly):
- SCALE. Linear, zero-based, area-free. One encoding only: stage WIDTH = stage population,
  where 640px = stage 1's population (100%). 1% of base = 6.4px. Widths shrink monotonically
  by construction — a later stage drawn WIDER than its predecessor is a data error, and
  if the data genuinely grows, this template is the wrong tool (use the lanes-to-target
  template or a bar chart).
- AXES / UNITS. No y-axis, no ticks, no gridlines, no axis title — the widths plus the
  printed values ARE the scale, stated once in the header ("Stage volumes, unique
  respondents · linear, zero-based, width ∝ population"). Heights carry no number; say so
  in the small print below the funnel. Units are people; the base sentence states what a
  person is, the window, and the source. Percentages always name their base
  ("of base", "of considerers"), never a bare "%".
- VALUE-LABEL PLACEMENT. Inside the bar when width ≥150 (name / value / sub, left-aligned
  18px inside the bar's left edge). Right of the bar when narrower, 12px past the edge.
  Never centred on a bar you can't fill. Retention numbers live in the gap column at a
  fixed x — if you ever find yourself placing a chip inside a bar, the layout is broken.
- EMPHASIS RULES. One accent. The stage that carries the argument gets the accent fill AND
  the accent gap arrow AND the accent rail row — three coordinated mentions, one colour.
  Colour is assigned by argument, not by value: high does not mean dark. The single
  `--accent-1` tint may mark the stage adjacent to the emphasis (context), nothing else.
  Grey means "measured, not-argued-about". Never highlight with size, outline, or shadow.
- HONEST-SCALE GUARDS. (a) Stage 1 must be the largest by width — if not, you normalised
  to the wrong base; (b) all stages are the SAME cohort, so the base sentence must say
  "tracked forward, not four samples"; (c) the loss numbers must reconcile: sum of losses
  = v(1) − v(last) (1,284,000 − 41,900 = 1,242,100 here — write it into the base note if
  the page is scrutinised); (d) retention chips must equal the rail numerals exactly —
  same number, two places, never recomputed independently.
- ARITHMETIC OF THE RAIL. Every rail percentage is a ratio of two stage values; every
  delta is in percentage POINTS against a named benchmark, with the benchmark value
  printed next to it so the reader can subtract. If the benchmark is not comparable
  (different market, different window), it does not appear on this page.
- DROPOFFS. Every gap gets a chip — no silent gaps. A gap with no data is drawn with a
  grey dashed bar and "not measured", never with the funnel visually continuous.

VERIFY:
- [ ] Title ≤15 words, ≤2 lines at 27px, and it names a stage or a leak, not a topic.
- [ ] Source line bottom-left + "14 | JOURNEY" bottom-right + sup markers on title/source.
- [ ] Widths monotone; stage 1 = 640px wide; each width matches round(v/v1*640).
- [ ] Every gap has a chip; chips == rail numerals; losses reconcile to v(1) − v(last).
- [ ] Exactly one accent fill, one accent arrow, one accent rail row; all else grey + one tint.
- [ ] White text only on `--accent`; `--ink`/`--gray-1` text on `--accent-1` and greys.
- [ ] One annotation block, three lines max, containing a derived number.
- [ ] Base sentence present, says "tracked forward", gives n and fieldwork window.
- [ ] Zero network requests (grep for http:// / https:// in the file returns nothing).

DON'T:
- Ten-stage funnels with 12px bars and inside labels — the corpus decks that squeeze text
  into 1px bands. Beyond 5 stages, split pages.
- 3D funnels, perspective funnels, gradient-filled funnels (the source deck's violet→teal
  gradient is an editorial event, not a chart). No clipart people, no "funnel" icons.
- Topic titles ("THE CUSTOMER JOURNEY"), or a title that is a topic with a "so what" bolted on.
- Two emphasis colours ("lost stage" in blue, "benchmark" in red) — the red/blue pairing is
  the most common failure in this genre. One colour, greys carry the rest.
- Logarithmic or "visual" width scaling, or scaling width to the SQUARE of the value.
- Truncated stages: the funnel must not start at the "20% of base" point to make the shape
  look dramatic; stage 1 is always the full 640.
- Rail rows that restate the title as prose instead of printing the number.
- Percentages without a base, or "% of base" used where "% of considerers" is what's meant.

SOURCE: firm = Accenture. Page: p39 of *Accelerating global companies toward net zero by
2050* (`accenture__accenture_accelerating_global_companies_toward_net_zero_by_2`), read on
`sw_sheets/accenture__accenture_accelerating_global_companies_toward_net_zero_by_2_s03.jpg`
(sheet index floor(39/10)=3; 5col×2row row-major → page 39 = row 2, col 4). The page shows
"COMPANIES WITH SUFFICIENT DATA (n=1,394) → MODELLING & TARGET SAMPLE (n=827) → NET ZERO
SAMPLE (n=675) → LEADING COMPANIES (n=109)" as stacked definition boxes on a numeric spine,
with the excluded populations (156, 10) annotated off the spine and one stage recoloured
green — the deck's single-hue purple system analysed in
`reviews/accenture__accenture_accelerating_global_companies_toward_net_zero_by_2.md`
("single-hue system … one darker/lighter pairing … footnote/sample-size rigor"). The
funnel-to-target and callout-arrow variants are corroborated in the catalog rows S0018
(`corpus/sheets/sheet_002.jpg` frame 8), S0257 (`corpus/sheets/sheet_026.jpg`) and S0266
(`corpus/sheets/sheet_027.jpg`). The purple/violet palette was deliberately NOT ported
(one-emphasis-colour rule, DESIGN_PLAYBOOK line 57); palette here is the kit default.
