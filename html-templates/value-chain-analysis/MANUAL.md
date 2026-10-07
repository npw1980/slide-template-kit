# value-chain-analysis — Value-chain stages + segment × dimension matrix (1280×720)

WHEN: Value-chain page where the chain segments are the SPINE and a fixed set of
analysis dimensions (here: APPLICATIONS / BENEFITS / END USERS) is applied to
each segment below. Source form: `pwc_strategy__pwc_copernicus_market_report_2019`
p40 (`sw_sheets/pwc_strategy__pwc_copernicus_market_report_2019_s03.jpg`, 5×2
row-major, row 1 col 4) and the "table + callouts" variant harvested at p89
(sheet `s08.jpg`). Review: `reviews/pwc_strategy__pwc_copernicus_market_report_2019.md`
§5 / §36-44. Use this when the argument is "we know who does what, what they
get, and who pays" — the who/what/why inventory, not a flow. Companion:
`value-chain-3box` (chain + callouts + value bars).

FONTS: firm face is PwC Sans (proprietary); `"Helvetica Neue", Arial` stands in.

ANATOMY (slot map, stage px; `1rem = 1 stage px` via the `html` rule):
1. `band` — div x64 y36 1152×106, gray-4 fill (family header grammar).
2. `title` — in-band x28 y14, w1020, 25/31 bold navy.
3. `sub` — in-band x28 y80, 12 bold uppercase accent: one extra judgment.
4. `icon` — 56px disc, band right 22 / top 26: three-node chain glyph (drawn).
5. `stage-col-1..3` — SVG groups `translate(64|461|857, 160)`: numeral + stage name + accent/gray underline chip + 4 tick-bullets (local y 40/62/84/106). Binding stage = all accents (numeral, underline, ticks).
6. `divider` — hairline y330 (chain over matrix).
7. `matrix-head` — column headers y366 at x 270/590/910 + 1.4 ink rule y376 (the matrix's "definition of the dimensions" line).
8. `matrix` — 3 row bands x 192-wide ink chip + 3 content cells between vertical guides x256/576/896. Row y starts 386 / 466 / 546, height 76 each; row hairlines 464/544.
9. `matrix-base` — 1.4 ink bottom rule y624 + footnote line y646 (9.5 gray-3, bold "1").
10. `foot-src` bottom-left, `foot-page` `1 | VALUE CHAIN` bottom-right.

Row pitch is 80 (386→466→546); a 4th segment shifts everything below the
divider down 80 and grows the matrix (see FILL §4).

SLOTS:
- `title`: ≤15 words / 2 lines. Good: promises the matrix itself (who does what, who pays). Bad: "Value Chain Overview".
- `sub`: ≤15 words uppercase; the second claim, not a restatement.
- stage names (14 bold caps `.06em`, ≤18 chars): SAME names as the stage columns AND the row chips — column, row, and chip use identical strings, that's the whole point of the page (row↔column binding). If you rename one, rename both.
- stage bullets: 4 lines × ~46 chars; binding stage's ticks are accent (one accent cluster only).
- matrix cells: 2 lines × ~38 chars per cell, 11px. Good: concrete actors/uses. Bad: "various / many / some".
- `matrix-head`: three fixed dimension names, never per-engagement inventions unless they replace all three consistently; dimensions repeat across every chain page in the system (that's what the footnote promises).
- Footnote: what the end-user classification is based on (superscript 1).

FILL:
1. Replace all `<text>` contents: band title/sub, stage names + bullets in `stage-col-1..3`, matrix headers + 9 cell pairs, row chip names, footnote, footer. Coordinates fixed; text length is what you control.
2. Recolor accent: `--accent` (e.g. PwC red `#C3002F`; keep `--ink` navy so row chips stay ink and only the binding stage goes accent). The third row chip uses `--accent` fill — if a different stage binds, move the accent chip there (row 1/2 chips are `var(--ink)`).
3. Dim a segment you did not assess: that `stage-col-N` ticks/text to gray-3, that row chip `fill:var(--gray-5)` with text `--gray-2` + its cells gray-3; state in title it was not assessed.
4. ADD/REMOVE ROWS/NODES — this is the part that must work:
   - Matrix rows are bands at y 386 + 80·i; row group = `<g id="row-N">` (chip rect + 2 chip texts + 3×2 cell texts). ADD a 4th segment: set rows to y 366/446/526/606 (pitch 70 to fit the stage band), chip rects h76→h66 with single-line chip name, cells 2 lines at row+28/+46. The `line x1..` guides stay put; extend them and the base rule (`y624` → `y684`). If that collides with the 664 footer line, raise rows to pitch 66 (366/432/498/564/630?) — simpler: for 4 segments the matrix must lose the stage-column band; keep the chain as ONE horizontal strip at y160 (chips 150 tall removed) and the matrix keeps 76 pitch. Do NOT silently let cells overlap the base rule.
   - Stage columns = one `<g id="stage-col-N">` each with a single translate; add a 4th at translate(1253,160) is OFF-STAGE — instead re-anchor all four at pitch 288 (64/352/640/928, bullets wrap ≤40 chars) which is a text-wrapping decision, not a coordinate one. The honest 4-segment move is to fold the 4th stage into 3 bullets and keep the chain 3-wide.
   - Rename a segment: change both the column name and the row chip (identical strings).
5. The three matrix columns are NOT a data array — there is no series to swap; "fill" is 6 text pairs per row. The encoding lives entirely in geometry + one accent.

VERIFY:
- [ ] Title ≤15 words / ≤2 lines (placeholder 15 words).
- [ ] Column names and row-chip names are byte-identical per segment.
- [ ] One accent: binding stage only (underline + ticks + its row chip). Ink chips carry the other rows.
- [ ] Every matrix cell filled, ≤2 lines × ~38 chars; nothing crosses x256/576/896 or the base rule y624.
- [ ] Source line + `1 | VALUE CHAIN` present; superscript 1 on END USERS header points to the footnote.
- [ ] No more than 2 hues on the page (navy + one accent) + grays.

DON'T: inventing per-page matrix dimensions ("STAKEHOLDERS", "RISKS" on one page only); 10-cell wall of bullets without the row-chip rhythm (that's a data table, not a chain); topic titles; dimming everything; a fourth analysis column (3 is the grid's honest capacity at 11px/2 lines).

SOURCE: `pwc_strategy__pwc_copernicus_market_report_2019`, p40 read from
`sw_sheets/pwc_strategy__pwc_copernicus_market_report_2019_s03.jpg` (row 1
col 4) + harvested "value chain 3-box … table + callouts" variants (p53/p64/
p76/p89, sheets s05–s08); chapter-template inventory + palette hexes from
`reviews/pwc_strategy__pwc_copernicus_market_report_2019.md` §5, §36-44.
