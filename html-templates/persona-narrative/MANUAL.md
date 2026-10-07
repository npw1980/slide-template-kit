# persona-narrative — Single Persona Told As A Story

WHEN: One named persona carries the page — a "here is the customer/learner/user in one sentence, then three facts about their life" argument. Extracted from a Gartner-type catalog page (`S0036`): sentence title in brand blue, bold narrative lead-in, en-dash bullets, cut-out portrait bottom-right, firm lockup. Use when depth on one person beats breadth over several; for multiple personas side by side use `persona-intro-grid`.

ANATOMY (1280×720 stage):
1. Title (h1) — (64, 56), 1152 wide, 42px/1.08 weight 800, brand blue, max 2 lines.
2. Lead-in line — (64, 168), 780 wide, 21px weight 700 ink; the persona name highlighted in accent.
3. Story list (ol.story) — (64, 240), 790 wide, three en-dash `<li>` rows, 17px/1.5 gray-1, dash marker in accent. Text column stops ~x=854 so the portrait never competes.
4. Portrait — right:64, top:262, 250×290 SVG placeholder (rounded rect + silhouette) with a 1-line gray caption under it.
5. Firm lockup — right:64, bottom:52, 15px bold accent, "YOUR FIRM.®" stand-in.
6. Foot rule — hairline (64→1216) at y=662.
7. Source line — (64, 674), 9.5px gray: study, n, what was anonymized.
8. Running head — "NN | SECTION", right-aligned, bottom 18, `NN` in accent.

SLOTS:
- title: one claim sentence ≤15 words / 2 lines at 42px. It states what the persona teaches, not that the persona exists.
- lead: one sentence ≤24 words, "This is the story of NAME — who they are" shape; NAME colored.
- story1..3: each ≤30 words, one fact each — background fact, constraint fact, implication fact (the three that make the title true). En-dashes, not smartart arrows.
- portrait_caption: photo credit or "cut-out, right-aligned" note, ≤50 chars.
- lockup: your wordmark; one hue (accent), no tagline.
- source: survey/interview n + the anonymization sentence — this page's honesty gate.
- runhead: page + section.

FILL:
1. Rewrite h1, lead, and the three `<li>` items; keep dash markers (`::before`) as-is.
2. Swap the portrait `<svg>` for an `<img>` in the same 250×290 right-anchored box (object-fit: cover if the photo's taller than wide).
3. Replace "YOUR FIRM.®" in `.lockup` with the real wordmark text; keep `color:var(--accent)`.
4. Recolor `--accent` for a different house (title blue is eye-sampled ~#1560A8 — the catalog block has no review hex list; treat it as placeholder).
5. If bullets grow to four, drop the list font to 16px and tighten `margin-bottom` from 18 to 14 so block stays inside y≈240–600.

CHART RECIPE: n/a — this template encodes nothing numerically; the n= belongs in the source line as text.

VERIFY:
- Title ≤15 words / ≤2 lines; lead ≤2 lines; three story lines ≤2 lines each.
- Text column right edge (x=854) stays clear of the portrait box (x=966→1216); nothing past y=714.
- One accent hue on white — blue #1560A8 ≈ 5.2:1 (passes 4.5:1); accent used on title, name, dashes, lockup, runhead number only; body is gray ramp.
- Source line states n and the anonymization/composite disclosure.
- Lockup present bottom-right above the running head.

DON'T:
- A portrait that collides with text — the whole design is text-left / portrait-right; if you need a full-bleed image this is the wrong template.
- More than ~4 story bullets (this is a story, not a findings list; more belong in an exhibit page).
- Making the persona name bigger than the claim title — hierarchy is title > lead > facts.
- Stock-photo "thinking woman" clichés as-is (the source deck's own weakness); state composite/anonymized honestly in the source line.
- Topic title ("Example: our typical student"). The title must say what changes because of her.

SOURCE: Catalog slide S0036 (Gartner-type persona-narrative page) — `corpus/sheets/sheet_004.jpg` (10-page sheet, 5×2 row-major; page 36 = row 2, col 1). Catalog line: `catalog_1-20.csv` row S0036 — "dash narrative; photo, blue title, story left; thinking-woman photo". No per-deck review file exists for this catalog block, so palette hexes are eye-sampled from the rendered page, not review-cited.
