# matrix-2x2-panels — 2x2 Stakeholder / Theme Panel Grid (1280×720)

WHEN: Parallel-voice framework page — four stakeholder groups, four lenses on one question, four operating-model views. The boxes are peers; there is no measured axis between them. If the page has to *argue* that position is meaningful, use `matrix-2x2-scenario` instead. This pattern carries the most reused page family in the corpus (Deloitte ran it five times on one engagement: p26/31/36/41/50). Provenance: Deloitte *Accelerated Access Review — UK mapping* (2015) p26 + p31; grid discipline cross-checked against PwC boardroom p35.

ANATOMY (numbered slot map, 1280×720 stage px):
1. `kicker` — x64 y40, 12/14 uppercase letterspaced; `02 | Development: stakeholder views`.
2. `title` — x64 y64, width 1152, 31/42 bold, 2-line box (84 tall). Second line may run italic via `<em>`.
3. `deck-tag-line` — x64 y152, 12/15 gray-3: the fieldwork stamp (basis, counts).
4. `panels` — x64 y174, **1152 × 442**, grid `1fr 1fr` × `1fr 1fr`, `gap:18`. Each card is 567 × 212.
   4a. `card-N` ×4 — `border:1px var(--rule-strong)`, radius 6. `.lead` = 2px accent border; `.tint` = gray-4 wash.
   4b. inside each card: `c-chip` 19×19 numbered circle, `c-title` (uppercase 14/17), `c-count` right-aligned 10.5 (respondent count); then `c-icons` strip (3 glyphs, 26 tall); then `c-body` bullets 11.5/15 with bold lead-ins.
5. `so-what` — x64 y634, full-bleed strip, 3px accent left rule, accent-soft wash, 12/16 with `<sup>`.
6. `source` — x64 bottom 20, 10/13 gray-3, max-width 660, footnote marker; `deck-tag` centred; `page` bottom-right bold.

SLOTS (name — limit — what makes it good / bad):
- `kicker` / `title` — 46 / **≤15 words, 2 lines** — the title states what the four panels *disagree about or add up to*, not "Stakeholder views".
- `deck-tag-line` — 60-90 chars — basis + counts ("62 stakeholders across 4 groups"). A panel page without a basis line is unanchored opinion.
- `card-N-title` — 12-24 chars, uppercase — the voice/reader, e.g. "HMG / ALB views". Never a topic noun the reader could guess.
- `card-N-count` — ≤10 chars — n per group. This is the slot the corpus skips and the one that separates a research page from a poster.
- `card-N-chip` — 1 char — numbering is what lets the `so-what` and the body text refer to "panel 3". Keep them sequential in DOM order.
- `card-N-points` — 3-5 bullets, ≤20 words each — bold lead-in **inside** the sentence, not as a label. ≥1 bullet per card with a number or a named party; cards that say only "there are challenges" waste the slot.
- `so-what` — 160-230 chars — one move/implication, referencing the panels ("panel 2 and 3 collide on…"). This device is ours, not the source page's — the source pages ship without it and the corpus reads as four feature dumps.
- `source` / `deck-tag` / `page` — always present.

