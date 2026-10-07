# org-hub-map-orbit — Capability Orbit Hub (1280×720)

WHEN: Capability / operating-model page where "X works only as a whole": a target operating model, a platform-hub story, one strategy ringed by the capabilities that must move together. Provenance: PwC Strategy *Insurance Reimagined — Spotlight on Trust, Convergence and Competition* p18 ("Adaptive ways to reimagine your business"), read from `sw_sheets/pwc_strategy__pwc_insurance_reimagined_spotlight_on_trust_convergence_and__s01.jpg` (row 2, centre cell): white ground, hub disc ringed by white satellite discs (icon + name + one-line description), claim line under the kicker, firm red as emphasis.

ANATOMY (numbered slot map, stage px; all diagram coords live inside the full-stage SVG `viewBox="0 0 1280 720"` so SVG numbers == stage numbers):
1. `kicker` — x64 y36, 11px bold uppercase letterspaced; leading `N |` in accent.
2. `title` — x64 y58, width 1152, 30/36 bold, 2-line max (box height 76; overflow hidden — a 3rd line is clipped, fix the text).
3. `lead` — x64 y150, width 860, 15/21 semibold `--gray-1`; one phrase wrapped in `.em` (accent).
4. `diagram` — full-stage SVG:
   4a. `orbit` — dashed track `<circle cx="640" cy="418" r="198">`.
   4b. `spokes` — five `<line>`s from hub edge to satellite edge: start `640+88·cosA, 418+88·sinA`, end `640+142·cosA, 418+142·sinA` (A per node below).
   4c. `hub` `<g id="hub">` — white disc r=88 accent ring at C=(640,418); texts at y394/418/436 (`hub-kick` / `hub-name` / `hub-sub`).
   4d. `sat-1..sat-5` `<g class="sat" data-slot="sat-N">` — circle r=56 + icon `<g class="icon" transform="translate(cx,cy)">` + `sat-name` at (cx, cy+75) + `sat-desc` at (cx, cy+91). Positions (R=198, angle_i = −90° + 72·i):
       sat-1 (640.0, 220.0) · sat-2 (828.3, 356.8) · sat-3 (756.4, 578.2) · sat-4 (523.6, 578.2) · sat-5 (451.7, 356.8).
5. `footer` — hairline x64..1216 y698; `source` bottom-left 10/13 `--gray-note`, `<sup>1</sup>` for the n= claim; `pageno` bottom-right, page number bold ink.

SLOTS (name — limit — good / bad):
- `kicker` — 55 chars — section marker. Kicker-wall text is a corpus flaw.
- `title` — **≤15 words / 2 lines** — an assertion ("…decide whether the operating model holds"); "Operating model" topic-title fails the gate.
- `lead` — ≤115 chars, one line — the so-what sentence under the title, not a second paragraph; exactly one `.em` accent phrase.
- `hub-name` — ≤22 chars — the *claim target* ("One operating model"); `hub-sub` ≤34 — "what it takes" line; `hub-kick` — 8–16 caps ("At the centre").
- `sat-1..sat-5` — name ≤20 chars + description ≤40 chars — name = capability *family* (noun), description = the mechanism ("one data estate, shared models"), not marketing fluff. ≥1 description should carry a number.
- One satellite carries the emphasis triple (default sat-2 `Data & analytics`). Two louder satellites = a colour wheel, not a point.
- `source` / `pageno` — always present; sup marker wherever n= or methodology appears.

FILL (build order, then resizing — this diagram must be editable, not a picture):
1. Text first: `kicker`, `title`, `lead`, `hub-*`, each sat's `sat-name`/`sat-desc` (and sat-3's spoke `class="spoke"` if emphasis moves). Replace inner text only; keep tags, classes, data-slot attrs.
2. Recolor the accent: change `--accent` only — hub ring, emphasized sat-hi (ring+icon+spoke), `.em`, kicker `N |`, lead all follow. `--accent-soft` is the highlight disc fill: keep it a same-hue pale; if the new accent is dark, keep `#FFFFFF` disc fill.
3. **Rename / retag a satellite:** edit its two `<text>`s. Circle and icon never need moving. Swap an icon by replacing the shapes inside that sat's `<g class="icon" translate(...)>` — every icon lives in local coords around (0,0), so any 20×20 mark fits (line/circle/rect/path; stroke inherits the sat's colour).
4. **Remove a satellite (5 → 4):** delete the sat's `<g>` **and** its spoke `<line>`; set the orbit circle's `r` to the new R; place 4 sats at 0/90/180/270 from straight up: C=(640,400), R=195 → (640,205) (835,400) (640,595) (445,400). Recompute every spoke with the formula using 88/139 instead of 142 (hub r and sat r may change). Labels stay at cy+75/+91 per sat.
5. **Add a satellite (5 → 6):** copy one `<g class="sat">` wholesale, edit its `data-slot`, its circle cx/cy, and its icon translate — *then re-space all satellites* (6 at 72° collide on the ring): 6-up geometry C=(640,410), R=180 → (640,230) (795.9,320) (795.9,500) (640,590) (484.1,500) (484.1,320), sat r 56→52, hub r 88→84 (spokes start at +84). The two bottom satellites land near the footer: keep their `sat-desc` (baseline ≤691 is still clear of the hairline at 698) or drop the desc and keep only the name at cy+72.
   - General formula for N nodes: angle_i = −90° + 360°/N; cx = Cx + R·cos(angle), cy = Cy + R·sin(angle); spokes run C + hubR·u → C + (R−satR)·u; orbit circle r = R. Keep satR ≥ 48 and R ≥ 170 or the ring reads as a cluster.
   - Max sane density on this canvas: 7; at 8 the bottom labels collide with the footer — either shrink descriptions to name-only or switch templates.
