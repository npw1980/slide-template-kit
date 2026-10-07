# hbar-likert — 100% stacked Likert bars with top-two-box aggregates

WHEN: A survey page reporting "how important is X" — one full-width stacked horizontal bar per
statement/attribute, the ordinal scale encoded as a dark-to-pale purple tint ramp, grey reserved
for "don't know / not applicable", and the two-box aggregate (Important + Very important) circled
in the right column. Evidence: `accenture__accenture_2021_p_c_underwriting_survey_2021` p19 / p28
(purple 5-step ordinal scale + grey-for-neutral + circled top-box callouts, the deck's signature
device on p19/28/40/45/46/49/52/54). Use it for agreement / importance / satisfaction scales across
3–6 statements; a single-series ranking goes in `hbar-ranked` instead.

ANATOMY: numbered slot map on the 1280×720 stage (stage px = rem in the file):

1. `kicker` — 64, 36 → 1152×20. Grey question line, purple bold "Q3:" device + one highlighted
   keyword, sup 1 for the scale note.
2. `title` — 64, 64 → 1152 wide, 2-line cap (72px). 28px bold claim with one number in accent.
3. `chart` — 356 → 996 stack zone (100% = 640px), y 196 → 458. Rows are
   `<g transform="translate(0, row*58)">`, bars 30px tall. Category labels right-aligned x=346
   (2 lines allowed), segment % labels inside (≥8% rule).
4. `pill column` — 1107 → 1173, one 66×28 rounded outline pill per row starting y = 197 + row*58
   (the top-two-box figure), header caption "Important + Very important" at y=176.
5. `axis` — hairline y=470 with ticks 0 / 50 / 100% at x 356 / 676 / 996 (labels y=488, italic
   caption "share of respondents" y=504). No gridlines.
6. `legend` — 64, 528 → single row of six swatches (5 tints + grey DK), 11px grey.
7. `note` — 64, 566 → methodology line carrying sup 1 (scale + rounding rule).
8. `footer` — source line left; `Number of responses` + page number right.

SLOTS:
- `title` → ≤15 words / 2 lines, box-capped. GOOD: names the two leading factors and the aggregate
  number ("Quality and Service Speed Lead the Investment Agenda for 96% of Underwriters"). BAD:
  "Factors driving investment" (topic).
- `rows[]` → 3–6 statements is ideal (5 at pitch 58; 6 still fits, 7+ is crowded). Each label
  ≤48 chars per line, ≤2 lines. Row order = argument order (leading factor first, or reverse if
  building down to the outlier) — not alphabetical.
- `seg[]` → six floats summing to 100 (1 dp allowed). Zero values: omit the rect entirely (a zero
  rect with a stroke is a hairline artifact).
- `topline` → seg[0]+seg[1] to the stated rounding; the pill must equal the sum of the two darkest
  segments ON THE BAR, not an independently computed figure with different rounding.
- `note` → ≤2 lines, the methodology claim (scale + aggregation rule) with sup 1 — this is what
  makes the circled numbers defensible.

FILL (step by step):
1. Replace kicker + title (keep the number inside `<em>`).
2. Chart: edit the DATA ARRAY block in the file header. For each row group:
   - category `<text class="cat">`: text (and `<tspan>` line 2 if needed).
   - segment rects: for value v in seg, width = v × 6.4; x = 356 + 6.4 × (sum of prior segments).
     Segment order is fixed: seg-a (very imp), seg-b (imp), seg-c, seg-d, seg-e, seg-x (DK grey).
   - segment labels: keep only where width ≥ 51px (≈8%); class `seg-lb` (white text) on seg-a/b,
     `seg-lt` (ink) on seg-c/d/e/x.
   - pill: `<text>` value only — geometry (x 1107–1173, y row*58+197) never changes.
3. Add/remove rows: copy one `<g>`, change only the translate `row*58` multiplier; pitch 58 keeps
   186px of clearance under the axis for legend/note/footer.
4. Grey rule: grey `seg-x` appears ONLY for don't-know/non-response. If a question has none, omit
   all seg-x rects but keep the legend entry (the scale still includes the option).
