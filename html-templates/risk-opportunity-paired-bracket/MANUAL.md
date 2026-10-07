# risk-opportunity-paired-bracket — Risk ↔ Opportunity Pair Ladder

WHEN: A risk page that has to argue, not list — every material RISK is bracketed across a
"response lever" gutter to the OPPORTUNITY it converts into. Use it when the ask is "what do
these exposures buy us if we act?" (post-workshop risk-to-value, portfolio response pages,
CEO/CFO outlook risk sections). Evidence: `kpmg__kpmg_genai_survey_2024_key_insights_2024`
p9 (risk items drawn as ranked tracks over grey, one value numeral per item —
`sw_sheets/kpmg__kpmg_genai_survey_2024_key_insights_2024_s00.jpg`),
`kpmg__kpmg_kpmg_2022_ceo_outlook_2022` p5 (numbered risk list + "Source:" line under every
exhibit — `sw_sheets/kpmg__kpmg_kpmg_2022_ceo_outlook_2022_s00.jpg` row 1 col 5), and
`pwc_strategy__pwc_boardroom_agenda_2022` p26 (numbered blocks whose own copy reads
"Risks/opportunities identified over short/medium/long term" —
`sw_sheets/pwc_strategy__pwc_boardroom_agenda_2022_s02.jpg`).

ANATOMY: numbered slot map, px on the 1280×720 stage (1rem = 1 stage px; SVG user-units are
the same px because the overlay maps `0 0 1280 720` onto the stage):
1. `kicker` — "04 | Risk & opportunity — conversion view", x:64, y:36, 11.5px caps, tracking
   .2rem; the section digit is `.n` (accent).
2. `title` (h1) — claim title, x:64, y:56, width 696, 27/34px, navy `--ink`, letter-spacing
   -.3rem; trailing `sup` footnote marker.
3. `strip` — 3 count figures, right-aligned ending at x:1216, y:56; each `.fig` 25px + `.lab`
   8.5px caps. The page's own roll-up; outside the diagram loop.
4. `hdr` — column headers: "Risk — what could go wrong" x:64, "Response lever" centred x:640,
   "Opportunity — what we can claim" x:856, all baseline y:176. Right header carries `.sub`
   (accent) because the opportunity side is the emphasis.
5. `frame` — hairline rule y:186 (x 64→1216) + gutter spine `line` x:640, y 196→628.
6. `pair` ×N — one per risk/opportunity conversion, default 4. Row CENTRES y = 242 / 354 /
   466 / 578 (pitch 112). Each pair spans: risk block x:64..424 (360 wide), gutter 424..856
   with the knot at x:640, opportunity block x:856..1216 (360 wide). Block height 92 = centre ±46.
   6a. `risk-box` rect 6a. `rank-box` x:76 w:22 + `.rank` id text 6a. `.r-head` text x:106
   (2 lines via one `tspan`) 6a. `sev-box` pill x:366 w:46 + `.sev` 6a. `.sev` trend line.
   6b. `conn` path (M424 0 H616 M664 0 H856) 6b. `knot` rotated square centred (640,0)
   6b. `lever` text centred x:640 y:-24.
   6c. `opp-box` rect x:856 6c. `.o-head` x:876 (2 lines) 6c. `.o-val` x:876 y:28 with a
   `.o-cap` suffix.
7. `footrule` y:676, `source` bottom-left (x:64, 10px, `sup` markers), `pageno` bottom-right.

