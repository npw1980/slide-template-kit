# pyramid-tiers-value — Centered three-tier value pyramid with per-tier notes

WHEN: The "value moves up the pyramid" page — a claim that the business shifts
from a low-value base to a high-value apex (pricing, transformation maturity,
from-to economics). Drawn from the Gartner services-transformation page
(catalog S0034, seen on corpus/sheets/sheet_004.jpg frame 4): blue 2-line claim
title, one centered triangle cut into three tiers with labels centered inside.
This is the kit's replacement for "SmartArt pyramid + bullets".

ANATOMY (stage 1280×720, all numbers px; SVG viewBox 0 0 1280 720):
1  kicker          x64 y34   "N | SECTION" (index in accent)
2  claim title     x64 y56   2-line slot, clip-gated (3rd line clips)
3  lead             x64 y150  one sentence, one accent span inside
4  triangle         apex (515,168), base y560, half-base 250 → 265..765.
   Tier cuts y299 / y429 (thirds). Right edge: xEdge = 515 + 250*(y−168)/392.
   #tier-1 apex band  grey-1 · #tier-2 middle band  ACCENT (emphasis) ·
   #tier-3 base band  grey-3. White seams via stroke:var(--bg) 3px.
5  per-tier groups  one <g class="tier-group" id="tier-k"> PER TIER holding
   polygon + 2 label lines + leader (to x800) + numbered disc (x812) +
   note-kick + note-title + 2 note-body lines (rail x836..1216, 380px wide)
6  escalation arrow  x228 (vertical 156px, rotated label, grey-2)
7  pyramid caption   centered x515 y606 — the "from → to" line
8  hairline y682; source line x64 bottom; page stamp bottom-right

SLOTS (name, max, good/bad):
- kicker: "N | SECTION", ≤ 4 words after the pipe.
- title: action title ≤ 15 words / ≤ 2 lines. GOOD: the shown claim (13 words,
  states the direction of travel). BAD: "Three-tier value pyramid" — topic
  label; the tier names below are the topic, the title must be the argument.
- lead: bridge sentence ≤ 2 lines, exactly one accent span.
- tier-k.label: ≤ 4 words per line, noun phrase naming the TIER'S ROLE
  ("Deliver value for the money"), not an initiative name.
- tier-k.note-title: ≤ 6 words, an imperative or claim — what the tier does.
  BAD: "Commentary" filler; every note must state an action or an amount.
- tier-k.note-body: 2 lines × ≤ 68 chars, contains ≥ 1 hard number
  (%, bps, counts). The worst plausible fill is shown (1,412 / −180 bps / 245).
- pyramid caption: "from X → to Y" — mirrors the title's verb, no new info.
- source-line: data basis + n + footnote markers (sup) where methodology claims.

FILL (step by step):
1. Header: replace kicker div, h1.title, p.lead (keep <span class="em">).
2. TIER TEXT: each tier is one self-contained <g class="tier-group"> —
   polygon (geometry stays), the two centered <text> label lines, the leader
   line, the numbered disc, and its 4 note texts. Replace only text content.
3. ADD A TIER (e.g. four moves instead of three): COPY #tier-2 (an accent-
   free band copy it as grey first: change its polygon fill class). Insert it
   between existing bands and re-cut ALL horizontal cuts evenly: for N tiers,
   cut-k y = 168 + k*(560−168)/N. For each tier below the insertion, shift
   EVERYTHING in its group by the same dy (polygon y's, label y's, leader
   y1/y2, disc cy + disc text y, note-kick/note-title/note-body y's) — a
   tier-group is a rigid unit, that is what makes resize safe. The right-edge
   leader start recomputes: x1 = 515 + 250*(leadY − 168)/392.
4. REMOVE A TIER: delete its whole <g>; re-cut cuts the same way, shift the
   groups below up by dy; renumber the discs (text inside .disc-n).
5. EMPHASIS: move accent by swapping the fill class on exactly ONE polygon
   (tier-em ↔ tier-top/tier-base); make that band's note-kick class "em".
   Everything else stays grey ramp + white/ink text.
6. RENAME A ZONE of the arrow label ("CAPABILITY LADDER") or delete #escalation
   if the page has no directional story (the caption line carries it alone).
7. Footer: source line + page stamp; keep sup markers aligned to claims.

CHART RECIPE: The figure encodes POSITION = value rank (apex highest), no
quantitative scale; tiers are ordinal bands, so never put axis numbers on the
triangle. One accent: exactly one band accent-filled (white label clears 6.0:1);
apex band grey-1 with white label (9.8:1); base band grey-3 with ink label
(11.8:1). Numbers live only in the notes rail, never on the triangle. Leader
lines connect each band to its note at band mid-height — that is the reading
order, so keep them horizontal and unnumbered except the disc.

VERIFY: title ≤ 15 words / 2 lines (clip gate); source line present + sup
markers; exactly one accent hue + greys (no blue+amber like the original);
white text clears contrast per band; page stamp present; each tier group
self-contained (copy-paste test passes).

DON'T: topic title; amber+blue multicolor tiers (the corpus original does this
— kit rule is one accent + greys); notes that restate the tier label;
percentages painted on the triangle; kicker as a wall of text; letting a tier
note overflow its 2 lines (widen wording tolerance or move detail to footnote).

SOURCE: corpus slide S0034 (slides_manifest id, tag "4890"; original
corpus/pdfpages/4890_49c9_a1ee_77b0f75a86c7_St_-01.png) — visual read on
corpus/sheets/sheet_004.jpg frame 4 (S0031–S0040 row-major 5col×2row);
catalog row: catalog_1-20.csv S0034 "three-tier pyramid · white text on tiers
· blue plus amber pyramid · centered pyramid · blue amber value pyramid".
Family harvest: TEMPLATE_HARVEST.json "pyramid-tiers" (5 exemplars; the
levels-pyramid S0259/S0260/S0264/S0269 resolve to Bing photo pages — see
pyramid-tiers-levels SOURCE note).
