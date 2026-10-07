# methodology-fieldwork-rail — N-figure rail + azure callout + approach columns, EY-style

WHEN: survey-deck methodology page for an executive audience — one giant N figure, a compact
fieldwork table (window / mode / geography / response / weighting), the approach told in three
columns, and an explicit limitations line. From EY-Parthenon's "Generative AI in retail and
commercial banking" (2023), "Background and methodology" p3, with the highlighted limitation
device read from the ICO deck (p12). Use whenever the honesty of the sample is the argument.

ANATOMY (1280×720 stage):
1. Title block — 56,40 → 1168×114: blue kicker (12px caps), 32px label title
   ("Background and methodology"), 2px `--accent-dk` rule under.
2. Azure callout band — 56,160 → 1168×92: one white sentence that *restates the survey in full*
   (who, how many, when), with the count bolded.
3. Left rail — 56,286 × 300 wide: giant `N=151` figure (58px, accent) + caption, then a 5-row
   fieldwork table (104px label column, hairline rows), then the date pill ("Conducted in July
   2023"). This is the template's spine: N table as a vertical rail.
4. Approach columns — 414,286 → 1168×264, 3 equal columns (30px gutters): each h2 (12.5px,
   1.5px accent underline) + 3 bullets, 12.5px gray body, square accent markers.
5. Limitation line — 414, bottom:120 → 1168 wide: `--tint` wash + 4px accent left border,
   bold uppercase "LIMITATIONS —" opener. The honesty device, always present.
6. Footer — source line bottom-left (max 860px), firm lockup + page number bottom-right.

SLOTS:
- kicker — ≤ 30 chars, the section name ("Methodology of survey"), not a slogan.
- title — label title ≤15 words / 2 lines; "Background and methodology" is correct; a full
  claim sentence belongs in the callout, not here.
- callout — ~230–280 chars, exactly one sentence; must contain the number and the date. Good:
  bolded N inside. Bad: restating the research topic.
- n-figure — "N=151" style, ≤8 chars, the page's dominant figure.
- n-caption — one line naming the population.
- field-* ×5 — short values, ≤6 words each, one footnoted (weighting claims always footnoted).
- approach-head ×3 — 2–4 word group labels (population/instrument/analysis, or equivalents).
- approach-bullets ×3 — ≤ 3 per column, ~110 chars, each a decision made, not marketing.
- limit — one sentence naming what the numbers are NOT. Non-optional.
- pill — fieldwork month; mirror, not extra info.
- source-line — the deck's convention: instrument, date, (n=…, n=…, n=…) with stage counts.

FILL:
- Replace every text node. A fourth approach column: `grid-template-columns:repeat(4,1fr)` and
  drop bullets to 2 per column. Fewer than three: one wide column left-aligned.
- Table: add/remove `<tr>` — the hairline is per-row, the label column stays 104px. Five rows is
  the cap at 286rem start before the rail collides with the pill (21rem/baseline max).
- Footnotes: superscript letters (a,b,c,d) trail the claims they modify; the numbered ones
  (1,2) live in the approach columns; the final note lands in the source line as "see notes
  page NN". Keep the pairs consistent when editing.
- Recolor: swap `--accent` / `--accent-dk` (and keep `--yellow` for the lockup only — the
  source rule is yellow never appears outside the logo). Any 4.5:1-blue with white text works;
  if the brand is very light, keep `--accent-dk` at the darker value for band/pill/borders.

VERIFY:
- [ ] Title ≤15 words / ≤2 lines; kicker is a section name.
- [ ] Callout sentence has bolded count + date; ≤3 lines.
- [ ] N figure present and dominant; table rows ≤5.
- [ ] Limitations line present and honestly worded.
- [ ] One emphasis color + gray ramp; yellow only in the lockup.
- [ ] White-on-callout contrast ≥4.5:1 (#095FA4 ≈ 6.4:1 — do not swap to a lighter brand blue without re-checking).
- [ ] Source line with stage n's, page number bottom-right.

DON'T:
- Don't delete the limitations line — an unweighted survey presented as projectable is the #1
  methodology-page failure in the corpus.
- Don't make the approach bullets into survey content ("we asked about budgets") — they must be
  *method* decisions (who was in, what was piloted, how it was cut).
- Don't stack more than 5 table rows or the rail runs into the footer.
- Don't color table labels with the accent; labels are gray, values are ink, only the N figure
  and markers carry the accent.

SOURCE: EY | Parthenon — "Generative AI in retail and commercial banking"
(ey__ey_generative_ai_in_retail_and_commercial_banking_2023), "Background and methodology" p3,
read in sw_sheets/ey__ey_generative_ai_in_retail_and_commercial_banking_2023_s00.jpg (row 2,
frame 3); archetype "methodology / callout+columns" per TEMPLATE_HARVEST.json. Limitation-line
device cross-read from ey__ey_study_initial_coin_offerings_icos_the_class_of_2017_on p12
("highlighted limitation line + approach bullets"). Palette, kicker/claim-title three-zone
structure, giant-numeral habit, stage-count source-line convention and "yellow inside the logo
only" rule from reviews/ey__ey_generative_ai_in_retail_and_commercial_banking_2023.md; the
azure is deepened from the deck's ~#1B96E0 to #0A74C4/#095FA4 to pass the 4.5:1 text-on-accent
gate.
