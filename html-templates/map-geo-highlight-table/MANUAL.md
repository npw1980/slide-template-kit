# map-geo-highlight-table — Highlight region map + numbered policy-focus table

WHEN: "Everyone is doing X, but each on their own thing" — a jurisdiction map
where ONE region is the subject of the claim and a numbered table carries each
region's actual position/target. From pwc_strategy `e-mobility in India`
p11 (sheet sw_sheets/pwc_strategy__pwc_e_mobility_in_india_market_paradigms_and_ways_to_play_20_s01.jpg
row 1 frame 2): grey India map, stacked dark lever callouts over its edge,
10-row State | Key Focus table with accent disc badges.

ANATOMY (1280×720; SVG layer is stage coords):
1 kicker   64,36 w1152 — base line (policy set + period), footnote marker
2 title    64,59 w1152 — serif editorial claim, ≤15 words / 2 lines, em-clause accent-deep
3 map body 64..360 × 170..600 — country silhouette, flat grey; 1 accent region, 2 mid-grey
4 levers   x138 w175 h24 pitch 57, 6 bars, 189..504 — charcoal callouts overlapping map edge
5 leader   one accent hairline from focus region blob into the lever stack
6 map note 64,616 9.5px — what filled/darker means (replaces a legend)
7 table    430..1216 — heads 228 / rule 236; 10 rows, pitch 44, first baseline 250
8 badge    disc r10 cx447, accent fill, white digit; FOCUS row badge in accent-deep
9 source   64,681 — documents + method caveat + footnote expansion
10 pageno  right:64, 681 — page | SECTION

SLOTS:
- title: claim + operative clause ("Ten states have carved out their own EV
  policies — each on different adoption levers"). Topic title = wrong template.
- region names: real jurisdiction names; the FOCUS name appears in BOTH map and
  table (badge + name in accent-deep) so the reader can't miss the link.
- lever bars: 6 short noun-phrases ("Charging infrastructure"), not sentences.
  These are the CATEGORIES, the table rows are the EVIDENCE — if the same text
  appears in both, you've duplicated, not encoded.
- focus text (per row): 1–2 lines, one bolded quantitative anchor ("25% EV
  share of sales by 2024"); ≤ ~150 chars visible.
- kicker: base + date range only. "For details click here" links are not
  reproduced — a slide has no click.

FILL:
1. Table first: replace each row's name + focus text (arrays in the index.html
   header comment: states[] n/name/focus). Row count changes → keep pitch 44;
   row i baseline = 250 + 44(i−1); rules +20; badges 4 below baseline (r10).
2. Focus state: give it the accent fill on the map (its polygon), its badge in
   --accent-deep, and its name in accent-deep. Everything else stays badge-accent.
3. Map: swap `<g id="map-geometry">` for real SVG (state polygons) on the SAME
   frame (x = 64 + (lon−65)/33 × 296, y = 600 − (lat−7)/29 × 430). Recolor via
   fill classes: accent / --region-mid / --region-gray. White 1px stroke
   between neighbours; keep the country silhouette as one flat base.
4. Levers: replace the six `<text>` strings. Bar text one line ≤ ~30 chars
   @10.5px (drop to 9.5 if longer); never re-stack to 2 lines inside 24px.
5. Recolor accent family: set --accent + --accent-deep; white-on-accent digits
   must clear 4.5:1 (orange #ED8B28 keeps it; light accents need ink digits).
6. Bold anchors: wrap each row's key number in `<tspan font-weight="700"
   fill="var(--ink)">` inside the gray-ink row text. Exactly one anchor per row.

CHART RECIPE:
- Choropleth-LITE is the rule: fill states are BINARY classes (focus / named /
  rest), never a continuous ramp. Continuous ramps on 10 states read as noise
  and steal the argument from the table. If a value must drive shading, that's
  the bubble template's job.
- One hue: single --accent family; the map greys (--region-gray #D9DEE2,
  --region-mid #AEB6BD) and charcoal levers #3A3F45 are ink not hue. Total
  hues: 1 (orange) + gray ramp.
- Emphasis: exactly one accent-filled region + its accent-deep badge/leader.
  A second "also highlight it" region collapses the hierarchy — that's what
  --region-mid is for.
- No scale, no legend, no axes: this exhibit is categorical. Scale lives in
  the table's bold numbers. The 9.5px map note replaces a legend.
- Callout bars: flat charcoal, 3px radius, white text, right edge bleeding
  into the map (they are annotations, not data marks); ≤ 6 bars.
- Table: right-angle grid = consulting discipline. Row rules full-width;
  badges in a single column rhythm; the eye reads badge order, not map order.

VERIFY:
- [ ] title ≤15 words, ≤2 lines serif 27px (1152px column); em-clause present
- [ ] ONE region accent-filled; second-level regions only --region-mid
- [ ] one accent-deep badge (the focus state); other badges stay accent; no rainbow
- [ ] every table row has exactly one bold quantitative anchor (or explicit none)
- [ ] source line with document basis + caveat, footnote marker expanded
- [ ] page | SECTION running head bottom-right
- [ ] zero network calls (network tab empty apart from the file)

DON'T:
- Topic title as page header ("State EV policies overview").
- A continuous 10-shade choropleth, or coloring >1 region accent.
- 10+ rows at 44px pitch with 3-line focus text — the table's ceiling is 10
  rows × 2 lines; more states go into an appendix back-matter template.
- Legend boxes / scale bars / a "you are here" compass — categorical map.
- SmartArt auto-shapes or WordArt map — everything here is hand-drawn SVG.
- Making the lever bars a second data series (color-coding them by state) —
  they're categories; color is ink.
- Duplicated content: "Tax rebates" as a lever bar AND as a row's focus text.

SOURCE: pwc_strategy__pwc_e_mobility_in_india_market_paradigms_and_ways_to_play_20
— p11, read on sw_sheets/pwc_strategy__pwc_e_mobility_in_india_market_paradigms_and_ways_to_play_20_s01.jpg
row 1 frame 2 (sheet pages 5col×2row row-major). Numbered-disc table device +
grey-country/one-accent convention cross-checked against pwc_strategy__pwc_five_global_shifts
p21 evidence-band practice; palette (orange accent, gray ramp, editorial serif)
from the kit's pwc_strategy review notes. Real font: PwC house serif display →
Georgia stand-in (stated honestly — house faces are not web-licensable).
