# donut-pair-contrast — Dual donut "market disconnect" (one accent arc per ring, centre gap numeral + arrows)

WHEN: Two one-number measures of the SAME metric compared across two populations,
periods, or "what's happening vs. what should happen" (current vs. optimal, two
markets, audience vs. budget). It is the Accenture moneyball deck's signature
device (p23 "20% vs 8% = 12% Market Disconnect", variant p10). Do NOT use this
for composition-of-total charts — that is `stacked-share-100col` or the 100%
stack family; here the rings are gauges, not pies.

ANATOMY (1280×720 stage, rem == stage px):
1. `kicker/claim title` — h1, left 64, top 52, width 1152, 31/38px all-caps bold.
2. `subline` — red all-caps chart description, left 64, top 156, 15px +7% tracking.
3. `left ring` — track+arc circle centre (340, 388), outer r 132, stroke 34 (circle r 115).
4. `left value` — giant centre numeral, (340, 410) baseline, 64px bold + footnote sup.
5. `right ring` — identical geometry, centre (946, 388).
6. `right value` — centre numeral (946, 410).
7. `gap block` — centred x 643: numeral y 348 (58px), two-line label y 380/396, arrows at y 430 pointing outward (left arrow spans 576–616, right 670–710).
8. `captions` — two-line bold labels under rings, boxes left 200 / left 808, top 560, 280 wide, 16px.
9. `baseline` — hairline (180→1100, y 536) tying ring bases together.
10. `footer` — hairline top 676: source left, note mid, `1 | SECTION` running head right.

SLOTS:
- `claim_title`: ≤15 words / 2 lines, QUANTITATIVE claim with the numbers shown
  in the figure. Good: "Viewership has grown at a 20% CAGR, while ad spend has
  grown at only 8%". Bad: "Market disconnect analysis" (topic — fails the MBB gate).
  Exactly ONE clause is red; more than one kills the emphasis mechanic.
- `subline`: one line, all-caps, ≤110 chars: what is being compared, for which
  scope and period. Add sup footnote here if the measure needs defining.
- `left_value` / `right_value`: max 4 chars ("20%"/"8%") — they're 64px; a
  three-digit number still fits, "$1.4B" needs the font dropped to ~52px.
- `gap_numeral` / `gap_label`: numeral = difference of the two shares (12 points,
  NOT 12 percent — say "points"/"pt" if space allows in the label); label = two
  words max, all-caps ("MARKET / DISCONNECT").
- `captions`: ≤22 chars per line, 2 lines: measure name + period/scope.
- `source_line`: real sources, comma-separated; `note`: one definition line
  ("CAGR = compound annual growth rate"); `page`: `N | SECTION` running head.

FILL (all edits inside index.html, clearly marked DATA comments):
1. Replace title clause, subline, captions text nodes.
2. `LEFT_SHARE`/`RIGHT_SHARE`: set the two dash lengths —
   arc length = share/100 × 722.566 (722.566 = 2π·115; r 115 is fixed).
   Left donut: dasharray "144.51 722.57" → "X 722.57" with X = 7.2257 × share.
   Right donut: same rule (8% → 57.81). Keep the second number 722.57.
3. Centre numerals: two `<text>` nodes per donut + the 16px sup marker; if you
   drop the footnote, delete the matching sup text too.
4. Gap: numeral `12%` = LEFT − RIGHT (recompute by hand — it is the difference,
   shown as points). Arrows need no edit unless labels get longer: widen the two
   rects symmetrically around x 616/670.
5. Recolour for another firm: change `--accent` (one variable). Leave the grey
   ring `--gray-2 #BFBFBF` — the grey ring IS the message ("the rest").
   Keep title/numerals `--ink`; if the brand accent is light (yellow/cyan), swap
   numerals/arrows stays ink — never set numerals on accent on this page.

CHART RECIPE (the rulebook for anyone swapping numbers into this SVG):
- **What the ring encodes**: each ring = ONE value, read as the red arc's share
  of the full circle. The circle is 100% of "the measure's scale" (a growth
  rate is shown as its share of a notional 100 — it's a gauge, not a composition).
  Both rings MUST be the same size, or the visual comparison is a lie.
- **Scale rules**: zero-based by construction; arc length is linear in the
  value (no sqrt, no log). Arc starts at 12 o'clock, runs clockwise. Values
  above 100 (e.g. 140% index) do not fit the ring — move those to a bar.
- **Value labels**: on the element itself — giant numeral in the hole (64px
  bold), NOT on the arc, NOT in a legend. Two rings → exactly two numerals +
  one gap numeral. No legends, no callout boxes elsewhere.
- **Emphasis (one accent + grey)**: accent red only on the two arcs and the
  title's claim clause. Everything else: ink (numerals, captions, arrows) and
  one grey (#BFBFBF) for the ring track. If the two rings deserve equal
  emphasis, still give both arcs the same accent — the argument lives in the
  GAP block, which is black (comparison), never a second hue.
- **Gap block**: numeral = LEFT − RIGHT expressed in POINTS for % data
  ("12 pts" beats "12%" for a difference of shares; state the unit in the note
  line when ambiguous). Arrows point OUTWARD toward each ring (the gap belongs
  to both), 6px shaft + triangle head, black.
- **Axis/unit rules**: units live once — subline (period, scope) + note
  (definition). Never label arcs with "CAGR" twice; captions carry the measure.
- **Precision**: one decimal max; round the gap from the unrounded values, not
  from the displayed ones.

VERIFY (before delivery):
- [ ] Title ≤15 words, ≤2 lines at 31/38px (the placeholder fills 2 lines by design).
- [ ] Both ring arcs start 12 o'clock, share/100 × 722.566 dash, correct clockwise.
- [ ] Gap numeral equals LEFT − RIGHT (points, unit stated once in note).
- [ ] Exactly one hue (accent) + grey; numerals/arrows are ink.
- [ ] Source line present bottom-left; running head `N | SECTION` bottom-right.
- [ ] Superscript footnote markers only where a definition/method claim exists.
- [ ] Render: both rings read as identical gauges; no legend box anywhere.

DON'T (corpus failure modes):
- 10+ hue rings or adding a legend (moneyball p24 "segment soup" — the review
  says ignore). This page is exactly two numbers + their gap.
- Topic titles ("comparison of CAGR trends") — the title IS the finding.
- Different ring sizes, inner "3D" donuts, gradient arcs, or a second accent
  colour for the second ring (breaks the red=highlight semantics).
- Double-punchline kicker: the subline describes, it does not argue (the red
  "YET…" line on p8 is flagged in the review).
- Gap expressed as a % of a % ("12%") without stating "points" in the note.

SOURCE: accenture__accenture_the_moneyball_moment_for_marketing_in_canada_2019,
p23 (`sw_pages/…/pg-23.png`, also sheet `sw_sheets/…_s02.jpg`; variant p10).
Analyzed in `reviews/accenture__accenture_the_moneyball_moment_for_marketing_in_canada_2019.md`
(signature device + colour-semantics + "ignore" list for p24 pie soup).
Fonts: the source renders Arial Black; per the review ("low craft ceiling —
substitute a proper grotesque") this template uses the Helvetica Neue stack.
Palette: arc red #DC0017 + title red #FF0000 sampled from the source page,
grey #BFBFBF sampled from the ring track.
