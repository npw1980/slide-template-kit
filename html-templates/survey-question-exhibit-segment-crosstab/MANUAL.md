# survey-question-exhibit-segment-crosstab — One survey question, grouped bars by respondent segment

WHEN: A single survey question whose story is not "what people said" but *who
said it*. One answer option per group, one bar per respondent segment, so the
reader reads segment gaps and option preference in one pass. Straight from the
Accenture consumer-study house device: question verbatim in the kicker, claim
title, assertive coloured lead line, and small unframed series bars with a fixed
segment legend (`accenture__accenture_2019_accenture_global_financial_services_consumer`
p23 / p29).

ANATOMY (1280×720 stage; `html{font-size:min(100vw/1280,100vh/720)}` makes 1rem = 1 stage px):
1. question kicker — x 64, y 34, w 1152, 15px, grey `--gray-1`, 1–2 lines, sup marker
2. claim title — x 64, y 62, w 1152, 28px/700 display, line-height 34, hard cap 68px (2 lines)
3. rule-top — y 146, x 64→1216, 1px `--rule`
4. assertive lead line — x 64, y 158, 17px/700 `--accent-ink`, 1 line (the recommendation)
5. figure caption — x 64, y 184, 11px "Figure N." + neutral descriptor; legend on the same line, right-aligned
6. chart plot — x 110→1150, baseline y 532, 1 percentage point = 3px;
   group i left edge 136 + 260*i, bar k at +74*k, bar width 60, centre +30
   group centres 240 / 500 / 760 / 1020; option label lines y 552 and y 570;
   the "all respondents" value repeated under the axis at y 588 (class `grp-sub`)
7. methodology note — x 64, y 610, 11px, two lines, carries sup 1
8. footer — y 696: source line bottom-left; bottom-right `Number of responses = n`
   + `1 | SECTION` running head + bold page number

SLOTS:
- `kicker` (question text) — 155 chars / 2 lines. Good: the question as asked, with its
  scale named ("How interested…", "single choice"). Bad: a topic label like "Attitudes".
- `title` (claim) — ≤15 words / 2 lines at 28px. Good: a number + a contrast
  ("The 63% who want a bundle are already engaged — the rest mostly are not").
  Bad: "Attitudes towards bundling" (topic, no claim).
- `lead` (so-what) — 90 chars / 1 line. Good: an action the data supports. Bad: a restatement of the title.
- `figure-cap` — 60 chars. "Figure N." bold, then what is counted and how. Neutral, never a second claim.
- `options[i].label` — 2 lines × 26 chars. Good: the answer option as respondents saw it.
- `segments[k].name` + `n` — 14 chars + base. Every series must show its base.
- `source-line` / `runhead` / `pageno` — required furniture, see VERIFY.
- `note` — 2 lines max; states scale type, base, and how "all" is computed.

FILL:
1. Replace the kicker / title / lead / caption text nodes. Do not touch geometry if you
   respect the caps above.
2. Chart data lives in the header comment as `options` (4 options × `seg` of 3 values)
   and `segments` (names + n). Swap numbers there, then re-derive every drawn number:
   - bar rect: `height = seg*3`, `y = 532 - seg*3`
   - value label: same x as bar centre, `y = bar_y - 7`
   - dotted all-line: `y = 532 - 3*all`
   - delta chip: `seg[0] - all`, printed as `+N pp vs. all respondents`; chip box
     314–338, leader line down to the focus bar's top — keep the chip above the
     dashed 50% rule (y 382) so it is never mistaken for a reading on that line
   - if the option order changes, only the `grp` labels move with it (centres are fixed)
3. Segments: 3 is the design. For 2 segments widen bars to 96 and set the step to 116;
   for 4, drop bar width to 50 and step 60. Never run 5+ series in this template.
4. Recolour: set `--accent` / `--accent-ink`. Series 2 and 3 stay `--gray-1` / `--gray-2`
   — do not give them brand colours just because the source deck had four.
5. Fonts: the real Accenture face is the Accenture Sans family;
   `"Helvetica Neue", Arial, sans-serif` stands in for it, weight-driven hierarchy only.

