# case-study-three-column — Single Case, Three Color-Headed Panels

WHEN: one story told in one page, split into three fixed-framing columns — Background (what is
true) / Issues (what is not working) / Challenges (what stands in the way) — each column a solid
color-headed panel with an icon-rail item list, plus a solid implication bar beneath. This is the
Deloitte Monitor "3-column case study" pattern, used 3× in the same report. Evidence:
`deloitte__deloitte_accelerated_access_review_uk_mapping_2015` p43 / p67 / p68
(`sw_sheets/deloitte__deloitte_accelerated_access_review_uk_mapping_2015_s04.jpg` row 2 frame 3
and `..._s06.jpg` row 2 frame 4 / 5). Palette facts: brand green for titles/branding, deep navy
structure, neutral grays; the green band carries **ink** text (2.6:1 as white-on-green fails the
contrast gate — that is a deliberate fix, not a lapse).

ANATOMY: slot map with px coords on the 1280×720 stage (1rem = 1 stage px):
1. `topic` (h1) — green topic title, x:56 y:40, 27px; pattern = `<span class="lbl">Case study:</span> <Name>`.
2. `message` — the claim line, x:56 y:~74, 13.5px/1.4 ink, max-width 1080 (2-line gate).
   In this house style the claim is the subtitle, not the title.
3. `panels` — x:56→1224, y:150, height 452; three panels 373 wide, gap 24, hairline border.
4. `band` — color header 34px: navy `Background`, green `Issues`, gray `Challenges`
   (`panel--navy` / `panel--green` / `panel--gray`).
5. `item` rows — icon (20px inline SVG) + text, 3 per column; column body field `--tint`.
6. `implication` — solid navy bar, x:56→1224 y:620 h:40: `tag` "IMPLICATION" + one sentence.
7. `src` / `run` — source line bottom-left, "43 | CASE STUDIES" page stamp bottom-right.

SLOTS:
- `topic .name` — 1–3 words ("Pharma", "Medical devices"). Never a sentence — the sentence is
  `message`'s job; a sentence here is the double-title failure.
- `message` — 12–15 words, ≤ 2 lines, quantitative where possible ("...stays limited despite clear
  clinical and cost benefits"). This is the page's thesis; if it reads like a label, move the verb up.
- `band[i]` — 1 word each, fixed set. Renaming to "Context/Problems/Barriers" is allowed for a
  client vocabulary but keep all three single-word.
- `item[i].text` — 15–30 words, one fact per item, ≤ 4 rendered lines. Bold (`.b`) max one phrase
  per item. 3 items per column is the written fill; a 4th item is safe in Background only
  (21px line-height headroom) — test at 2 lines max.
- `implication` — the decision the case forces, ≤ ~110 chars, one bolded lever.
- `src` — data basis + sample size + copyright line (the deck's rigid footer).

FILL: replace topic name, message text, per panel: band label stays unless client vocabulary;
replace each `item` paragraph keeping its `<svg><use href="#i-..."/></svg>` — icons are inline
symbols (`#i-doc #i-check #i-bank #i-clock #i-warn #i-chat #i-cycle #i-scale #i-coin`); pick the
symbol that matches the fact (doc=approval/document fact, bank=institution, clock=time gap,
warn=caution, chat=stakeholder disagreement, cycle=policy loop, scale=budget, coin=money,
check=verification gap). To recolor: brand hue = `--brand` (band) + `--green-ink` (title/icon);
for a client on one brand color set all three bands a lightness ramp of the brand and use ink
text on the two lighter bands. For 2 panels instead of 3, drop one `.panel` (flex equalizes).

CHART RECIPE: none — this is a framing page. Color rule: the three band colors are **semantic
roles, not decoration** (structure / friction / barrier); they must stay distinguishable, and
text colors are locked per band (white on navy 12:1, ink on green 7.8:1, white on gray 4.8:1).

VERIFY: message ≤ 15 words / 2 lines; title is topic-only; each item ≤ 4 lines so columns align
without overflow (flex `gap:16` gives headroom for one longer item per column); contrast as listed
per band (do NOT flip ink-on-green to white-on-green); icon strokes inherit column color — no
stray hues; source line present with © line; page stamp present.

DON'T: sentence-length topic title; equal 3-line-everywhere fill — vary item length (the pattern
reads as argument when Background is longer than Challenges); 3 accent hues as decoration (the
colors are role labels; if the deck has 6 stage colors they belong to swimlanes, not this page);
SmartArt boxes (custom-drawn panels only); implication bar turned into a fourth full panel.

SOURCE: extracted from `deloitte__deloitte_accelerated_access_review_uk_mapping_2015` p43, p67,
p68 — read on `sw_sheets/deloitte__deloitte_accelerated_access_review_uk_mapping_2015_s04.jpg`
(sheet s04, p43 row 2 frame 3) and `..._s06.jpg` (p67/p68 row 2 frames 4–5); title-zone + kicker-bar
facts from `reviews/deloitte__deloitte_accelerated_access_review_uk_mapping_2015.md`
(§Title zone, §Color system, pattern "7. 3-column case study").
