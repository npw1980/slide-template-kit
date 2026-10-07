# model-diagram-asis-tobe — As-is vs future-state operating model: mirrored panels + spectrum rail

WHEN: The "transformation" page — what changes between today's fragmented
operating model and the target one, shown as two mirrored text-box panels
(component by component, 1:1) with a vertical ordinal side rail (centralised →
hybrid → decentralised) carrying today/target markers. From the Deloitte New
Mexico State staffing / operating-model study ("As-Is vs Future-State operating
model spread", review archetype item 9). Distinct from before-after chart
pages: this is a STRUCTURAL comparison with no per-metric bars.

ANATOMY (stage 1280×720, all numbers px):
1  kicker          x64  y34   "N | SECTION" (section index in accent)
2  claim title     x64  y56   2-line slot, clip-gated
3  lead line       x64  y138  one sentence, one accent span inside
4  AS-IS panel     x64   w544: header band y178 h34 (grey), body y212 h356,
   4 component rows y226/302/378/454 h64 (pitch 76), row bg x78 w516
5  TO-BE panel     x676  w450: same vertical grid (rows mirror 1:1 by y);
   rows x690 w422; header + body in accent
6  MOVE arrow      chevron x629..661 centred on the 612..676 gap (64px),
   chevron y352..380, "phase 1–2" caption below
7  SPECTRUM RAIL   track x1168 w14 y178 h436; thirds centred y251 (centralised)
   / 396 (hybrid) / 541 (decentralised); today dash y552 grey, target dash
   y382 accent + grey-lightness band over the target (hybrid) third 324..469
8  hairline        y682;  9 source line x64 bottom;  10 page stamp bottom-right

SLOTS (name, max, good/bad):
- kicker: "N | SECTION" section index, ≤ 4 words.
- title: action title ≤ 15 words / 2 lines. GOOD: "A hybrid shared-services
  model removes duplication without giving up campus ownership" — names the
  target AND the tension. BAD: "As-is and to-be operating models" (that is a
  file name, not a claim — and the source deck's whole weakness is titleless
  data pages, see review §Action titles).
- lead line: the mechanism sentence (what moves = what changes the answer),
  one accent span, ≤ 2 lines.
- panel-cap (×2): "AS-IS — CURRENT STATE" / "TO-BE — FUTURE STATE". Fixed.
- row-head (×8): the operating-model component ≤ 3 words. The two panels MUST
  carry the SAME component list 1:1 (structure/ownership/process/technology/
  people…) — mirroring is the whole diagram; unpaired rows break it.
- row-body (×8): 1–2 lines × ≤ 70 chars. GOOD: numbers ("24 FTE", "4 handoffs
  (was 14)"), not adjectives ("more efficient").
- rail labels: centralised / hybrid / decentralised — ordinal scale, fixed.
  today / target markers are ONE dash each.
- transition caption: phase name or "phase 1–2" — not a sentence.
- source-line: benchmark range used (soC 8:1–12:1) + headcount basis;
  "model illustrative" footnote where the diagram is a proposal.

FILL (step by step):
1. Replace header text: kicker div, h1.title, p.lead (keep `<span class="em">`).
2. ROWS: each component row is one `<g class="row" id="as-row-N">` (bg rect +
   row-head + 2 body tspans) — same for `#to-row-N`. Text ys stay; the only
   edit is the tspans. Row height is fixed 64: more than ~2 body lines
   overflows.
   ADD A COMPONENT: copy one row pair (as-row-N + to-row-N), paste at the
   position, then shift every lower row down by +76 (row rect y, head y, body
   y — keep as-row and to-row ys equal). If 6+ pairs, shrink the previous
   pitch (76 → 64) for ALL rows and reset panel body rect heights (h356 both)
   instead of cropping.
   REMOVE: delete both paired rows, shift lower rows up by 76. NEVER delete
   only one side of a pair — mirroring is the encoding.
3. MOVE ARROW: `<g id="move">` — the chevron sits at row-pair midpoint
   y366 (rows 226..518). After row-count changes, re-centre: chevron y =
   (first row y + last row y + 64)/2; captions move with it (−152/+30).
4. RAIL: one `<g id="rail">`. Scale words stay (centralised / hybrid /
   decentralised fixed). MARKERS: a dash = line x1158..1190 + its label, dash
   y = (third centre − 14) with label below/above as coded (TODAY on the
   552/decentralised side, TARGET on the 382/hybrid side). The TARGET band
   rect (x1168 w14, h145) must be moved TOGETHER with the target dash:
   band y = dash third top (396 for hybrid). REMOVE A MARKER: delete dash +
   label; delete the band rect if its target moves.
5. RECOLOR: swap --accent + --accent-soft at :root; to-be panel head/border,
   row fills, chevron, target dash follow. AS-IS stays grey — never give both
   panels accent.

CHART RECIPE (diagram encoding, no chart here):
- One accent rule: grey = what exists, accent = what changes / where you're
  going (to-be panel, its rows, target marker). Exactly one hue; the rail's
  target band is ONE LIGHTNESS of grey, not a second hue.
- Emphasis rules: no shadows, no 3-D, no gradients; the 1.4px accent border is
  the only highlight the right panel gets.
- Ordinal rail discipline: markers sit ON one of the three named thirds (no
  arbitrary positions — that implies false precision); if today spans two,
  draw a dash across both or two dashes.
- Units: none; numbers live inside row-body text (bold allowed once per row).

VERIFY:
[ ] title ≤ 15 words / 2 lines, nothing clipped
[ ] row components paired 1:1 across panels (same count, same order)
[ ] exactly ONE hue (accent + grey ramp); as-is panel is grey-filled
[ ] rail has ≤ 2 markers and they sit on named thirds
[ ] source line cites the benchmark scale and headcount basis (this genre is
    benchmark-anchored or it's opinion)
[ ] page stamp bottom-right present

DON'T:
- Don't put before/after bar charts inside the panels — the source spread has
  NO per-metric bars; that would duplicate before-after-state-pair.
- Don't mirror with adjective filler; paired rows must carry real numbers /
  owners, or the page is decoration.
- Don't copy the diagonal "Illustrative: for discussion purposes" watermark —
  the review's §IGNORE calls it a working-session artifact; keep "model
  illustrative" as a plain footnote instead.
- Don't give both panels the same header colour — then "where's the change?"
  reads nothing.
- Don't exceed 6 component pairs; pitch floor 64 keeps label text legible at
  projection size.

SOURCE: Deloitte, "New Mexico State University staffing / operating-model
study" — the per-function "As-Is vs Future-State operating model" spread
(review archetype item 9: two mirrored text-box panels + vertical side rails
(Centralized/Hybrid/Decentralized; Relationship to University)). Reviewed in
`reviews/deloitte__deloitte_new_mexico_state_university_staffing_study_opportun.md`
(§Color system crimson semantics; §"What a template designer should COPY"
lists this spread inside the per-function analytical rhythm — "as-is/future
model" step; §IGNORE rejects the illustrative watermark). Contact-sheet
pages: sw_sheets/deloitte__deloitte_new_mexico_state_university_staffing_study_opportun_s0*.jpg.
Real fonts: Deloitte Graphik (display + body) + brand serif; Helvetica/Arial
stacks stand in. Palette: crimson/magenta brand anchor per review §Color
(darkened here to #A1194B for AA), greys #D9D9D9/#F2F2F2, near-black #1A1A1A.
