# stat-callout-list-kpmg-rail — Blue Claim Title + Stat-Callout Rail

WHEN: A page whose message is "we have N figures that prove one claim." One evidence-backed
claim at top, a supporting argument column, and a right rail where each item is a big figure
with a caption — the KPMG "blue title + stat callouts" pattern. Evidence:
`kpmg__kpmg_kpmg_our_impact_plan_2024_update_2024` p27 (wellbeing stats page, 5 numbers, blue
statement title over columns) and p32 (blue title + stat callouts). Sheet:
`sw_sheets/kpmg__kpmg_kpmg_our_impact_plan_2024_update_2024_s02.jpg` (p21–p30; p27 sits row 2, col 2).

ANATOMY: numbered slot map, px coords on the 1280×720 stage (1rem = 1 stage px):
1. `edgerail` — purple strip, x:0–6, y:0–720 (the deck's chip-rail motif, decorative).
2. `kicker` — chip label "01 People", x:56, y:44, purple fill, 12px caps w/ tracking.
3. `claim` (h1) — blue action title, x:56, y:88, 34px/1.14, max-width 1120px (2-line gate).
4. `rule` — hairline under title, y:170.
5. `lead` — bold one-sentence framing, x:56, y:206, 17.5px (left column width 604).
6. `points` — 3 checkmark bullets, x:56, y:~296+, 14.5px.
7. `method` — methodology aside w/ purple left border, x:56, bottom:96.
8. `rail` — stat-callout list, x:664→1224 (560 wide), y:206–654, purple-tinted fill.
9. `callout` ×3 — figure (52px blue, 26px purple unit) + label (13.5 bold) + note (12 gray),
   stacked with hairline dividers.
10. `source` / `pageno` — footer rule y:666, source bottom-left, "27 | PEOPLE" bottom-right.

SLOTS:
- `claim` — max ~15 words / 2 lines. Must be a judgment claim ("scaled activity, but impact
  tracking has not kept pace"), not a topic ("wellbeing statistics"). If it wraps to a 3rd line,
  cut words; never shrink the type.
- `lead` — one sentence, ≤ 30 words. States the so-what the figures prove.
- `points[i].text` — 25–45 words each, one embedded **bold figure** per bullet max; bullets carry
  the mechanism, the rail carries the numbers. Don't duplicate the rail's figures verbatim.
- `callout.fig` — the number itself, up to 6 glyphs + unit (`12,870 hrs`) + optional `†` footnote.
  52px is the ceiling: any longer (e.g. "€1.2bn+") and the `.unit` shrinks to 22px — test fill.
- `callout.lab` — one line (max ~55 chars), what the figure IS. Noun phrase, not a sentence.
- `callout.note` — ≤ 90 chars: why the number matters / its comparator. This is where "4.2× the
  FY21 total" lives; without a comparator the callout is decoration.
- `kicker` / `pageno` — section id, 1–3 words.

FILL: replace the four text blocks under `header/head`, the `.lead` p, three `<li>` texts, then
for each `.callout` swap `.fig` (keep the `<span class="unit">`/`sup` markup for unit/footnote
marks), `.lab`, `.note`. Recolor the rail via `--rail-bg`; swap `--accent` to the client's brand
blue for other firms (purple `--accent-2` drives chip + unit marks — recolor as a pair). To go
to 4 callouts, drop one `.note` (rail fits 4 @ ~140px each) or remove the `#people` chip rule;
to go to 5 callouts, use the `stat-callout-list-cards` sibling instead — the rail will not fit 5.

CHART RECIPE: none — figures are typographic. The one figure per callout rule holds; two numbers
in one `.fig` (e.g. "12,870 / 3,100") reads as a pair, put the comparison in `.note` instead.

VERIFY: claim ≤ 15 words AND ≤ 2 rendered lines; exactly one accent (blue) + one purple mark
color, grays for all secondary text; source line present bottom-left w/ footnote sup if the
method box exists; page number "NN | SECTION" bottom-right; rail text contrast: note #59595F on
#F4F1F8 ≈ 6.6:1 ✓; figs #00338D on rail ≈ 9:1 ✓.

DON'T: topic titles; stat walls with no caption/label (a number without its noun is unreadable);
figures duplicated between bullets and rail; 10+ callouts (this pattern caps at 4); kicker walls
of text; webfonts; more than 3 total hues (navy, purple, gray).

SOURCE: firm KPMG. Deck `kpmg__kpmg_kpmg_our_impact_plan_2024_update_2024` (2024 update of the
Our Impact Plan family). Pages p27 and p32 via
`sw_sheets/kpmg__kpmg_kpmg_our_impact_plan_2024_update_2024_s02.jpg` (p21–p30). Palette facts
(hexes #00338D blue, #6D207E/#8E298C purple, typography: single-family humanist sans, oversized
numerals on stat pages p25/p27) from
`reviews/kpmg__kpmg_kpmg_our_impact_plan_2024_update_2024.md` §4. Real house font is KPMG Sans
(Avenir-like); the Helvetica/Arial stack stands in.
