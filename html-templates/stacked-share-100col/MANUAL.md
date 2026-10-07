# stacked-share-100col — 100% Stacked Columns with Segment Share Labels + pp-Shift Band

WHEN: An "everything-sums-to-100, how it moved" page: the composition of one whole (revenue,
budget, spend, time) across 3–4 periods or categories, shown as 100%-normalised stacked columns,
plus a right-hand band quantifying the shift in percentage points. Straight from Accenture,
2023 Post/Parcel Industry Trends p11 (three 100%-stacked columns 2007/2014/2021 + "+/−pp" stats
column) and the nbn-effect master (monochrome violet + grey stacks, legend chips, footer
contract). Pick this when the argument is *composition drift*, not levels — the reader compares
segment shares, never absolute sizes.

ANATOMY (1280×720 stage, coords from the CSS/SVG source):
1. kicker      — framing line, 64,34, 1152×20, 15px grey, one purple keyword phrase, sup marker
2. title       — claim title, 64,62, 1152 wide, 28px bold, 2-line slot (72rem)
3. rule        — hairline 64→1216 at y=138
4. chart       — full-bleed inline SVG 1280×720: baseline y=560 (96→660), 3 columns of width
                 108 at x = 132 / 320 / 508 (pitch 188), column band y = 200…560 (360px = 100%)
5. shift band  — right panel x 712→1216: caption y=196 + 5 rows centred on y = 232 + i×66,
                 each row = triangle (x 712–724) + pp numeral (x 730, 26px) + segment name
                 (x 830, 13px bold) + from→to (x 830, 11px grey); hairlines between rows
6. divider     — vertical hairline x=682, y 164→640, separating exhibit from band
7. legend      — 96,604, five 11px swatch chips, segment order = stack bottom→top
8. base note   — 96,628, 10px grey, the n=/indexing line ("indexed to 100 per column")
9. footer      — source bottom-left 64,~690 with sup; running head "11 | SECTION" bottom-right

