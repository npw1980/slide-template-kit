# donut-claim-center — Multi-segment allocation donut with the argument sentence in the hole, radial labels + spend-vs-reach bridge rail

WHEN: "The composition of X argues Y." A single donut of ≤5 segments — spend,
budget, portfolio, response mix — whose HOLE carries a claim sentence (not a
bare %), paired with an interpretation rail (allocation vs. effectiveness) that
turns the composition into a decision. This is the Accenture nbn deck's donut
device: "center holds the sentence, donut is argumentative not decorative"
(p16/p21/p29 per its review), with radial segment labels as evidenced on the
moneyball deck p24. Use when one segment (or one pair) is the protagonist; for
a plain two-value contrast use `donut-pair-contrast`.

ANATOMY (1280×720 stage, rem == stage px):
1. `kicker chip` — white-on-violet pill, left 64, top 44, h 30, 11px +11% caps.
2. `claim title` — sentence-case h1, left 64, top 96, width 1050, 26/33px bold.
3. `donut` — centre (418, 398), outer r 176, ring 64 → circle r 144, C 904.779.
4. `in-ring % labels` — 12.5–13px bold at each segment's mid-angle (r 144),
   white on dark segments, ink on light ones.
5. `centre claim` — x 418: overline "THE GAP" y 366 (10px +16% tracking, gray),
   claim sentence 15px bold y 390/408/426 (max 3 lines inside r 112).
6. `radial labels` — leader per segment: exit r 182 → elbow r 205 → 28px stub;
   bold NAME + small gray "reach NN%" beside the stub end (coords in comments).
7. `rail` — right, 792–1216: header y ~196; 5 rows, baseline y = 232 + i·54;
   name 792 (13px bold), spend bar lavender + reach bar violet (x 966, 175px
   = 100%), values inline after bar ends, delta chip `+10 pt` pill x 1160–1212.
8. `implication band` — 792–1178, top ~486, violet 3px left rule, wash fill
   `--wash`, "IMPLICATION" header + 2-line takeaway.
9. `footer` — hairline top 674: violet chevron, source left, note, `N | SECTION` right.

SLOTS:
- `claim_title`: ≤15 words / 2 lines, quantitative; the accent span marks the
  operative quantity ("just a third"). Bad: "Media allocation study".
- `chip`: ≤34 chars, deck-section label — wayfinding, not a claim.
- `centre_claim`: the argument sentence, ≤7 words per line × 3 lines.
  Overline ≤9 chars. If it collapses to a bare %, you have a pie, not this page.
- `segments`: 3–5, values sum to 100. One protagonist (accent) — the rest go
  violet-light → lavender → grey. Six+ = segment soup (corpus failure mode).
- `radial_name`: ≤16 chars caps. `radial_sub`: "reach NN%" ≤11 chars.
- `rail_rows`: name ≤17 chars; values whole %; delta chip "±NN pt" — the sign
  does the arguing. Implication: one actionable sentence with a number + unit.
- `source` / `note` / `page`: real panel with n and dates (nbn footer contract).

FILL:
1. Text nodes: chip, title span, centre overline/sentence, rail names+bars+chips,
   implication sentence, footer source/note/page.
2. The donut: edit the `SEGMENTS` array values (sum 100!). Each segment circle:
   `dasharray = len C`, `dashoffset = −cum_before`; len = value × 9.04779
   (904.779/100). Recompute offsets as running sums. Segment 1 must keep the
   accent fill — it's the protagonist, not the largest by accident.
3. In-ring % texts + radial labels sit on mid-angle r·sin/cos of
   360°×(start+value/2)/100 from 12 o'clock; if segment sizes change, move the
   5 label pairs and leader polylines together, or the leaders mis-point.
   (With wildly new values, recompute with the formula in the header comment.)
4. Right rail: bar widths = value × 1.75; delta chip = reach − spend (points,
   sums to zero across rows — if not, your reach column isn't normalised).
   Bars >75px wide can carry their value inside instead of after.
5. Recolour: swap `--accent`; the ramp tokens (--accent-2/-3, --lav-1/2) are
   lightness steps — keep ONE hue + grey. Grey `--gray-2` is reserved for the
   residual "other" series ("grey is the alternative", nbn rule).

CHART RECIPE:
- **What the ring encodes**: composition of one quantity, share of 100, drawn
  clockwise from 12 in array order. It is 100%-normalised by construction —
  never let segment values not sum to 100; the residual is a named segment.
- **Scales**: area-of-ring linear in value (angle = value × 3.6°); no 3D, no
  exploded slices, no radius encoding. Ring thickness uniform 64px: donut,
  not pie — the hole is load-bearing (it holds the claim).
- **Value-label placement**: % inside the ring at each segment's mid-angle
  (white on the two darkest segments, ink on the lighter three — check 4.5:1
  or drop to the ink colour). Names OUTSIDE on leaders; names never inside
  (<12% segments can't hold text). "reach NN%" on the label re-links the ring
  to the rail — keep it, it is the page's connective tissue.
- **Emphasis, one accent + grey**: one segment in `--accent`, the rest descend
  in same-hue lightness to lavender, then one grey for "other". Two max
  semantics: violet shades = the named channels, grey = residual.
- **Axis/unit rules**: the donut needs NO axis (100% ring). Rail bars carry
  the only scale (175px = 100%, zero baseline). Units stated once in the note
  (allocation = % spend, reach = % weekly reach). Delta chips in POINTS.
- **Centre text**: sentence, not number. If your argument is numeric, the
  number goes in the rail or title — centre text must survive if the ring were
  hidden (that's what "argumentative not decorative" means).

VERIFY:
- [ ] Segment values sum to exactly 100; dash lengths = value × 9.04779.
- [ ] Centre reads as a sentence; overline ≤9 chars; 3 lines max inside hole.
- [ ] One accent + lightness ramp + grey residual; zero other hues.
- [ ] White text only on #7500C0 / #8E24EA segments; ink on the light three.
- [ ] Rail deltas sum to 0 pt; each bar pair's values match the ring's.
- [ ] Title ≤15 words / 2 lines; source with n + dates; page running head.
- [ ] No legend box: colour↔name mapping lives on the labels themselves.

DON'T:
- Bare "%" in the hole (that's `donut-pair-contrast`'s job — and even there
  it's a gauge, not a composition).
- 10+ segment donuts / 10-hue pies — moneyball p24 "segment soup" flagged.
- SmartArt ring presets, radial hubs, Deloitte-style 12-node rings (the
  playbook's only donut-family SMARTART flags) — this is hand-built SVG.
- Two donuts for "vs." comparisons (use donut-pair-contrast), pie chart,
  donut with leader lines to a side legend column (legend = chart junk here).
- Claim sentence longer than ~21 words or split across title+centre (the
  review's double-punchline failure).

SOURCE: accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o
p16 (`sw_pages/…/pg-16.png`, sheet `sw_sheets/…_s01.jpg`), donut device list
p16/p21/p29 + footer contract from
`reviews/accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o.md`;
radial-label pattern per moneyball p24, flagged "segment soup" so capped at 5
segments. Palette: band violet sampled #7500C0; ramp tokens #8E24EA / #A45CF0 /
#D9C6F4 / #E7D9F8 and grey #B8B8B8 cited from the review's lightness-token
palette. Fonts: Helvetica Neue stack standing in for the firm's grotesque.
