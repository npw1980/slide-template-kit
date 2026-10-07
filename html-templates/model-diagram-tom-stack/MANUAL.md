# model-diagram-tom-stack — Target operating model: layer stack + callout leaders

WHEN: The "one-page operating model" page — a full management system (vision,
processes, organisation, technology, performance, people, governance) drawn as
a vertical stack of named layer bands, detail columns under the expandable
layers, and claim callouts in the margins joined by leader lines. Straight from
PwC's Treasury target-operating-model page (deck + page in SOURCE). This is the
kit's answer to "this diagram had to be drawn, not found in SmartArt."

ANATOMY (stage 1280×720, all numbers px):
1  kicker          x64  y34   "N | SECTION" (section index in accent)
2  claim title     x64  y56   2-line slot, clip-gated
3  lead line       x64  y144  one sentence, one accent span inside
4  layer stack     x318..962 (W 644). Bands: Vision y178 h30 (accent),
   Processes y216 h24, Organisation y470 h24, Technology y576 h22 (EMPHASIS,
   accent), Performance y604, People y630, Governance y656 (each h22, pitch 26)
5  detail block A  4 columns under Processes, y246..458, x 318/481/644/807 w155
6  detail block B  3 columns under Organisation, y500..562,
   x 318/535.3/752.6 w209
7  callouts        3 left chips x66 w192 + 3 right chips x1024 w192, each with
   a two-segment leader line + accent dot at the band edge it targets
8  hairline        y682;  9 source line x64 bottom;  10 page stamp bottom-right

SLOTS (name, max, good/bad):
- kicker: "N | SECTION", ≤ 4 words after the pipe — section index, not a phrase.
- title: action title ≤ 15 words / ≤ 2 lines (a 3rd line is clipped by design).
  GOOD: "Technology is what makes a single Treasury operating model possible" —
  a directional claim the stack itself proves. BAD: "Target operating model" —
  topic label; the source page's own title is graded PARTIAL in the review for
  exactly this, so the slot must stay claim-shaped.
- lead line: bridge sentence, one accent span max, ≤ 2 lines.
- band-name (×7): ≤ 5 words, noun phrase for the layer. The stack must
  MECE-cover a management system — invented layer names break the diagram.
- col-head: ≤ 4 words uppercase. col-bullet: 3–8 bullets ≤ 11 words each;
  worst plausible fill is shown in columns cash/corporate-finance (2-line wraps).
- callout kicker: the layer targeted (1 word). callout title ≤ 6 words, a claim.
  callout body ≤ 3 lines / ~150 chars.
- source-line: dataset + n + what "target" means, with footnote markers.

FILL (step by step — build instructions for their page):
1. Replace header text: kicker div, h1.title, p.lead (keep the `<span class="em">`).
2. LAYER STACK — each band is one `<g class="band" id="band-...">` holding a
   rect (x318 w644) + `<text class="band-name">`.
   ADD A LAYER: copy any plain grey band group (e.g. `#band-performance`),
   paste it below its intended position, then shift EVERY band below it and the
   two detail blocks down by +26 (each rect y, band-name y). If 8+ bands exceed
   the stage, shrink the detail-A columns (rects `height="212"`) instead of
   overlapping bands. REMOVE A LAYER: delete its `<g>`, shift the ones below up
   by 26.
3. DETAIL COLUMNS — `#detail-processes` and `#detail-org`; one column = one
   `<g class="dcol">` (bg rect + col-head + col-bullet tspans).
   ADD A COLUMN: copy a dcol; set its x = 318 + k·(colW+gap) and its width =
   (644 − (n−1)·gap)/n for n columns (gap 8), then re-sweep every sibling's x
   and rect width to the new equal grid (block A: cols y246 h212; block B:
   y500 h62). REMOVE: delete and widen the rest to the new grid.
   BULLETS: inside col-bullet, add `<tspan class="b" x="X" dy="12">▪</tspan> text`
   lines (wrap continuations with their own tspan keeping x).