5. Recolor: to shift the hue family, retoken `--s1..--s5` as a dark→pale ramp of ONE hue
   (keep s1/s2 luminance gap ≥35 L*), and keep `--gray-dk` grey — grey is semantic, never themeable
   into the accent family.
6. Footer/note: source names the survey + question number; n in the footer = n in the note.

CHART RECIPE (the part that matters):
- **Scale**: 100% stacked, zero-based, one row per statement, no row sorting by value (the ordering
  is rhetorical). Total width 640px = 100%, so value→geometry is `w = v × 6.4` and `x = 356 + 6.4 ×
  cumulative_before`. No axis gridlines — one hairline + 0/50/100 ticks is the entire axis.
- **Encoding = tint, not hue**: five levels of one purple run dark→pale in ordinal order
  (#4B0E8F → #8E24EA → #C9A2F4 → #E7D9F8 → #F4EEFC). The ramp must be readable as a grayscale
  ladder too (it is) — colorblind-safe by luminance, so no pattern fallback is needed. Pale levels
  4/5 get a #D9D9D9 hairline stroke so they don't dissolve into white.
- **Grey semantics**: #B8B8B8 = don't know / not applicable. Nothing else renders grey. Any
  comparison series goes in another stacked bar with the same ramp (e.g. "by line of business" —
  see source p15), never in a new hue.
- **Value labels**: inside the segment, centered, bold 11.5px — white on s1/s2 (both clear 4.5:1
  on their fills), ink on s3/s4/s5/grey. Label a segment only when its bar width ≥51px (≈8%);
  smaller segments stay unlabeled — the pill + legend carry them. Never label across a segment edge.
- **Aggregate pills**: outline 66×28, stroke `--accent` 1.8px, number bold `--accent-ink` —
  the ONLY outline device on the page; it must equal seg[0]+seg[1]. One header caption above the
  column replaces a per-row repeated phrase.
- **Axis/unit rules**: percent of respondents is stated once (axis caption + note); if the unit
  changes to "minutes/week per respondent", drop the stacking (100% stacks are a % device) — pick
  hbar-ranked with absolute bars instead.
- **Emphasis**: exactly one device per page. Here it is the pill column; do NOT add yellow
  callouts on top (the ranked template owns the yellow device).

VERIFY:
- [ ] Title ≤15 words / 2 lines (box caps at 72px — overflow = fail).
- [ ] Each row's segments sum to 100 (sum the floats; a 99 or 101 sum means wrong data or the
      rounding note is wrong).
- [ ] Each pill = seg[0]+seg[1] of its own row.
- [ ] Five purple tints + grey only — no other hue anywhere; grey appears only on DK segments.
- [ ] Segment labels only on ≥51px segments; white text only on s1/s2 (contrast ≥4.5:1).
- [ ] Axis hairline present, no gridlines; legend + note + source + page number present.

DON'T (failure modes seen in the corpus):
- 10+ hues / rainbow segment sets — this genre's #1 failure; the whole point is 1 hue + grey.
- Grey used for "the rest" of a comparison series — grey is exclusively don't-know/non-response.
- Segment labels under 8% — creates micro-text overlap; that's why the pill exists.
- Sorting rows by topline blindly — the ordering should follow the argument (and the source deck's
  convention: leading factor on top).
- Repeating "Important + Very important" as text on every row — the pill column + one caption does
  that job once.
- 3D, rounded, or gradient segments; stacked-bar outlines as separators (white hairline strokes
  only) — anything heavier reads as chart-junk.

SOURCE: `sw_sheets/accenture__accenture_2021_p_c_underwriting_survey_2021_s01.jpg` (row 2, cell 4
= p19: stacked Likert bars with circled 96%/93% top-box callouts, legend below; p15 in the same
sheet shows the by-segment stacked variant). Analyzed in
`reviews/accenture__accenture_2021_p_c_underwriting_survey_2021.md` (ordinal purple tint scale,
grey-for-neutral semantic rule, circled callouts as signature device) with palette hexes confirmed
against `reviews/accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o.md`
(#4B0E8F/#6E00C9/#8E24EA/#E7D9F8/#B8B8B8/#7D7D7D). Fonts: source deck is a Helvetica/Arial-family
sans throughout — the stack here is the honest substitute.
