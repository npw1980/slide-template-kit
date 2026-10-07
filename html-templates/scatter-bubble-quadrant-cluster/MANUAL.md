# scatter-bubble-quadrant-cluster — Bubble scatter with shaded region and highlight callout

WHEN: A survey/telemetry page that plots categories of things on two continuous measures
(here: hours spent vs enjoyment share) where the argument is "most items sit here, one exception
sits there." One bubble per item, sized by a third variable (volume/base), a shaded region naming
the "quiet cluster", and exactly one solid-accent bubble with a callout for the exception. From
Accenture's nbn value report: `accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o`
p13 (enjoyment-% vs avg-hours bubble scatter with category legend, dashed "Time saving essentials"
box, 1-million reference circle, dashed callout with leader) — read from
`sw_sheets/accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o_s01.jpg` sheet
row 1; the region/callout devices recur across p08/p12/p22/p24 per
`reviews/accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o.md` (§signature
exhibits, §color system).

ANATOMY (numbered slot map, stage px on 1280×720; SVG user units are 1:1 with stage px):

1. `band` — 0,0 → 1280×104. Deep-violet gradient claim band. Title text sits at 64,16 → 1152
   wide, 25px bold, 2-line cap (max 66px), white.
2. `sub_kicker` — 64,118 → 1152×17. Bold violet panel line naming the exhibit.
3. `sub_line` — 64,139 → 1152×15. Grey line stating both axis units + the size encoding.
4. `rule_top` — 64,158 → 1152×1. Hairline separator.
5. `plot` — the SVG spans the whole stage; the figure itself lives at x 120→1152, y 236→600
   (1032×364). Domain: x = 0–17 hrs/wk (60.71 px per hour), y = 0–90 % (4.044 px per %).
   Gridlines every 10% / every 2 hrs; axis lines ink 1.5 on left + bottom only.
6. `region` — dashed rect 120,390.9 → 546×209 (hours 0–9 × pct 0–51.7), lavender fill + violet
   dashed stroke; label `region_label` inside bottom-left at 134,586.
7. `legend_cat` — inside plot upper-left, y 258: three 7px swatch+label chips (gray / tint /
   accent at cx 138 / 246 / 322).
8. `size_key` — empty band above the plot: reference circle r=7 (true scale, = 1 million) at
   1036,181 with "1 million" at 1049,185; two right-aligned caption lines at 1160,211/222.
9. `points` — 12 `<g data-series data-name data-hours data-pct data-millions>` groups, one
   circle each; 3 inline point labels (20px right of bubble center).
10. `callout` — white box 900,336 → 216×52, violet stroke 1.3, rounded 6; dashed leader
    `M1008 336 L 990 285` to the highlight bubble edge (bubble edge ≈ (990,285): center
    985.9,258.5 r 21.9). Two text lines: name + "84% enjoy · 14.2 hrs/wk".
11. `axis_x_title` — right-aligned 1152,641 bold violet. `axis_y_title` — rotated −90° at
    88,560.
12. `footer` — 64→1216, bottom 14: source+note line left, `13 | SURVEY FINDINGS` right.

SLOTS:
- `band_title` → ≤15 words / 2 lines. GOOD: a two-variable claim naming where both axes land
  ("Enjoyment tracks hours spent — but time-saving essentials cluster…"). BAD: "Enjoyment vs
  hours spent" (topic, not claim). The box physically caps at 2 lines — overflow means the title
  is wrong, not the box.
- `sub_line` → one line ≤ ~150 chars: both units + size encoding, each with its `sup` marker.
- `points[]` → 8–15 items; each is (hours, pct, millions). Under 8 the field reads empty; over
  ~18 bubbles start colliding with the fixed legends.
- `series` → 2–4 categories, mapped to gray / accent-lightness / accent. A 4th category reuses
  a gray lightness, never a new hue.
- `inline labels` → ≤3 (placeholders: Emails, Government services, Social media). They name the
  anchors the reader needs; labeling every bubble is chart-junk.
- `callout` → ≤2 lines, ≤ ~40 chars/line: the exception item + its two values.
- `region_label` → 1–3 words + the region rectangle is drawn from the two thresholds, not by eye.

FILL:
1. Title/kicker/subline: swap text; keep the `sup 1` markers; the highlighted word can carry a
   `<b>` (color stays ink inside the white band, violet only in the sub-kicker).
2. Points: edit the `data-*` attributes to your values, then set each circle's geometry with the
   three formulas — `cx = 120 + 60.71*hours`, `cy = 600 − 4.044*pct`, `r = 7*sqrt(millions)`.
   Recolor by series class: Essentials gray `var(--gray-1)`, Social `var(--tint)`, Entertainment
   `var(--accent)` (see tokens).
3. Region: `x=120`, `width = 60.71*h_limit`, `y = 600 − 4.044*p_limit`, `height = 40.9+y offset`
   — i.e. bottom-left corner of the plot to (h_limit, p_limit). The dashed stroke is fixed.
