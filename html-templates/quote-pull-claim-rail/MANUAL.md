# quote-pull-claim-rail — Violet pull-quote rail with evidence column

WHEN: A single expert / customer / executive quote carries the page, and the
quote is strong enough to be the argument. The source is Accenture's Global
Financial Services Consumer Study (2019): the violet pull-quote + justified-
body synthesis pages, p28 measured, same grammar p31/p35/p41/p48 and the
"pull quotes in oversized purple type" device the review credits p28/p33/p36.
Use it when you have one memorable line and the evidence that supports it;
use `quote-pull-bubble-cluster` instead when many voices make the point.

ANATOMY (1280×720 stage; all coords are stage px, `index.html` uses `1rem = 1 stage px`):
1. kicker — left 64, top 38, width 660 — two uppercase lines: `SECTION:` + `N. FINDING` (11px bold, azure / gray second line).
2. hashtag — right 64, top 38 — deck hashtag, 12px bold near-black.
3. claim tick — left 64, top 76, 64×3 — short azure rule.
4. claim line — left 64, top 92, width 600 — 19px bold azure, ≤2 lines. THIS IS THE GATE.
5. pull-quote rail — left 128, top 180, width 300: violet bar 56×4 (top), quote 25px bold violet (≈5–6 lines), violet bar 56×4 (bottom, +14px), attribution 11px.
6. evidence column — left 504, top 180, width 600 — 13px/1.58 justified, 2 paragraphs, `<sup>` footnote markers in violet.
7. figure tag — left 128, top 580, width 300 — `Figure N.` + one clause.
8. footer rule — left/right 64, top 648, 1px `--rule`.
9. source line — left 64, top 660, width 820 — 9.5px gray + `<sup>1</sup>`.
10. running head — right 64, top 660 — `28 | APPETITE 1` (page number near-black).

SLOTS:
- `kicker` — 2 lines × ≤55 chars. Good: section label + numbered finding, the way the deck tags every content page. Bad: a sentence, or a wall — the kicker is wayfinding, not copy.
- `hashtag` — ≤18 chars. Good: the deck's real hashtag. Bad: invented campaign tag.
- `claim_line` — **≤15 words, ≤2 lines** (19px × 600px ≈ 90 chars/line). Good: a quantitative or directional claim. Bad: a topic label ("Ecosystem views") — that is what the kicker is for.
- `quote_text` — 25px × 300px ≈ 21 chars/line; keep ≤150 chars so it ends inside 6 lines. Good: first-person spoken language with the claim embedded. Bad: a paraphrase of the paragraph below it (then the page says the same thing twice).
- `attribution` — 1 line who + 1 line role/where-from, ≤45 chars each. Good: named role + date/context so the quote is falsifiable. Bad: "Industry expert".
- `evidence_1`, `evidence_2` — ≤3 lines each at 13px × 600px; 2 paragraphs total. Good: concrete named example + the "so what" with a number. Bad: 5-line paragraphs, or 3 paragraphs (the rail's vertical centre will drift).
- `figure_tag` — ≤2 lines. Good: `Figure N.` + the figure's scope. Bad: duplicating the source line.
- `source_line` — ≤2 lines including `n=`, fieldwork window, footnote marker.
- `running_head` — `PAGE | SECTION`.

FILL:
1. Replace `.kicker` (keep the `<br>`), `.hashtag`, `.claim`, `.quote` (keep the `&#8220;` span and the trailing `&nbsp;` to keep "paperwork" off a lone line), `.attribution`, `.evidence p` ×2, `.figure-tag`, `.source`, `.running`.
2. Nothing else is editable by design: the bars, the rule and the rail width are the layout.
3. Recolour for a different client: `--accent` (quote + bars), `--accent-deep` (quote mark), `--azure` (kicker + claim line + tick). Two brand colours is the maximum — if the client is monochrome, set `--azure: var(--accent)`.
4. Footnotes: each `<sup>` in the body needs a matching entry in the back-matter; keep them numbered 2/3/4 with `1` reserved for the source line.

CHART RECIPE: n/a — no figure on this page; the pull quote is the exhibit. If a small figure is added, it belongs in the rail under the attribution at ≤300px wide, with the violet accent and the rest of the series in the gray ramp.

VERIFY:
- [ ] claim line is ≤15 words and renders in ≤2 lines at 600px (gate).
- [ ] exactly one emphasis hue on the page (violet); azure appears only in kicker/claim/tick.
- [ ] quote fits 6 lines or fewer before the bottom bar; bars 56×4 unchanged.
- [ ] source line present bottom-left with n= and fieldwork window; footnote markers match.
- [ ] page number + section in the running head, right-aligned.
- [ ] text on violet appears only as violet-on-white (never white-on-violet here); contrast of `--gray-1` #7D7D7D on white is 4.4:1 — bump to #6E6E6E if the deck is projected.

DON'T (corpus failure modes):
- Do not let the quote become a topic restatement of the claim line; in the source deck the lead line and the quote are different voices.
- Do not run body text 3+ lines per paragraph — p28's own body runs long and the review calls the deck's text pages its weakest grammar; keep discipline tighter than the exemplar.
- Do not add a second accent (photo duotone, chart fill) beside the violet.
- Do not fill the kicker with a sentence; caps + 55 chars is the whole allowance.
- Do not put a wall of quotes here — that is `quote-pull-bubble-cluster`.

SOURCE: firm Accenture · deck `accenture__accenture_2019_accenture_global_financial_services_consumer_` · page 28 measured on contact sheet `sw_sheets/accenture__accenture_2019_accenture_global_financial_services_consumer__s02.jpg` (tile 8, printed footer 27) and re-cropped for palette: quote-violet glyph core #6917A4–#6F08AF, bar #5F0097–#720BB6, kicker azure #297FBF–#378ED5, body gray #BFBFBF edges; family anchors #6E00C9–#7B1FF0 / deep #3C0A80–#4B0E8F from `reviews/accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o.md` §palette. Layout/device claims (kicker + hashtag + "Figure N" + page|study footer, recurring p31/p35/p41/p48) from `reviews/accenture__accenture_2019_accenture_global_financial_services_consumer_.md` §Recurring devices / §Layout archetypes #9. Real font: Accenture's proprietary grotesque ("Accenture Sans" family, one-family weight-driven hierarchy per §Typography) → substituted by the Helvetica Neue / Arial stacks here.
