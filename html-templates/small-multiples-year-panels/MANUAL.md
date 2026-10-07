# small-multiples-year-panels — 2×3 grid of annual column panels, current-year emphasis

WHEN: A multi-year "what changed" story told per segment with the SAME four
years repeated in every panel — the KPMG Pulse-of-Fintech grid, where the
current year (accent) versus history bars (gray ramp) is itself the argument.
Evidence: kpmg__kpmg_pulse_of_fintech_h1_21_2021 p07/p12 — "annual
small-multiples 2×3 grids (2018–2021) ... the same exhibit set — a template,
not bespoke"; "Current-year 2021 bars purple against history bars — a clear
what-changed device". Use it when the claim is about ONE year's deviation
across many segments; if years are the comparison (one metric, many years),
use one chart, not six.

ANATOMY (1280×720 stage, all coords px):
1. kicker — (64, 38) w960: question/method line, bold lead + footnote marks.
2. title — (64, 63) w1000, 28px/35px display, 2-line slot; `em` = operative clause.
3. shared legend — (64, 142): ONE key for all six panels: 3 gray swatches + accent swatch.
4. chart layer — SVG overlay; panel title x = 72/462/852, metric sub-line below;
   row1 baseline y=384, row2 baseline y=644; columns w=56 at panelX+30/+114/+198/+282.
5. zero lines — 1px axis rule across each panel baseline (196→384 / 456→644 zones).
6. delta chip — ONE pill max, above the claim panel's current-year column (here (354,556) in Asia-Pacific).
7. source — (64, 692) w1000; page number (1216, 692) "07 | GLOBAL".

SLOTS:
- title: ≤15 words / 2 lines, quantitative claim with the deviation inside ("2021 outpaces every prior year, but the rebound is concentrated in venture and M&A"). Topic titles fail the gate.
- kicker: ≤170 chars; must state unit ($bn) and vintage. No background paragraphs.
- panel titles: ≤21 chars ("Middle East & Africa" is the long case). Sub-line names the metric + unit, ≤26 chars.
- year labels: fixed 2018–2021 — if your window is different (5 years), drop columns evenly, never rotate labels.
- value labels: one decimal, on EVERY column top, label baseline = barTop−6. Never on alternating bars.
- delta chip: max ~11 chars ("2.4× 2018"); ONE per page, on the panel that carries the title claim.

FILL (replace text + numbers, never geometry):
1. Swap kicker/title/legend/source/page texts.
2. Edit the 6×4 value texts. Recompute every column: height = round(v × 150 / PAGE_MAX)
   where PAGE_MAX = the largest value across all six panels (the tallest
   column is exactly 150px). Bars sit y = baseline − height; baselines: 384
   (row 1), 644 (row 2). If the new max shrinks/changes, keep 150 as full
   height and keep the factor consistent — never rescale per panel.
3. Current year = last column: keep class `bc` + value class `vc`; history keeps `b0/b1/b2` (oldest→lightest gray).
4. Move the delta chip if the claim panel changes (pill y = current-year barTop − 28); delete it if no ratio is claimable.
5. Retargeting segments: grid stays 2×3 (≤6 panels). A 4th column of panels needs 88px panels — do not.
6. Different brand: recolor `--accent` (current-year) + `--accent-deep`; the three grays are ramp tokens, adjust lightness order, don't add hues.

CHART RECIPE:
- Encoding: column height = value in $bn, ZERO baseline mandatory (the axis
  rule is drawn on every panel — this is the fixed KPMG weakness, keep it).
- Scale: ONE SHARED height scale across all six panels: 150px per PAGE_MAX.
  Shared scale is what makes "2021 is big everywhere" legible; per-panel
  normalization is the #1 lie available in this layout — if a value exceeds
  150px the layout is wrong (raise PAGE_MAX or trim the panel set, don't
  squeeze one panel).
- Axis: no y-ticks anywhere. Values printed on bar tops carry the scale
  (values-on-bars convention from the review). Years on the baseline, 10.5px
  gray. Unit appears once per panel sub-line + in the kicker — never as a
  vertical unit axis.
- Emphasis / one-accent rule: the current-year column is --accent #90278E
  (KPMG purple; deck used purple-vs-navy — this build converts history to
  the gray ramp so exactly ONE hue exists on the canvas). History columns
  gray ramp ordered by recency: 2018 #D1D3D4 → 2019 #B7BBC0 → 2020 #9CA1A6.
  All value emphasis text --accent-deep; history labels gray ink. Nothing
  else takes color: no per-region fills, no trend line, no second series.
- Labels: 1 decimal, right-aligned over each column, single consistent
  placement (barTop−6); bold 11.5px for current year, 10.5px gray for history.
  No rotated labels, no decimal commas vs points mixing.
- Grid furniture: hairline dividers between panel cells (#E4E5E7), not boxes;
  panel title + metric sub-line at top-left of each cell; whitespace carries
  separation.
- Units: money ($bn/$M — one per page), years integer. Negative values would
  extend below the baseline rule with the label below; not shown — flag if
  your data goes negative.

VERIFY:
- title ≤15 words / 2 lines and it names the deviation (which year, what changed).
- exactly ONE hue (purple) + gray ramp; current year accent in ALL panels.
- shared scale: tallest column anywhere = 150px; eyeball cross-panel (M&A 2021 vs Global venture 2021 ratio = 43.8/38.9 ≈ 1.12× height).
- zero-line rule drawn on all 6 baselines; values on every column (≤6 ×4 here); ONE legend row, not six.
- ONE delta chip max; source bottom-left with n=/basis; "N | SECTION" bottom-right; title gate passes.
- contrast: value labels gray-ink #58595B on white ≈ 7:1; white pill text on #5A1758 > 4.5:1.

DON'T:
- per-panel scaling ("looks more comparable") — destroys the cross-panel claim.
- legends repeated inside each subplot (the corpus weakness), 3D columns, rounded bars, gradient fills.
- topic titles ("Fintech deal value by region") — that is a caption, not a claim.
- second series per panel (dual-axis) — one metric per panel or split into two grids.
- more than one delta chip (everything becomes "important", so nothing is).

SOURCE: kpmg__kpmg_pulse_of_fintech_h1_21_2021 — p07/p12 (sw_sheets/
kpmg__kpmg_pulse_of_fintech_h1_21_2021_s00.jpg, sheet index floor(7/10)=0);
2×3 grid, current-year accent, values-on-bars, shared-legend fix and purple
#90278E / gray #D1D3D4 / ink #58595B anchors from
reviews/kpmg__kpmg_pulse_of_fintech_h1_21_2021.md §charts/§palette.
