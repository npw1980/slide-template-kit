# case-study-example-grid — Named Example-Card Grid

WHEN: a page that proves a claim by pointing at 2–6 *named real-world examples* laid out as a
card grid, where the card name itself carries the credibility. Two sources observed: the Accenture
net-zero report p26 "Examples of leading company decarbonization initiatives" (3×2 grid of company
cards, violet name + underline rule over dense prose) and the same family in KPMG Our Impact Plan
2022 p19 (two side-by-side "Case study" panels — the pattern scales down to 2×1). Palette facts:
single-hue purple ramp + neutral gray/white; deep violet fills, mid-purple kickers, light-purple
tint, black/gray/white neutrals.

ANATOMY: slot map with px coords on the 1280×720 stage (1rem = 1 stage px):
1. `eyebrow` — kicker, x:56 y:44, 12.5px caps, letter-spacing .15em, violet.
2. `claim` (h1) — action title, x:56 y:76, 30px bold, max-width 1120 (2-line gate).
3. `lede` — bridge sentence, x:56 y:~128, 13.5px gray-1, carries the "what links the examples".
4. `grid` — x:56→1224, y:236; CSS grid 3 cols × 2 rows, row-gap 26, column hairline rules.
5. `card[i].name` — company name, 15px bold violet with 2px violet underline, per card.
6. `card[i].body` — the example itself, 10.5px/1.47 gray-1, with violet bold emphases.
7. `source` — bottom-left, 8.5px gray-2, with superscript footnote marker.
8. `run` — "36 | CASE STUDIES" running head, bottom-right.

SLOTS:
- `claim` — 13–15 words, ≤ 2 lines. Must be a conclusion the examples support ("Companies that
  embed decarbonisation in core decisions, not just targets, cut emissions fastest"), not the
  topic "Examples of…". The corpus title ("Examples of leading company…") is the classic
  topic-title failure the spec's MBB gate forbids — the deck's real claim lives in its dividers.
- `lede` — ≤ ~150 chars, the connective tissue between claim and grid. It names the *common trait*,
  not the grid contents ("across the 109-company sample…").
- `card[i].name` — proper noun only. Max ~28 chars (long "Mahindra & Mahindra" fits at 15px with
  `max-width:max-content`). If names must be longer, drop to 13px and let the underline shrink.
- `card[i].body` — 3–5 lines (≤ ~230 chars). Good is *quantified past action* ("50% absolute cut
  by 2030, validated by SBTi, 76% renewable") with exactly one violet `b` emphasis and numerals
  set in bold `--ink`; bad is a second description of the problem, or a wall with no number.
- `source` — the analysis + registry/disclosure basis; superscript marker ties to a footnote line.
- `run` — page number + section name, deck running-head style.

FILL: replace `.eyebrow`, h1 text, `.lede` text. Then per card: `.name` text, `.body` text keeping
the `<b>` (violet emphasis) and `<span class="num">` (bold figure) wrappers — remove `.num` spans
where the sentence has no figure. Grid scales: 2 wide × 1 tall (KPMG variant) → set
`grid-template-columns:1fr 1fr; grid-auto-rows:auto` and give cards `padding:0 34rem`; 6-up is the
default written. For 4 cards use 2×2 with `grid-auto-rows:1fr 1fr`. For a client with no purple,
recolor `--accent` to the brand hue and keep one hue only — the deck is single-hue by design.
Footnote: `<span class="sup">a</span>` appears in both `.lede` and the source line (the
superscript-marker convention).

CHART RECIPE: none — typographic cards. Emphasis discipline per playbook: one accent (violet, the
name kickers + one bold phrase per card) + gray ramp for "the rest"; figures bold-black, never
colored. Never let a card carry more than one hue.

VERIFY: claim ≤ 15 words / 2 lines; source line present; exactly one emphasis hue (violet) plus
grays; contrast — `--accent-deep` #660099 on white = 12.6:1 ✓, `--accent` #A100FF on white as
large 15px bold name = 3.9:1 (passes AA large text; if used below 14px set it in `--accent-deep`);
body #4D4D4D on white = 7.8:1 ✓; running head present; no card exceeds 5 text lines.

DON'T: topic titles ("Examples of…") where the claim belongs; violet bold every number (the deck
bolds *one* phrase per card, numerals stay ink-black); kicker walls — a 4-line kicker above a
6-card grid reads as double title; equal-length cards that force the whole grid to the tallest
one's line count; photo per card (photo persona pages are the `persona-cards` pattern, not this).

SOURCE: extracted from `accenture__accenture_accelerating_global_companies_toward_net_zero_by_2`
p26 — read on `sw_sheets/accenture__accenture_accelerating_global_companies_toward_net_zero_by_2_s02.jpg`
(sheet s02, row 2 frame 1); count-variant evidence `kpmg__kpmg_kpmg_our_impact_plan_2022_update_2022`
p19 (`sw_sheets/kpmg__kpmg_kpmg_our_impact_plan_2022_update_2022_s01.jpg`, row 2 frame 5). Palette:
`reviews/accenture__accenture_accelerating_global_companies_toward_net_zero_by_2.md`
§Color system.
