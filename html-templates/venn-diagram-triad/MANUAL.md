# venn-diagram-triad — Three-Set Venn with Intersection Claim (1280×720)

WHEN: Capability / framework page where an argument lives in an **overlap**, not in the sets: "X happens where A, B and C meet", three-party operating models, competency mindsets, ecosystem fit. Provenance: EY *Academic Resource Center — Analytics Mindset* (2019) p10, read in `sw_sheets/ey__ey_ey_academic_resource_center_mission_2019_s00.jpg` row 2 — bullets left, 3-circle Venn right, yellow callout chip fanning connectors into the overlaps, triple intersection filled solid yellow.

ANATOMY (numbered slot map, 1280×720 stage px):
1. `kicker` — x64 y36, 12/14 bold uppercase letterspaced 1.8, `04 | Section` in accent.
2. `title` — x64 y60, width 1152, 31/42 bold white, 2-line box (max-height 84); `<sup>1</sup>` footnote marker.
3. `bullet-1..6` — rail x64 y166, width 560, six lines 14/19.5, yellow wedge marker via `::before`, ~37 px pitch.
4. `venn` — x676 y110, 540 × 530, inline `svg` viewBox `0 0 540 530`, 1:1 mapping.
   4a. `#sets` — three `<g data-slot="set-a|b|c">`, each one visible `<circle r="150">`; centres (270,203) / (186,348.5) / (354,348.5) = radius 97 from C=(270,300) at 120°, C at (270,300).
   4b. intersection — nested `clip-path` groups (clip-a › clip-b › clip-c) over a full-viewBox accent rect: solid accent exactly where all three discs overlap.
   4c. `callout` — accent chip 240×35 at (150..390, 61..96) + three 1.6px connector lines to (228,264), (312,264), (270,346) — the pairwise lens centres — each capped by an accent dot.
   4d. `label-a|b|c` — `<text>` pairs at (270,115/131), (150,410/426), (400,410/426), text-anchor middle: name 15.5 bold white + role tag 12 gray-2.
5. footer — `lockup` x64 y~688 (letter-spaced caps, hairline rule right), `source` 10/13 gray-3 max-width 640 with `<sup>1</sup>`, `runhead` right: `page` bold + section.

SLOTS (name — limit — good / bad):
- `kicker` — 55 chars — section marker. A kicker wall of text is the corpus flaw.
- `title` — **≤15 words, 2 lines** — asserts *what the overlap produces* ("works only when … move together"); "Three-circle Venn" topic-title fails.
- `chip` — ≤26 chars — names the intersection ("The analytics mindset"); the claim is the chip, the page then explains it.
- `label-a|b|c` — 22 + 13 chars — role **name** + role **type** tag; the parenthetical (consumers/producers/enablers) is what stops this being three random bubbles.
- `bullet-1..6` — ≤95 chars each (2 lines max) — one per "how the mindset is built"; at least one numeric; a two-line bullet is expected fill, not an emergency.
- `lockup` / `source` / `page` — always present; source line carries the footnote where "n = 41 modules" is a methodology claim.

