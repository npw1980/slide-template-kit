# icon-column-advice-trio — Three advice columns with line icons and violet action leads

WHEN: Use when the page tells one audience "it depends where you are" and hands each segment its own
next move — the classic maturity-spectrum / playbook page. The device is a line icon opening each
column, a bold group label, an accent-colored imperative line, and a plain body paragraph. Evidence:
accenture__accenture_accelerating_global_companies_toward_net_zero_by_2 p30 ("maturity-spectrum
advice"), read in `sw_sheets/accenture__accenture_accelerating_global_companies_toward_net_zero_by_2_s02.jpg`
(row 2, last frame). The same icon stroke appears as a captioned icon row under the carbon-intelligence
columns on p27/p28 (same sheet, row 2 frames 2–3), so the icon family is one system, not one page.

ANATOMY: numbered slot map on the 1280×720 stage (all coords px, `rem` == stage px in the file):
1. `slot-kicker` — 56,38 → width ≤400. Uppercase 11px, letterspaced .14em, gray-2.
2. `slot-title` — 56,56 → max-width 1160. 27px bold Helvetica stack, line-height 1.22, up to 2 lines.
3. Column 1 block — x 56, y 150, width 378 (right edge 434). Icon 46px at (56,150), label starts y 212.
4. Column 2 block — x 435 (hairline border-left at x 435, padding-left 30), width 378 → right edge 813.
5. Column 3 block — x 835 (hairline at 835), width 378 → right edge 1183, flush to the right margin.
6. Inside each column: icon 46×46 → 16px gap → label (14.5px bold) → 2px accent underline 34px wide →
   13px gap → action line (13.5px bold, `--accent`) → 13px gap → body (11.5px / 1.52 / gray-1).
7. `source` — 56, bottom 28 → max-width 1000. 10.5px gray-2, superscript markers.
8. `pagestamp` — right margin, bottom 28. "p. 30 | ADVISORY PLAYBOOK", page part set in accent.

SLOTS:
- `slot-kicker` — ≤38 chars. A section name, not a sentence ("Maturity spectrum — where you are"). Bad: a full claim duplicating the title.
- `slot-title` — action title, HARD GATE ≤15 words / ≤2 lines. Quantitative or comparative claim, not a topic. Bad: "Maturity model" / "Our view on net zero".
- `slot-label-1..3` — ≤40 chars, ends with a colon, names the segment as a noun phrase. Bad: "Phase 1" (no audience), or three labels of unequal length that rag the columns.
- `slot-action-1..3` — ≤90 chars / ≤3 lines. One imperative sentence: verb first, no "should", no "consider". These three lines are the page's argument — if they read the same, the page says nothing.
- `slot-body-1..3` — ≤900 chars / ≤13 lines at 11.5px within the 348px text column (the render fills 10–12
  lines; three columns whose bodies all bottom out at the same baseline is the target). Plain prose,
  one bold phrase inside each, superscript marker only where a methodology claim needs one. Bad: three
  identical boilerplate paragraphs, or bodies of unequal length that rag the page bottom.
- `source` / `pagestamp` — required, never empty.
- Column count: 3 is the proven shape (1183−56 = 1127 usable px, 378 each + 30 gutter). A 4-column variant needs each width ≤265 and a shorter action line — not recommended below 13px.

FILL:
1. Replace `slot-kicker`, `slot-title`, then the three `slot-label-N` / `slot-action-N` / `slot-body-N`
   text nodes. Column order is a reading order — put the segment your reader belongs to first.
2. Swap the icon: each `<svg class="icon">` holds 2–3 primitive paths in a 46×46 viewBox; stroke rules
   live in `.icon .ln` (stroke `--accent`, width 1.5) and the fill dot in `.icon .dot`. Replace only the
   `d`/`cx`/`cy` values inside one svg — never add a `stroke` attribute inline or the recolour rule breaks.
   Keep icon weight identical across the three, otherwise the columns look like three different decks.
3. Recolour: change `--accent` only. `--accent-2` and `--accent-bg` inherit nothing, so set them to
   lighter/darker values of the new hue (`--accent-2` ≈ accent mixed 45% white, `--accent-bg` ≈ 90% white)
   or leave them — nothing on this page renders `--accent-bg`, it exists for a tinted variant.
4. Body emphasis: wrap the phrase in `<b>` inside `slot-body-N`; the `b` rule raises it to `--ink` and
   weight 700, so it reads as the column's point without colour.
5. Footnotes: add `<sup>a</sup>` in the body and the matching letter in the source line. Three markers on
   one page is the ceiling; more means the reader stops checking.

VERIFY:
- [ ] Title ≤15 words and ≤2 lines at 27px within 1160px. If it wraps to 3, resize the slot — do not trim copy silently.
- [ ] Each column's action line is a different imperative and a different colour (accent) from its label.
- [ ] Exactly one hue on the page: violet. Greys are `#4A4F55 / #7D7D7D / #B8B8B8 / #D9D9D9` — no second brand colour.
- [ ] Text on the accent line: 13.5px bold `#7B1FF0` on white ≈ 6.5:1 — clears 4.5:1. Do not lighten `--accent` below `#8E24EA` for text.
- [ ] Source line bottom-left present with superscript markers; page number bottom-right.
- [ ] No icon filled solid — all three are strokes, matching the deck.

DON'T:
- Topic titles ("Carbon intelligence", "Next steps") — the deck never titles a content page with a noun.
- Icons as colour blobs or stock glyphs; the corpus page uses 2px-equivalent monoline strokes.
- An action line that restates the label ("Get started" under "Companies just getting started").
- Walls of kicker text above the columns — the kicker is one short line; emphasis lives inside the columns.
- Four hues because each column "deserves" its own. Single-hue restraint is the reason this reads as consulting.

SOURCE: accenture__accenture_accelerating_global_companies_toward_net_zero_by_2, deck "Accelerating
global companies toward net zero by 2050" — p30 (maturity-spectrum advice, `sw_sheets/…_s02.jpg` row 2
frame 5), with the icon-row device from p27–p28 (`…_s02.jpg` row 2 frames 2–3). Palette and layout
facts from `reviews/accenture__accenture_accelerating_global_companies_toward_net_zero_by_2.md`
(three-zone layout, purple-semantic-only, no kicker above titles) and hex values from
`reviews/accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o.md` §Color system
(#7B1FF0 / #A45CF0 / #E7D9F8 / #7D7D7D / #B8B8B8 / #1A1A1A).