4. Callout: move the box so it does not cover any bubble; re-anchor the leader endpoint to
   `cx + r*0.72, cy − r*0.72` (a 45° edge point) of your highlight bubble. The highlight bubble
   itself: solid `var(--accent)` fill, `var(--accent-ink)` stroke 1.8 — change its class only
   here; every other bubble keeps its series fill.
5. Axis domains: if your hours max is not ~17, re-derive the px-per-unit constant
   (`1032/new_max`) and update tick labels + the gridline positions accordingly; keep tick
   spacing to integers for hours, multiples of 10 for percents.
6. Recolor: set `--accent` / `--accent-ink` / `--tint` to your brand hue triplet; `--gray-*`,
   `--rule`, `--zone-*` keep their roles and never change hue.

CHART RECIPE:
- **Scales.** Both axes linear, zero-based, domains chosen as a rounded headroom above the data
  max (here 17 hrs for a 14.2 max; 90% for an 85% max) so no bubble sits on the axis line. x:
  60.71 px/hr, plot 120→1152. y: 4.044 px/%, plot 236→600. Bubble radius: AREA-proportional,
  `r = 7*sqrt(millions)` — diameter-proportional bubbles visually lie by the square of the
  difference. Faint gridlines (gray at 30–35%) carry the reading; ticks carry the numbers.
- **Value-label placement.** No per-point value labels by default — position IS the value. Only
  named anchors (≤3) get inline labels, placed 20px to the right of the bubble center on its
  edge, format `Name 63% · 3.5 hrs/wk` (name ink, both figures bold). The exception item is
  labeled by the callout, never inline. Leader line: dashed gray 1.2px, from box edge to bubble
  edge — never crossing another bubble.
- **One accent + gray.** Exactly one hue (violet here) plus gray. Series hierarchy: gray =
  "the many / the rest" (Essentials), tint = same hue one lightness down (Social), accent =
  the focus category (Entertainment). The ONE solid-accent bubble with stroke is the page's
  emphasis carrier — if you emphasize an item that is not the callout's item, you have two
  stories. Nothing else gets the accent stroke.
- **Region rectangle.** The shaded rectangle is an argument ("these items form a cluster"), not
  decoration: state both thresholds via the rectangle's extent, label it inside bottom-left in
  bold gray (not accent), and give it a dashed stroke so it reads as annotation, not a data mark.
  One region per page.
- **Axis/unit rules.** Units live in the sub-line AND in both axis titles ("Avg. weekly hours
  spent¹"); tick numbers carry no unit suffix. Every methodology-dependent figure gets `¹`, and
  the footer NOTE line repeats what `¹` means. Percent axis is labeled in whole points; don't
  write "84%" at every tenth gridline.
- **Emphasis count:** one region, one callout, one inline-bold anchor set (≤3). A fourth device
  and the page stops being one argument.

VERIFY:
- [ ] Title ≤15 words, ≤2 lines (the band box caps it — overflow = fix the text, not the box).
- [ ] SOURCE line bottom-left with NOTE + `¹` marker; page stamp `NN | SECTION` bottom-right.
- [ ] Exactly one hue: violet family + gray ramp only (max 3 lightnesses); no green/blue/red.
- [ ] Exactly one solid-accent bubble; every other point is gray/tint/series-fill.
- [ ] Text contrast: ink on white ≥ 4.5:1; `--accent-ink` (#6E00C9) on white passes, `--accent`
      (#7B1FF0) is used for fills/labels ≥11px only.
- [ ] Bubbles inside plot bounds; nothing collides with size key / legend; no bubble on an axis.
- [ ] r follows `7*sqrt(m)` — spot-check two bubbles.

DON'T:
- Topic titles ("Enjoyment vs time spent") — the claim band demands a quantitative claim.
- Label every bubble, or use 4+ hues for "category colors" (corpus failure mode: 10-hue chart).
- Scale bubbles by value (diameter) instead of sqrt — a 4× base renders as 16× the area.
- Draw the region to look "roughly right" — its edges are data thresholds and must be computed.
- Use a red "warning" region or gradient-filled bubbles; the deck's language is violet + gray.
- Let legends drift into data territory: they live in the reserved bands (y<236 upper, inside
  upper-left for series), never over points.

SOURCE: `reviews/accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o.md` +
`sw_sheets/accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o_s01.jpg`
(sheet 2 row 3 = slide p13, cross-checked against p12/p22/p24 descriptions in the same review).
Firm fonts: Accenture GT/Eurostile-family custom; the `"Helvetica Neue", Arial` display stack
stands in for it; body stack is Arial (Calibri per deck) — see `TEMPLATE_SPEC.md` font clause.
Hexes #7B1FF0/#6E00C9/#C9A9E9/#7D7D7D taken from the review's color system, not invented.
