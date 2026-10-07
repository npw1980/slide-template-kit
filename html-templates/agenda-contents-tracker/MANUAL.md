# agenda-contents-tracker — Contents that doubles as a section-progress tracker

WHEN: A long document (50+ pages) needs one contents page that keeps working after
page 1. The same section list is reprinted on later pages with the section you are in
marked — Monitor Deloitte ran exactly this on 7 of its contents pages in the
Accelerated Access Review, and the review calls it out as the device to copy.
Use it for a TOC that must also orient a reader mid-document; not for a 12-page deck,
where a plain list is enough.

ANATOMY (1280×720 stage, left/right margin 88px; 1rem == 1px, everything is absolute on one canvas):
1. `kicker` running head — left 88, top 48, width 700. 11px uppercase, 0.16 tracking, grey.
2. `brandmark` — right 88, top 46. 14px bold, one `dot` span coloured.
3. `title` (the section-label slot) — left 88, top 92, width 900, 40px/1.05, tracking −0.7, dark green.
4. `message` — left 88, top 158, width 760, 16px/1.45, grey-1, `<b>` for the inked phrase.
5. `progress` read-out — right 88, top 158, width 338. Caption 10px, numeral 26px, bar 338×6.
6. `sections` list — `nav.toc` left/right 88, top 230; column-head row 14+6 tall, then 7 rows × 58px
   ending at 656; a hairline rule closes it at top 660.
   Inside each `li.row`: marker (x≈90, 9px square, rail line at x=94.5), label from x=126
   (max width 640, nowrap+ellipsis), span column right edge 1076, tag right edge 962, page column right edge 1192.
7. `source` line — left 88, bottom 26, 11px + `sup` marker. `legal` line — left 88, bottom 12, 9px.
8. `pageno` running head — right 88, bottom 26: `<b>20</b> | Introduction`.

SLOTS:
- kicker — ≤70 chars, one line, uppercase. Good: document name + worksheet. Bad: a sentence.
- title — 1–2 words (a label: "Contents" / "Agenda"). It is a LABEL page; the gate applies to the message line.
- message — ≤34 words / 2 lines. Good: says how to read the document (order vs drop-in). Bad: restating the title.
- sections[n].label — ≤54 chars, one line, 16 words max. Good: the exact section title as printed. Bad: "Overview"/"More info".
- sections[n].span — "4 – 12" style page range (en dash, spaces). Three to five characters of value; wrong ranges are the classic contents lie.
- sections[n].page — the section's starting page. Right column is 40px wide minimum for 3 digits.
- sections[n].state — one of `read` / `current` / `next`. EXACTLY ONE row is `current` + `aria-current="true"`.
- progress.num — "2 <small>of 7 · page 20 of 109</small>". The bar width must equal (page−1)/(total−1) of a section, not of the bar's own mood.
- source / legal / pageno — footer furniture; the `sup` after the analysis clause is required where the deck claims analysis.

FILL:
1. Replace the `kicker` and `brandmark` text nodes; swap the `dot` span's colour if the firm differs.
2. Replace `h1.title` and the `p.message` text — keep the `<b>`.
3. Edit the `ol.rows` list. Duplicate or delete `li.row` blocks for your section count (5–9 fit; 10+ needs row height 50px and `padding` recalc — keep list bottom under 656).
4. Set each row's state by class only: `read`, `current`, `next`. Give the current row `aria-current="true"` and keep its `.tag` chip; delete `.tag` from all other rows.
5. Change page numbers in `.pg` and ranges in `.sp`; the columns are right-anchored so no x-coordinates move.
6. Progress read-out: set `.num` text and the green `<i>` width to the same fraction; the grey `<i class="rail">` is the remainder.
7. Re-theme: change `--accent` (markers, rail, bar, ring) and `--accent-deep` (ALL green type) together, plus `--accent-wash` (the current-row band). If the new accent is dark, set `--accent-wash` to a pale manual step.
8. Fonts: `--font-display` (Helvetica Neue/Arial) stands in for Deloitte's Pentagram Insights house family (Open Sans with Verdana fallback per DESIGN_PLAYBOOK); `--font-body` is Verdana-first so the substitute reads humanist rather than grotesque. Say which of the two is the real face.

CHART RECIPE: n/a — no data figure on this page. The one number-bearing device is the progress bar: one accent fill + one grey remainder, no axis, no labels on the bar, ratio derived from the page position, never rounded to a tidy 25%.

VERIFY:
- Exactly one row is `current`, one `.tag`, and `aria-current="true"` present.
- Message line renders in 2 lines or fewer at 760px width.
- No row label truncates (max-width 640, ellipsis is a last resort, not a layout plan).
- One emphasis colour: green appears only in accent/`accent-deep`; everything else is the grey ramp.
- Green text is `--accent-deep` (#356604, 6.9:1 on white) — never raw `--accent` (#86BC25, 2.3:1).
- Page column: 3 digits fit; page numbers match the actual deck, and the ranges are contiguous with no gaps or overlaps.
- Source line present bottom-left with its `sup`, page number + section running head bottom-right.

DON'T:
- Do not print raw brand green for the title the way Deloitte does — it fails contrast at any size.
- Do not use "you are here" on two rows, or on none — the value is precisely one unambiguous marker.
- Do not let the page numbers and ranges disagree (the review notes Deloitte's own deck skips a section label on p36; a contents page that disagrees with its dividers is worse than no contents).
- Do not put a kicker wall of text under the label title; one message line, then the list.
- Do not add leader dots — this page's structure is carried by the rail, the rules and the right-anchored page column.

SOURCE: Monitor Deloitte — "Accelerated Access Review: UK Mapping" (2015), deck id
`deloitte__deloitte_accelerated_access_review_uk_mapping_2015`. Contents appears as p3
(reprinted p12, p20, p44, p69) — read at
`sw_pages/deloitte__deloitte_accelerated_access_review_uk_mapping_2015/pg-003.png` and
`sw_sheets/deloitte__deloitte_accelerated_access_review_uk_mapping_2015_s00.jpg` (sheet 0,
row-major 5×2). Analysis: `reviews/deloitte__deloitte_accelerated_access_review_uk_mapping_2015.md`
(Narrative/section structure: "Contents pages (7 of them) double as section-progress trackers";
COPY list names "contents-as-section-tracker"; footer discipline: source + "Private and confidential").
Palette note: Deloitte's green hexes are unresolved across regional toolkits per `DESIGN_PLAYBOOK.md` line 53 —
which is why brand lime is confined to graphics here.
