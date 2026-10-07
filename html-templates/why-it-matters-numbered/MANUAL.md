# why-it-matters-numbered — Claim Title + Four Numbered Moves + Bottom Line Band

WHEN: The follow-on page to an "admits-the-question" opener: the section has established *whether*
the trend matters, and this page says what the audience should *do*. It carries a claim title, four
numbered action columns, and a grey "Bottom Line" verdict band that closes the section. Evidence:
"be TMT Predictions 2025" (Deloitte Belgium, deck slug `content_dam_assets_zone2_be_e`), p9 (S0057,
corpus/sheets/sheet_006.jpg row 2 col 2), and the recurring "What should companies consider?" shape
on p14/p18/p21 (S0062, S0066, S0069 in sheet_007.jpg). Catalog archetype: "why-it-matters numbered",
device "four numbered columns / photo corner / Bottom Line".

Firm font note: source is the Deloitte house sans (2023 identity "STardom"); this template stands
in with `"Helvetica Neue", Arial` grotesque. Titles stay black on this variant — the deck does not
paint the claim title with the gradient here; the gradient is reserved for the numbered squares and
the kicker/band label, and that restraint is why the page reads professional.

ANATOMY: numbered slot map, px coords on the 1280×720 stage (1rem = 1 stage px):
1. `kicker` — x:64, y:50, w:760, 11.5px caps, 1.8px tracking, gray-2.
2. `claim` (h1) — x:64, y:84, w:1152, 30px/1.25, black, 2-line gate.
3. `cols` ×4 — x:64 / 360 / 656 / 952 (264 wide each), y:216. Each column:
   `n` 34px rounded square, 135° gradient `grad-a → block` (#D5379A → #B94B9F), white numeral;
   `h` 13.5px bold lead-in; `t` 12.5px body, gray-1.
4. `band` — Bottom Line: x:64, y:560, w:1152, fill `--band-bg #E7E9EA`, 5px left border in grad-a,
   label (10.5px caps, grad-a) + one bold verdict sentence (15px, ≤3 lines).
5. `foot` — rule y:680; source line x:64 (9.5px, footnote sup where survey/method claims live);
   page number right ("NN | SECTION", number grad-a).

SLOTS:
- `kicker` — max ~60 chars: "2025 Global TMT Predictions · Power & compute" style. Locator, not thesis.
- `claim` — max 115 chars / 2 lines, ≤15 words, quantitative where honest. The source deck often
  writes the question form ("What should companies consider?") — permitted, but a numbered-move
  page earns more trust with the answer in the title and the question demoted to the kicker.
- `cols[].h` — max ~55 chars / 2 lines. An imperative or decision noun phrase ("Lock the energy
  contract before the build, not after."). Bad: "Considerations"/"Area 3".
- `cols[].t` — max ~200 chars / 5–6 lines. One action + one proof point each; if a number is the
  argument, it goes here, not in the headline slot.
- `band.b` — max ~230 chars / 3 lines. The section's one-sentence verdict — a "should", not a summary.
- `source`, `pageno` — same discipline as the opener.

FILL: (1) replace `claim`, the four `col` triplets (`n`/`h`/`t`) and `band.b` — the geometry never
moves. (2) Numbers: edit `.n` text (1–4; if you have three moves, widen columns to 374px each by
overriding `.col1..col3` widths and drop `.col4`; never keep an empty "4"). (3) Band label is
fixed copy "Bottom Line" — resist "Takeaways". (4) Footer text + `sup`. (5) Recolor for another
firm: only `--grad-a/--grad-b/--block` change, always as a pair (warm → cool, ~180° apart);
single-hue clients use `--grad-a` flat (the 135° gradient still renders, just monochrome) — do not
introduce a third hue.

CHART RECIPE: none by design; this is the action page, not the evidence page. If a proof figure is
required it belongs on the opener or an exhibit page; a bar chart here competes with the four
columns and breaks the page's job.

VERIFY: `claim` ≤15 words / ≤2 lines at 30px/1152 (if line 3 appears, cut the claim, not the font);
all four columns end above y:560 (band top); band sentence ends above y:646; one colour device only
(gradient squares + band border in the same accent pair — squares and band must match); text
contrast: `claim` and `band.b` black-on-`--bg`/on band ≥ 12:1, column body gray-1 ≥ 4.5:1, white
numerals on gradient squares ≥ 3:1 (dark magenta end keeps this); source + page number present;
no webfonts, zero network calls.

DON'T (corpus failure modes): topic-titled columns ("Marketing", "Operations"); numbers used as
decoration — four identical paragraphs with 1–4 painted on (the source always pairs the number with
an imperative); kicker walls; a Bottom Line band that restates the title instead of ruling;
gradient on everything (the deck keeps the huge gradient only on the interrogative opener, not on
this page); more than four moves — a fifth column collapses the grid; ten-hue charts jammed beside
columns.

SOURCE: firm Deloitte (Belgium). Deck `content_dam_assets_zone2_be_e` ("be TMT Predictions 2025").
Pages 9 (S0057), 14 (S0062), 18 (S0066), 21 (S0069) — sheet_006.jpg row 2 col 2 for S0057,
sheet_007.jpg for the rest (S0062 row 1 col 2, S0066 row 2 col 1, S0069 row 2 col 4). Catalog
`catalog_1-20.csv` archetype "why-it-matters numbered" (device "four numbered columns / Bottom
Line"). Palette pixel-sampled from `corpus/pdfpages/_content_dam_assets_zone2_be_e_-13.png`
(teal #36e0df, magenta ramp #d5379a/#b94b9f, paper #f2f2f2); no `reviews/` file existed for this
deck.
