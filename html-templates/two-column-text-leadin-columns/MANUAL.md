# two-column-text-leadin-columns — Two prose columns, bold run-in leads, one accent kicker sentence

WHEN: The page that carries an argument in the analyst's own words, where every
exhibit would be a distraction: findings narrative, context/"why now" pages, a
section that must be read linearly. It comes from
`accenture__accenture_accelerating_global_companies_toward_net_zero_by_2` p3/p5/p8,
where the review records both rules this template encodes — "body zone: 2–4 columns
of ~8–9pt text" (p12) and "kicker/so-what devices appear as purple bold lead-ins
*within* columns rather than separate banner boxes" (p9). The single-column sibling
of the same grammar is `deloitte__deloitte_town_of_tillsonburg_it_strategic_review_council_upd`
p7/p9 (plain bold-lead-in bullets).

ANATOMY (1280×720 stage; `html{font-size:min(100vw/1280,100vh/720)}` → 1rem = 1
stage px; index.html's lengths are the same coordinates):

| # | slot | box (x0,y0 → x1,y1) | type |
|---|------|---------------------|------|
| 1 | claim title | 76,66 → 1116,133 | 29px bold display, ≤2 lines |
| 2 | eyebrow | 76,44 → 1116,58 | 11px caps, +2.4px tracking, gray-1 |
| 3 | column A | 76,146 → 624,578 | 548 wide, 2–3 lead-in paragraphs |
| 4 | column A paragraphs | 76,146 → 624,~470 | 13.5px/1.62 justified, bold run-in lead per paragraph |
| 5 | column B kicker | 656,146 → 1204,~235 | 14px accent bold + 3px accent left rule |
| 6 | column B paragraphs | 656,~255 → 1204,578 | 2 lead-in paragraphs + 1 indented sub-para |
| 7 | method band | 76,596 → 1204,~663 | accent-tint fill, gray top rule, 168px label + text |
| 8 | source line | 76,686 → 1016,703 | 8.5px gray-1, superscripts |
| 9 | running head | 1128,686 → 1204,703 | "N | SECTION", right-aligned |
| — | footer rule | 76,670 → 1204,671 | 1px `--gray-2` |

Column pitch: 548 + 32 gutter + 548 = 1128, inside a 76px side margin. `.cols` is a
flex row; `triple` pitch is available by adding class `tri` to `.cols` (3 × 354 + 2 × 32
= 1126) — the source deck runs 3 columns for exactly the same character count, so it
is a re-pitch of the text, never extra copy.

SLOTS:
- **claim title** — 11–15 words, ≤2 lines at 29px. Good: a measured comparison
  ("cut emissions three times faster than single-target peers"). Bad: a label or a
  question. If it needs 3 lines, it is two findings and the page needs splitting.
- **eyebrow** — "FINDINGS 02 · TARGET-SETTING": section number + sub-topic, ≤6 words.
- **lead-in paragraphs (both columns)** — 4–6 lines each. The first 2–7 words are
  the bold accent run-in and must be a compressed claim, not "Background:" or "Note:".
  Body text never bolded beyond the lead.
- **kicker (column B, slot 5)** — exactly one sentence, ≤34 words. This is the
  deck's signature device: the so-what sits *inside* the text flow in accent bold
  with a 3px accent rule, not in a banner box. Two kickers on one page = no kicker.
- **sub-paragraph (indented)** — optional, ≤2 lines, indented 16px, used for a
  qualifier list ("what separates the fast movers"). One per page.
- **method band** — the label is one word (Method / Basis / Note); text is 2–3
  lines of sample/fieldwork/dates. This is what makes the claims above falsifiable.
- **source line** — all external citations, 8.5px. Superscripts pair with the body.
- **running head** — page number then section.

FILL:
1. Replace `h1.title`; hold the ≤15-word gate. If it wraps to 3 lines, the width is
   right (1040px) and the text is wrong.
2. Fill column A top-down: paragraph 1 = evidence of the trend, paragraph 2 = the
   counter-evidence or the mechanism. Column B opens with the kicker sentence.
   Reading order is A→B, top→bottom; a reader who stops at column A must still get
   the "but", so put the tension in the kicker at the head of B, not the tail.
3. Each paragraph: wrap the lead phrase in `<b>`. Colour comes from the token, so
   never write inline colour.
4. The indented sub-para is `.col p.sub` — keep `margin-left` as-is; it is what
   signals "qualifier" rather than "new point".
5. Method band: `.note > .lab` (one word) + `.note > .txt`. Add the sample-size
   sentence first, then fieldwork window, then the mapping caveat and its `<sup>`.
6. Recolour: `--accent` drives kicker, rules, bold leads, method label, tint. Set
   it once and the page is coherent; a second hue anywhere breaks the single-hue
   claim the source deck earns.
7. Optional third column: `<div class="cols tri">` — same copy, taller page feel.
   Requires dropping ~15% of the text or the columns overflow past y=578.

CHART RECIPE: none by design. The page's data density lives in inline numerals
(71%, 38%, USD 50/tCO₂e) inside sentences, each with a superscript. Never place a
chart on a `two-column-text` page; if you find yourself wanting one, the exhibit
belongs on the next page and the kicker is its headline.

VERIFY:
- [ ] title ≤15 words / ≤2 lines; kicker is one sentence
- [ ] one emphasis colour only (accent) — page must be accent + grays
- [ ] accent text on white clears 4.5:1 (#051C2C on #FFFFFF = 16.1:1)
- [ ] every superscript marker has a matching entry in the source line
- [ ] body columns end above y=578; method band ends above y=670 (render check)
- [ ] no widow line — if a paragraph leaves 1 line alone, cut 8 words
- [ ] method band present with a sample/fieldwork sentence
- [ ] page number + section bottom-right

DON'T:
- Bold lead-in as a label ("Inflation:", "Supply chains:") without a claim — the
  source deck's leads are assertions, and the review credits them for that.
- Kicker walls: >1 kicker sentence, or a kicker longer than 2 lines, is the exact
  report-isms the review tells us to ignore ("the sheer density of the white text
  pages — walls … too dense for a stage template").
- Three or four type sizes competing — the hierarchy here is title / body / footnote,
  plus bold. Anything else is decoration.
- Justified text with huge gaps — if the measure (548px) goes ragged, it is the
  wrong number of words, not the wrong word-spacing.
- Photos or icons: this template is a wall-of-reason test. If it needs a photo,
  it is the wrong template.

SOURCE: accenture__accenture_accelerating_global_companies_toward_net_zero_by_2,
p3 (three-column body with purple bold leads, p3 kicker device per review §layout
item 4) and p5/p8 for the same device; the Deloitte single-column analogue is
`deloitte__...tillsonburg..._p7/p9`. Page images:
`sw_sheets/accenture__accenture_accelerating_global_companies_toward_net_zero_by_2_s00.jpg`
(sheet 0, third tile in the top row = p3; pages sit 5 per row × 2 rows, row-major).
Analysis: `reviews/accenture__accenture_accelerating_global_companies_toward_net_zero_by_2.md`
(§structure p12 "2–4 columns", §copy p9 "kicker as purple bold lead-ins within
columns", §colour p18 "single-hue system", §ignore — "walls … too dense for a stage
template" is the reason this template caps the text). Palette note: the review names
the firm's purple but documents no hex anywhere in the corpus, so `--accent` is the
DESIGN_PLAYBOOK-approved deep navy #051C2C and is explicitly remappable.
