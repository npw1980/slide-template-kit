# isometric-illustration-cutaway — Labeled 3D Cutaway of a Reference Stack

WHEN: An architecture / target-state page whose exhibit IS the object: a
cutaway 3D structure with capability labels pinned to the surfaces they live
on. From the isometric-diagram family in the catalog (S1009 "technical-
isometric-diagram", S1476 "diagram-isometric") — real diagrams drawn in true
2:1 isometric with ray lines and pinned callouts, the anti-SmartArt device.
Use when the story is "where things sit", not "how much vs how many".

ANATOMY (1280×720 stage px):
1 kicker      "EXHIBIT 2 · TARGET ARCHITECTURE" (64,60), 11px, +14% tracking, gray-2
2 title       30px bold ink, 1 line — baseline y=104, x=64
3 sub         12.5px gray-1 one-liner — y=130
4 scene       `<g id="scene" transform="translate(620,378)">` — the whole object.
   Inside it, mapping is FIXED: screen(x,y,z) = (x−y, (x+y)/2 − z).
   Elements: ground slab; two back walls (open front = the cut-away side);
   4 layer plates (flat iso rects stacked in z); 2 gray service `<g class="box">`;
   1 accent box (`class="box"` w/ `a-*` faces) sitting in the open front;
   dashed ray lines + floor arrows + one accent exit arrow.
5 callouts    6 × `<g class="call">` in STAGE space: leader line (2-point or
   elbow polyline) + anchor dot + 1–2 lines of label text
6 source      bottom-left (64,694) with footnote (1)
7 runhead     "4 | ARCHITECTURE" bottom-right (1216,694)

SLOTS:
- kicker/title/sub: claim title — 1 line ≤15 words ("Real-time ingest replaces
  the nightly batch"). The title names the CHANGE; the diagram shows where.
- sub: names the count ("four in-shell layers + two side services") so the
  reader can audit the object against the sentence. If you add a box, add it
  to this count.
- box (feature): one `<g class="box">` = 3 faces (f-top/f-r/f-l or a-top/a-r/a-l).
  Faces ARE the data: size/position = where the capability sits in the stack.
- call: label (12.5px bold) + optional micro-line (10.5px). One callout per
  box/feature; the emphasized feature's call is the ONLY `t-lab-a` accent one.
- exit arrow: exactly one, accent — the "so what" leaving the object.
- source/runhead: real strings.

FILL (add/remove nodes — which group to copy, what reflows):
1. ADD A FEATURE: (a) copy one `<g class="box">` block inside `#scene`; (b)
   recompute its 4×3 face corners from the box params (x0,y0,w,d,h) with the
   mapping above — worked example: box x0=−92,y0=−62,w=46,d=34,h=36 gives
   f-top `-30,-113 16,-90 -18,-73 -64,-96`, f-r `16,-90 16,-54 -18,-37 -18,-73`,
   f-l `-64,-96 -18,-73 -18,-37 -64,-60` (each face: the four corner points
   (x0,y0,h),(x1,y0,h),(x1,y1,h),(x0,y1,h) fed through screen()). x1=x0+w, y1=y0+d.
   (c) copy a `<g class="call">` block, move its text into a free label zone,
   set the leader's far end onto a face point of your new box, and the dot at
   (box-anchor + translate(620,378)).
   NOTHING reflows automatically — leaders and labels are manual. Reflow check
   rule: labels live outside the object's screen bbox x∈[391,865] y∈[180,520]
   or above/below it; leader elbows run horizontal-then-diagonal (see C1/C3).
2. REMOVE A FEATURE: delete its `<g class="box">` AND its `<g class="call">`;
   update the count in the `sub` line; leftover dashed plates/rays: if a layer
   plate becomes empty, delete the plate polygon group too.
3. EMPHASIZE A DIFFERENT BOX: swap faces f-top/f-r/f-l → a-top/a-r/a-l and move
   the `t-lab-a` class to that box's callout label (keep exactly one).
4. STACK LAYERS: the 4 layer plates are flat iso rects offset by ~16px screen-y
   each (`-96,-76 …` → `-72,-88 …`); to make 3, delete the top plate + its dash
   outline and re-pin C1's leader end. To make 5, add a plate at z-offset −8.
5. RECOLOR: one token — `--accent` (+ `--accent-1` tint = its 20% mix). The
   gray ramp is fixed; recoloring the ramp to a second hue is forbidden.

CHART RECIPE: This is not a data chart — encoding is POSITION. Rules that keep
it a diagram, not clip-art: walls meet on the shared back corner (2:1 dimetric,
18°-ish slopes, never 45°); boxes sit ON the floor plane (z=0 base) unless they
are layer plates (flat quads at constant z); light source fixed at upper-left
so top faces are white, right faces darker than left; ray/flow arrows run
along the iso axes only; exactly ONE feature is accent-colored and it must be
the one the claim is about — everything else is gray. No shadows, no gradients.

VERIFY: title ≤15 words / 1 line · counts in `sub` match visible boxes ·
exactly 1 accent box + 1 accent callout + 1 accent exit arrow · no callout
text overlaps the object bbox · leaders end on real face points (visible dot) ·
source line + footnote (1) present · runhead "N | SECTION" · contrast: gray-1
12.5px labels on white ≥7:1, accent #2E4374 8.8:1 ✓.

DON'T: labels floating unanchored (the whole point is pinned text) · a second
accent hue "to tell layers apart" (use z-position + hairlines instead) ·
45°/perspective cheating the 2:1 mapping (faces stop reading as one object) ·
gradient shadows — dated S1009-style ray "glow" (use plain dashes) · box walls
of 8+ features (this template tops out at ~6; more means a different template) ·
title that just labels the diagram ("Target architecture") instead of claiming.

SOURCE: Catalog S1009 (`catalog_101-134.csv`, arch "technical-isometric-
diagram"), read on corpus/sheets/sheet_101.jpg frame 9 (sheet ceil(1009/10)=101,
5col×2row row-major → frame 9 = row 2 col 4): sun-angle ray lines, Solar PV
@42°, thermal mass / cross-ventilation callouts pinned to a cutaway building.
Sibling archetype S1476 (`catalog_135-167.csv`, "diagram-isometric", sheet_148
frame 6). Neither has a reviews/*.md file, so the palette is NOT firm-evidenced:
the kit's default accent (#2E4374, 8.8:1 on white) + gray ramp was chosen per
the one-accent/gray rule, and the source's multi-hue labels were collapsed.
Screenshot QA: qa/isometric-illustration/cutaway.png.
