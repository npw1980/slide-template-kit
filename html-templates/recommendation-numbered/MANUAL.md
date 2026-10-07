# recommendation-numbered — Numbered Recommendation List with Priority Emphasis

WHEN:
The closing / "next steps" page of a findings deck: an action title plus a numbered
list of recommendations, where 1–3 items are flagged as needing a decision. Derived
from `deloitte__deloitte_accelerated_access_review_uk_mapping_2015` p11 ("Top areas
for review in phase 2" — twelve numbered discs, two re-coloured green as priorities,
evidence-base lead-in sentence, two-part grey footer). The same grammar appears as an
EY "conclusion checklist" at `ey__ey_risk_management_in_a_time_of_transformation_2024`
p38 (variant noted in FILL).

ANATOMY (1280×720 stage):
1. kicker  `left:64  top:48   w:600`   — 12px, uppercase, tracking .14em
2. title   `left:64  top:72   w:1072`  — 31px/1.12 bold, action claim
3. lead    `left:64  top:146  w:1040`  — 16px/1.45, names the evidence base
4. legend  `left:64  top:181  w:620`   — 12px + 13px disc, says what green means
5. list    `col A left:64 w:540`, `col B left:676 w:540`, `top:214`, 6 items per column
   divider hairline `left:640 top:214 h:444`
6. items   local `top: i*74` (i = 0..5 per column); disc `28×28 left:0 top:1`;
   text `left:42 w:498` 14px/1.45
7. footnotes `left:64 right:64 bottom:56` — 10.5px, superscript definitions
8. footer  `left:64 right:64 bottom:24` — rule on top; source bottom-left,
   `11 | RECOMMENDATIONS` + copyright bottom-right

SLOTS:
- `kicker` — section chip. One line. Good: "Recommendations · Phase 2 scope". Bad: three sections listed.
- `title` — the claim, not a topic. Gate: ≤15 words / 2 lines. Good: "Twelve opportunities carry forward; two need a Phase 2 decision now". Bad: "Recommendations" / "Next steps".
- `lead` — 1 line max (~115 chars @ 16px). Names method + sample; this is the honest replacement for a source-less page.
- `legend` — states the priority rule as a count ("2 of 12"), so emphasis is not decoration.
- `item.N` — 2 lines max @ 14px/1.45. Lead-in = verb-first action ("Standardise…", "Retire…"), tail = the measured reason or scope number. No bare nouns.
- `prio` — apply `class="prio"` to items the client must decide. Emphasis = deep-green disc fill + bright-green ring + bold text; 1–2 items per page.
- `source` / `page` — required; superscripts only where a methodology claim needs them.

FILL:
1. Replace `kicker`, `title`, `lead`, `legend` text nodes.
2. Replace each `.item`'s `<span class="disc">` number and `<span class="txt">` content.
   Numbering is manual text, not CSS counters — keep 1..12 reading column A then column B.
3. Priority: move `class="prio"` onto the chosen `.item` divs; keep everything else default.
4. Item count: pitch is the only structural number. 12 items = pitch 74 (built);
   10 items = pitch 88 (`nth-child(2..6)` = 88/176/264/352/440); 16 items = pitch 55 with
   8 per column and 13.5px text. Do not shrink the disc below 24.
5. Accent swap: `--accent` (default `#7CB518`) is the emphasis hue; `--accent-deep` is the
   same hue one lightness darker and is what sits behind the priority numerals — change
   the pair together, because an accent light enough to read as decoration breaks the
   4.5:1 numeral check. `--num` is the non-emphasis disc hue; `--title` the title colour;
   `--ink` body text. Set `--accent: var(--accent-deep)` if the brand accent is already dark.
6. EY conclusion-checklist variant: same geometry, replace the disc with a square outline
   (`border-radius:0; background:#fff; border:2px solid var(--num)`) and put a ✓ glyph on
   items already satisfied — one page, conclusions checked rather than ranked.

CHART RECIPE: N/A — no chart. The "quantitative" content lives in the item tails and the
title (percentages, day counts, n=). Keep one number per item; a second number belongs in a footnote.

VERIFY:
- [ ] title ≤ 15 words and ≤ 2 lines at 31px/1.12 (measured as shipped: 11 words, 1 line)
- [ ] source line present bottom-left; page stamp + running section bottom-right
- [ ] one emphasis color (`--accent`); non-emphasis discs are one other hue + gray
- [ ] ≤ 3 hues total on the page (title navy, disc teal, accent green)
- [ ] white numerals on the disc clear 4.5:1 — teal `#10708C` 5.5:1 and deep green `#46710E` 5.8:1 pass.
      The bright green `#7CB518` sits behind no text: it is the legend dot and the disc ring only.
- [ ] no item runs to a third line; footnote superscripts have matching definitions
- [ ] no network calls: system font stacks only, zero JS, zero images

DON'T:
- Topic titles ("Recommendations", "Next steps") — the source deck's own weakness; the review explicitly says copy the pattern, not the title practice.
- Highlighting more than 2 items — priority emphasis collapses into noise above 2.
- Numbering as decoration: 12 items means 12 real, distinct actions, not 12 restated findings.
- A wall-of-text lead-in; it is one line naming evidence base and sample size.
- Duplicating a number across lead-in and item (the shipped placeholder deliberately uses distinct samples: 37 interviews / 12 assessments / 218 of 434).
- Mixing boxes + chevrons + discs; this page is plain numbering with color semantics.

SOURCE:
Firm: Deloitte (Deecon) — `deloitte__deloitte_accelerated_access_review_uk_mapping_2015`,
p11 (visual read on `sw_sheets/deloitte__deloitte_accelerated_access_review_uk_mapping_2015_s01.jpg`,
sheet index 1 = floor(11/10), page 11 = row 1 col 1). Corroborating exemplar:
`ey__ey_risk_management_in_a_time_of_transformation_2024` p38 (conclusion checklist).
Palette roles and the "topic-title anti-pattern" ruling: `reviews/deloitte__deloitte_town_of_tillsonburg_it_strategic_review_council_upd.md` §Title-zone anatomy / §Copy vs ignore,
plus `DESIGN_PLAYBOOK.md` §palette ruling. Sampled hues: deep navy-teal title, blue-teal
`#10708C` numbering, Deloitte 2015 green `#7CB518` emphasis (regional green variants differ; remappable).
