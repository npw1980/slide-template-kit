# kpi-numerals-band — KPI stat band (four giant numerals in a full-bleed grey field) + so-what claim + evidence floor

WHEN: Capability / practice-overview pages that must open with proof-before-prose: one claim title, a full-bleed light-grey band carrying four giant numerals each with a caption beside it, one line of "so what", and a supporting evidence floor (lead box + dated callouts). From Deloitte's 2018 Digital Transformation practice deck, page 2 ("Salesforce Practice Overview"), same grammar reused across practice-overview pages in that family.

ANATOMY (1280×720 stage; all coords in stage px):
1. kicker       — x76 y46 w700, 11px bold UPPERCASE, 2.8px tracking, grey #7D7D7D.
2. title        — x76 y66 w1010, 27px bold display, ink #1A1A1A, line-height 1.18 (2 lines max).
3. band         — x0 y138 w1280 h126 FULL-BLEED, fill `--band` #6D6E76 (darkened silver field — see SOURCE). Inner row x76→x1204, 4 cells, pitch 282px, 1px rgba(255,255,255,.35) dividers between cells 2–4.
4. num-1..4     — inside each cell, left-aligned, 46px bold display, WHITE on the band, letter-spacing −1px, no wrap.
5. cap-1..4     — right of the numeral inside the cell, 11.5px white (93% opacity), 2 lines max.
6. claim        — x76 y286 w1130, 16px grey #595959, one line (~15 words), bold ink core sentence.
7. vlabel       — x76 y330 w14 h318, vertical brand word, 11px bold, dark green, 3.2px tracking.
8. leadbox      — x108 y330 w498 h318, 2px accent-green border.
9. box-head / 10. box-body — 15px bold ink + 12.5px grey, ≤3-line paragraph (measured: body field fits ~580 chars at 3.5 lines; keep ≤480).
11–13. awards   — x648 w556, three dated callouts, 12px grey + year chip (1px green outline), hairline-separated.
14. source      — x76 y696, 10.5px grey, long method string allowed (≤180 chars).
15. page        — right x1204 y695, bold page numeral + " | SECTION" running head.

SLOTS:
- kicker: ≤5 words, the practice/section name. Topic label is fine HERE; the title carries the claim.
- title: action claim ≤15 words / 2 lines at 27px in 1010px — quantitative or comparative, not "Practice Overview".
- num-1..4: display numerals — max 6 chars incl. thousands separator / % / # ("1,000+", "#1", "97%", "5,200+"). Mixed shapes (1 digit, comma, %) stress-test the row best. All four should measure different things (reach, rank, rate, headcount) — four of the same metric is a table, not a band.
- cap-1..4: ≤60 chars / 2 lines; each names WHAT the number counts (population + period). An unattributed giant numeral is the corpus failure mode.
- claim: 1 sentence ≤15 words; bold spans the interpretive core.
- box-head/box-body: head ≤8 words; body ≤480 chars, ≤3 lines — mechanism, not more stats (stats belong in the band).
- awards: year chip ≤6 chars; text ≤130 chars / 2 lines; source-bearing ("Gartner… 2017") not self-praise.
- source: full method string — sample size, field dates, database; this slot absorbs long honest strings.

FILL:
1. Swap kicker + title first (title drives the page).
2. Band cells: replace `.num` (single string per cell) and `.cap`. Keep 4 cells; a 5th numeral breaks the 282px pitch — fold it into the lead box instead.
3. Recolor for a different house: set `--accent` (borders, chips, vlabel) and `--accent-ink` (text on white — must clear 4.5:1). The band field `--band` stays a neutral dark silver; `--band-ink` stays white — numerals never take the brand hue (facts, not marketing).
4. Evidence floor: rewrite lead box head/body and the three award rows. Year chips: swap chip text only.
5. Footer: source string left, bold page number + section running head right.

CHART RECIPE: no chart — the band IS the encoding. Encoding rules: (a) one metric per cell, no axis, no labels beyond the caption; (b) order cells by argument, not magnitude — usually reach → rank → rate → headcount, or lead with the one that makes the title true; (c) the giant-numeral device relies on NUMERALS staying neutral near-black; emphasis hue belongs to the evidence layer (borders/chips) so "the numbers" read as facts, not claims; (d) if one numeral dominates (e.g. 10× the others), keep it but let the caption carry the caveat — never shrink it to fit a scale.

VERIFY: title ≤15 words / 2 lines (27px × 2 lines ≤64px, band starts y128 — overflow collides with the band); each caption ≤2 lines at 11.5px/1.35 in the 126px cell (fits at ≤60 chars); band dividers land between cells not through numerals; text on green chip ≥4.5:1 (use `--accent-ink` #3A5A0F ≈ 6.4:1, raw #86BC25 is ~1.9:1 — NEVER green text on white); exactly one hue (green) + near-black + greys; source line present; bold page numeral present.

DON'T:
- Topic title ("Salesforce Practice Overview") — that was the deck's own title habit; our gate demands a claim. If only a topic fits, the page isn't ready.
- Tinted or accent-coloured numerals on the band — turns evidence into marketing; inside the band the numerals are white-on-silver, period.
- A light silver band with white numerals — the deck's own #F0F0F0-ish field reads ~1.9:1 with white text; the template ships a darkened field that keeps the inverted device and passes contrast.
- Four numbers measuring the same thing ("2M, $54M, 70%, 3B" with no common frame) — a stat salad; pick four distinct dimensions.
- Captions that restate the numeral ("1,000+ — over 1,000").
- Green text on white; green is border/chip-only, ink-dark for anything text-sized.
- A caption wall: 2 lines max — the deck's own p2 captions are 2-line; longer means the metric is too fuzzy for a band.
- Filling the evidence floor with a logo wall (the deck's real p2 has one — logos can't ship portably and go stale; dated callouts with sources age better).

SOURCE: deloitte__deloitte_digital_transformation_2018 — page 2 read from sw_sheets/deloitte__deloitte_digital_transformation_2018_s00.jpg row0/col1 (band field #F0F0F0 pixel-sampled: 240/240/240 dominant; green border pixels ~#A8D868 anti-aliased over white); device notes per reviews/deloitte__deloitte_digital_transformation_2018.md §color and §copy. Brand face is Open Sans with Verdana fallback (playbook §Deloitte); the file ships an Arial/Helvetica stand-in. Green hex unresolved across Deloitte regional toolkits (playbook flags this) — #86BC25 is the commonly-cited value, treat as remappable token, not brand truth. Band field: page-background pixels sample #F0F0F0; the zoomed band reads mid-silver with white numerals (device kept, field darkened to #6D6E76 so white text clears 4.5:1 — deviation documented here rather than copied as-is).
