# timeline-gantt-roadmap — Year × workstream roadmap grid, state-coded bars

WHEN: When the deliverable is "how the work is scheduled, sequenced, and funded" — implementation roadmaps, remediation plans, post-M&A integration schedules, council/board decision timetables. Evidence: Deloitte *Town of Tillsonburg IT Strategy Review — Council Update* p11 "5 year roadmap" (year × workstream grid with numbered callouts); same grid device at weekly scale in the Deloitte NMSU staffing-study engagement timeline (p8).

ANATOMY (1280×720 stage px):
1. Kicker: 64,30 — one line, bold accent lead.
2. Title (claim): 64,48 — sans 28px bold, 2 lines, ≤15 words.
3. Lead line: 64,98 — 12px gray, one sentence framing sequencing logic.
4. Header bands: "Initiative" corner 64–254 (y 176–224, gray-1 fill); year band 254–1054 (y 176–204, gray-1, white 12px); half-year band (y 204–224, gray-4, 8.5px "Jan–Jun | Jul–Dec").
5. Grid: 7 row bands × 56px (y 224→616), zebra gray-5; half-year hairlines 0.7px rule-color; year-boundary rules 1.2px gray-2 from header to grid bottom.
6. Row labels: x 76, bold 11px gray-1, "1.0 Governance" style codes.
7. Bars: rounded pills (rx 7, h 14) at rowTop+24, spanning x(m0)→x(m1); fill encodes funding state (see CHART RECIPE).
8. Value tags: above each bar — bold code + "Mon YYYY → Mon YYYY · N mo" (9.5px).
9. Milestones: gray diamond at bar end; dates live in the tag, not the diamond.
10. Callouts: numbered circle (gray-1 disc, white numeral) on a bar + grey callout box in the right column x 1066–1216, leader runs horizontally inside the row band (never diagonal).
11. Today marker: dashed accent vertical + chip — the page's ONLY accent bar-free object besides the current-initiative bar.
12. Legend: y 632, six keys (Completed / Ongoing / Planned / Current initiative / Milestone / Today).
13. Source: 64,bottom-24 + footnote marker; running head "11 | ROADMAP" bottom-right.

SLOTS:
- title-claim: ≤15 words/2 lines; must say what the schedule *demands* ("front-load governance"), not "5-year roadmap".
- lead: 1 sentence (max ~2 lines) explaining the weighting logic; this is where "why the first two years are heavy" belongs.
- row.label: code + ≤22 chars; codes matter — every bar tag reuses its initiative code.
- bar.name: ≤34 chars inside bar; bar <150px wide shows code only.
- bar.tag: "start → end · N mo" — all three, always.
- callout: lead ≤16 chars + 2–3 lines ≤26 chars; the decision it names must have an owner/date.
- source-line: register + method + "planned start, not contractual" disclaimer where relevant.

FILL:
1. Replace kicker/title/lead text.
2. Edit the DATA ARRAY in the comment: rows → tasks {code, m0, m1, state}. Recompute x = 254 + m×13.3333 (m = months since window start; year = 160px). Bar rect: x = x(m0), width = (m1−m0)×13.3333. Move the bar's tag with it (tag x = bar x, tag y = rowTop+17).
3. Change window length: update the month constant and the year-band labels (each year = 160px); half-year labels repeat 2× per year.
4. States: recolor by swapping the bar rect's fill/stroke to the state triplet (see recipe). Do not invent new fills.
5. Milestone: replace diamond polygon at x(m_end), rowTop+31 (points (x−6,m),(x,m−6),(x+6,m),(x,m+6)).
6. Callouts: circle x inside the bar near its end, then the box text (lead + 2 lines); if only one callout, delete the pair (circle + dashed leader + box), not just one half.
7. Today: change the vertical line x (all three places: rule, pointer triangle, chip rect+text) to x(t_today).
8. Recolor: set `--accent`; the header band stays gray-1.

CHART RECIPE:
- **Scale:** linear calendar, x = 254 + m×13.333 (1 month = 13.33px, 1 year = 160px). Bars must be date-scaled — equal-width cells with unequal spans lie about overlap. Week-granularity engagements: same grid, set the multiplier so the window (e.g. 26 weeks) spans 800px.
- **Value labels:** one per bar, above the bar: bold code + start → end · duration. Never put dates on the bar ends as separate text (corpus failure: date clutter that can't be re-used). Name inside the bar when width ≥150px. When a right tag would collide with its left neighbour's tag, it drops below the bar (see 2.2).
- **State encoding = one accent + gray ramp:** DONE = gray-4 fill / gray-3 stroke (solid); ONGOING = gray-2 solid; PLANNED = white fill + gray-2 dashed stroke (unfunded must read as hollow); CURRENT INITIATIVE = solid `--accent` — exactly ONE bar in accent, the one the audience should fund or watch. Traffic-light red/amber/green fills are FORBIDDEN as state colors (semantic overload; the Deloitte review counts RAG as semantic-only on risk tables, and this grid has another axis — time).
- **Emphasis order:** accent bar (current) → accent today line (now) → everything else gray. A second accent bar is the same as having no focus.
- **Axis/unit rules:** year band centered per year, half labels under it; no month ticks inside a year (too dense — the half bands do that job); grid bottom rule closes the plot; vertical year rules connect the header band to the grid so bars can be read against the header without tracing.
- **Milestones:** diamonds only at decision points the audience owns (sign-off, go-live) — 2–3 per grid maximum, dates in the tag.
- **Callouts:** numbered + right-margin box; the number must appear on the bar (circle) AND the box; no leader crosses another row.

VERIFY: title ≤15w/2 lines ✓ | source line + disclaimer ✓ | exactly ONE bar takes the accent ✓ | ≤3 hues (accent, ink/gray ramp) ✓ | every bar tagged (start·end·duration) ✓ | planned bars visibly hollow (white + dashed) ✓ | white-on-accent chip/bar text clears 4.5:1 (#1F69AD = 5.0:1) ✓ | page stamp ✓ | legend complete ✓.

DON'T:
- Topic title ("Roadmap" / "Next steps") — the claim is the sequencing logic itself.
- Color per workstream (each row a different hue) — this is the classic 8-hue Gantt; state, not owner, is what the fill encodes.
- Solid fills for planned work — hollow + dashed is what makes "not yet funded" honest.
- RAG traffic lights for status — reserved semantic device, not schedule decoration.
- Diagonal leader lines from bars to boxes — they cross the grid and read as a relationship that isn't there.
- Date clutter at every bar end — the tag line carries dates; the bar carries span.
- >20 bars: past ~20 the grid stops being readable on one 1280×720 page — split by phase.

SOURCE: Deloitte *Town of Tillsonburg — IT Strategy Review, Council Update* p11 (of 20) — sw_pages/deloitte__deloitte_town_of_tillsonburg_it_strategic_review_council_upd/pg-11.png (sheet sw_sheets/deloitte__deloitte_town_of_tillsonburg_it_strategic_review_council_upd_s01.jpg, row 1 frame 1). Review: reviews/deloitte__deloitte_town_of_tillsonburg_it_strategic_review_council_upd.md (gantt-grid device line 21, palette register line 18, COPY steal-list line 27). Secondary: Deloitte *NMSU Staffing Study* p8 engagement timeline (week-range bars) per TEMPLATE_HARVEST "timeline" exemplars. Original's navy/gold bar fills were mapped to the kit's one-accent + gray-ramp system per the color rule.
