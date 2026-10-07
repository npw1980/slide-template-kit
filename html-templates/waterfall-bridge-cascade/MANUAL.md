# waterfall-bridge-cascade — 100% Failure-Mode Cascade (step-down waterfall)

WHEN: One page that decomposes a fixed whole ("the 100% of value forgone / spend lost / failures observed") into named buckets that cascade down-and-to-the-right into a closing 100% bar. Built from corpus sheet **S114** (`corpus/sheets/sheet_012.jpg`, row 1 col 4 — the "failure-mode waterfall" page: relative share of primary failure modes, pink bars stepping toward a full-width total). Use it when the argument is "this is all one pie and here's where it goes wrong", NOT for a start→end value bridge with signed deltas (that is `waterfall-bridge-deltas`).

ANATOMY (px on the 1280×720 stage):
1. Claim title — left 64, top 34, width 1152, two lines of 29px/37px, the finding in a `.em` accent span.
2. Kicker — left 64, top 116, 14px all-caps with footnote mark: what is being decomposed + the unit ("% of total").
3. Chart SVG — full stage. Plot band x 460→1160 (1% = 7px), zero rail at x=460. Row centres y = 214 + i×48 for i=0..6; total-row centre 550. Bar height 30.
4. Left label column — right-anchored x=440, series-coloured.
5. Legend — three chips at y=150 (accent series / grey series / total).
6. Method note — left 64, bottom 34, one honesty line.
7. Footer — source bottom-left, `N | SECTION` bottom-right.

SLOTS:
- title — ≤15 words / 2 lines. GOOD: names the decomposition + the dominant bucket as a claim ("Value leaks, not execution, account for 84% of forgone value"). BAD: "Failure modes" (topic). The share cited must be reconstructable from the bars (the sum of the named rows it refers to).
- kicker — the universe being made 100% ("of total forgone value"), ≤12 words + footnote mark. This chart is a SHARE chart; the denominator belongs in the kicker, not the fine print.
- rows — 6–8 bars: value = share of total (must sum to 100 ±1), kind = "accent" or "gray". GOOD: MECE buckets, largest-first ordering so the cascade descends left-to-right. BAD: overlapping categories (a failure coded into two buckets inflates the bar), an "Other" > 15%.
- value labels — signed-free percentages, one decimal only if the whole axis uses one decimal. Inside the bar (white bold) when bar width ≥ 46px; OUTSIDE, dark ink, just right of the bar end when narrower (see "Channel conflict 6%" — every reader must still see it).
- note — one line stating how rows were coded (single-largest-mode coding is the standard here) and that shares don't net against realised outcomes.
- source — study, N, period, metric definition ("EBITDA gap vs synergy plan¹").

FILL (step by step):
1. Edit the DATA ARRAY comment: `{label, value, kind}` rows; confirm `Σvalues = 100`. Reorder largest→smallest (the cascade shape depends on it).
2. Recompute cumulative starts and rewrite each `<g class="row">`: `rect x = 460 + (cumulative-before × 7)`, `width = value × 7`. Row geometry (pitch 48, height 30, x-band 460–1160) NEVER changes — only x/width and the two text nodes per row.
3. Value label: if `width ≥ 46` keep centred white inside (`x = rect.x + width/2`); else move outside: `x = rect.x + width + 8`, `text-anchor="start"`, fill ink.
4. Dashed connector: the `line` at each row's right-edge x, from bar bottom to next row's bar top — its x always equals that row's bar-end x; update when you move bars.
5. Grey rows: exactly one `kind:"gray"` (the residual/bucket that is not the claim). Its label is ink, not accent; its connector is grey.
6. Total row: always full-width 700px, dark fill, single centred "100%". Never shrink it.
7. Recolour: set `--accent` to the brand hue; `--gray-bar`/`--total` stay as-is. White 12.5px-700 text on the accent must clear 4.5:1 (it does at the stock magenta #E61A57 — a pale brand hue means you switch inside labels to dark ink).

CHART RECIPE (the encoding, for swapping numbers into the SVG):
- **Scale**: linear share scale, zero-based, x = 460 + pct×7 px; no axis labels — the % rail is implied by the zero line at x=460 and the "100%" inside the total bar. Unit goes in the kicker once ("% OF TOTAL FORGONE VALUE"); the total bar states 100% explicitly.
- **Cascade placement**: each bar starts exactly where the running cumulative ends — bar k's left edge = bar k−1's right edge's x, one row lower. The eye reads "we're adding up to 100" from the stair, so ordering (largest first) IS part of the encoding.
- **Value labels**: on/inside bars (this kit always labels the bars themselves, not the axis); white 700 inside when width ≥ 46px, outside-ink when narrower; the number is the bar's only label — category names live in the left column so they don't rotate or stack on tiny bars.
- **Emphasis — one accent + grey ramp**: accent = the claim series; ONE grey bar = everything that isn't the claim; dark grey = the total. No third hue. Category labels echo series colour (accent labels on accent rows, ink on the grey/total rows) — that colour-echo is what ties text to bars in S114 and must be preserved.
- **Connectors**: dashed (3-3) vertical steps, same hue as the row they leave — they are guides, not data; keep them ≤1.2px so they don't read as a chart element.
- **Total bar**: dark-grey full-width 100% bar is the family signature: it makes the share-denominator honest and gives the cascade a "closes at 100" punchline. Never let it overlap the legend or the note.
- **Axis/unit rules**: one unit per figure (% of total — never % of each row), shares to whole % unless precision is real, and if two shares are <1% apart they should be labelled with one decimal or merged.

VERIFY:
- [ ] title ≤15 words / 2 lines; the % cited in the title = sum of the bars it names
- [ ] rows sum to 100 (re-add them — rounding must be disclosed in the note if they sum to 99/101)
- [ ] source line present; `N | SECTION` present; footnote mark where methodology claims exist
- [ ] one hue + grey ramp only; white-on-accent inside labels clear 4.5:1, outside labels ink on white
- [ ] every bar has a value label; bars under 46px use the OUTSIDE treatment (not squished white text)
- [ ] total bar full-width, dark, "100%" centred; legend colours match the fills actually used
- [ ] no more than 8 rows (pitch would collide with the note block)

DON'T:
- multi-coded failures double-counted into every bar ("wrong ecosystem configuration" style multi-labels) — state single-coding in the note or the pie lies;
- >8 buckets — past that the stair degrades into stripes; roll into "Other" and cap it;
- ordering by category name or by the story's order — the descending stair only reads as addition when sorted largest-first;
- adding a second grey bar to "show nuance" — the grey row is the residual; nuance goes in the note slot;
- topic titles, kicker walls, or axis grids — S114 has none, and neither should this;
- letting connectors become solid guide-lines (chart-junk).

SOURCE: corpus sheet `corpus/sheets/sheet_012.jpg` cell S114 (deck: BCG Henderson Institute ecosystem study, p.11 in-deck) — measured fill pink ≈ #E61A57 (pixel-sampled from the sheet; that deck has no entry in `reviews/`, so the palette is cited from the image itself, not a review md). Layout, label placement, dashed steps, and the total bar are transcribed from that page; text content is new placeholder (post-merger value-leakage framing, realistic n=112 / 2019–24 / EBITDA-gap metric) so no deck text is reproduced.
