# timeline-node-milestones — Dated node rail with alternating callout flags

WHEN: When the argument is "X happened in N distinct waves and each wave answered the last gap" — policy histories, M&A/market event records, investment-round timelines. Two-firm evidence: PwC Strategy& *e-Mobility in India* p10 (review CSV p09), government-measures rail Mar 2011–Apr 2021 with 11 numbered nodes and above/below callout flags; the same convention repeats on the battery-investments rail (2019–21) in that deck.

ANATOMY (1280×720 stage px):
1. Kicker: 64,34 — bold accent lead + gray rest, one line.
2. Title (claim): 64,56 — Georgia serif 30px, max 2 lines, ≤15 words.
3. Rail: y=430, x 90→1172, 3px gray-2; grey double chevron 1172→1206 marks time direction.
4. Node discs: cx = x(t), cy 430, r 17, gray-1 fill, white number.
5. Date labels: 12.5px bold — below the rail (y=465) for odd nodes, above (y=415) for even nodes (opposite the callout).
6. Callout flags: rounded 176-px boxes, ABOVE (bottom y=390) for odd nodes, BELOW (top y=500) for even; grey 1.5px connector + arrowhead from disc to box.
7. Today marker: dashed accent vertical at x = x(t_today), chip "TODAY" (accent fill, white 9.5px).
8. Caption strip: 90,688 — italic 10.5px stating what the rail encodes + the scale formula.
9. Source line: 64,bottom-24 — 11px gray-1, footnote marker sup.
10. Running head / page stamp: right 64,bottom-26 — bold "NN | SECTION".

SLOTS:
- kicker: ≤110 chars; bold the part that names the track, not the whole line.
- title-claim: ≤15 words / 2 lines; must be an assertion ("each wave narrowed the gaps"), not "Timeline of X".
- node.date: "Mon YYYY", 8 chars; anchored on the node.
- node.lead: ≤28 chars/line, 1–2 lines — what happened (verb phrase).
- node.body: 11px, 2–3 lines ≤ 34 chars — why it mattered / what was still missing. 4+ lines means you're writing paragraph, not flag.
- today.date: same format as node dates.
- source-line: dataset + method + window; add footnote marker if any date is approximate.

FILL:
1. Replace title / kicker / lead-in text nodes (they carry the claim).
2. Edit the DATA ARRAY in the HTML comment: for each node set date label, month offset t (from window start), lead + body lines. Recompute x = x0 + t × ((x1 − x0)/(T_end − T_start)) (currently 90 + t×9.15, t = months from Jan 2011). Move the disc `cx`, its number, date, connector line/polygon; connectors must sit at the exact cx.
3. Callout box text: replace `<text>` spans (lead at box x+12 / body at box x+12); keep box x = node x − 88 (clamped inside [66, 1216]); adjust `height` to fit 2–3 body lines + lead (92–112 px).
4. Today marker: change x at the three places (vertical line, pointer triangle, chip rect+text; chip centred on same x). If "today" equals a node, keep the marker — the node stays gray; the accent marks "now", not "important".
5. Window change: adjust the two scale constants (x0 and the multiplier) and T_end; node geometry follows from the formula.
6. Recolor: set `--accent` to your brand hex; node discs/callouts/rail never change hue (gray ramp only).

CHART RECIPE:
- **Scale:** linear calendar scale — real dates, not index-equal spacing. Months t from window start map x = 90 + t×9.15 over 123 months (2011→2021); the rail is date-scaled so quiet stretches read as gaps. If your events span years with clusters, the honest alternative is a broken rail — but then say "scale discontinuity" in the caption and add break marks.
- **Value-label placement:** dates pinned to the node (centre, text-anchor middle), always on the side opposite the flag; event text in the flag, never on the rail. No other numbers on the figure.
- **Emphasis:** exactly one object may take `--accent` — the today marker (chip + dashed rule). All nodes are equal-weight gray-1 discs; the reader locates "now" first, then reads the flags. The chevron is gray; direction must not shout.
- **One accent + gray rule:** hues on page ≤ 2 (accent + ink) + gray ramp (#56616C / #9AA0A6 / #D9D9D9 / #F7F8F9). Never color flags by category on this page (that's the gantt sibling's job); category coding on a single-rail page multiplies hues.
- **Axis/unit rules:** no y-axis (single series of events); time axis labeled only at nodes — do not add month/quarter ticks under a sparse rail, they invite the reader to interpolate dates that aren't claimed. Window bounds appear in the kicker or caption, not as first/last tick labels.
- **Density:** 5–8 nodes is the legible band; >9 forces the alternation pattern of the source (up/down flags) and 90px+ node spacing. Adjacent nodes <90px apart: drop the date of the one whose date repeats a label that already appears (e.g. two events in "2019").

VERIFY: title ≤15 words / 2 lines ✓ | source line + window ✓ | exactly one accent object (today marker) ✓ | ≤2 hues on page ✓ | white-on-accent chip clears 4.5:1 (PwC red #E2192A: 4.7:1 — recoloring to a pale brand red fails; use dark text instead) ✓ | page stamp present ✓ | every flag text inside its box, no connector crossing a date ✓.

DON'T:
- Topic title ("Policy timeline") — the page must assert what the timeline proves.
- Accent-filled "important" node discs — breaks the one-emphasis rule; the story here is sequencing, not ranking.
- Category-colored flags (red/blue/green by ministry) — turns the rail into a 4-hue soup, the classic corpus failure.
- Kicker wall of text — one line; the flags carry the detail.
- Connecting arrows in accent (source did; kit rules say connectors stay gray — today owns the hue).
- Equal-spacing the nodes "because it looks tidy" — a date-scaled rail that lies about gaps is worse than none.

SOURCE: PwC Strategy& *e-Mobility in India: Market paradigms and ways to play* (2020), p10 of 55+ deck — sw_pages/pwc_strategy__pwc_e_mobility_in_india_market_paradigms_and_ways_to_play_20/pg-10.png (sheet sw_sheets/...s00.jpg, row 2 last frame). Convention + palette from reviews/pwc_strategy__pwc_e_mobility_in_india_market_paradigms_and_ways_to_play_20.md (timeline convention line 40, steal-list line 51, hexes #E2192A/#F2F2F2/#D9D9D9/#9AA0A6/#1A1A1A). Title register = PwC serif takeaway convention.
