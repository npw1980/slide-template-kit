# text-bullets-numbered-blocks — Numbered color blocks + chevron + single-bullet claim rail

WHEN: A page that groups one argument into 2–4 labeled themes and expands each
with exactly one supporting sentence — the "grouped opportunities" pattern.
From Deloitte UK's NHS access review (deloitte__deloitte_accelerated_access_review_uk_mapping_2015),
page 10 ("Opportunities for improved access"); same grammar on p11 (numbered-dot
claim list, "Top areas for review in phase 2").

ANATOMY (1280×720 stage; all coords in stage px):
1. title          — x64  y48  w1152, 32px/1.15 bold, brand green, sentence case.
2. claim line     — x64  y104 w1000, 17px/1.45, bold lead-in run; this is the page's argument.
3. row r0/r1/r2   — block-top y = 200 / 340 / 480 (pitch 140). Each row holds:
   3a. block      — x64  w300  h92  radius 8, solid semantic fill, white 15px/1.3 bold label (padding-left 30).
   3b. badge      — d32 circle, navy, 16px white numeral, straddling the block's left edge (left:-16 relative to block, vertically centered).
   3c. chevron    — x400 y+28 w56 h52, inline SVG pentagon `points="0,2 56,26 0,50 12,26"` filled navy.
   3d. bullet     — x520 y+14 w696, 16px/1.5, CSS middle-dot marker at x-24.
4. footer         — x64→x1216 y-bottom-30, 1px #D9D9D9 rule on top, 11px gray; page numeral (bold ink) + rights line right-aligned.

SLOTS:
- title: 1 line best, 2 max (≤15 words / 2 lines gate applies page-level). Short topic label is fine HERE only because the claim lives in slot 2.
- claim: ≤15 words, ≤2 lines. Must be a quantitative/positional statement ("Twelve priority opportunities span…"), not "Opportunities overview".
- blk-label: ≤3 lines × ~18 chars. Good: "End-to-end access pathway opportunities". Bad: a sentence — it is a THEME NAME, not a claim.
- badge: 1,2,3 — ordinal grouping only.
- bullet: ≤3 lines (~265 chars). One sentence per block. If you need two, you have two themes.
- source: ≤110 chars, real method string. page: deck numeral. rights: one-line house notice.

FILL:
1. Replace the four text blocks (title, claim, three block labels, three bullets).
2. Number the badges 1..N.
3. Swap the three semantic fills `--c-1 --c-2 --c-3` (teal #107BA9 / gray #595959 / green #2E6126) — colors denote THEME/SECTION, never rank. If themes don't carry color semantics, make all three `--gray-2` and keep one accent.
4. Recolor `--navy` for badges + chevrons (one emphasis color).
5. 4 rows: set pitch 108 / block height 76 in `.row.rN` tops and `.block`; labels shrink to 2 lines.
6. Footer: replace source string, page number, copyright.

CHART RECIPE: N/A — text page. The chevron SVG is furniture, not data.

VERIFY: claim ≤15 words / ≤2 lines; title + claim both present (title-only page fails); one emphasis color (navy) + brand green + semantic block colors only; block labels fit ≤3 lines without touching badge; source line present; page numeral present; white-on-block contrast ≥4.5:1 (all sampled fills pass).

DON'T:
- Topic title with no claim line — the genre's whole job is the message line under the green label.
- More than one bullet per block (then you have two themes; add a row).
- Block colors as rank/traffic-light — palette is semantic (stage/theme), per the deck's own color-logic.
- Labels over 3 lines (widen the block before shrinking type), or sentences in labels.
- Chevrons recolored into rainbow hues; they are navigation furniture, one navy.

SOURCE: deloitte__deloitte_accelerated_access_review_uk_mapping_2015 — page 10 read from sw_sheets/deloitte__deloitte_accelerated_access_review_uk_mapping_2015_s00.jpg cell row1/col4; p11 corroboration at _s01.jpg row0/col0. Block fills and chevron navy pixel-sampled from p10; title green per reviews/deloitte__deloitte_accelerated_access_review_uk_mapping_2015.md §palette ("Deloitte green titles, deep navy structure"). Brand face is Deloitte's brand family of the period; the file ships a Helvetica/Arial stand-in stack.