CHART RECIPE:
- **Encoding.** Position on a shared 0 baseline: bars in a group differ only in which
  segment they represent; groups differ in answer option. Grouping is by option
  (not by segment) so the eye compares like-for-like across segments.
- **Scale.** Linear, 0–100% of respondents. 1pp = 3px; baseline y 532 is the zero and
  must be visible. Do not zoom the axis: a 15pp gap rendered on a truncated baseline is
  a lie. Ticks: 0 and 50 only, with one dashed `--gray-3` rule at 50; no gridline wall.
- **Value labels.** On/over the bars, centred, 12px, always with `%`. The focus series
  label is bold `--accent-ink`; other series labels are `--gray-1` bold — emphasis lives
  in the label as much as the fill. Drop a label when the bar is narrower than 9px
  (<3pp) rather than let it spill; print those values in the note or a small table.
- **One accent + grey ramp.** Exactly one hue on the page: series 1 = `--accent`,
  series 2 = `--gray-1`, series 3 = `--gray-2`, chrome/rules = `--rule`/`--gray-3`.
  The "all respondents" marker is a dotted grey line + a grey value under the axis —
  it is a reference, not a fourth series, so it must not get a fourth hue.
- **Axis / unit rules.** One unit: percent of respondents. Differences between two
  percentages are printed in **pp** (never "%" — "+15 pp" not "+15%"), signed. Percent
  signs appear on the first tick and in every value label; the axis title is rotated
  90° left. No secondary axis, no dual scale, no log scale.
- **Base discipline.** n for each series goes in the legend (not under the axis, which
  is already carrying 4 option labels × 2 lines); the total n goes in the footer.
  A cross-tab page without bases is not usable.
- **Sorting.** If the argument is "preference order", sort `options` by descending
  focus-segment value so the ramp reads as a ladder. If the argument is the gap, keep
  the questionnaire order and let the chip carry the finding.

VERIFY:
- [ ] claim title ≤ 15 words and lands in 2 lines (28px slot caps at 68px)
- [ ] source line present bottom-left with its sup marker
- [ ] exactly one hue + grey ramp (count: 1 accent, 3 greys, no other fills)
- [ ] accent text clears 4.5:1 on white (`--accent-ink` #5A0FB0 ≈ 9.9:1, `--accent` #7B1FF0 ≈ 6.4:1 —
      both clear it, but accent-size *text* should still take the -ink value for the title `em` and kicker)
- [ ] running head `N | SECTION` + bold page number bottom-right, and total n stated
- [ ] every `seg` array sums to 100; every bar was recomputed from the array, not nudged
- [ ] the delta chip says `pp`, and the dotted line is explained in the note

DON'T:
- Topic title with the claim parked in the body (the corpus's most common failure).
- Four series in four brand hues because the source deck persona-coded them; the kit is
  one hue + grey, persona colour-coding is an exception you may only make deck-wide.
- Legend without base sizes; chart-junk legend repeated on four pages in different colours.
- Gridlines every 10pp, drop shadows on bars, 3D extrusion, rounded bar tops.
- A kicker that becomes a paragraph — 2 lines max, the question, then stop.
- Writing "significant" without a stated test; write the gap in pp and let it argue.
- Reversing the meaning of grey: here grey is the *non-focus* population, nothing else.

SOURCE: `accenture__accenture_2019_accenture_global_financial_services_consumer`,
p23 (grouped persona columns + the percentage matrix under them) and p29 (grouped bars
under an "Engaging through personalization" question header), read on
`sw_sheets/accenture__accenture_2019_accenture_global_financial_services_consumer__s02.jpg`;
device and colour-system claims from `reviews/accenture__accenture_2019_accenture_global_financial_services_consumer_.md`
§Color system (line 31: violet + azure, persona code) and line 37/60 ("all charts are
small, unframed, label-heavy and persona-color-coded"; "Persona color legend fixed on
every chart"). Sibling precedent for the stage/scaling idiom: `hbar-likert`.
The placeholder values are invented for the slot and are not the deck's numbers.
