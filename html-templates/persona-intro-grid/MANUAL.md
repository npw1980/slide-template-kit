# persona-intro-grid — 4-Column Persona Intro Row

WHEN: A survey segmentation page that introduces 3–5 customer/mindset personas side by side, each with a photo, a colored name, a one-line positioning claim, and a short body. Extracted from Accenture's *Global Financial Services Consumer Study 2019* "Meet the personas:" (p8). Use when the argument IS the persona set — not when one persona needs a story (see `persona-narrative`).

ANATOMY (1280×720 stage):
1. Kicker — (64, 36), 640 wide, 11px bold all-caps, accent violet, letter-spaced.
2. Study hashtag — right-aligned at x=1216, y=36, 11px gray (the deck pins `#FSConsumerStudy` top-right on every content page).
3. Title (h1) — (64, 72), 1152 wide, 54px/1.04 weight 800, max 2 lines. Claim title, not a topic.
4. Persona row — (64, 208): 4 figure cards, each 270px wide, 24px flex gap.
   4a. Photo placeholder — 270×150 inline SVG rect (rx 4) + generic silhouette + caption line. Replace with a real cut-out.
   4b. Persona name — 18px below photo, 16px weight 800, ends with a colon.
   4c. Claim line — 16px/1.28 weight 700 ink, 2 lines max.
   4d. Body copy — 12.5px/1.55 gray, 4–6 lines, ends with the segment share ("account for N percent of respondents").
5. Foot rule — hairline across (64→1216) at y=650.
6. Source line — (64, 666), 10px gray, with `<sup>` marker; footnote line at (64, 692), 8.5px.
7. Running head — right-aligned "NN | SECTION", bottom 28, `NN` in accent.

SLOTS:
- kicker: ≤45 chars, all-caps, names the study lens. Bad: "Personas" (topic). Good: "CUSTOMER PERSONAS · SURVEY SEGMENTATION".
- hashtag: deck hashtag, ≤25 chars; delete if the deck has none.
- title: 1 claim sentence, ≤15 words, ≤2 lines at 54px/1152. Quantitative > topic ("Four service personas explain why one in three customers churn" vs "Customer personas").
- persona_nameN: 1–12 chars + colon; the name is a label, the color is one token (see DON'T).
- claimN: ≤12 words, one positioning statement the persona actually implies. Bad: restating the name.
- bodyN: ≤90 words / 6 lines; must carry the segment share % (ties the persona to data).
- photoN: real photography (people in context) or a real illustration; the SVG placeholder is replacement fuel, not the show.
- source: survey name, year, n, markets, weighting note — with a `<sup>` footnote marker; footnote line explains the methodology claim.
- runhead: page + section.

FILL:
1. Replace the h1 text with your claim title (check: ≤15 words/2 lines).
2. For each of the four `figure.card` blocks: swap the `<svg class="photo">` for an `<img>` (same 270×150 box) or keep the placeholder; rewrite name/claim/body; keep the `c1..c4` classes so the color ramp order holds.
3. Percentages: change the "account for N percent" sentences; make them sum to ~100.
4. Accent swap: set `--accent` in `:root` (e.g. KPMG `#00338D`, PwC red `#C8102E`); `--accent-soft` is auto-derived by eye — pick a step ~35% lighter (violet example: #8E24EA → #B983F2).
5. Column count: the flex row takes 3 or 5 cards with `flex:0 0 270rem` swapped to `(1152 − 24·(n−1))/n` per card.
6. Footer: rewrite source/footnote/runhead; the sup stays attached to the methodology phrase in the source line.

CHART RECIPE: n/a — this is a text-card grid; the only data visible is the body percentages (state them as sentences, not charts, matching the source).

VERIFY:
- Title ≤15 words, ≤2 lines at 54px.
- Source line present with a `<sup>` marker where n/weighting is claimed; footnote line exists.
- One emphasis hue (accent) + gray ramp; names use accent / accent-soft / gray only — contrast of accent violet on white ≈ 6.6:1 for bold text (passes 4.5:1).
- Body percentages sum to ~100; runhead present; nothing past y=714.
- Photos are honest boxes with a caption until replaced.

DON'T:
- Four-drama color cycle per persona (source deck really does violet/cyan/charcoal/blue) — the kit gate is one accent + gray ramp + one lightness step; document the source behavior, ship the restrained version.
- Names without claims ("Innovators:" with nothing under it) or topic titles.
- Kicker walls (kicker is one short line; the story is the claim).
- Photo strip taller than 150px — it pushes the copy off the canvas, as happens in the source deck's 3-column variants.
- Making a persona's body an essay; if >6 lines, the claim isn't doing its job.

SOURCE: Accenture, `accenture_2019_accenture_global_financial_services_consumer` p8 ("Meet the personas:") — page rendered in `sw_sheets/accenture__accenture_2019_accenture_global_financial_services_consumer__s00.jpg` (sheet = pages 1–10, 5×2 row-major, page 8 = row 2, col 3). Analyzed in `reviews/accenture__accenture_2019_accenture_global_financial_services_consumer_.md` (kicker/hashtag convention, weight-driven one-family hierarchy, persona palette narrative). Violet hex family (#8E24EA etc.) sampled from sibling Accenture reviews in the same corpus.
