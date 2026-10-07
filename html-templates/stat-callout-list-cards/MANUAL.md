# stat-callout-list-cards — Serif Claim + Solid Callout Boxes

WHEN: a page that argues from 2–4 headline figures presented as **filled callout boxes** —
figure plus a full sentence inside the box, the box colour carrying the emphasis. This is the
PwC boardroom "3 coloured callout boxes" pattern, where readers scan by colour and each box is
a self-contained claim. Evidence: `pwc_strategy__pwc_boardroom_agenda_2022` p1 (row of coloured
boxes beside an aerial photo) and p24 (callout column + photo);
`sw_sheets/pwc_strategy__pwc_boardroom_agenda_2022_s00.jpg` (p1 row 0 col 0) and
`..._s02.jpg` (p21–p30 sheet, p24). Palette facts: brand orange #D04800 (nominally #D04A19;
compression shifts the sample), highlight yellow #F8B000, slate blue #98B0C8 (deck's only cool
accent), grays #F0F0F0 / #DCDCDC / #464646.

ANATOMY: slot map with px coords on the 1280×720 stage (1rem = 1 stage px):
1. `eyebrow` — kicker, x:56 y:40, 12.5px orange caps (letter-spacing .15em).
2. `claim` (h1) — serif claim title, x:56 y:66, 31px/1.16, max-width 1130 (2-line gate).
3. `rule` — hairline, y:~172.
4. `cards` row — x:56→1224, y:214; three boxes 379×268, gap 20. Each box = `ck` kicker
   (10.5px caps), `fig` figure, `sen` sentence.
5. `card--orange` (figure #1, the emphasis box), `card--blue`, `card--yellow` — fixed order,
   emphasis first.
6. `sowhat` band — x:56, y:520, orange left-border + tint field, the "so what" sentence.
7. `ctx` card — 300px gray block, the method/n note (the deck's gray-box habit).
8. `source` / `pageno` — footer rule y:666; source bottom-left, "24 | SECTION" bottom-right.

SLOTS:
- `claim` — 13–15 words, ≤ 2 lines. Must be a conclusion the figures support ("Retention now
  turns on personalisation, not price…"), not a section label.
- `card[i].ck` — 1–3 words, the *kind* of evidence: "Stated preference", "Value at stake",
  "Downside". A wall of identical kickers kills the scan.
- `card[i].fig` — the figure only: max 5 glyphs + unit span (`68%`, `2.7×`, `$1.4bn`). 56px is
  sized for ≤ 5 glyphs; longer fills ("€1.24bn") drop the unit to 24px and test for wrap.
- `card[i].sen` — 1–2 lines (≤ ~90 chars), full sentence with the figure's referent. No figure
  inside the sentence — it's already the heading.
- `sowhat` — ≤ ~140 chars, the decision the page forces. Starts with a bolded "So what:".
- `ctx` — method/n detail ≤ 2 lines; if absent, widen `.band` to full row.

FILL: replace `.eyebrow`, h1 text, then per card: kicker text, `.fig` number (keep the
`<span class="unit">` wrapper — the unit is deliberately smaller), `.sen` sentence. Reorder the
three cards by argument order, not magnitude. Swap box colors by class (`card--orange` →
`card--yellow`); for a one-colour client make box 1 `--accent` solid, boxes 2–3 `--field` gray
with `--ink` text (gray-for-the-rest is the honest fallback, keep orange only as the single
emphasis). Recolor via `:root` tokens only.

CHART RECIPE: none — typographic figures. The "one accent + gray" rule becomes "one emphasis
fill (orange) + muted companions"; if a client palette forces three fills, they must be one
hue's lightness steps, not three hues (the review flags p27/p31 hue-scatter as a defect).

VERIFY: claim ≤ 15 words / 2 lines; page reads with one accent (orange) — check no stray blue
text outside its box; contrast — white on #D04800 = 4.53:1 ✓ (borderline, keep figures ≥ 13px
bold), ink #1A1A1A on #F8B000 = 13:1 ✓, ink on #98B0C8 = 9.5:1 ✓ (that's why the blue/yellow
boxes take dark text, white would fail); figure has a unit span not a run-on string; source line
present + footnote sup; page number "24 | SECTION".

DON'T: topic title; white text on yellow (fails contrast) or yellow text on white; more than 4
boxes on one page (the deck's six-hue scatter is explicitly called a defect in the review);
kickers that just repeat the figures; boxes as decoration disconnected from the claim.

SOURCE: firm PwC (strategy). Deck `pwc_strategy__pwc_boardroom_agenda_2022`, pages p1 and p24
via `sw_sheets/pwc_strategy__pwc_boardroom_agenda_2022_s00.jpg` (p1) / `..._s02.jpg` (p21–p30).
Palette/typography facts (orange #D04800, serif titles 24–30pt, coarse size hierarchy, colour
by layout not meaning) from `reviews/pwc_strategy__pwc_boardroom_agenda_2022.md` §Colour system.
Real house face is a PwC serif (Avenir body); Georgia stands in for the title face.
