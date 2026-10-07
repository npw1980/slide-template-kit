# org-hub-map-network — Partner-Universe Network Map (1280×720)

WHEN: Ecosystem / "network of networks" page: who the client connects to and *where* trust or value sits — partner universes, ecosystem plays, "advisor at the centre of a web" claims. The page's argument is adjacency, not hierarchy: a node is a *category you could plug into*, not a box on an org chart. Provenance: Accenture *2019 Global Financial Services Consumer* p25 ("What does this mean for financial providers?"), read from `sw_sheets/accenture__accenture_2019_accenture_global_financial_services_consumer__s02.jpg` (row 1, last cell): white page, claim column left (topic title + assertive lead), big violet ecosystem disc right with a central white advisor node ringed by ~16 small labelled nodes in a growth-inducing universe web, Figure-1 caption block, network-effect footnote.

ANATOMY (stage px; everything in the right-side full-stage SVG `viewBox="0 0 1280 720"`, SVG numbers == stage numbers):
1. `kicker` — x64 y38, width 396, 11px bold uppercase letterspaced, `N |` in accent.
2. `title` — x64 y62, width 396, 24/29 bold, 2-line gate (box 396×60, overflow hidden).
3. `lead` — x64 y134, width 390, 13.5/19 bold, accent colour (one sentence, the assertive claim line).
4. `body` — x64 y196, width 390, 11.5/16 gray-1, two paragraphs; `<b>` for the question pivot; `<sup>1</sup>` on the methodology phrase.
5. `fig` block — x64 y376, left-accent bar: `fig-tag` ("Figure 1", 12 bold accent), `fig-cap` 11/15.5 (the caption is a *sentence*, not a label), `fig-sub` 9.5 gray-note.
6. `fnote` — x64 y600, 9.5/13.5 gray-note under a hairline: the one-line mechanism claim ("Network effect: …").
7. `map` — full-stage SVG (disc occupies x582..1178 so the claim column never collides):
   7a. `disc` — `<circle class="disc" cx="880" cy="400" r="298">`, accent-soft fill (accent at its lightest).
   7b. tracks — `track-outer` dashed r=218, `track-inner` grey r=118, both centred D=(880,400).
   7c. `web` — ten adjacent-ring chord `<line>`s (deep purple, opacity .12) between successive outer nodes; decorative, see FILL 6.
   7d. `spokes` — 16 `<line class="spoke-in">`s from D to every node centre (nodes draw over them).
   7e. `hub` — central white disc r=56, accent ring; texts y376/398/416 (`hub-kick` "At the centre", `hub-name`, `hub-sub`).
   7f. outer ring nodes `node-1..node-10` `<g class="node" data-slot>`: circle r=9 + dot r=3 + label. Ring: angle_k = −90° + 36°·k, node = (880 + 218·cos, 400 + 218·sin):
       n1 (880,182) Retail · n2 (1008.1,223.7) Telco · n3 (1087.3,332.6) Media · n4 (1087.3,467.4) Energy · n5 (1008.1,576.3) Health · n6 (880,618) Transport · n7 (751.9,576.3) Hospitality · n8 (672.7,467.4) Public sector · n9 (672.7,332.6) Education · n10 (751.9,223.7) Utilities.
   7g. inner ring nodes `asset-1..asset-6`: circle r=7 grey, angle_k = −90° + 60°·k, node = (880 + 118·cos, 400 + 118·sin): (880,282) Payments · (982.2,341) Identity · (982.2,459) Marketplaces · (880,518) Rewards · (777.8,459) Trust scores · (777.8,341) Loyalty. Label = 13px below centre.
   7h. legend — two `tag` lines right-anchored at x1168, y128/144, inside the disc edge: "● partner category" / "○ connectable asset".
8. `footer` — `source` bottom-left x64 (gray-note, `<sup>1</sup>`), `pageno` bottom-right.

SLOTS (name — limit — good / bad):
- `title` — **≤15 words / 2 lines** (the narrow column clips a 3rd line). Interrogative/declarative claim ("Trust is the product — …"); a bare topic ("Ecosystem economics") belongs in the kicker, not the title.
- `lead` — ≤80 chars — the assertive Accenture-style claim sentence; one sentence only, it is the argument's headline.
- `body` — ~2×55 words — why the centre holds; second paragraph lands the *question* ("not how many, but which few").
- `hub-name` — ≤18 chars — the claim position ("Trusted advisor"), NOT the client's company name; `hub-kick` ≤16 caps; `hub-sub` ≤18 lowercase.
- `node-1..10` — ≤14 chars — partner *categories*, not firms ("Telco", not "Vodafone"); the source line must then say non-exhaustive/representative.
- `asset-1..6` — ≤12 chars — connectable assets; keep them generic-platform, they read as "the rest" so grey-on-grey is correct.
- `fig-tag/fig-cap/fig-sub` — 12 / ≤120 / ≤80 chars — caption is a full sentence naming what the disc *is*; fig-sub is the honesty line ("ring position carries no ranking").
- `fnote` / `source` / `pageno` — always present; source carries `<sup>1</sup>` for the compiled-from-public-disclosures claim.

