# agenda-contents-ruleset — Numbered contents table on a ruled grid

WHEN: A report needs a formal table of contents — numbered sections, one line each,
page numbers aligned in a column, no leader dots. It is the "document" flavour of the
family: rules and columns carry the structure, so it suits numbered-section reports
(25–60 pages) more than a short pitch deck. A you-are-here band is available for the
same page when it is reprinted later in the document.

ANATOMY (1280×720 stage, left/right margin 88px; 1rem == 1px; one absolute canvas):
1. `rule-top` hairline — left/right 88, y 64. `kicker` running head — left 88, y 78, 11px uppercase.
2. `title` label — left 88, y 100, 44px/1.0, tracking −0.8, grey (the deck paints the TOC title grey on purpose).
3. `rule-brand` — left 88, y 158, 760×4 solid accent (the page's only brand mark besides the footer).
4. `message` line — left 88, y 182, width 790, 15px/1.45, with one `<b>` clause.
5. `edition` block — right 88, y 100, width 330, right-aligned: bold line + grey detail line.
6. `toc` table — left/right 88 (1104 wide), top 244. Header row `thead` (10px uppercase, 1px dark rule under);
   five body rows, padding 12/14, 1px dark rule under each, then `tfoot` note.
   Columns: `No.` 74px · `Content` flexible · `Page` 150px right-aligned.
7. Row internals: `n` numeral 19px · `t` section title 18px bold · `d` one-line descriptor 11.5px/1.35
   · `p` page number right-aligned 19px · `chip` 9px uppercase on accent, inline after the title.
8. Footer band: `source` left 88, y≈680 with `sup` marker · centred deck title + page number (420 wide)
   · brand mark right 88, y bottom 22 (inline SVG, 52×21).

SLOTS:
- kicker — ≤70 chars, one line. Good: what the document is + when. Bad: the deck title again.
- title — 1–2 words. This is a label page, not a claim page; the claim lives in `message`.
- message — ≤30 words / 2 lines. Good: which sections hold the exhibit weight. Bad: "An overview of the report."
- edition — ≤2 lines: one bold line ("Edition 2015") + a detail line with sample size / markets. Stresses to ~34 chars.
- row.title — ≤50 chars, one line. Good: the printed section name. Bad: "Section 1" (the numeral already says that).
- row.desc — ≤90 chars / 1 line. Good: what the reader will find inside, quantitative if possible ("11 exhibits").
- row.page / row.num — integers, right column; numerals must be sequential and must match the dividers.
- row.state — `read` (greyed, already visited), `here` (accent band + chip), or none (upcoming).
  One `here` maximum; on a first-page TOC, no row carries a state at all.
- source / foot-center / brand mark — footer furniture, present on every content page.

FILL:
1. Swap `kicker`, `h1.title`, `p.message` (keep the `<b>`), and the `div.edition` two lines.
2. Edit `table.toc` rows: one `<tr>` per section. To add/remove rows copy a `<tr>...</tr>` block —
   rows are 61–67px each so 7 fit before the note; 8+ means cutting `padding` on `tbody td` to 9rem.
3. Set each row's state by class: `class="read"`, `class="here"`, or nothing. The `here` row needs
   its `<span class="chip">`; delete the chip from every other row.
4. Swap numerals in `td.n` and page numbers in `td.p` — both columns are fixed width, nothing reflows.
5. `tfoot` note is part of the table: rewrite it in place (it cannot collide with a row by construction).
6. Re-theme: set `--accent` (brand rule, chip fill, `here` wash via `--accent-wash`, numeral on the
   `here` row via `--accent-deep`). One variable move. For a dark-accent firm, set `--accent-wash` to a
   manual 6–8% tint and `--accent-deep` to the accent itself.
7. Brand mark: replace the SVG `<text>` (19px, `--ink`) and its underline `<rect>` (`--accent`, 2.4px)
   with your lockup; keep width 52–70 so the right margin holds.
8. Fonts: `--font-display` (Helvetica Neue/Arial) stands in for the survey deck's house sans;
   `--font-body` is Calibri-first. State the firm's real face in your deck notes.

CHART RECIPE: n/a — no chart. Alignment rule that matters instead: the page column is right-aligned
on the same baseline grid (19px), row rules are 1px dark grey (#595959), the brand rule is 4px accent.
Never both a leader-dot column and a ruleset — pick one.

VERIFY:
- Message line is ≤2 lines; the table still ends above y 660 (note row included).
- Exactly one `here` row (or none); the chip's black-on-accent clears 4.5:1 (black on #FFE600 does).
- Grey-on-grey check: read-state titles at #7D7D7D on white are ~3.6:1 — accept for muted text only,
  not for anything you need read aloud; if the section must be legible, drop `class="read"`.
- One emphasis colour: accent appears as rule + chip + wash only; no second hue anywhere on the page.
- Source line bottom-left with `sup`; page number visible in the centre band; deck title present.
- Numerals 1..N sequential with no skipped label (the source deck skips section 4 on its dividers — don't).

DON'T:
- Do not add leader dots: alignment here is columns + rules (the observed deck does exactly this and nothing else).
- Do not give rows their own hues (section colour coding is a different template family).
- Do not stack more than one descriptor line per row — the row rhythm (61–67px) collapses and the page drifts.
- Do not make the title the accent colour "for brand presence": it is painted grey so the rule under it is the accent.
- Do not keep the chip on a first-edition TOC where nobody has read anything yet.

SOURCE: EY — "European Banking Barometer 2015", deck id
`ey__ey_european_banking_barometer_2015_2015`, Contents = p2. Read page-level at
`sw_pages/ey__ey_european_banking_barometer_2015_2015/pg-02.png` (and contact sheet
`sw_sheets/ey__ey_european_banking_barometer_2015_2015_s00.jpg`, cell 2). Layout facts
(title grey, yellow rule under title, dark row rules, right page column, no leader dots,
footer band page/title/logo) come from `reviews/ey__ey_european_banking_barometer_2015_2015.md`
(layout section + COPY list "contents list" and "the footer band"); palette #FFE600 is the
review's brand-yellow value, flagged in `DESIGN_PLAYBOOK.md` as commonly cited / unconfirmed.
The row-state device (read / you-are-here / upcoming) ports from
`reviews/deloitte__deloitte_accelerated_access_review_uk_mapping_2015.md` ("contents-as-section-tracker").
