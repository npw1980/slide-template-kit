# pyramid-tiers-levels — Five-level decision pyramid with aligned text rows

WHEN: The "tiers of the organisation" page — who decides what along a
corporate-to-operational ladder (delegation of authority, operating model
levels, decision rights). From the corpus levels-pyramid pattern (S0259):
5-tier triangle with a label inside each tier and a text line per tier
beside it. Kit encoding: one accent band + outlined grey bands + a
metrics rail, so the ladder argues instead of colouring.

ANATOMY (stage 1280×720, all numbers px; SVG viewBox 0 0 1280 720):
1  kicker          x64 y34   "N | SECTION" (index in accent)
2  claim title     x64 y56   2-line slot, clip-gated
3  lead             x64 y150 one sentence, one accent span inside
4  triangle         apex (430,170), base y580, half-base 300 → 130..730.
   Cuts every 82px: 170 / 252 / 334 / 416 / 498 / 580.
   Edge x: xE = 430 ± 300*(y−170)/410 (right edge = leader start).
   #tier-1 apex band ACCENT-filled (white label); #tier-2..5 outlined
   white bands (grey-2 stroke) with ink labels.
5  tier groups      one <g class="tier-group" id="tier-k"> PER TIER:
   band polygon + centered tier name (+ tier number), dashed leader +
   dot to rail, numbered disc (x716), rail row (name x734, 2-line desc,
   right-aligned metric + "OF DECISIONS" unit at x1216), bottom hairline.
   Rail x 700..1216; band mid-height = row line (211/293/375/457/539).
6  zone brackets    x112: STRATEGIC 170-334, TACTICAL 334-416,
   OPERATIONAL 416-580, labels above each bracket at x116
7  delegation line dashed grey at the 2|3 cut y334, label above right
8  pyramid note     centered x430 y610 — "band size shows X, not Y"
9  hairline y682; source line x64 bottom; page stamp bottom-right

SLOTS (name, max, good/bad):
- kicker: "N | SECTION", ≤ 4 words after the pipe.
- title: action title ≤ 15 words / 2 lines. GOOD: the shown claim (15 words
  — at the gate). BAD: "Levels pyramid" / "Decision rights" — topics.
- lead: bridge ≤ 2 lines, one accent span.
- tier-k.name (in band): ≤ 3 words, the LEVEL, not the company's org chart
  label ("Field operations"), ≤ 21 chars — must fit the band width at its
  baseline (see geometry: a long name at tier 1/2 wraps out of the triangle).
- row-k.name: ≤ 3 words. row-k.desc: ≤ 2 lines × ≤ 54 chars; states OWNERSHIP
  ("owns", "inside the envelope", "by design") — never a wishy-washy summary.
- row-k.metric: 1 figure + unit ("11%", "1,204 decisions"); the unit line is
  the same on every row — the metric must be comparable across tiers. The
  shown shares sum to 100% deliberately: if they don't, the page is broken.
- zones: one of STRATEGIC / TACTICAL / OPERATIONAL — rename in pairs
  (front/back-office), never invent five.
- pyramid note: one honest methodology line with one bold qualifier.

FILL (step by step):
1. Header: replace kicker div, h1.title, p.lead (keep <span class="em">).
2. TIERS ARE RIGID GROUPS: to add/remove tiers copy or delete whole
   <g class="tier-group"> blocks. For N tiers, re-cut evenly: cut_k =
   170 + k*(580−170)/N. For every group below the change, shift its y's by
   the same dy: polygon points, band name y, leader y1/y2 + dot cy,
   disc cy/text y, row name/desc/metric/unit y's, hairline y1/y2. All are
   plain constants in the markup — add dy, don't recompute per element.
   Recompute each leader's x1 = 430 + 300*(bandMid − 170)/410, each
   leader dot at the same point; tier 5 leader may be near zero-length.
3. ADD A TIER: copy the nearest similar tier (e.g. #tier-3), paste below,
   shift, swap texts. The accent band stays #tier-1; an added tier 1 is
   allowed but then move band-em class (and the 4px rail bar) to the new
   accent tier and revert the old one to outlined.
4. REMOVE A TIER: delete its group; re-cut; shift lower groups up; the
   bottom hairline of the deleted band goes away with it. Renumber discs.
5. METRICS: replace each row-metric value text; if you drop metrics
   entirely, delete row-metric + row-unit in all groups and widen the
   row-desc wrap to x1216 (then also delete "OF DECISIONS" units). The
   pyramid note must then stop claiming "logged share".
6. ZONES/ENVELOPE: bracket y's track the cuts — after any re-cut move the
   bracket path d's and their label y. Delete #envelope if no delegation
   story. #envelope's label sits 6px above the y334 line: keep that.
7. Footer: source line + page stamp; sup markers follow claims made.

CHART RECIPE: triangle encodes ORDINAL rank only — no value axis, band size
not drawn to scale (the note says so; don't let it become headcount). One
accent: exactly one band filled (tier-1) + its rail bar; the rest outlined.
Numbers live exclusively in the rail metrics (right-aligned so the eye
compares), never on the triangle. Leader lines dashed to read "annotation,
not flow"; dots mark the exact band edge touched. Hairlines separate rows
and stop at band boundaries. Zone brackets + envelope are grey-2, no hue.

VERIFY: title ≤ 15 words / 2 lines; metrics comparable & sum check (if using
shares); white text only on the accent band, ink on outlined bands
(16.9:1 / 9.8:1 / 15px+ white-on-grey would need 4.5:1 — outlined bands use
ink, so fine); one accent hue + greys; leaders start ON band mids after any
resize; page stamp present.

DON'T: five-hue tiers (corpus original's red-yellow-teal-blue — a rainbow
page, kit forbids); white labels inside outlined white bands (readability);
metrics in non-comparable units (11% vs "10 people"); row description that
paraphrases the tier name; an "org chart" inside the bands (that's another
template — org-hub-map); letting tier names grow past ~21 chars.

SOURCE: corpus levels-pyramid family, TEMPLATE_HARVEST.json "pyramid-tiers"
exemplar S0259 — catalog_21-62.csv: "levels pyramid · white label per tier ·
5-tier pyramid + text · corporate-to-operational tiers". HONEST NOTE: the
sheet resolution (corpus/sheets/sheet_026.jpg frame 9, ceil(259/10)=026) and
sheet_027 frames land on Bing photo pages (S0251–S0270 tag [bing:benchmarking]),
not deck pages — the slide images behind that catalog row are not usable
diagrams. So this template reconstructs the documented archetype (5 tiers,
label-in-band, side text) from the catalog description and kit rules, and
recolours per DESIGN_PLAYBOOK. The sibling pyramid-tiers-value keeps the
one fully visual exemplar (S0034).
