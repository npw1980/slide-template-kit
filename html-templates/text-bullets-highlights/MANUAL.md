# text-bullets-highlights — All-caps title + section kicker + giant KPI numeral + purple subhead / bold-lead-in paragraphs

WHEN: A "key highlights" page for survey or technical reports — an all-caps
label title, a section sub-label, one giant sample-size KPI as display type,
and 3–5 theme blocks each written as purple claim-subhead + bold-lead-in
paragraph. From Accenture's 2021 P&C Underwriting survey, page 5 (identical
grammar p4). Review explicitly flags p4–p5 as text walls — this template is
the SAME device with the overflow discipline added.

ANATOMY (1280×720 stage; all coords in stage px):
1. title        — x76  y50  w520, 28px bold ALL-CAPS, dark grey #3F3F3F, 0.5px tracking.
2. kicker       — x76  y87, 12px bold uppercase, 2.6px tracking, grey — names the section/cut.
3. KPI rail     — x960 y36 w244, right-of-title: numeral 64px bold purple #5E3078 + 2-line caption (12px bold + 10.5px grey small line).
4. blocks b0..b3— x76  w1120; top = 150 / 280 / 410 / 540 (pitch 130). Each block: subhead 15px bold deep-purple #401C5C (margin-bottom 4) + justified body 12.5px/1.5, ≤3 lines; bold runs render deep purple; `<q>` renders italic.
5. footer       — x76→x1204 y-bottom-26, 1px rule, 11px grey; left = SVG tick + "Source: …" string; right = "Number of responses = 295" + page numeral (bold ink).

SLOTS:
- title: all-caps deck-label — ≤4 words. No claim here (genre convention: claims live in the purple subheads).
- kicker: ≤4 words, the population/section cut ("COMMERCIAL LINES").
- kpi-num: 1–3 digits, the sample-size or headline figure (295). Display type — only big number on the page.
- kpi-cap + small: ≤8 words + ≤5 words; must say WHAT the number counts.
- sub: 2–4 words, quantitative/positional claim ("Underwriting Quality", "Investment Priorities") — this is the slot carrying the argument.
- body: ≤3 lines (~430 chars), one idea, opens with a bold lead-in that is itself readable as the sentence's subject; embed at most one inline statistic cluster (3-digit % allowed) and at most one italic respondent quote.
- source: long real method string allowed (≤120 chars — slot is sized for it). resp-count line + page numeral.

FILL:
1. Replace title, kicker, and the KPI numeral + 2 caption lines.
2. For each block: swap `.sub` text (claim words) and `.body` text. Bold what leads; keep ≤3 lines. A 5th block: pitch 108, but only with 2-line bodies — overflow is the failure mode, not style.
3. Accent recolor: `--accent` (KPI numeral) and `--accent-deep` (subheads, bold runs) move together. Everything else stays ink/grey.
4. The `<q>` element renders italic — delete it with the quote text if unused.
5. Footer: method string + response count + page.

CHART RECIPE: N/A — text page; the KPI numeral is the only "figure" (it is the deck's display-type device, paired with a caption naming the population).

VERIFY: no subhead/body block taller than 130px (3 body lines max); ≤15 words / 2 lines gate holds trivially at title level but each `sub` must still read as a claim, not a topic noun; ONE hue (purple ramp) + ink/grey only; `--accent-deep` #401C5C on white ≥4.5:1 (~9:1) and grey kicker ≥4.5:1 (pass at 12px bold); page numeral + response count both present; no more than one giant numeral.

DON'T:
- The p5 failure: five 4-line paragraphs = text wall. This template enforces 3 lines; trim claims, don't shrink type.
- Grey or black subheads — the purple claim-subhead IS the scanning device.
- More than one display-size numeral (it competes with the KPI; inline %s stay text-weight).
- Topic-only subheads ("Technology", "Talent") with the claim hidden in body prose.
- Italics or serifs outside respondent quotes; the deck is Helvetica/Arial all-weight.
- A second color family (the survey's rainbow segment palette is called out as off-brand in the review — don't reintroduce it).

SOURCE: accenture__accenture_2021_p_c_underwriting_survey_2021 — page 5 read from sw_sheets/accenture__accenture_2021_p_c_underwriting_survey_2021_s00.jpg cell row0/col4, p4 grammar corroborated; device inventory + KPI-numeral and monochrome-purple rules per reviews/accenture__accenture_2021_p_c_underwriting_survey_2021.md §1, §type, §color. Purples pixel-sampled from p5 (#401C5C–#704692 band); brand face is Univers Next-family on the real deck — the file ships a Helvetica/Arial stand-in.