FILL (build order, plus resizing — this page exists to be resized):
1. Write the four card titles + counts first; then bullets. The four titles must be the *same kind of noun* (all stakeholder groups / all four lenses), or the grid stops being a grid.
2. Lead card: add class `lead` to the card that carries the conclusion (1 card). Others stay gray-bordered. Never border two cards in accent — the page then has no focus.
3. Icons: 3 glyphs per card from one stroke weight (1.4). Edit the `<svg>` paths, keep viewBox `0 0 24 24` and the 24×24 box; a card's icon strip is "who is talking", not decoration per bullet.
4. Bullet text: replace `<li>` content only; the square marker and the indent are CSS. Bold the operative phrase in each bullet, nothing else.
5. **Add a 5th or 6th panel (3 across × 2 rows):** copy a `.card` block, set `style="grid-column:3;grid-row:1"` (then `:3;:2`), and change `.panels` to `grid-template-columns:1fr 1fr 1fr`. Card size 567×212 → **372×212**; 5 cards leave one empty cell — keep that node with class `dim` and a title like `Not interviewed`, do not leave a hole (a blank grid cell reads as a rendering bug).
6. **Add a 3rd row of panels:** copy cards with `grid-row:3`, set `grid-template-rows:1fr 1fr 1fr`; card height 212 → **135** (`(442 − 2×gaps)/3`). At 135: keep the icons strip, cap bullets at 2 (or drop the strip and cap at 3). If you need 9 panels, that is 135×372 and this template is the wrong tool — split the page.
7. **Fewer than 4 panels (3):** `grid-template-columns:1fr 1fr 1fr; grid-template-rows:1fr`, and set `--p-h:212rem` so the row keeps its card proportions instead of stretching to 442. Then move `.so-what` up: its `top` = `--p-top` + `--p-h` + 18 (174 + 442 + 18 = 634 today, 404 in that case), and the `.foot` rule and page number stay put.
8. **Remove a panel:** delete the `.card` node **and** renumber the surviving `grid-column` / `grid-row` values plus the `c-chip` numbers. Left-over numbering ("1, 2, 4") is the visible symptom of skipping this.
9. Reflow is free otherwise: cards are `1fr` inside a fixed container, so nothing has coordinates to recompute; the only numbers that change are bullet counts (per the size table above).
10. Accent change: recolor `--accent` (and `--accent-soft`, which must stay ≥12:1 against the ink text it carries — accent-soft is a wash, never a text ground). Do not recolor per card (see DON'T).

CHART RECIPE (how this figure encodes):
- No scale, no geometry — the page encodes by *position and count*. Equal cards = equal weight; that is the whole argument. If one panel should matter more, give it the `lead` border, not a bigger box (bigger box = a claim about quantity this page cannot support).
- One accent (the lead card's border/chip/markers/so-what rule) + gray ramp everywhere else; ≤2 hues in the frame.
- Direct labels: respondent counts inside the card, bolded operative phrases inside bullets. No legends, no keys, no connector arrows — arrows would imply sequence and these boxes are simultaneous.
- Contrast floor: bullets `--gray-2` 11.5px on white (8.6:1); white 11px on the accent chip (5.7:1); `--gray-3` only for 14px-bold labels and the 10px source line.

VERIFY (run against the render):
- [ ] Title ≤15 words / 2 lines; card titles all the same grammatical type.
- [ ] Every card shows a count (or an explicit `Not interviewed`), ≥1 numeric/named claim.
- [ ] One accent color; one `lead` card; no card larger than another.
- [ ] `so-what` present, ≤230 chars, and it names which panels drive the move.
- [ ] Source line with basis + footnote marker; page number bottom-right.
- [ ] Text contrast: body 11.5px gray-2 (8.6:1), chip label white-on-accent (5.7:1), nothing at 10px bold gray-3 or below.
- [ ] Resize proof: 5 cards per FILL 5 reflow to 372×212 with only `grid-column` values edited.

DON'T (failure modes seen in the corpus):
- Four hues for four cards (the Deloitte source page literally does this: navy/chartreuse/teal/green borders) — the kit rule is one accent + gray; per-card color is the corpus's loudest flaw.
- Speech-pointer/arrow devices between the boxes (PwC p35) when nothing flows; the review there calls it "arrows imply interaction but no diagram semantics".
- A card title as a topic ("Regulation") while the bullets repeat the title.
- Bold-everything bullets, or a bold label before every bullet ("Key point:").
- Kicker walls / a 25-word lead-in above the grid; the grid is the exhibit.
- Gray-on-gray: 10px `--gray-3` body text (the Accenture IAC message-grid page cited in DESIGN_PLAYBOOK as the low-contrast flaw).
- Equal-weight boxes with no `so-what` — the page then reports four opinions instead of one finding.
- Lorem, `Text`, `XXX`, or `Your logo here` residue: this family is where placeholder-driven SmartArt decks show.

SOURCE: extracted from `sw_pages/deloitte__deloitte_accelerated_access_review_uk_mapping_2015/pg-026.png` (sheet `deloitte__deloitte_accelerated_access_review_uk_mapping_2015_s02.jpg`, floor(26/10)=2, row-major 5 col × 2 row) — read as a full page: 4 bordered rounded cards in 2×2, centered uppercase heading over a hairline, row of 5 line icons, 3-5 bullets with in-sentence bold lead-ins, footer `26 | Source: Stakeholder interviews, workshops and Deloitte analysis | © 2015 Deloitte MCS Limited`. Same page recurs at p31/p36/p41/p50 of that deck, which is why the page is a template and not one slide. Second reference: `sw_pages/pwc_strategy__pwc_boardroom_agenda_2022/pg-35.png` (2×2 quad, four hues + white speech pointers — kept as the negative example). Catalog rows: `reviews/deloitte__deloitte_accelerated_access_review_uk_mapping_2015_slides.csv` (archetype "2x2 stakeholder-view panel", charts "none") and `reviews/pwc_strategy__pwc_boardroom_agenda_2022_slides.csv` p35 ("2x2 icon quad", "quad with arrow pointers", "real content not lorem / arrows imply interaction but no diagram semantics"). House tokens and the one-accent rule: `DESIGN_PLAYBOOK.md` §palette ruling; the four-hue caution also appears in `reviews/umbrex_patterns.md` (off-palette ribbon slides flagged).
