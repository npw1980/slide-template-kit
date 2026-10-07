# stacked-share-bars — Horizontal 100% Stacked Bars by Respondent Group, Callout Rail + n-Breakdown

WHEN: A "profile of each respondent group" page: one horizontal 100% stack per group (by size,
segment, firmography), so the reader compares *mix*, never counts. Straight from the Accenture
2021 P&C Underwriting Survey "profile by segment" pages (p8/p9, sheet s00; cross-tab variant
p15) rendered in the nbn-effect lightness-token palette. Pick this when the argument is "the
same question, but whose book is built differently" — groups down the left, mix across. It
replaces the deck's donut+stack pairing on those pages, which the deck's own review says should
be split.

ANATOMY (1280×720 stage, coords from the CSS/SVG source):
1. kicker     — survey question line, 64,34, 1152×20, 15px grey, ONE purple keyword phrase + sup
2. title      — claim title, 64,62, 1152 wide, 28px bold, 2-line slot (72rem)
3. rule       — hairline 64→1216 at y=138
4. legend     — 350,162, five 11px swatch chips, aligned to the bar start
5. chart      — full-bleed inline SVG 1280×720: 4 rows of 100%-wide stacked bars
                x = 350…1090 (740px = 100%), row i y = 196 + i×70, bar height 44;
                row labels x = 64 (name 13.5px + sub line 10px) left of each bar
6. callout rail — dashed rects around the two compared segments (right edges at x 986 / 992
                etc) + rail path M 1090,midY → 1150 → 428 → back to 1090 + pill (1108,305,
                100×34): ratio numeral 15px + from→to 9px
7. REMARKS bar — 64,474, 1152×66, deep-purple: REMARKS cap + 2 numbered takeaways + n-rail right
8. base note  — 64,552, 10px grey: what the 100% is of + normalisation rule, sup marker
9. footer     — source bottom-left 64,~690; running head "9 | SECTION" bottom-right

SLOTS:
- kicker: survey question verbatim is fine (genre convention); ≤170 chars, ONE bolded phrase,
  never two. The sup must resolve to a methodology note in the source line.
