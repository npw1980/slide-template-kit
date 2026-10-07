# appendix-backmatter-definitions — Appendix Glossary / Key-Definitions Table

WHEN: A back-matter page that defines the taxonomy the whole report leans on, so the reader can
re-enter mid-deck and decode a term. Derived from Deloitte's "Key Definitions" page (p21 of
deloitte__deloitte_new_mexico_state_university_staffing_study_opportun), the table companion of
the same deck's p10 taxonomy diagram. Use when the deck invents its own terms — SoC, fragmentation,
benchmark set — and body pages reference them without re-explaining.

ANATOMY (1280×720 stage; all values in px):
1. Kicker — x56 y40 w1168 h14, 12px uppercase +10% tracking, band-maroon.
2. Title — x56 y56 w1120, 30px display, max 2 lines. No rule under the title — the table header does that job.
3. Table — x56 y150 w1168. Header band (Term / Definition) 40px maroon; rows separated by 10px white gutters.
4. Term column — 300px wide inside the table: bold 12.5px display, left-aligned; optional one-line sub-label 10.5px gray.
5. Definition column — remaining ~868px: 11.5px gray-1, bulleted, on a light zebra fill (odd rows #F4F4F6, even #E8E8EA).
6. Footnote line — x56 y600 w1168, 10px, holds the definition-page's own methodology footnote.
7. Source line — x56 y660 max-w 900, 10.5px gray-3.
8. Page stamp + firm lockup — right 56 y660, "Page 21 | APPENDIX".

SLOTS:
- kicker: ≤4 words, "Appendix C — definitions" pattern (letter the appendix; the reader navigates by it).
- title: ≤15 words / 2 lines. State the contract: which document uses these terms, not just "Definitions".
- col-term / col-def: the header cells. Keep them one word each.
- term ×5: ≤28 chars. The exact phrase used in body pages — mismatch here breaks every cross-reference.
- sub-label (optional): one short line under a term, e.g. "comparison cohort". Max one term per page.
- definition bullets ×2–3 per row: ≤38 words total per row. A definition is an operational rule ("50% or less of FTEs are not centrally located"), not a dictionary entry.
- example-line: the second bullet of row 1 is an "Example:" line — keep at most one example row; examples belong in footnotes otherwise.
- footnote-line: screening window / cohort size — the one methodology claim this page owns, marked sup(1) on the term.
- source-line: where the terms came from + taxonomy version.
- page-stamp: "N | APPENDIX".

FILL:
1. Replace kicker/title. The title has no rule slot — resist adding one; the maroon band is the page's rule.
2. Rows: each <tr> is one term. Copy a <tr> to add a 6th row only if every definition fits 2 bullets (the gutter eats ~86px/row); 5 rows is the safe cap at 600px of table height.
3. Definition column is a semantic <ul> per row — add/remove <li>, keep bullets flat (one level).
4. To recolor: --band drives header band + bullet markers + kicker (one color decision). --accent is the red for footnote markers/emphasis only. Zebra fills are hardcoded grays — leave them, the band is the only hue.
5. Footnote: sup marker lives inside the <th> of the referenced term; footnote text sits in .notes, not the source line.

CHART RECIPE: n/a — table template. The discipline is the header-band + zebra + single-hue rule.

VERIFY:
- Title ≤15 words / ≤2 lines.
- Header band present and legible (white on band clears 4.5:1 — check the swapped brand color if recolored).
- Every term row has 1–3 bullets; none over 2 definition bullets wrapped past 3 lines.
- One hue (band) + grays; red reserved for the footnote mark. No blue/yellow data palette bleeding into a definitions page.
- Source line bottom-left; page stamp bottom-right.

DON'T:
- Dictionary definitions — the corpus page wins by encoding measurement ("calculated estimated FTEs per process"), not etymology.
- A definitions page for terms the body pages never use — that's decoration.
- More than one accent: the maroon band is the emphasis; adding the deck's chart blue/green/yellow makes it a second content page, not an appendix.
- Nesting bullets or numbering rows — the row order carries no sequence; alphabetize or order by first appearance in the body.
- Letting the term column wrap: terms are the lookup anchor, keep them ≤28 chars.

SOURCE: deloitte__deloitte_new_mexico_state_university_staffing_study_opportun p21 "Key
Definitions" (sheet sw_sheets/deloitte__deloitte_new_mexico_state_university_staffing_study_opportun_s02.jpg,
row 3 frame 1); taxonomy context from the same deck p10. Palette notes (blue+yellow data pair,
red emphasis; maroon band observed on-sheet, hex not published) from
reviews/deloitte__deloitte_new_mexico_state_university_staffing_study_opportun.md §Color system.
