# hbar-ranked — Ranked horizontal bars with end labels and question kicker

WHEN: A survey "which items matter / what are the challenges" page — one ranked horizontal-bar
series, sorted descending, percentage value labels at bar ends, with the question text as the
title kicker and a purple REMARKS bar carrying the takeaways. Comes from Accenture's survey-report
genre: `accenture__accenture_2021_p_c_underwriting_survey_2021` p16 (ranked bars + Q-kicker +
remarks bar) and `accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o` p10
(ranking bars with a right-hand annotation column). Use it when the argument is "X dominates the
ranking"; if you have before/after pairs use a paired-bars template instead, if you have ordinal
scale data use the likert-stack template.

ANATOMY: numbered slot map on the 1280×720 stage (stage px = rem in the file):

1. `kicker` — 64, 36 → 1152×20. Grey 15px question line with purple bold "Q2:" prefix and one
   purple highlighted keyword; sup 1 marker for the methodology note.
2. `title` — 64, 64 → 1152 wide, 2-line cap (72px). 28px bold display, −0.6 tracking, one number
   set in accent-ink.
3. `chart` — 298 → ~780 plot band, y 182 → 516. Baseline hairline at x=298 (the plot's only axis
   line). 8 row groups (`<g transform="translate(0, row*41)">`), bar 26px tall starting y=182.
   Category labels right-aligned at x=288, value labels 10px after the bar end (x = 308 + width).
4. `callout` — dashed yellow box 740→950 × 152→184, leader line down-left to the highlight bar tip.
5. `annot-rail` — 1030 (hairline) + notes from x=1042, y=200/282/364. Three notes max.
6. `legend` — 64, 556. One swatch + the response-type line ("multiple response …").
7. `remarks` — 64, 596 → 1152 wide × 66, deep-purple fill. Cap line (left 18), numbered list
   (left 150, 680 wide), response breakdown (right block 290).
8. `footer` — 64 → 1216, bottom 16. Source line left, n + page number right.

