# value-chain-3box — Three-box value chain with stage callouts (1280×720)

WHEN: Industry value-chain page drawn as three linked stage boxes, each stage
carrying its own evidence bullets + a value-capture bar, over a bottom
challenge strip. This is PwC's workhorse chain: the Copernicus market report
repeats "Acquiring / Processing / Users" across ~11 sector chapters. Use when
the argument is *where value sits along the chain*, not process or org.
Source form: `pwc_strategy__pwc_copernicus_market_report_2019`, chapter pages
around p40–p89 (sheets `sw_sheets/pwc_strategy__pwc_copernicus_market_report_2019_s03.jpg`–`s08.jpg`,
5 cols × 2 rows row-major); grammar + palette from
`reviews/pwc_strategy__pwc_copernicus_market_report_2019.md` §5/§53.

FONTS: the firm's real face is PwC Sans (proprietary, not available). The
`"Helvetica Neue", Arial` stack stands in for it — same neutral grotesque,
slightly tighter; keep letter-spacing on caps as set.

ANATOMY (slot map, stage px; `1rem = 1 stage px` via the `html` rule):
1. `band` — div, x64 y36, 1152×106, fill gray-4. The header band: title + subtitle + icon disc all live inside it.
2. `title` — inside band, local x28 y14, width 1020, 25/31 bold navy (`--ink`), 2-line box.
3. `sub` — inside band, local x28 y80, 12 bold uppercase `.06em`, accent colour — the takeaway line (second register of PwC titles).
4. `icon` — SVG inside band, right 22 / top 26, 56px disc: orbit arc + 3 dots + satellite glyph (drawn, not an icon font).
5. `stage-1` — SVG group `translate(64,164)`, local rect 357×116. Box 1 (acquisition).
6. `stage-2` — `translate(461,164)`, 357×116. Box 2 (processing).
7. `stage-3` — `translate(857,164)`, 357×116, accent-tinted fill + 1.4 accent stroke = the BINDING stage.
8. `arrows` — two polygons, centred in the gutters (x 432–456 and 828–852, y 214–244).
9. `bullets-1..3` — `translate(64|461|857, 300)`, three tick+text lines each (local y 7/27/47). Binding stage's ticks are accent.
10. `value-bars` — `translate(64,392)`: label line, three 357×9 tracks with fill widths 54 / 125 / 179 (= 15% / 35% / 50% × 357) and % labels after each fill.
11. `divider` — hairline y464, full content width.
12. `challenges` — 3 blocks at x 64 / 461 / 857, heading y500 + 2 text lines y522/538.
13. `fnote` — x64 y612, 9.5 gray-3, bold "1" marker: the methodology line.
14. `foot-src` — bottom-left 9.5 gray-3; `foot-page` — bottom-right 10 bold `1 | VALUE CHAIN`. Footer strip is 56 tall with 1px top rule.

Stage x-anchors: 64 / 461 / 857, box width 357, gutter 40. Boxes, bullets,
bars and challenges ALL share these anchors — that is what makes the page
resizable.

