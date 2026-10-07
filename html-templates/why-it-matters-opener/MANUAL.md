# why-it-matters-opener — Giant Gradient "Why Does It Matter?" + Photo + Numbered Blocks

WHEN: An argument-setting page that admits the topic is a question and answers it by force of
typography. Use when you need the audience to re-decide whether a trend deserves attention before
you hand them the recommendations. Two observed shapes in the same deck: this one (photo + lead +
numbered blocks) is the page that *opens* a section. Evidence: "be TMT Predictions 2025"
(Deloitte Belgium, deck slug `content_dam_assets_zone2_be_e`), p8 (S0056,
corpus/sheets/sheet_006.jpg row 2 col 1) and the same device on p17/p20/p23
(sheet_007.jpg S0065 row 1 col 5, S0068 row 2 col 3). No review file exists for this deck.

Firm font note: the source sets titles in the Deloitte house sans (2023 identity "STardom" family).
The template stands in `"Helvetica Neue", Arial` at weight 800, tight tracking — same heavy grotesque
read. Do not substitute a serif or a rounded face.

ANATOMY: numbered slot map, px coords on the 1280×720 stage (1rem = 1 stage px):
1. `kicker` — section label, x:64, y:52, w:640, 11.5px caps, 1.8px tracking, gray-2.
2. `why` — the fixed interrogative device, x:64, y:78, w:600, h:190. 82px, weight 800,
   tracking −7.5px, uppercase, exactly 2 lines ("Why does" / "it matter?"). Gradient fill is
   `linear-gradient(90deg, grad-a, #A76FC4 52%, grad-b)` clipped to text — that 90° sweep is the
   device; it is NOT a per-slide colour to keep swapping.
3. `photo` — x:64, y:300, w:560, h:344 (16:10). Duotone teal: deep `--duo-lo #16323B` shadows,
   `--duo-hi #36E0DF` highlights, midtones pulled to blue-green.
4. `lead` — the claim sentence, x:680, y:96, w:536, 19.5px bold, ink. Sits opposite the title.
5. `sub` — support paragraph, x:680, y:204, w:536, 13.5px, gray-1, max ~3 lines.
6. `blocks` ×4 — numbered reasons, x:680, y:296, w:536, stacked; each 28px rounded gradient
   square (grad-a → block-purple `#B94B9F`) + 13px bold lead-in + 12.5px body, ~74px tall.
7. `foot` — rule at y:680; source line x:64 9.5px with superscript footnote marker; page number
   right x:64 margin ("NN | SECTION", section word in gray, number in grad-a).

SLOTS:
- `kicker` — max ~60 chars. Good: "2025 Global TMT Predictions · GenAI adoption". Bad: a
  paragraph-sized mission statement (the kicker is a locator, not a thesis).
- `why` — FIXED copy "Why does it matter?". The only editable variant is the trailing punctuation
  question. It is a device, not a headline: never replace it with a real title here — the real
  argument lives in `lead`.
- `lead` — max ~150 chars / 3 lines, ≤15 words. It must be a claim ("gen AI has compounded
  existing grid constraints"), not a topic ("electricity and AI"). This is the slot the MBB title
  gate actually applies to.
- `sub` — max ~270 chars / 3 lines. Support, not a second headline; 1–2 sentences.
- `blocks[].h` — max ~28 chars. Bold lead-in naming the lever ("Sourcing:", "Cooling and
  efficiency:"). Good = a lever a reader could act on. Bad = "Background"/"Context".
- `blocks[].t` — max ~150 chars / 2.5 lines, quantitative where possible (years, PUE, %, n=).
- `source` — max ~180 chars / 2 lines: report/edition, vintage, survey n where the deck cites
  survey data; footnote marker `sup` where methodology claims exist.
- `pageno` — page number + section name in caps.

FILL: (1) replace `lead` and `sub` text — this is 80% of the work; the page is a title device with
a right-hand argument column. (2) Replace the photo SVG: delete the two `<rect>` groups and the
`<defs>` gradient, put `<img src="photo.jpg">` (or a CSS background-image) inside `.photo`, then
enforce duotone with a grayscale filter plus the `--duo-*` colours as overlay/blend; never ship the
teal placeholder rects as-is. (3) Edit each `.blk` `.n` (number), `.h` (lead-in), `.t` (body).
(4) Footer: edit `.source` (keep the `<sup>1</sup>` if any methodology claim is on the page) and
`.pageno`. (5) Recolor: only `--grad-a`, `--grad-b` and `--block` move for a different client —
keep them one hue apart (warm→cool) or the gradient device dies; `--ink/--gray-*` stay.

CHART RECIPE: none — this template is text/typography only. If an exhibit is needed, put it in the
photo slot as a duotone data-visual, not a chart pasted beside the title.

VERIFY: `lead` ≤15 words / ≤2–3 lines at 19.5px/536px (measure, don't eyeball); `sub` ends above
y:296 (blocks' top); photo region is duotone not full-colour; page carries exactly one colour
device (the gradient) + black/gray ink; contrast: `lead` black-on-paper ≥ 12:1, block body gray-1
on `--bg` ≥ 4.5:1; gradient title keeps legibility (the 82px weight-800 fill must not read pink on
one end and cyan on the other with a muddy middle — check the 52% stop); source line present with
footnote mark; page number present; no webfonts, no network calls.

DON'T (corpus failure modes): kicker walls of text; `lead` degraded into a topic label
("Adoption trends") — the gradient title already says the page is asking, the claim is your job;
four numbered blocks that are four restated opinions with no numbers (the deck always pairs each
number with a stat or an actionable verb); full-colour photos that break the duotone system;
stacking the title into 3 lines by shrinking the column (the gate is 2 lines); 10-hue accents
painted onto the squares.

SOURCE: firm Deloitte (Belgium). Deck `content_dam_assets_zone2_be_e` ("be TMT Predictions 2025",
tmt/2025). Pages 8, 17, 20, 23 of the PDF — pages S0056 (sheet_006.jpg, row 2 col 1), S0065
(sheet_007.jpg, row 1 col 5), S0068 (sheet_007.jpg, row 2 col 3), S0071 (sheet_008.jpg). Catalog
archetype labels "why-it-matters opener / numbered" (`catalog_1-20.csv`, device note "gradient
interrogative title"). Palette pixel-sampled from `corpus/pdfpages/_content_dam_assets_zone2_be_e_-08.png`
and `_-13.png` (teal #36e0df, magenta #d5379a/#b94b9f, paper #f2f2f2); no `reviews/` file existed
for this deck, so palette claims come from the pixels, not from prose.