6. Reflow notes: nothing moves by itself except the emphasis triple. The diagram is absolute SVG — adding/removing means editing group + matching spoke, and (N≠5) re-spacing *all* satellites because the angles change.
7. Independent of the diagram: sat labels/lead are text; if the claim works without satellites, delete the SVG and widen nothing else — the page still stands as claim-page + kicker.

CHART RECIPE (how this figure encodes):
- Encoding = membership on a ring: every satellite is equidistant from the hub by construction — the figure says "same claim, different capabilities", not "more/less of it". If you need emphasis-by-size, make one satellite r=72, not bigger-by-eye.
- Tone: satellites are one grey family (white disc, #C9C9C9 ring, grey icons) — set colour would say "different kinds of member". The one accent satellite is a *triple* (disc ring + icon + spoke) so the emphasis is unambiguous.
- The hub is the only ring with an accent outline: it marks the claim itself, never a category.
- Labels: name below, description below that, both centered under the node (text-anchor middle) — never a leader line from label to node.

VERIFY:
- [ ] Title ≤15 words / ≤2 lines (h1 box is 1152×76; overflow hidden — if you see 2 lines but clipped descenders, fix text).
- [ ] One emphasis hue: accent + greys only (≤2 hues total on page).
- [ ] Exactly ONE satellite carries sat-hi/icon-hi/spoke-hi.
- [ ] Orbit circle `r` equals the sat ring radius R you actually used (grep both numbers).
- [ ] Each spoke's second point stops at that sat's near edge (R−56), not at its centre.
- [ ] Note-size text uses `--gray-note` (5.9:1); text on accent white≥6.6:1.
- [ ] Source line + `<sup>1</sup>` + page number bottom-right.
- [ ] Resize proof: after following FILL 4/5, grep `data-slot="sat-` — count of sat groups == count of spoke lines, orbit `r` matches, no orphan `<line>`s pointing at empty space.

DON'T (corpus failure modes):
- One hue per satellite ("blue = ops, green = product") — that is a legend, not an argument.
- Topic sat-names with fluffy descriptions; the mechanism line is what makes it a consulting exhibit.
- Hub text as a logo/brand name — the hub slot is the *claim*, not the client.
- Leader lines, drop shadows, or 3-D bevels on the discs (SmartArt residue; the source page is flat hairlines).
- Putting the caption/source inside the diagram band on a white page.
- A 9-node ring because "the framework has nine elements" — cap at 7, cut or group the rest.

SOURCE: PwC Strategy — `pwc_strategy__pwc_insurance_reimagined_spotlight_on_trust_convergence_and` p18; read 1:1 from `sw_sheets/pwc_strategy__pwc_insurance_reimagined_spotlight_on_trust_convergence_and__s01.jpg` (row 2). Palette cited from `reviews/pwc_strategy__pwc_insurance_reimagined_spotlight_on_trust_convergence_and_.md` §color: PwC brand red bands ≈ #A6192E–#C1272D (token set to #A6192E), grey ramp #D9D9D9 / #8C8C8C / #404040, white ground, body text #333333 (review notes hexes are eyeballed from JPEG, ±10% — good enough for tokens). Font fact: PwC Propers (Helvetica-family grotesque) — the Helvetica Neue/Arial stack stands in per kit rule; note the review's "red/orange/yellow + charcoal" — the second (orange) accent was deliberately dropped to keep the one-accent gate. Structure (hub + satellites + claim lead under kicker) follows the p18/p19 hub pages; kit ground rules from DESIGN_PLAYBOOK (2-line title gate, footer anatomy, one accent + grays).