SLOTS:
- kicker: ≤150 chars, one b-tagged keyword phrase max. Bad: three bolded phrases or a second
  sentence (that's a wall of text, not a kicker).
- title: ≤15 words, ≤2 lines at 28px/72rem. Must name the shift quantitatively ("Fallen 21
  Points", "Only Partly Offset"), not announce the topic ("Revenue mix").
- columns: 3 columns is the geometry as built (x-pitch 188 is tuned for that). 4 columns fits
  with pitch 155; ≥5 — use the bar variant (stacked-share-bars) or split pages.
- segments: 3–5 per column. 6+ bands make inside labels impossible below 6%; merge into "Other".
- inside labels: "57%" per band ≥6%. One label per band, never two, never a value outside the
  band if the band is ≥6% tall.
- external labels: for bands <6%, leader line + label outside column edge (one style, right side).
- shift band: 1 row per segment, order matches the stack (or rank by |pp|). Numeral = pp delta
  with explicit sign; from→to line repeats the endpoint shares. Rows: names ≤20 chars.
- legend: segment names ≤17 chars ("Financial services" is at the limit).
- base note: states the base (what, who, how indexed). A 100% stack without a base note is
  an unsourced claim.
- footer: source ≤110 chars + sup¹; running head = page number + ALL-CAPS section.

FILL:
1. Header comment holds the two arrays: `columns = [{label, segs:[5 values]}…]` and `shift`.
   Each `segs` must sum to exactly 100 (the template's last segment absorbs rounding; your
   numbers must not). For each column re-draw 5 rects: h = round(v×3.6), stack bottom-up from
   baseline y=560 (Mail) to top y=200 (Other), the TOP rect getting h = 360 − sum(others).
   Update the inside-label y per band: y = band_y + h/2 + 4. Geometry (x, widths, pitch)
   NEVER changes when swapping numbers.
2. Shift band: recompute delta = last − first per segment; sign decides class: `.num-pos` +
   `.tri-up` (accent) vs `.num-neg` + `.tri-dn` (grey). fromTo strings come straight from the
   first/last column values. Rows stay at y = 232 + i×66; edit only text + triangle direction.
3. Leader-label pattern (see 2007·Logistics 4%): line x1=column right edge, x2=+18, y = band
   centre; text at x2+4. One leader style only — leaders always exit right.
4. Recolour for another brand: set --accent/--accent-ink to the brand hue, then --seg-mail
   (deep), --seg-parcel (mid), --seg-log (light) as three lightness steps of that hue, and
   keep --seg-fin #B8B8B8 / --seg-oth #E6E6E6 grey. Nothing else changes.

CHART RECIPE (this is the page type — follow exactly):
- SCALE. 100%-normalised, linear, zero-based. Column band = 360px for 100% (1pp = 3.6px),
  baseline y=560, top y=200, fixed across all columns — every column is the same height by
  design; the whole point is that only segment boundaries move. Never scale a column to its
  "real" value (that's a different chart — a level stack).
- AXES. No y-axis line, no ticks, no gridlines — the inside labels ARE the scale. One dark
  baseline rule #333 1.6px under the columns; year/category labels centred below, 12px. No
  axis title; units live in the base note ("FY revenue, $B … indexed to 100 per column").
- STACK ORDER = BUSINESS LOGIC, held constant across columns: subject segment (the "hero"/
  displaced one) at the bottom reading bottom-up, residual "Other" always last (top). Same
  segment order in every column, legend, and shift band — re-ordering per column is a lie.
- VALUE-LABEL PLACEMENT.
  * band ≥ 6% (≥ ~22px tall): label inside, centred horizontally on the column, vertically
    centred (y = band_y + h/2 + 4).
  * white text on deep/mid accent fills (--seg-mail, --seg-parcel); NEAR-BLACK text on light
    tints and greys (.lbl-d). This is non-negotiable — white on #C9A6F2 or #B8B8B8 fails 4.5:1.
  * band < 6%: no inside text; leader line (grey #B8B8B8, 1px) out of the column's right edge
    + external "v%" (10px, bold, grey-ink). All sub-6% segments share this one style.
  * labels never stack: if two adjacent bands both sit at the inside/leader boundary, the
    smaller becomes a leader regardless of the 6% line.
- ONE ACCENT + GREY RAMP. Three lightness steps of ONE purple (deep #6E00C9 → mid #A45CF0 →
  light #C9A6F2) carry the "meaningful" series; greys #B8B8B8/#E6E6E6 carry the displaced
  series and the residual "Other". The chart has exactly one emphasis colour (purple family);
  grey is reserved for "the rest", never for decoration. Max 2 warm/other hues: none here.
- EMPHASIS RULES. Emphasis is *assigned*, not automatic: positive shifts get accent numerals
  (.num-pos/.tri-up), negative get grey (.num-neg/.tri-dn) — colour encodes direction, not
  importance. Do not repaint one band a second hue to "highlight" it; highlight via the title
  and the pp band. Lightness ≠ rank: ramp follows segment ORDER, not values.
- UNITS. Shares inside bands as integers + "%" ("17%", never 17.2%). Shift band numerals in
  percentage POINTS with explicit sign ("−21 pp") — pp, not %, and say so in the band caption.
  The from→to line repeats endpoint shares so the reader can re-derive the delta.
- ORDER. Columns left→right = time (oldest→newest) or the reader-facing sequence; never by
  size. Segments bottom→up = subject → support → residual, identical everywhere.

VERIFY:
- [ ] Claim title ≤15 words, ≤2 lines at 28px/72rem.
- [ ] Source line bottom-left; page + section running head bottom-right; sup markers where a
      methodology/base claim exists.
- [ ] Each column's segs array sums to 100 and the drawn rects close at y=200/560.
- [ ] Every band ≥6% labelled inside; every band <6% has one leader style (right edge only).
- [ ] Text on every fill clears 4.5:1 — white only on #6E00C9/#A45CF0; black on tints/greys.
- [ ] One emphasis hue (purple family) + greys; positive=n accent, negative=n grey.
- [ ] Shift band says "percentage points", numerals carry signs, from→to repeats endpoints.
- [ ] Zero network requests (grep http:// / https:// in the file = none).

DON'T:
- Two hues of equal weight (purple + teal "because the data is 5-segment") — the nbn master is
  one hue + grey, and the review's whole palette section says distinction rides on lightness.
- Level stacks (column heights ∝ value) masquerading as share stacks — this template is
  share-normalised by construction; levels belong in a different template.
- 10+ tiny segments with inside labels (corpus decks that squeeze "0.4%" onto a 1px band) —
  merge into Other or drop to the leader style.
- Shift band that duplicates the title (same sentence restated) — band = per-segment numbers,
  title = the argument.
- Topic titles ("REVENUE MIX, FY07–FY21") — genre, not argument.
- Decimals anywhere; legend colours unlabelled segments (every fill must match a chip).

SOURCE: firm = Accenture. Pages: p11 of accenture__accenture_2023_post_parcel_industry_trends_
2023 (100%-stacked columns 2007/2014/2021 + right "+/−%" shift stats), viewed from
sw_sheets/accenture__accenture_2023_post_parcel_industry_trends_2023_s01.jpg row 1 col 1 (sheet
index floor(11/10)=1, 5col×2row row-major); palette/footer/legend contract from p07 of
accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o…
(sw_sheets/…nbn…s00.jpg row 2) and its review
reviews/accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o.md
(Colour system: "semantic lightness mapping… grey = the opposition", NOTE/footer contract).