FILL (build order, plus resizing — the diagram must be editable, not a picture):
1. Text first: `kicker`, `title`, six `bullets`, three `label-*`, `chip`. All text nodes are `data-slot`; replace inner text, keep tags/classes.
2. Accent change: recolor `--accent` (chip, connectors, wedge markers, intersection fill) and, if the new hue is dark, `--ink-accent` stays the dark navy on it. `--bg` is the brand field, not an accent slot.
3. **Rename / retag a set:** edit the `label-*` text pair; the circles and clips never move. One set carrying the argument alone? Give it `fill-opacity=".45"` on its visible circle only — one louder set, same palette.
4. **Remove a set (3 → 2 Venn):** delete `set-b`'s `<g>` and `label-b` **and** one clip level: flatten the intersection from `clip-a›clip-b›clip-c` to `clip-a›clip-c` (drop the inner `<g clip-path="url(#clip-c)">` wrapper… precisely: keep `clip-a` outer and `clip-c` inner by editing the nested groups, deleting the `<g clip-path="url(#clip-b)">` element itself). Then move the remaining discs toward symmetric pair geometry: centre A (215,300), centre C (325,300), r=150, and edit `<defs>` circle cx/cy to match — the lenses, accent lens shape and chip connectors then land automatically because they are clipped, not drawn. The third connector line/dot comes out with the set.
5. **Add a set (3 → 4):** copy one `set-*` group, set `cx="270" cy="445"` (120° spacing fails; four sets sit at 45/135/225/315° — re-space all four to centres (187.7,202.5)/(352.3,202.5)/(187.7,397.5)/(352.3,397.5) at r=150, d≈118 from C) — copy the `<circle>` into `<defs>` as `clip-d` and nest it innermost (`clip-a›clip-b›clip-c›clip-d`), then re-point the three connectors at the new pairwise lens midpoints ((270,203±… use midpoints of centre pairs) and add a fourth `label-*`. **Honest warning:** a 4-disc Venn cannot show *every* region like a 4-ellipse public-set diagram; if the page's argument is region-by-region comparison, this is the wrong template — switch to a grid.
6. Reflow notes: nothing reflows by itself except the clip-carved region — circles, chip, connectors and labels are absolute SVG coords, so **each** added/removed disc means editing its group + `<defs>` entry + connector pair, and the label offset goes outward from each new centre (centre − C, scaled ×1.35).
7. Left rail is independent: bullets are `<li>` in normal flow — add a 7th, the stack grows down from y166 (cap at 8 before the footer band; beyond that cut text, don't shrink font below 13 px).
8. Swap the whole diagram for a 2-column text page: delete the `svg` and widen `ul.bullets` to `width:1152rem` — no other element references it.

CHART RECIPE (how this figure encodes):
- Encoding = membership: a concept is "in" to the extent it sits in that disc; the overlap is where the argument lives. No areas are scaled to values — say so in the source line if data people read the page ("circles are conceptual, not to scale").
- Tone: all three discs the same gray-4 tone at fill-opacity .33; overlaps brighten by stacking (.55 pairs / .70 triple). One tone on purpose — set *color* would say "different kinds of member".
- Emphasis: accent appears as solid only in the triple region + chip + connectors. White text on gray-4 fills (5.5:1+); dark navy on yellow (10.4:1). Never put gray-3 text inside a disc.
- The chip claims, the connectors *prove* the claim is about intersections — that wire is what separates this from SmartArt. No connectors = three floating circles.
- Region micro-labels: none. Pairwise lenses stay unnamed unless a pair alone carries the story (then: one dot, no new fill).

VERIFY:
- [ ] Title ≤15 words / ≤2 lines (`h1.title` box is 84 tall; a third line is overflow).
- [ ] One emphasis hue (accent + grays + white on navy; ≤2 hues total).
- [ ] Intersection solid, chip wired with exactly one connector per remaining set.
- [ ] Each label inside its disc and clear of lenses (test: does the text survive if that disc's fill is hidden?).
- [ ] Text-on-accent 10.4:1; body on `--bg` ≥4.5:1.
- [ ] Source line present, `<sup>1</sup>` present, page number bottom-right.
- [ ] Resize proof: following FILL 4 leaves a clean 2-set lens with no orphan clip defs (grep for `clip-b` — must be gone).

DON'T (corpus failure modes):
- Labeling every region of the Venn with its own caption — the EY page labels nothing in the lenses; labels there are SmartArt residue.
- One disc per stakeholder hue ("blue = finance, purple = product"): that is a colour wheel, not an argument.
- Topic titles ("Analytics mindset"), kicker walls, 8+ bullets of one line each.
- Drawing the intersection as a hand-kerned yellow triangle — here it is clipped geometry so it follows the discs.
- Shadow gradients inside the circles (the original deck's one cliché; deliberately not ported).
- Putting the source line *inside* the exhibit area on a dark page.

SOURCE: EY — `ey__ey_ey_academic_resource_center_mission_2019` p10; read from `sw_sheets/ey__ey_ey_academic_resource_center_mission_2019_s00.jpg` cell (row 2, last) at 1:1; colors sampled from the crop: field #264F83, EY yellow #FDE700, gray-2 #A8BCD8. Slide row: `reviews/ey__ey_ey_academic_resource_center_mission_2019_slides.csv` p10 ("3-circle Venn + title/bullets", "white, grey/blue circle tones, yellow highlight box"); analysis `reviews/ey__ey_ey_academic_resource_center_mission_2019.md` §mineable devices item 7 ("Venn diagram p10: business analysts / analytics modelers / analytics architects with yellow 'analytics mindset' callout box") and its brand section (single accent hue + grey system, EY FOUNDATION lockup + page number). Font fact: EY House Sans (Helvetica-family) per the review's typography section — the Arial/Helvetica stack stands in. Kit ground rules from DESIGN_PLAYBOOK (one accent + grays, footer anatomy, 2-line title gate). The corpus "2-circle venn" row S00638 was checked and is a stock photograph (`corpus/sheets/sheet_064.jpg`), not a diagram — not used.
