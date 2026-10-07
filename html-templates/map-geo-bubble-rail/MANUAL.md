# map-geo-bubble-rail — Proportional-symbol world map + ranked region rail

WHEN: A geographic claim whose argument is "region X is the outlier". The map
proves WHERE, the rail proves HOW MUCH — same array, two encodings. From
pwc_strategy `five global shifts reshaping the world` p21 ("Megatrends: Social
instability"): balloon markers per region with label + one-decimal % at the
marker, ranked list beside them on one evidence band. Companion pattern:
pwc_copernicus_market_report_2019 p14 (map + charts sharing one band).

ANATOMY (1280×720 stage; SVG layer is also stage coords):
1 kicker   64,38 w1050 — base/definition line with footnote marker
2 title    64,63 w940 — 2-line action claim, ≤15 words, em-clause in accent-deep
3 band     64..1216 × 150..610 — light evidence band; vertical divider x744
4 map      64..716 × 210..463 — ocean fill + schematic continents + graticule + frame
5 markers  #markers — one <circle data-*> per region (data array in index.html header)
6 labels   value % under each bubble; focus bubble gets "Name · 24.7%" above
7 legend   10/20/25 size-key at ~100..286 × 570
8 rail     760..1184, rows 194..610 pitch 51 — rank digit, name, right-aligned value, bar w=16v
9 source   64,681 w1020 — ILOstat-style source + footnote expansion
10 pageno  right:64, top:681 — page | SECTION, page digit in accent-deep

SLOTS:
- title: action title = a quantitative claim ("tops 20% only in North Africa"),
  not a topic. 2 lines max, 26px display, ≤15 words. Overflow = resize slot, never the text.
- kicker: one base-definition sentence, one footnote marker. A wall of kicker text kills the page.
- region labels: full display names, not ISO codes; "&" kept literal. 8 regions is the rail's practical max.
- source: methodology must say the base (annual average, weighting, exclusions) — map claims get challenged.
- pageno: "NN | SECTION" — uppercase section, real page number.

FILL:
1. Edit the `markers` array in the index.html header comment — one row per region:
   `lat`, `lon`, `v`. Recompute every dependent (index.html documents both):
   cx = 64 + (lon+180)/360*652 ; cy = 210 + (80−lat)/140*253 ; r = round(4.83×√v), floor 6.
2. Update the 8 `<circle>` rows in #markers (cx/cy/r + data-label/data-v). Keep the
   `class="m-focus"` circle as the focus region; other markers stay flat gray.
3. Sort rail rows DESC by v. Each row: rank digit (1,2,3...), name, value at
   text-anchor="end" x=1184, bar `width = round(v×16.0)`. If a new max value
   breaks 400px, re-derive the multiplier: 400/vmax.
4. Bubble labels: value under bubble at cy + r + 12 (the focus keeps "Name · v%"
   above at cy − r − 4).
5. Replace `<g id="map-geometry">` paths with real map SVG — Natural Earth or any
   equirectangular-cropped export fits this frame; if your geometry is in a
   different projection, edit only the transform comment, don't touch markers.
6. Different accent: set --accent + --accent-deep (contrast of white/ink text on
   the focus bubble must clear 4.5:1 — keep accent-deep for text).
7. Footnote: keep `<sup>1</sup>` in kicker + its expansion in the source line.

CHART RECIPE:
- Two views, ONE dataset: the map (geography, area-proportional) and the rail
  (rank, length) must carry identical values — the reader cross-checks, and any
  mismatch destroys both exhibits. Sort rail DESC; ties broken alphabetically.
- Scales: area-proportional circles, r = 4.83×√v (≈ 10% → 15px, 25% → 24px).
  Area-proportional means radii for close values look alike; that is honest.
  The rail is the precision reader — if someone asks for exact read-off, point
  to the rail bars (16px/%). Never scale bubbles by diameter (2× values would
  read as 4×).
- Value labels: printed AT the marker (under the bubble), one per circle,
  always "d.d%" (one decimal — integers imply false precision on aggregates).
  Bubble name ABOVE only for the focus marker, to keep the map label-quiet.
- Emphasis: ONE region in --accent (the claim subject), everything else flat
  gray #8A939C (map) / #C9CED3 (bars) — one hue + gray ramp, no ramps across
  geographies, no "highlight the second one too".
- Bars: flat #C9CED3, no gradient, no stroke, right-aligned one-decimal value;
  no gridlines, no bar axis — rank + labels carry it. The rail header is the
  only uppercase label.
- Map hygiene: graticule + frame = declared projection (the map says what
  "positioned by" means); continents gray (context), ocean flat; no country
  outlines, no shadows, no satellite imagery. Legend size-key shows 10/20/25%
  so the scale is readable without math.
- Map is not the argument: the map shows where the values are high; the rail
  states the ranking. If you can't write it that way, you don't have a chart —
  you have a poster.

VERIFY:
- [ ] title ≤15 words, renders ≤2 lines (26px/33px on 940px)
- [ ] kicker + source present; methodology footnote expanded in source line
- [ ] ONE accent hue; grays otherwise; text-on-accent ≥4.5:1 (accent-deep used for text)
- [ ] map markers and rail rows show identical values, one decimal
- [ ] rail sorted descending; rank digits contiguous; no bar wider than 400px
- [ ] page number + SECTION running head present, bottom-right
- [ ] zero network requests (check devtools network = empty except the file itself)

DON'T:
- Topic titles ("Youth unemployment across regions") — the claim must be in the title.
- Coloring "the other one" (Africa AND the Middle East both accent) — one focus.
- Diameter-proportional bubbles (2× reads as 4×), blue-rainbow choropleth, choropleth + bubbles stacked.
- Chart-junk legend: a "Bubble size = rate" caption with no reference circles; a key per series.
- Label walls: every bubble with its name; value labels inside small bubbles.
- Kicker walls of text; kicker is one base line.
- "1 | SECTION" running head misused as nav — this is a content page.
- A map with more than ~10 markers becomes a dot-wall; bucket the rest into "Other".
- Rasterizing the map to a PNG — markers stop being editable data.

SOURCE: pwc_strategy__pwc_five_global_shifts_reshaping_the_world_we_live_in_2022 —
read p21 on sw_sheets/pwc_strategy__pwc_five_global_shifts_reshaping_the_world_we_live_in_2022_s02.jpg
(row 1 frame 1); pattern confirmed against pwc_strategy__pwc_copernicus_market_report_2019 p14
(same sheet s01). Palette (orange accent on gray ramp, evidence band, graticule map)
per reviews/pwc_strategy__pwc_five_global_shifts_reshaping_the_world_we_live_in_2022.md
and the kit playbook. Font stand-in: PwC house sans ("PwC Proxima Nova" house
stack) → "Helvetica Neue", Arial, sans-serif.
