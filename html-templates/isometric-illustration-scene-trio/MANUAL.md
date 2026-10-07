# isometric-illustration-scene-trio — Isometric Scene Vignettes + C-suite Split Stats

WHEN: A "who does what / who owns what" survey or opinion exhibit: 3 (±1) role
or activity vignettes, each a small isometric scene on a floor plate, under a
two-tone serif takeaway headline, with one C-vs-non-C percent pair per scene.
From PwC Global Crisis Survey 2019 p09 (numbered chapter, red/black answer+
question headline, isometric vignettes with percent callouts — review line 72
calls the pattern "isometric 3D illustrations with percentage callouts used as
infographic"). This is the firm's infographic device, NOT an MBB chart: the
scenes carry the character, the stats carry the argument.

ANATOMY (1280×720 stage, all coords in stage px):
1 kicker      "SECTION 4 · WHO OWNS CRISIS" — (64,80), 11px bold, +14% tracking, accent
2 numeral     ink 56×56 square + chapter digit — (64,104)-(120,160), group `#numeral`
3 title-red   answer line, 28px Georgia bold accent — 2nd baseline y=212, x=64
4 title-ink   question line, 28px Georgia bold ink — 2nd baseline y=244
5 lead        3-line hand-wrapped 14.5px gray-1 paragraph — starts (64,284), 21px lines
6 commentary  two 11.5px blocks with bold leads — (64,408) and (336,408), ≤4 lines each
7 figure-line "Figure 3 | …" 11.5px gray-3 — (512,110) + hairline rule y=122, x 512→1216
8 nodes       three `<g class="node">` vignettes — centers (696,330),(894,330),(1092,330)
   inside each node (node-local coords, translate origin = plate center):
   plate diamond ±104×52, scene on plate (person + 1 object + 1-2 props),
   caption y=+112 centered, stat pair y=+152 (26px serif) + labels y=+168
9 source      bottom-left (64,694), one line + footnote (1)
10 runhead    "9 | WHO OWNS CRISIS" bottom-right (1216,694), 10.5px
11 edgebar    7px accent vertical bar flush left, full height (source-deck brand device)

SLOTS (what to rewrite; good/bad tests):
- kicker: 2-4 words + section no. Bad: "OVERVIEW". Good: "SECTION 4 · WHO OWNS CRISIS".
- numeral: single chapter digit. Bad: "4.1" or any text >1 char.
- title: TWO lines max, ≤15 words total. Red line = the answer as a claim; ink
  line = the question. Good: "Who owns crisis management? / Everyone — and no one."
  Bad: topic labels ("Crisis ownership"). Quantitative beats qualitative here.
- lead: 1 sentence, 3 hand-set lines × ≤56 chars (SVG text does not wrap —
  every line is a `<tspan x=… dy=…>`; keep all x equal).
- commentary: two blocks × 3 lines; each leads with a bold assertion. The two
  blocks must argue two DIFFERENT things, not the same point twice.
- node.caption: ≤26 chars, one line, the activity name. Not a sentence.
- node.stats: two numbers: `t-stat-acc` (red) + `t-stat-gray`. Same unit, the
  "bad" side gray. Red ≥ gray is the usual emphasis direction.
- node.scene: 1 flat figure + 1 anchor object + ≤2 props. If the scene has zero
  identifiable activity cues (board/desk/megaphone/phone/paper), it is decor.
- figure-line / source / runhead: real strings, not lorem.

FILL (build order; SVG is the whole page, no HTML text elements):
1. Titles/lead/footers: replace `<text>` / `<tspan>` strings only. Lead lines:
   keep `x=64 dy=21`; re-wrap by hand if text changes length.
2. Stats: swap the two numbers inside each node block
   (`t-stat-acc` x=-34, `t-stat-gray` x=+34) and keep label caps.
3. ADD A NODE: copy the entire `<g class="node" transform="translate(CX,330)">`
   block from node 3; set `translate(1290,330)` (pitch = 198; CXn+1 = CXn + 198)
   — a 4th node pushes past x=1396, so for 4 nodes shrink pitch first:
   set CX = 598/796/994/1192 (pitch 198, panel 512→1216), or compress to 190.
   Inside the copy: replace scene shapes + caption text + both stats. Everything
   inside a node is node-local; NO other element reflows.
4. REMOVE A NODE: delete its `<g class="node">` block and shift surviving CX by
   ±198 (center the row: 2 nodes → CX = 796, 1192).
5. Figures inside a node: person is fixed geometry (legs/torso/head/arm paths,
   translate to the standing spot); swap the anchor object group (whiteboard /
   desk+laptop / megaphone+panel) and the bars. To keep the iso read, plates and
   their 3-face box conventions are fixed — copy `<polygon class="f-*">` triples.
6. Recolor: set `--accent` (and `--accent-1` = 15% tint); grays are fixed.

CHART RECIPE: No axes — this is infographic-style encoding, per the source.
Each stat pair is one accent + one gray, equal 26px, centered under the
caption; the % sign is set with the number (SVG text is plain — no <tspan>
hacks). Emphasis direction per node is by which number is red, not size.
The plate/objects never encode data (unlike S1009's labels-on-surfaces —
this family member deliberately lets scenes be atmosphere and stats argue).

VERIFY: title ≤15 words / 2 lines · red line asserts, ink line questions ·
1 emphasis hue (accent) + grays only elsewhere · every node has caption + both
stats · figure rule present · source line bottom-left with footnote (1) ·
runhead bottom-right "N | SECTION" · no node's caption collides with the plate
edge of its neighbour (pitch check).

DON'T: topic-line titles ("Crisis ownership themes") · stat pairs both gray or
both same number · 3+ objects per scene (wallpaper) · caption walls of text ·
orange/a second hue (source deck had orange gradient chrome — collapsed here
per one-accent rule) · dropping the C-suite/Non-C labels so numbers float.

SOURCE: PwC — "Crisis Preparedness as the next competitive advantage" (Global
Crisis Survey 2019), deck `pwc_strategy__pwc_crisis_preparedness_as_the_next_
competitive_advantage_le`, p09 (read on sw_sheets/pwc_strategy__pwc_crisis_
preparedness_as_the_next_competitive_advantage_le_s00.jpg — sheet floor(09/10)=0,
frames 5col×2row row-major → p08=row2 col3, p09=row2 col4), analysed in
reviews/pwc_strategy__pwc_crisis_preparedness_as_the_next_competitive_advantage_le.md
(lines 14,17,72: numbered chapters, Fig 5 split percentages 42/25/41/24/39/20,
isometric+callout infographic note). Palette from review line 54 (brand red
#E30613/#E1251B → rendered #D60A2C). Screenshot QA: qa/isometric-illustration/
scene-trio.png.
