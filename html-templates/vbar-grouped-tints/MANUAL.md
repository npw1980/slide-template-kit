# vbar-grouped-tints — Clustered Vertical Columns, Grey Overall + Purple Tint Series

WHEN: A survey / cross-tab data page comparing one measured share across 5 categories and 5
respondent segments (line of business, account size, firmography). Straight from the
Accenture 2021 P&C Underwriting Survey clustered-column pages (p17, p18, p20 of
accenture__accenture_2021_p_c_underwriting_survey_2021, sheet s01 row 2 cols 2–5).
Pick this when the argument is "the same challenge, sliced by segment" — one chart,
one page, no combo charts (the deck's own multi-chart slides were rejected by its review).

ANATOMY (1280×720 stage, coords from the CSS/SVG source):
1. kicker   — question line, 64,36, 1040×20, 15px grey "Qn:" prefix + purple keyword
2. title    — claim title, 64,64, 1040 wide, 28px bold, 2-line slot (72rem)
3. chip     — cross-tab chip "By size of account", 64,36 right, purple fill white text
4. rule     — hairline 64→1216 at y=130
5. chart    — full-bleed inline SVG 1280×720; baseline y=490 (58→1222), 5 group slots
              of 230.4px starting x=58+78=136…1216 (bar x = group translate + 78 + s*42)
6. legend   — 64,568, five 11px swatch chips
7. REMARKS  — purple bar 64,596 1152×66, cap + numbered takeaways + n-breakdown rail
8. footer   — source bottom-left 64,704; "Number of responses = 434 | SECTION n" bottom-right

SLOTS:
- kicker: survey question verbatim is fine here (genre convention); ≤170 chars. Good:
  names the question + highlights ONE keyword phrase in purple. Bad: three bold keywords.
- title: ≤15 words, ≤2 lines, quantitative claim ("78% Rank Them First"), not a topic.
- chip: 1–4 words ("By size of account"). It labels the cross-tab dimension.
- groups: 5 category groups × 5 series is the layout's sweet spot. Bars 34px wide, 42px
  pitch. 5 categories max or labels collide; 4 series if buckets are wide (100-char rows).
- value labels: "47%" one per bar, centred above. 2–3 digits + % — never decimals.
- category labels: ≤34 chars/line, ≤2 lines, centred under group.
- REMARKS: 2 numbered findings max/line ≤95 chars; they must be *comparisons* (X vs Y),
  not chart restatements. n-rail: Total + bucket n=, right-aligned.
- legend: series names ≤14 chars.

FILL:
1. Replace the 5 `series:[…]` arrays in the header comment and re-draw: for each value v,
   bar height = round(v×3.1), y = 490−height. Only `<rect height/y>` + the matching
   `<text>` value label change. Geometry (x, widths, group translates) NEVER changes.
2. Move the callout `<rect class="callout-box">` onto whichever bar your finding flags —
   frame it exactly around bar+label (x≈bar x−4, y≈bar y−6, w=42, h=bar height+12). Max 2.
3. Title/kicker/remarks/footer text: plain HTML, lengths per SLOTS.
4. Re-tint for another brand: set --accent/--accent-ink to brand purple, then --s1..--s4
   to 4 lightness steps of it (lightest→darkest) and keep --s0 grey. Nothing else.

CHART RECIPE (this is the page type — follow exactly):
- SCALE. Linear, zero-based, vertical. height_px = value × 3.1 on the 1280×720 stage
  (100% ⇒ 310px, bars span baseline y=490 upward; chart top buffer y≈160 for labels).
  If data can exceed 100%, keep 3.1px/% and raise baseline, never truncate a bar.
- AXES. No y-axis line, no y ticks, no gridlines — the value labels above bars ARE the
  scale. One baseline rule: #333 1.6px stroke across the plot. No x-axis title; category
  labels sit centred under each group, 2 lines max, 11px.
- VALUE LABELS. Always. Centred horizontally over the bar's 34px column, 7px above bar
  top (text y = bar_y − 7). One emphasis label gets class .val.hi (bold). If two bars
  within a group would collide with their labels (>~3pt difference is fine, don't stack
  labels), it's the bars that are too narrow — fewer series, not smaller labels.
- ONE ACCENT + GREY RAMP. Series 1 "Overall" (or "All respondents") is GREY #B8B8B8 —
  grey is RESERVED for the reference, never for decoration. The segment series are ONE
  hue's four lightness steps (pale lavender → deep purple) ordered small→large bucket.
  The chart gets exactly one emphasis colour: the REMARKS-bar / chip / keyword purple.
  Yellow appears ONLY as the callout box (dashed #E0AA00, 14% fill) — the deck's own
  signature, used 2× per page max.
- EMPHASIS RULES. Darker tint ≠ better: ramp follows the bucket ORDER (size/order of
  category), never the values — otherwise the chart lies. The highlighted finding is
  flagged by a callout box, not by repainting a bar a second hue.
- UNITS. Percent share in the value label ("47%"); the n per segment goes in the n-rail
  of REMARKS, not on the axis. If values are not %, drop % and put units in the kicker.
- ORDER. Groups left→right = deck's question order or descending total — never random.

VERIFY:
- [ ] Claim title ≤15 words, ≤2 lines at 28px/72rem slot.
- [ ] Source line bottom-left; page + section bottom-right.
- [ ] Exactly one emphasis hue (purple family) + grey + yellow callouts — no rainbow.
- [ ] Grey series exists and is "Overall" (reference), not a random segment.
- [ ] Every bar has a value label; callout boxes ≤2.
- [ ] White text on the REMARKS purple passes 4.5:1 (it does at --accent-ink #6E00C9;
      do not lighten the bar below #7B1FF0 for white text).
- [ ] No y-axis, no gridlines, single baseline rule.
- [ ] Zero network requests (grep for http:// / https:// in the file = none).

DON'T:
- Rainbow segment palettes — the survey deck used grey/blue/red/green/cyan and its own
  review calls it "functional but off-palette and clashing". This template encodes the
  corrected rule: grey + ONE hue's ramp.
- Topic titles ("TOP 5 CHALLENGES" as in the source) — the genre does that, the kit doesn't.
- >2 callout boxes (the deck hits 4–5 per page on some slides; that's noise).
- Duplicating the takeaway in both REMARKS and the title — title states, REMARKS compares.
- Combo pages (column + donut + table on one slide) — the review says split.
- Decimals on labels (71% not 71.2%) — survey percentages read as integers.

SOURCE: firm = Accenture (2021 P&C Underwriting Survey, Oct 2021). Pages p17/p18/p20 of
accenture__accenture_2021_p_c_underwriting_survey_2021, viewed from
sw_sheets/accenture__accenture_2021_p_c_underwriting_survey_2021_s01.jpg row 2 (sheet
index floor(p/10)); the tint-scale + grey-for-Overall rule comes from
reviews/accenture__accenture_2021_p_c_underwriting_survey_2021.md (Colour + Copy sections:
"neutral grey reserved exclusively for Don't know / Overall", yellow dashed callouts as
the signature device). Delta-arrow cousin evidence: accenture_the_moneyball_moment… p11.