FILL (build order, then resizing — the map must be re-plottable, not a picture):
1. Text first: `kicker/title/lead/body/fig-*/fnote/hub-*`, then node labels. All text is plain HTML text or `<text>` in SVG; replace inner text, keep tags and `data-slot` attrs.
2. Recolor: `--accent` alone — disc ground, hub ring, node rings/dots, spokes, lead, Figure bar follow. `--accent-deep` (chords) and `--accent-soft` (disc) are the SAME hue at depth/lightness — if you change the accent, set both by hand to keep them in-family (no auto tooling in plain SVG).
3. **Add an outer node (10 → 11):** copy any `<g class="node" data-slot="node-N">` and set `cx/cy` to the new ring point, angle = −90° + 360°/N·k (11-up: 32.7° steps). Add ONE `<line class="spoke-in" x1="880" y1="400" …>` to the spokes group. Optionally extend the web: two chords to its new neighbours — or skip chords entirely (FILL 6). Then give it a label with the side-aware rule: right half → `style="text-anchor:start"`, x = node.x + 15–25; left half → `end`, x = node.x − 15–25; straight up/down → middle, y ± (16–20). Keep labels ~20px clear of the node circle; if a long name would exit the disc (r=298), shorten it, don't let it cross the edge.
   - Honest cap: ~12 outer + 8 inner. Beyond that labels collide and the disc reads as static noise; group categories instead of adding nodes.
4. **Remove an outer node:** delete its `<g>`, its spoke `<line>`, and the two adjacent chords (grep the deleted node's coords — a chord still touching the hole is the classic leftover). The ring gaps stay even because positions are polar, not chained — nothing else reflows.
5. **Inner ring:** same procedure at R=118 (60° steps). Inner labels sit 13px below each node; keep inner names ≤12 chars or they cross the hub ring.
6. **The web is optional:** `<g id="web">` (chords) can be deleted wholesale without touching spokes/nodes/tracks — the figure still reads. It is what the source page's "universe" looks like, not load-bearing.
7. **Emphasis moves as a triple** on the hub (ring + kick + name). Beyond the hub, one *pair* is allowed: promote a single outer node by swapping its `class="node-out"` dot to solid — at most one; more solid dots = a scatterplot, not a hub map.
8. Retitle as a plain claim page: delete the `<svg class="map">` and widen `.body`/`.fig` widths to 1152 — nothing references the SVG.

CHART RECIPE (how this figure encodes):
- Encoding = centrality-by-construction: only the hub is solid; everything else is a ring/track member. Position on the ring means *category slot*, deliberately NOT value or ranking — say that in `fig-sub` like the template does.
- Two-tier truth: outer ring = things you could *partner with* (accent = the client's own universe), inner ring = *connectable assets* (grey = "the rest"). That is why the legend exists and why one accent is enough.
- Scale rules: disc r=298 fixed; rings 218/118 (keep ≥70px gap); spokes straight; no arrows — direction is implied by the hub. No area/size scales.
- One accent + grey: accent appears in lead, hub ring, node rings/dots, spokes, Figure bar; everything else is ink/gray ramp. The real deck's second highlight (azure) is NOT ported — see DON'T.

VERIFY:
- [ ] Title ≤15 words / 2 lines (clip box is 396×60).
- [ ] ≤2 hues: violet (+its deep/soft lightness = 1 hue) + greys. No cyan/azure creeping back.
- [ ] Hub is the only solid-accent element; node count == spoke count (grep `spoke-in`); chords touch only existing nodes.
- [ ] No label crosses the disc edge x>1178 or the left boundary x<582 near the claim column.
- [ ] Note-size text uses `--gray-note` (5.9:1); lead/white-on-accent checks: ink #1A1A1A on white, #7500C1 ≥7.6:1.
- [ ] Legend present when there are two node tiers; source + sup + page present.
- [ ] Resize proof: after FILL 3/4, every `data-slot="node-N"` group has a matching spoke line and no orphaned chord endpoints (`grep -c` both).

DON'T (corpus failure modes):
- Naming real firms on the nodes ("this is Vodafone") — categories only; the source page is a *universe*, not a partner list.
- Size-encoding nodes ("bigger = bigger market") — this page's claim is centrality, not magnitude; if magnitude is the story, switch to a bubble chart.
- Second highlight hue (the real deck's cyan) — breaks the one-accent gate; the deck's own persona colours stay out.
- SmartArt chevrons/balloons instead of the polar ring, or freehand dragging nodes off the tracks.
- Arrows on every spoke (a web, not an org chart with reporting lines) — the source disc is undirected.
- Ranking language (1, 2, 3… on nodes) while claiming non-ranking; one contradiction and the honesty line is dead copy.

SOURCE: Accenture — `accenture__accenture_2019_accenture_global_financial_services_consumer` p25; read 1:1 from `sw_sheets/accenture__accenture_2019_accenture_global_financial_services_consumer__s02.jpg` (row 1, col 5). Palette pixel-sampled from that crop: bright violet #7500C1 (dominant disc), deep purple #460074 (second dominant) on white ground; `reviews/accenture__accenture_2019_accenture_global_financial_services_consumer_.md` §color confirms the violet-dominant + azure-second system and §type the one-family house grotesque (display black weight, tight leading) — the Helvetica/Arial stack stands in. The deck's p25 lead style (topic title + assertive accent lead + Figure-1 caption + footnote) is reproduced structurally; cyan lead highlight was consciously dropped per kit one-accent rule. Kit ground rules from DESIGN_PLAYBOOK (2-line title gate, footer anatomy, honest placeholders, one accent + grays).