SLOTS:
- `title` → ≤15 words, ≤2 lines (box caps at 2 lines — a third line overflows and is the signal
  to cut). GOOD: a ranked claim with the number ("Systems and Analytics Gaps Dominate — 71% Rank
  Them as the Top Constraint"). BAD: topic label ("Underwriting challenges").
- `kicker` → one line ≤ ~150 chars. Good: the verbatim survey question + "select top 3" device.
  Bad: a second headline or a paragraph wall.
- `rows[]` → 6–10 rows work; >10 makes 41px pitch impossible (grow bar pitch, shrink label to
  10px). Keep descending sort — a rank chart out of order is two charts pretending to be one.
- `value labels` → 2–3 chars plus "%"; if a value is <~5%, put it OUTSIDE far enough that the
  text never sits on the bar.
- `remarks` → 2 numbered findings ≤ ~110 chars each + the n-breakdown. Bad: restating one bar.
- `annot-rail` → ≤3 one-liners. This is optional — delete the rail group entirely for a clean page.

FILL (step by step):
1. Replace the kicker text and the highlighted keyword inside `<b>`.
2. Replace the title. Keep the `71%` inside `<em>` — the number is the accent carrier.
3. Chart: edit the DATA ARRAY block in the file header (label, value, highlight flag). For each
   row group, change only three things: the `<text class="cat">` label, the `<rect>` `width`
   (= value × 5.5, rounded), and the value `<text>` string + its `x` (= 298 + width + 10). The
   `translate(0, row*41)` y-offsets never change. Keep rows sorted descending.
4. Highlighting: exactly ONE bar gets `class="bar hi"` (darker fill); all others stay `class="bar"`
   (mid purple). A second series you compare against (benchmark, overall, last year) renders as
   `class="bar ref"` — grey fill, same 26px lane split 12+14 or stacked under — never a new hue.
5. Callout: re-text `callout-tx` and move the `rect`/`path` together (leader endpoint at the bar tip:
   `x = 298 + width`, `y = row center`). Delete the whole group if there is no single-figure story.
6. Annotation rail: keep ≤3 notes; each must anchor to a specific row (draw a 4×1 tick if the note
   floats far from its bar).
7. Recoloring for a different accent: set `--accent: #A100FF-like mid`, `--accent-ink: deep`,
   keep `--gray-2` for reference series. Grey tokens (`--gray-1/2/3`, `--rule`) never change hue.
8. Footer: source line carries the survey instrument name + question number; `Number of responses`
   mirrors the remarks n. Page number right.

CHART RECIPE (the part that matters):
- **Scale**: linear, zero-based, 1 stage px per 1/5.5 of a percent (value × 5.5 = bar width px).
  Plot width 658px ≈ 119% headroom on the 100% value; if a value exceeds ~117% (rare, index scales)
  reduce the multiplier and say so in the caption. No gridlines, no tick labels — the value labels
  ARE the scale reading; a baseline hairline only.
- **Value-label placement**: always 10px beyond the bar end, outside, in bold ink. Inside-label
  only when the bar fills the plot and you have a reason (never here). Same font size for every
  label (11.4px) so no label looks more important than another — importance is encoded by bar length
  and the single highlighted bar only.
- **One accent + gray ramp**: the series is one hue (purple). Hierarchy: `--accent-ink` (darker) =
  the highlighted bar; `--accent` = every other bar; `--gray-2` (#B8B8B8) = any comparison/benchmark
  series or "non-focus" item. Never green/blue/red for the "what about the rest" bar — that's how
  survey decks end up with 5-hue charts.
- **Axis/unit rules**: percent of respondents, stated once (legend line), not repeated on a fake
  axis. If data is not percentages (days, USD), change the unit token in the label and the legend
  text, not the geometry; note non-summing multiples in footnote sup 1.
- **Emphasis**: exactly one yellow dashed callout allowed per page; the purple `sup 1` and the
  bold `71%` in the title must point at the SAME bar.

VERIFY:
- [ ] Title ≤15 words / 2 lines (the title box physically caps it — overflow = fail).
- [ ] Bars strictly descending; one and only one `bar hi`; any second series is grey.
- [ ] Value labels at bar end +10px, none inside bars, none overlapping the annotation rail (rail starts x=1030).
- [ ] One hue for the series (purple); yellow appears only as the dashed callout.
- [ ] Source line + "Number of responses" + page number present; n in remarks matches the footer.
- [ ] Text on the purple REMARKS bar: white 12.8px on #6E00C9 ≈ 7:1 ✓; do not lighten the bar fill.

DON'T (failure modes seen in the corpus):
- Topic titles ("Top 5 challenges") — that's the source deck's habit; the spec gate wants the claim.
- 10+ bars with 15px pitch — becomes a texture, not a ranking; bucket the tail into "Other".
- Adding a colored "benchmark" bar — grey or nothing (see one-accent rule).
- A legend that repeats the category labels the bars already carry.
- Left sidebar "TOP 5:" numbered wall + chart (the p16 device) — copy the remarks bar instead; the
  sidebar is the deck's cheapest habit, flagged in the review.
- Yellow fill (not dashed outline) behind multiple figures — yellow callouts are singular by design.

SOURCE: built from `sw_sheets/accenture__accenture_2021_p_c_underwriting_survey_2021_s01.jpg`
(row 2, cell 1 = p16; cell 3 = p18 shows the paired variant) and
`sw_sheets/accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o_s01.jpg`
(p10 = ranking bars with icon row + right growth-note column). Analyzed in
`reviews/accenture__accenture_2021_p_c_underwriting_survey_2021.md` (color system, remarks-bar
and question-kicker devices) and `reviews/accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o.md`
(palette hexes #6E00C9/#7B1FF0/#8E24EA/#E7D9F8, greys #7D7D7D/#B8B8B8). Fonts: the real deck runs
a Helvetica/Arial-family sans throughout — this template's stack is the honest substitute, not a
house face like Bower.