SLOTS:
- `title` — max 15 words, 2 lines at 27px/696px (~92 characters). Must be a judgement with a
  count in it ("Three of the four paired risks carry priced upside; two fund their own
  mitigation"), never a topic ("Risk register"). If it breaks to 3 lines, cut words; do not shrink the type.
- `strip.fig` ×3 — short figures (18 / 4 / 2 as shipped). 6 glyphs max per figure at 25px. The label
  under each is ≤12 chars; the middle one is `.accent` because it is the page's argument.
- `pair[i].rank` — R1, R2… exactly 2 glyphs. The numbering IS the reading order.
- `pair[i].r-head` — 2 lines × ~34 chars, verb-shaped ("Talent scarcity in four key markets").
  Bad: a bare noun ("Talent"). The line names what happens, not what it is called.
- `pair[i].sev` — HIGH / MED / LOW in the pill (≤4 chars) + a trend word below ("↑ 3 mo",
  "→ flat"). Two separate marks: how bad, and which way it is moving.
- `pair[i].lever` — 1 line, ≤26 chars, a verb phrase naming the move ("Automate 3 workflows",
  "Reprice + bundle"). This is the slot most people forget: without it the page says "bad
  thing → good thing" and is SmartArt.
- `pair[i].o-head` — 2 lines × ~34 chars, the claim in plain language with its number embedded.
- `pair[i].o-val` — the payoff figure (19px, accent) + `o-cap` (≤18 chars, "contribution p.a.").
  A number with no comparator is decoration; the caption is the comparator.
- `pair[i].variant` — the honest one: class `none` on the group draws a DASHED connector and a
  grey terminal block for a mitigation-only risk ("no upside identified at this horizon").
  Use it whenever a risk genuinely has no offset; that variant is what stops the page being
  optimistic.
- `source` / `pageno` — source string ≤150 chars incl. method date; `pageno` "NN | SECTION".

FILL (build order — and how to resize the diagram, which is the point of this page):
1. Replace `kicker`, `title`, the three `strip` cells. The strip is typographic HTML; edit the
   `.fig` text nodes in place.
2. Text inside a pair: the four text blocks in the risk side (`.rank`, `.r-head` 2 lines,
   `.sev` ×2), the `lever` text, and the opportunity side (`.o-head` 2 lines, `.o-val`,
   `.o-cap`). All are plain text nodes with fixed x — swap the characters, not the x/y.
   The 2-line blocks each hold ONE `<tspan x="…" dy="15">` — keep that pattern (line 2 is the
   tspan), otherwise the two lines collide.
3. TO ADD A PAIR: copy one whole `<g class="pair" id="pN" transform="translate(0,242)">` and
   paste it after the last one, changing `id` and the translate Y by +112 (242→354→466→578→690).
   Nothing else reflows. Do not touch `#p1`'s coordinates, the `hdr`, the spine, or the footer —
   pairs carry no absolute y of their own; the group translate is the row.
   The usable band is y 196→628 (432px). Block height 92, so the maths is:
     (N−1)×pitch + 92 ≤ 432.
   N=4 → pitch 112 (the default: 242/354/466/578). N=5 is the ceiling and needs SHORTER
   blocks: set every `pair` rect to y:-40 h:80, text to 11.5px, and use pitch 85 →
   centres 236/321/406/491/576. Do not stack 5 blocks at 92 tall; they overlap.
4. TO REMOVE A PAIR: delete the whole `<g>` element (open and close tags), then pull the
   remaining centres together by the same rule and re-number `id`s and R-codes. A gap where a
   pair used to be reads as a missing risk, which is worse than never having drawn it. Shorten
   the spine `y2` to last-centre + 50.
5. TO COMPRESS TO 3 PAIRS: pitch 168 → centres 242/410/578 (blocks stay 92 tall). Never leave
   three pairs on 112 pitch — the bottom half of the stage goes empty and the page reads
   unfinished.
6. CHART RECIPE: the emphasis rule is per-PAIR, not per-block. Mark one pair `class="pair focus"`
   (rank box fill, connector stroke, knot fill, lever label, and 2.2px opportunity outline all
   follow the `focus` class — that is the only place the accent geometry lives). Any other pair
   stays grey-connector + 1.5px accent outline. Exactly ONE pair may carry `focus`.
   Mark a pair `class="pair none"` for a risk with no offset — dashed connector, dashed outline,
   grey value.
7. RECOLOR: `--accent` alone moves the whole page (the rule in the KPMG review is one hue;
   the `--accent-1` value is unused in this template — leave it or set it to the client's tint).
   To make it a PwC page: `--accent:#D04800; --ink:#333333`. Greys do not need changing.

CHART RECIPE: This is a mapping diagram, not a plot — there are no scales. Encoding is positional
and by class: column (left = risk, right = opportunity), row (rank order = the register's own
order), connector (solid grey = paired, solid accent = the focus pair, dashed = paired-with-no-
offset). Value labels sit ON the element they quantify (`$2.4M` inside the opportunity block,
never floating). The gutter is a third column only for the LEVER; never let it become a fourth
column of prose. One accent + grey ramp + navy as ink — 3 total values, no second hue.

VERIFY: title ≤15 words AND ≤2 rendered lines (measure with a browser at 1280×720 — the stage
scales, it does not reflow); every pair has a lever (a pair without one is SmartArt); exactly
one `focus`; exactly one hue + grey ramp + navy; opportunity blocks all the same width (360) —
never grow one to fit text, cut the text; contrast: `$2.4M` accent #243CE4 on white = 7.4:1 ✓,
`.o-cap` #6E767F on white = 4.6:1 ✓; source line bottom-left present, `NN | SECTION`
bottom-right; page survives a 2-line `o-head` without overflowing the block.

DON'T: topic titles ("Risk assessment"); pair the risk to a value with no lever between them
(the classic two-box SmartArt tell); colour by column instead of by meaning; put the payoff
number in prose in the left block (it belongs on the opportunity side); use 10 pairs (the
pitch floor is 92px; 5 is the ceiling — beyond that, split the register across two pages);
a `none` pair that is secretly just a formatting accident (dashed means "we checked and there
is no offset"); 4+ hues (the PwC boardroom deck is the cautionary evidence: six unrelated
triggers in six hues, colour decorative not semantic); webfonts; lorem ipsum.

SOURCE: firm evidence — KPMG `kpmg__kpmg_genai_survey_2024_key_insights_2024` (2024) p9,
`kpmg__kpmg_kpmg_2022_ceo_outlook_2022` (2022) p5; PwC Strategy `pwc_strategy__pwc_boardroom_agenda_2022`
(2022) p26. Cells resolved from `sw_sheets/` contact sheets (5 col × 2 row, row-major).
Palette: `reviews/kpmg__kpmg_kpmg_2022_ceo_outlook_2022.md` (royal blue #243CE4, deep navy
#002478, greys #333/#4A4A4A/#999) and `reviews/pwc_strategy__pwc_boardroom_agenda_2022.md`
(its "colour is decorative, not semantic" finding is the reason this template's colour is
assigned by MEANING: grey = risk, one hue = upside). Fonts: real firms use KPMG Sans / PwC
custom faces; the `"Helvetica Neue", Arial` stack stands in for both — titles tight-tracked,
body Arial-class.