SLOTS:
- `title`: action title, ≤15 words / 2 lines at 25/31 (the gate). Good: names the stages that carry value + the number. Bad: "The Value Chain of EO Data" (the deck's own boilerplate, called a fail by the review).
- `sub`: one line ≤15 words uppercase; adds a second judgment the title can't carry. Never a paragraph.
- stage `name` (15 bold caps, letter-spacing .06em): ≤22 chars ("DATA ACQUISITION", "USER SERVICES"). Longer names push the numeral chip; drop the chip instead of shrinking the name.
- stage `desc` (11 italic, 3 lines × ~42 chars inside the box): what the stage is.
- stage `bullets` (11 gray-2, 3 lines × ~48 chars): evidence about the stage — economics, ownership, lock-in. One bullet may be accent-ticked ONLY on the binding stage.
- `value-bar` numbers: 3 two-digit percentages that must sum ≈100. The bar is the title's proof — if the title says 67%, the bars must show it.
- `challenge n` (11.5 bold caps + 2 lines × ~55 chars): constraints on the chain, numbered.

FILL:
1. Text: replace contents of `.band .title`, `.band .sub`, each stage group's `name`/`desc` texts, `bullets-1..3`, `%` labels, `challenges`, footer strings. Do not touch coordinates.
2. Recolor the accent: change `--accent` (and keep `--accent-1` a ~15%-tint of it — for PwC red: `--accent:#C3002F`, `--accent-1:#F5DEE3`). Everything that means "binding" follows accent automatically; ink stays navy.
3. Bar values: fill widths = pct × 3.57 (per stage, within that stage's 357px track: stage 2 fills start at local x 397). E.g. 40% → rect width 143, `%` label x = start + width + 8.
4. ADD/REMOVE/RESIZE NODES:
   - A box = one `<g id="stage-N">` with ONE `transform="translate(x,164)"`; internals are local. Moving a stage = editing its translate only.
   - To ADD a 4th stage: change all stage widths 357 → 267 (`rect width`, desc/bullet/track widths), set translates to 64 / 371 / 678 / 985 (pitch 307 = 267 + 40 gutter), move `bullets-N`, bar tracks (starts 64/371/678/985, width 267) and challenges to the same x set. The `value-bars` group is the only one with absolute starts inside — swap those four numbers too. Keep the numbered chips 1..N.
   - To REMOVE a stage (2-box chains): delete the group, set the remaining translates to 64 / 461, widen boxes to 397 each (delete the middle gutter), keep ONE arrow (polygon points shifted: 442,214 466,229 442,244), and re-derive bar widths from the same x set. Bullets/challenges follow.
   - The arrow group is separate from the boxes ON PURPOSE — do not nest it in a stage group, or moving one box silently severs the flow line.
   - Dim an unexamined stage (honest gaps): set that stage's rect `fill:var(--gray-5)`, all its text `fill:var(--gray-3)`, its bar fill gray-5, and keep its bullets — state in the title that the stage was not assessed.
5. Icon disc: swap the glyph paths inside `band .icon` per industry (satellite → pipeline/leaf/shield). Keep the white disc + rule ring; never fill the disc with accent (that competes with the binding-stage accent).

CHART RECIPE (value bars):
- Encoding: length = share of margin pool, % (2-digit, 3-digit OK); same 357px track per stage → comparing lengths compares stages directly.
- Emphasis: the binding stage's bar is `--accent`; all other stages gray ramp (`--gray-3` fill on `--gray-5` track). One hue, no per-stage colours.
- Labels: value after the bar end, bold 11.5 — ink only on the accent bar, gray-2 elsewhere.
- The caption line carries `1` (superscript) → methodology footnote; label reads "SHARE OF MARGIN POOL, INDICATIVE" — never imply measured precision without saying so.

VERIFY:
- [ ] Title ≤15 words / ≤2 lines (placeholder: 15 words).
- [ ] Bars sum ≈100 and match the % claimed in the title.
- [ ] Exactly ONE hue: ink navy + accent + grays; accent only on binding stage box, its bullet ticks, its bar.
- [ ] Source line bottom-left + `1 | VALUE CHAIN` bottom-right; superscript 1 on the bars label and both footer claims.
- [ ] Text contrast: ink 11.6:1, accent 7.2:1, gray-2 9.4:1; gray-3 used only for the source/fnote lines.
- [ ] No stage name exceeds ~22 chars or wraps into the chip.

DON'T: thematic "THE VALUE CHAIN OF …" titles (the deck's documented fail — use the two-register band instead); more than 3 challenge blocks (strip is 3 wide); topic-only bullets ("data services exist"); 5 hues of stage boxes; photos glued into stage boxes (photos elsewhere in the deck, not this page — this page's slot-filler is callouts); arrows crossing text.

SOURCE: extracted from `pwc_strategy__pwc_copernicus_market_report_2019` —
value-chain 3-box pages harvested at p41/p53/p64/p76/p89 (`sw_sheets/
pwc_strategy__pwc_copernicus_market_report_2019_s0X.jpg`, page→sheet =
floor(NN/10), row-major 5×2); page grammar (band + numbered callouts +
challenge strip) read directly from s07/s08 crops; "Acquiring/Processing/
Users" chain + palette hexes (#1F3864 / #1E5A90 / #A8C8E8) from
`reviews/pwc_strategy__pwc_copernicus_market_report_2019.md` §5, §36–44, §53.
