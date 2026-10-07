# three-horizons-circles — Three cascading horizons as overlapping circles with notes and a strategy loop

WHEN: The "how the horizons connect" page — a portfolio or strategy-architecture
claim that horizons are not three buckets but one funding chain, where the small
future is seeded by the big present and both are steered by one planning loop.
Drawn from the Gartner "Three Strategic Planning Horizons" page (corpus slide
S0030): three solid overlapping circles cascading down-right, biggest to smallest,
white labels inside, plus two strategy annotations ("Planned strategy: cascading
goals and continuous alignment" / "Emergent strategy: calibration and continuous
learning") joined by arrows. The kit's answer to "three SmartArt circles and a
bulleted list".

ANATOMY (stage 1280×720, all numbers px; one full-stage SVG viewBox 0 0 1280 720;
`html` font-size maps 1rem = 1 stage px, so the coords below are literal):
1  kicker          x64 y34    "N | SECTION" (index in accent)
2  claim title     x64 y56    2-line slot, clip-gated (3rd line clips)
3  lead            x64 y150   one sentence, exactly one accent span
4  CASCADE         three circles, back-to-front h1 → h2 → h3, each drawn with a
   3px --bg stroke so the overlap reads as one shape, not as a venn:
     #h1  (360,350) r145   ACCENT fill, white text   — the emphasis circle
     #h2  (593,365) r113   grey-1 fill, white text
     #h3  (762,380) r81    grey-3 fill, ink text
   Cascade rule:  r(k) = 150 − 32(k−1)
                  centre step dx(k) = r(k) + r(k+1) − 25   (a fixed 25px overlap)
                  dy = +15 per step, so the cascade falls to the right.
   h1 spans x215–505 / y205–495 · h2 x480–706 · h3 x681–843.
5  BADGES          white discs r13 with the horizon number, centred on each
   circle's 135° rim point: (258,248) · (513,285) · (705,323). They are what
   connects the diagram to the notes rail.
6  NOTES RAIL      x936–1216 (280 wide), three numbered note blocks, rules at
   y312 and y437. Block k: disc x916, kicker y(228|353|478), title +22, body +40
   and +55. Kicker #1 carries `.em` (accent) — it matches the accent circle.
7  ANNOTATIONS     two boxes 255×56 at x215 / x585, y596: 3px left rule grey-1,
   caps y616, two body lines y634 / y646. Each has a dashed grey leader with an
   up-arrowhead into the cascade (planned: x342 → y492, at h1's lower edge;
   emergent: x712 → y448, at h3's lower edge). Between them a two-headed
   horizontal arrow (x470→x585, y624) labelled "THE LOOP".
8  hairline y682 · source line x64 bottom · page stamp bottom-right.

SLOTS (name, max, good/bad):
- kicker: "N | SECTION", ≤ 4 words after the pipe.
- title: action title ≤ 15 words / ≤ 2 lines. GOOD: the shown claim (14 words,
  states the dependency between horizons). BAD: "Three horizons framework" —
  that is the diagram's name, not an argument.
- lead: 1 line, one accent span, must name the relationship ("hands over while
  it is still funded") — that is what the overlap means.
- horizon-k.caps: "HORIZON 1" (2 words). The name IS the framework's own noun;
  do not invent "Invest / Grow / Build" — the numbering is what ties to the rail.
- horizon-k.name: 2 lines × ≤ 17 chars. GOOD: "Maintain and / defend the core"
  — a verb phrase for what the org DOES in that horizon. BAD: one long line that
  spills past the circle's safe area (text is centred on the circle, so a wide
  line escapes the shape where the next circle overlaps it).
- horizon-k.pill: "1–3 yrs · 62% of revenue" — horizon duration + its share.
  This is the only place percentages appear on the diagram; the rail carries the
  amounts. Keep ≤ 22 chars or widen the rect (its width is set per circle).
- note-k.kick: 3–5 words of role ("THE BASE THAT BUYS TIME"), uppercase, wide
  tracking. BAD: "Commentary".
- note-k.title: ≤ 6 words, an imperative — what the org must DO.
- note-k.body: 2 lines × ≤ 44 chars with ≥ 1 hard number each (6–8% of costs,
  €40M revenue, €18M). The worst plausible fill is shown.
- ann caps: "PLANNED STRATEGY" / "EMERGENT STRATEGY" + 2 short lines each. These
  two boxes are the page's methodology claim: goals flow down, learning flows up.
- source-line: basis + n + sup markers (the horizon tagging, the thresholds).

FILL (step by step):
1. HEADER: replace kicker / h1.title / p.lead; keep <span class="em">.
2. RENAME A HORIZON: inside `<g class="horizon" id="h…">` replace the two `.nm-*`
   lines, the caps line and the pill text. Keep them centred (`text-anchor=middle`
   at the circle's cx) and ≤ 17 chars/line, and the geometry needs no touching.
3. ADD A HORIZON (e.g. a "horizon 0" or a fourth "wildcard"): COPY one whole
   `<g class="horizon" id="h…">` — it is a rigid unit: <circle> + caps + 2 name
   lines + pill rect + pill text. Then place the copy by the cascade rule:
   r(4) = 150 − 32×3 = 54, centre = previous centre + (r(prev)+r(4)−25) in x and
   +15 in y (so #h4 would sit at 762 + (81+54−25) = (872, 395) — and since the
   rail is at x922+, shrink the base radius instead of letting it collide: set
   r(1)=140 and re-derive the rest from the same formulas). Text inside a circle
   smaller than ~55px radius: keep only caps + one name line and DROP the pill.
   Also copy a note block (4th) and a badge, and renumber.
4. REMOVE A HORIZON: delete its whole `<g>`. The remaining circles do not move —
   they overlap only 25px, so no reflow is required and the cascade still reads.
   If one fewer circle looks sparse, widen the remaining ones by rebuilding their
   centres from the rule with k up to N−1 (dx grows, so they spread out).
   The notes rail must be re-flowed: blocks sit at pitch 125px (y 228 / 353 /
   478) with rules between; delete a block and pull the next two up by 125,
   moving each block's disc cy, kicker, title and both body lines by the same dy.
5. CHANGE THE EMPHASIS: swap the fill class on exactly one circle
   (`ring-1` accent / `ring-2` grey-1 / `ring-3` grey-3) and use the matching
   text class pair (`cap-w`+`nm-w`+`pill-w` for dark fills, `cap-k`+`nm-k`+
   `pill-k` for grey-3). Move `.em` to that note's kicker too. Never fill two
   circles with the accent — the whole diagram's argument is rank, not colour.
6. STRATEGY LOOP: the two `.ann` groups are independent — keep only one (delete
   the other and its leader) if the engagement has no emergent story; then move
   the survivor toward the centre so the band is not lopsided, and delete the
   two-headed arrow (the 2 polygons + 1 line + 1 caps text that sit between the
   boxes). To reverse the direction of a leader: flip the leader line's y1/y2 and
   move the `<polygon>` arrowhead to the far end (points = tip-2, tip+10).
7. RAIL NOTES: each note is one `<g class="note">` (disc + disc number + kicker +
   title + 2 body lines) — copy-paste safe; renumber both the rail disc text and
   the matching badge so the pairing holds.
8. FOOTER: source line + page stamp; keep sup markers on the claims.

CHART RECIPE: This figure encodes SIZE = scale/stage (radius shrinks as the
horizon recedes) and POSITION = cascade (later horizons sit lower-right, so the
funding flows downhill — that is why the leaders run upward: goals flow down,
learning flows up). There is no quantitative axis and none should be invented:
diameter is ordinal, so never label radii or add a scale bar. The overlap (25px)
is semantic — it is the "hand over while still funded" — so do not space the
circles apart. One accent: exactly one circle is accent-filled (its white label
clears 6.0:1); the others are grey-1 (white label 9.8:1) and grey-3 (ink label
11.8:1). Numbers live only inside pills and in the notes rail, never on the
diagram's body. No legend: the badges + the numbered rail are the index.

VERIFY: title ≤ 15 words / 2 lines (clip gate); source line present + sup
markers; exactly one accent hue + greys; white-on-fill contrast per circle; every
badge number appears once in the rail; no text crossing a circle's boundary into
the overlap; page stamp present; each horizon/note group passes the copy-paste
test.

DON'T: topic title; three equal-sized circles (equal size destroys the cascade
argument); accent-filled all three (10-colour SmartArt instinct); percentages
written on the circle bodies as well as the pills; notes that restate the circle
label; leader lines from every circle to the rail (badges + numbers do it, and
three crossing leaders is noise); kicker as a wall of text; an unlabelled "loop"
arrow with no boxes behind it.

SOURCE: corpus slide S0030 — Gartner "Three Strategic Planning Horizons", read on
corpus/sheets/sheet_003.jpg frame 10 (S0021–S0030 row-major 5col×2row, row 2
col 5); catalog row catalog_1-20.csv S0030 ("three overlapping circles plus box ·
blue circles · cascading-goals annotation box"). Observed at sheet level: solid
blue circles decreasing down-right, long/mid/short-term planning-horizon captions
inside, and the two strategy boxes top-right and bottom-left with arrows. The
notes rail, the share pills and the numbered badges are kit additions built to
the DESIGN_PLAYBOOK rules; the overlapping-circle cascade and the two strategy
annotations are the corpus's. Screenshots:
qa/three-horizons/three-horizons-circles.png.
