# recommendation-driver-map — Driver-to-Recommendation Mapping Table

WHEN:
The bridge page between findings and the roadmap: every recommendation is tied back to a
named driver and one measured finding, with owner and start date visible in the same row.
From `deloitte__deloitte_town_of_tillsonburg_it_strategic_review_council_upd` p8
("drivers → recommendations"), whose row labels deliberately mirror p6 ("drivers →
findings") — that mirror is the argumentative spine of the deck. Same boxed-table grammar
at p15 (option comparison with rating cells) and p12/p13 (cost tables).
Second exemplar class: `catalog_1-20.csv` S0057 "recommendation page".

ANATOMY (1280×720 stage):
1. kicker  `left:64 top:46  w:760`   — 12px uppercase tracked
2. title   `left:64 top:68  w:1152`  — 30px/1.12 bold claim
3. lead    `left:64 top:134 w:1080`  — 15px/1.4, one line stating the trace rule
4. table   `left:64 top:176 w:1152`, header band `h:40`, 4 body rows `h:100`,
   heavy `3px --navy` rule on the table's bottom edge
   columns (fixed colgroup): `# 46 · Driver 232 · What we found 286 · Recommendation 366 ·
   Owner 122 · Start 100` (sums to 1152 exactly)
5. `driver` cell — 14.5px bold navy label + 11.5px gray metric sub-line
6. `find` cell — 12.5px/1.5, up to 3 lines, carries the numbers
7. `rec` cell — 13px/1.5, verb-first action + 4px status bar on the cell's left edge
8. `owner` cell — 12px bold role + 11px gray deputy
9. `start` cell — quarter (bold) + status chip (PLAN / NOW / DECIDE)
10. status key + footnotes `left:64 right:64 bottom:34`
11. footer `left:64 right:64 bottom:10` — rule, source bottom-left, `8 | FINDINGS SUMMARY`
    + rights bottom-right

SLOTS:
- `title` — the claim that the table proves. Gate: ≤15 words / 2 lines. Good: "Four drivers set the IT strategy; each has one owner and one start date". Bad: "Drivers of the IT strategy review" (the source deck's exact failure).
- `lead` — one line stating the trace rule ("each recommendation traces to a driver and one finding"); it is what makes the table an argument rather than a list.
- `driver.N` — short noun + a measurable sub-line ("37 physical servers · 6 past end-of-support"). Keep driver labels identical to the findings page above this one.
- `find.N` — 3 lines max. One or two hard numbers, bold the decisive one. This is the column that stops a recommendation from being opinion.
- `rec.N` — 2 lines max, starts with a verb ("Split…", "Retire…", "Charter…"), and if sequencing matters, say it here ("before the ERP upgrade").
- `owner.N` — a named role, not a department. Deputy line optional.
- `start.N` — quarter + chip. One of `now` / `plan` / `decide` on the `<tr>`.
- `source` / `page` — required; the two `sup` markers carry the assumptions.

FILL:
1. Replace the four title/lead text nodes, then each row's five cells.
2. Row count: the table grows only by `<tr>`s at `height:100rem`. 3 rows read better with
   `h:100`; 5 rows → `h:80`; 6 rows → `h:66` and drop the driver sub-line to 11px.
   Do not exceed 6 rows on this stage (footnotes + footer need 84px).
3. Column widths are the `colgroup` numbers; they must keep summing to 1152. If findings
   run long, give `c-find` 322 and take 36 from `c-rec`; do not change `c-idx` (46).
4. Status semantics: set `class="now|plan|decide"` on each `<tr>`; the left bar (4px),
   the chip border/text and nothing else follow it. The bar+chip pair is the emphasis —
   no extra color anywhere else on the page.
5. Accent: `--sev-*` triples are semantic, so recolour them as a set for a different
   house (e.g. all-gray status = neutral table). Brand colour enters only via `--navy`.
6. Mirrored page: duplicate the file, keep the same `driver` column and swap `rec` for a
   "What that means" findings column — that is the p6/p8 pairing in the source deck.

CHART RECIPE: N/A — the table is the exhibit. If a chart is added under it, it must share
the row order and the status semantics, or the page loses its argument.

VERIFY:
- [ ] title ≤ 15 words / ≤ 2 lines (measured as shipped: 14 words, 1 line)
- [ ] every row has a driver, a number-bearing finding, an action, an owner and a start
- [ ] status colors used only on the left bar + chip (semantic); page otherwise navy + gray
- [ ] chip text `#2E5C1A / #6B4E00 / #8E2B20` on white all clear 4.5:1; body text `#1B1B1B` passes
- [ ] colgroup widths still sum to 1152; bottom heavy rule present above the status key
- [ ] source line bottom-left, page stamp + rights bottom-right; sup markers defined in footnotes
- [ ] no network calls: semantic `<table>`, inline CSS, system font stacks, zero JS, zero images

DON'T:
- Topic titles — the source deck's biggest documented weakness ("Drivers of the IT strategy review", "Conclusion"); import your own claim.
- A recommendation column written as a topic ("ERP strategy") instead of an action.
- Status color as decoration: three semantic levels only, never a fourth, never used for "importance" of the driver.
- Zebra shading plus heavy row rules plus colored cells all at once — pick the two you use (here: zebra + light cell rules + one status bar).
- More than 6 rows, or 3-line recommendations, or a "Notes" column nobody reads.
- Repeating the same number in the finding and the recommendation (the shipped placeholder deliberately keeps them distinct).
- Unnamed owners ("IT", "the team") and undated starts — the table's whole value is accountability.

SOURCE:
Firm: Deloitte LLP — `deloitte__deloitte_town_of_tillsonburg_it_strategic_review_council_upd`
(Town of Tillsonburg IT Strategic Review, Council Update, Jan 2014), p8; mirrored row device p6;
rating-cell discipline p15; totals rule p12/p13. Visual read:
`sw_sheets/deloitte__deloitte_town_of_tillsonburg_it_strategic_review_council_upd_s00.jpg`
(sheet index 0 = floor(8/10)). Palette + device rulings:
`reviews/deloitte__deloitte_town_of_tillsonburg_it_strategic_review_council_upd.md`
§Color system (navy dominant / green accent / traffic-light semantic-only, ≈4 hues),
§Recurring layout archetypes #2, §Copy vs ignore (copy tables, import titles).
Palette anchor note: the review records navy/green/yellow registers but no published hexes
(`DESIGN_PLAYBOOK.md` flags Deloitte hex conflicts across regional toolkits), so the tokens
here are a deep navy `#0B2C4A` with semantic status colors, explicitly remappable — not a claimed brand match.