- title: ≤15 words, ≤2 lines at 28px/72rem. Quantitative comparison ("Five-Fold from Large to
  Emerging", "Portfolio Depth Follows Scale"), not a topic ("PREMIUM MIX BY SIZE").
- rows: 4 rows is the geometry as built (y = 196 + i×70 tuned for it). 5 rows fit with pitch 60;
  ≥6 — switch to 3 rows + a second exhibit, never squash labels onto 45px pitch.
- row label: name ≤10 chars (Large/Mid/Small/Emerging), sub line "metric range · n = value"
  ≤22 chars. Exactly ONE row name takes the emphasis class (.rowname.hi) — the comparator.
- segments: 3–5 per row. "Other" always last (residual), grey. If a row needs 6 segments, one
  merges into Other.
- value labels: integer % per band. ≥44px wide → centred inside (26px baseline); <44px → leader
  10px straight UP from the bar's top edge + "v%" 4px above the leader. One style per case.
- callout rail: exactly ONE per page. Compares the focus segment across the two extreme rows;
  pill shows ratio (5.4×) + endpoints (28% → 5%).
- REMARKS: 2 findings max, ≤95 chars each, must be *comparisons* across rows, not chart
  restatement. n-rail: Total + per-row n.
- legend: series names ≤15 chars; chip order = stack order.

FILL:
1. Header comment holds `rows` (name/sub/n/segs) and `segments`. For each row: segment width =
   round(v×7.4), last segment = 740 − sum(previous) so the bar closes at x=1090; x accumulates
   left→right from 350 in segment order. Update each inside/external label to match. Geometry
   (bar y per row, 350→1090 span) NEVER changes when swapping numbers.
2. Inside-label y = rowY + 26 (215/285/355/425 patterns as built: name at rowY+19, n-line rowY+34).
   A band < 44px: swap the inside <text> for the leader pattern: line (segCentreX, rowY) up 10px,
   text 4px above. Leaders exit ONLY upward.
3. Callout rail: re-anchor the two dashed rects on the focus segment in the compared rows
   (rect = segment rect grown +10px x / +8px w / +12px h), keep rail path to x=1150, update pill
   text (ratio = value1/value2 one decimal, endpoints). Delete the whole rail block if the page
   makes no segment-comparison argument.
4. Title/kicker/remarks/base-note/footer: plain HTML, lengths per SLOTS.
5. Recolour for another brand: --accent/--accent-ink to brand hue; --seg-per/--seg-com/--seg-spe
   to three lightness steps of it (lightest→deepest, deepest = focus segment); keep --seg-rei
   #B8B8B8 and --seg-oth #E6E6E6 grey. Nothing else changes.

CHART RECIPE (this is the page type — follow exactly):
- SCALE. Each row is its OWN 100% bar: width_px = value × 7.4 on the 740px span (100% ⇒ 740,
  1% ⇒ 7.4). Zero-based, linear. Rows share the same x-span so equal shares align in columns —
  the eye reads mix, not length. Never scale to group size (n changes are in the n-rail).
- AXES. No x-axis, no ticks, no gridlines — inside labels ARE the scale. No y-axis line: row
  labels + one hairline REMARKS bar do the framing. Units are stated once (base note), never
  repeated per bar. If shares aren't %, drop "%" and put units in the kicker.
- VALUE-LABEL PLACEMENT (the part data people get wrong — swap numbers, obey these):
  * band ≥ 44px wide (≥ ~6%): text centred in the band, y = rowY + 26.
  * band < 44px: NO inside text (it would touch the white stack seams) — leader line straight
    up from the bar's top edge, label above it. Never label sideways, never angle, never stack
    two labels in one band.
  * colour of text follows the fill: WHITE on deep/mid accent fills only (#6E00C9, #A45CF0);
    NEAR-BLACK #1A1A1A on light tint and grey fills (#C9A6F2, #B8B8B8, #E6E6E6). White-on-
    grey fails 4.5:1 and is the single most common regression in the corpus.
  * a value appearing in ≥2 rows is labelled every time it appears — consistency beats cleverness.
- ONE ACCENT + GREY RAMP. Segment fills = one hue's lightness steps (deep = the focus segment
  under discussion) + grey for Reinsurance/Other ("the rest"). Exactly one emphasis colour;
  the dashed rail + pill use that SAME accent, never a second hue (no red flags, no yellow
  boxes here). Grey is reserved, never decorative.
- EMPHASIS RULES. The argument lives in the RAIL, not in repainting: one dashed rail, two
  dashed segment boxes, ratio pill. Emphasis row name is one .hi class. Do not bold the
  biggest number, do not add a second colour, do not frame more than two segments.
- ORDER. Segments left→right = fixed segment order (subject segment, support, residual), same
  in legend. Rows = natural ranking (largest→smallest, premium→emerging); NEVER sorted by any
  one segment's value — that hides the mix story and the x-spans stop lining up.
- N. Per-row n goes in the row sub line AND the REMARKS n-rail; the base note states
  normalisation ("each group normalised to 100% of its own NWP"). An unstated n on a profile
  page is an unsourced claim.

VERIFY:
- [ ] Claim title ≤15 words, ≤2 lines at 28px/72rem.
- [ ] Source line bottom-left; running head bottom-right; sup markers on kicker/source.
- [ ] Every row's segs sum to 100 and bars draw 350→1090.
- [ ] All labels: inside ≥44px, leader <44px; text colour matches fill rule; 4.5:1 holds.
- [ ] Exactly one dashed callout rail + one ratio pill; one .hi row name.
- [ ] One emphasis hue (accent family) + greys only — no rainbow, no second hue for flags.
- [ ] REMARKS ≤2 findings, both cross-row comparisons; n-rail present (Total + rows).
- [ ] Zero network requests (grep http:// / https:// in the file = none).

DON'T:
- Pairing this exhibit with a donut/pie on the same page (the survey deck does; its review says
  split) — one stack page = one argument.
- Sorting rows by a single segment's share — kills the equal-x-span comparison.
- "100%" bars with unequal widths, decimals, or inside labels on <44px bands touching seams.
- Labelling every segment twice (inside AND a right-hand list) or legend colouring that doesn't
  match the chip order.
- Rainbow segment palettes — corpus decks shipped blue/red/green/purple; the corrected rule the
  review endorses is one hue + grey.
- >1 callout rail or a second highlight colour (yellow boxes belong to the clustered-bar template,
  not this one).

SOURCE: firm = Accenture. Pages p8/p9 (profile by segment) and p15 (cross-tab stacks) of
accenture__accenture_2021_p_c_underwriting_survey_2021, viewed from
sw_sheets/accenture__accenture_2021_p_c_underwriting_survey_2021_s00.jpg (sheet index floor(p/10)=0,
5col×2row row-major) and s01 for p15; palette, footer contract and "grey reserved for the
reference series" rule from
reviews/accenture__accenture_2021_p_c_underwriting_survey_2021.md +
reviews/accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o.md
(monochrome lightness tokens, NOTE/SOURCE footer).