4. CALLOUTS — one `<g class="callout">` = chip rect + 3 texts + leader path +
   dot. ADD: copy a group; set the chip y and its three text ys by the same
   delta; edit the leader `d`: LEFT chips run M(258→278→down to target y→318),
   RIGHT chips run M(1024→1004→down→962); dot at (318, ty) or (962, ty). Keep
   verticals in the free channels x=278 / x=1004 and never cross a chip. Two
   callouts must not share one target y. REMOVE: delete the group — nothing
   reflows.
5. RECOLOR: swap `--accent` + `--accent-soft` at `:root`; vision band,
   technology band, dots, col-head, kicker pipe follow. Greys stay. Do not
   recolor grey bands.

CHART RECIPE (diagram encoding):
- "One accent + gray" here means: grey for what the model IS (layers, columns,
  chips), accent for what the ARGUMENT adds — vision band + technology band +
  leader dots + title pipe. Exactly one hue, two spots of fill.
- Leader lines: 1px grey, orthogonal two-segment (out horizontally 20px, down/
  up channel, in horizontally to band edge). Never diagonals, no arrowheads —
  the dot marks the anchor.
- Emphasis rules: the emphasized layer band is accent-filled with white text;
  if your claim sits elsewhere (e.g. People), move the `band-emph` class, don't
  add a second hue.
- Units: none needed (structural diagram); if you add figures inside bullets,
  put them in bold inside the tspan, not as a legend.

VERIFY:
[ ] title ≤ 15 words / 2 lines — confirm nothing clipped by the h1 overflow gate
[ ] layer stack: vision + ≥ 5 real layers; Processes and Organisation expanded
[ ] source line present bottom-left with n; footnote sup markers wherever the
    page claims "target"/"illustrative" content
[ ] exactly one hue (accent fills + grey ramp) — ≤ 2 fill spots of accent
[ ] white text on bands clears 4.5:1 (band grey #6E6E6E and accent #B23A00 do;
    re-verify after any recolor)
[ ] page stamp bottom-right present, page number plausible

DON'T:
- Don't substitute SmartArt / clip-art chevrons. The source page is in the
  reviews precisely because it's a drawn system; layer bars + detail columns
  ARE the diagram.
- Don't leave layers as topic labels only — Processes and Organisation must
  carry real sub-content, or the page reads as an empty org chart.
- Don't run more than 6 callouts or send two leaders to the same target y; the
  channels x278/x1004 are only that wide. (The original crammed 8 — redraw wins.)
- Don't "color-code" layers blue/green/green/yellow. Red = claim, grey = rest.
- Don't let the kicker wall-of-text in: it's a section index, ≤ 4 words.

SOURCE: PwC Strategy, "2019 Global Treasury Benchmarking Survey" (Digital
Treasury), p11 "Technology as core component of the Treasury target operating
model". Read from
`sw_sheets/pwc_strategy__pwc_2019_global_treasury_benchmarking_survey_2019_s01.jpg`
(sheet index floor(11/10)=1, frame row 1 col 1), visually confirmed: red banner
+ stacked grey layer bars, 4 Processes detail columns, 3 Organisation columns,
8 margin callouts with leader lines, `PwC | 2019 Global Treasury Benchmarking
Survey | 11` footer (kit draws 6 callouts — the redraw the review calls for).
Analyzed in
`reviews/pwc_strategy__pwc_2019_global_treasury_benchmarking_survey_2019.md`
(reusable item #7: "TOM nested box tree with margin callouts — needs redraw; the
original is dense"; §Color system for the hexes; §Action titles grades the page
itself PARTIAL — the slot rules above fix that). Real fonts: PwC Humanist 777 /
Bower for display, Calibri for body; Georgia + Arial stacks stand in. Palette:
brand red ≈ #D04A02 (darkened to #B23A00 for AA body text), greys #D9D9D9 /
#F2F2F2, near-black #1A1A1A, gold gutter band noted in the deck (not carried
over — kit standardizes margins).
