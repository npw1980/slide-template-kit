# journey-lanes-to-target — Path Lanes Converging on a Target Ring

WHEN: A "which paths feed the goal, and how far is the goal" page — several acquisition
paths (or journey legs) drawn as proportional bands running left→right, all converging into
one ring that carries the argument. Straight from PwC Strategy&, *Global Entertainment &
Media Outlook 2023–2027 (Hong Kong summary)* p28 — a two-zone band-over-column diagram with
small direct labels and white convergence arrows — plus the catalog "funnel-to-target"
device S0266 (4 bars converge into a target ring, `corpus/sheets/sheet_027.jpg` frame 6) and
S0018/S0257. Pick this when the argument is **mix plus ambition**: not "how much dropped",
but "which path is worth more, and how far we are from target". (For pure stage-to-stage
leakage, use `journey-conversion-funnel`.)

ANATOMY (1280×720 stage, coords from the CSS/SVG source; 1rem = 1 stage px):
1. kicker  — `17 | CUSTOMER JOURNEY — PATHS TO PURCHASE, FY26 YTD` 64,34, 1152×20, 12px caps
2. title   — claim title, 64,56, 1152 wide, 27px/35px bold, sup¹ marker
3. lead    — 64,102, 1152 wide, 13px bold, one accent figure + the totals sentence
4. stage axis — 64,34: three labels "Reach / Trial / Purchase" on one baseline with 1.2px
              ticks onto the lane field (x190 / x560 / x900) — the journey moments, stated once
5. lane field — wash rect x176,188 640×372 (fill-opacity .5) + left rule x=190
6. lanes   — 4 `<path>` bands, yc = 232 / 324 / 416 / 508 (pitch 92), thickness t =
              round(30·v/vmax) = 30 / 25 / 13 / 15px, straight x190→x900 then two edges
              tapering to the single mouth point (1004, 360). Band 3 is accent-filled.
7. conversion labels — right-aligned x=888 under each band's right end: rate 11px bold over
              "N buyers" 9.5px
8. note block — accent tick x=176 (574→600) + title y580 + 2 body lines y594/606, x190
9. target ring — cx=1112, cy=360; outline circles r=86 and r=76, 13px track ring,
              current arc = grey-1 dasharray 265.3/275.1 rotated −90° (49.1% of target),
              target notch = tick 267.5→248 + "TARGET 97,100" caps, centre text 4 lines
              (claim caps / 30px numeral / 11px / 9.5px)
10. footnote — inside SVG, x176,y620 — the attribution/credit rule
11. base   — 64,bottom52, 10px; source 64,bottom16 + sup²; running head right,bottom16

SLOTS:
- kicker: page + section + the period. Never a sentence.
- title: ≤15 words, ≤2 lines. Must contain the comparative ("2.5×", "twice", "the only
  path"), otherwise it is a topic.
- lead: one sentence ≤200 chars, ONE accent figure, then the totals ("1,184,000 reached,
  47,700 buyers, 49% of the FY27 ambition"). The totals also appear in the base line —
  that is the reconciliation, keep both consistent.
- lane names: 2 words max ("Retail partner", "Referral / advocacy" is the allowed long
  form). Caps 10.5px. Names go above the band's top edge, never inside, never rotated.
- lane value: 13px + the unit word "reached" at 9.5px. Inside the band when t ≥ 24px
  (baselines 232+6 / 324+6), below the band when thinner (416+6.5+15 / 508+7.5+15) so a
  13px-thick band never carries 13px text.
- lane conversion: one rate + one buyer count per lane, right-aligned under the band's
  right end. Rate is buys/reached for that lane; never a per-stage rate here.
- note block: ONE, ≤3 lines, must contain a derived number ("~13,900 buyers — 14% of
  target"). Its accent tick marks it as commentary; it does not mark the data.
- ring claim: the sentence inside the ring is the argument ("49% of the FY27 ambition"),
  not a bare percentage. 4 lines max: caps claim / numeral / 11px / 9.5px.
- base + footnote: base = what is counted, window, n; footnote = the credit rule
  ("counted once on the highest-scoring path") because multi-path pages always tempt
  double-counting.
- target: an ambition number that is NOT measured data — it must be sourced ("set in the
  2026 Commercial Plan"). An unsourced target belongs in a different page.

FILL (build a new page from this file):
1. Replace the four lane volumes and buyer counts (the `<g>` blocks). Recompute
   `t(i) = round(30 * v(i)/vmax)` with vmax = the largest reached. Rewrite each path's two
   y-pairs as `yc − t/2` and `yc + t/2`; the taper point (1004,360) and the straight span
   190→900 never change. If a lane's t drops below 24, move its value label below the band
   (`y = yc + t/2 + 15`).
2. Recompute each rate as `buys/reached`, one decimal + "%", and place at x=888 under the
   band (y = band bottom + 22 for thick bands, band bottom + 15 for thin ones — keep the
   existing pattern). The buyer count line always sits directly under its rate.
3. Ring: `arc% = today/target`. Circumference = 2π·86 = 540.4, so `dasharray =
   5.404·arc%` on, `540.4 −` that off, with `transform="rotate(-90 1112 360)"` so the arc
   starts at 12 o'clock. The centre numeral is TODAY; the notch label is TARGET; the
   11px line is the ratio. If today > target, cap the arc at the full ring and change the
   line to "ahead of target" rather than drawing past 100%.
4. Reconcile: `sum(reached) == 1,184,000`-style base total and `sum(buys) == 47,700`-style
   today. Both go in the base sentence. If they don't tie, the page is wrong, not the note.
5. Emphasis: exactly ONE lane keeps `fill="var(--accent)"`. Grey `#DEDEDE` is "the rest";
   the dark `#2D2D2D` is reserved for the ring's measured arc, not for a lane. To move the
   argument (say, retail instead of referral) move the accent fill, its `.hi` labels, and
   the note's arithmetic — and nothing else changes.
6. Recolour: brand hue into `--accent`, keep `--ink #051C2C`, grey ramp 2D2D2D/464646/
   7D7D7D/DEDEDE, `--rule #C7CDD3`. Do not reintroduce the source deck's magenta→orange
   band gradient; the kit collapses multi-hue bands to grey + one accent.
7. More/fewer lanes: pitch is 92px per lane over y188→560, so 3 lanes = pitch 124, 4 = 92
   (as built), 5 = 72 (then names move above and unit words drop). 6+ lanes belong on two
   pages or the hbar template.

CHART RECIPE (this is the page type — follow exactly):
- SCALE. Two encodings, kept strictly separate. (1) Lane THICKNESS = volume reached:
  linear, zero-based, 30px = the largest lane, so thickness is a proportion of the biggest
  path and thinner lanes are genuinely smaller populations. Never encode "converted" as
  thickness on the same page — the two would compete. (2) The ring is a GAUGE, not a
  scale: its whole circumference means 100% of the target, and only the arc is data. The
  ring is deliberately not sized to the lanes, so no one can read ring size as volume.
- AXIS / UNITS. The only axis is the three stage captions on the lane field's top edge
  (Reach / Trial / Purchase) with ticks — they name the moments, not numbers. No y-axis,
  no gridlines, no value axis anywhere. Units are people; every rate names its denominator
  ("of reach"), and the totals line states n + window. Percentages on the ring are explicitly
  "of the FY27 ambition", with the ambition's absolute value printed beside it.
- VALUE-LABEL PLACEMENT. Per lane: name above the band (−6px past the top edge), value on
  or below the band per the t≥24 rule, rate + buyer count below the band's right end
  right-aligned at x=888. Nothing on the taper, nothing inside the wedge beyond the value,
  no legend — direct labels are the legend. Inside the ring, four lines maximum and the
  biggest number is the measured one (today), with the target rendered as a tick + caps so
  it cannot be mistaken for data.
- EMPHASIS RULES. One accent: the lane the page argues about. Its name, value and rate go
  accent-bold as well, so the eye lands on the path before the ring. Grey = measured but
  not-argued-about. Dark grey = the ring's own measured arc (a third role, still not a hue).
  The note block's accent tick is commentary furniture, not a data mark. Never mark the
  "bad" lanes red — the argument is carried by the one highlighted path plus the numbers.
- HONEST-SCALE GUARDS. Thickness is proportional, so a lane half as thick is half the
  reach — do not boost thin lanes with a minimum thickness; a 13px floor is already what
  makes the smallest path readable, and that's stated. If a lane's reached volume is so
  small it is under ~5px, fold it into "Other paths" rather than drawing a hairline. The
  convergence point is geometric, not data — the taper encodes nothing, and the caption
  says "converged" so it is not read as a value.
- MIX RULE. Because paths overlap, the credit rule must be on the page (footnote) and the
  rates must be per-path, not blended. If two paths are nested (a channel inside another),
  draw one lane and annotate, or the page double-counts.
- ARITHMETIC OF THE RING. today/target appears three times in different forms — ring arc,
  ring 11px line, lead sentence — and they must be identical. The note's "14% of target" is
  a derived increment; state it as derived, and check it against (target − today) so the
  reader can sanity-check it.

VERIFY:
- [ ] Title ≤15 words / ≤2 lines and carries the comparative, not the topic.
- [ ] Source line + "17 | JOURNEY" running head + sup markers; footnote with the credit rule.
- [ ] Thicknesses = round(30·v/vmax), monotone with v; thin lanes' values below the band.
- [ ] Every lane has exactly one rate + one buyer count, right-aligned, nothing on the taper.
- [ ] Ring arc == today/target == lead sentence; circumference 540.4; arc capped at 100%.
- [ ] Sum of reached = base total; sum of buyers = ring numeral; both stated in the base.
- [ ] One accent (one lane + its labels). Grey = rest, dark grey = ring arc. No red, no gradient.
- [ ] Target labelled as ambition + source, not measured data.
- [ ] Zero network requests (grep http:// / https:// returns nothing).

DON'T:
- Multi-hue bands (the source deck's magenta→orange gradient) or "brand colours for each
  channel". One accent, everything else grey; that single change is what makes a path
  diagram readable.
- Making the ring's radius carry volume, or drawing the ring as a second funnel — the ring
  is a gauge and must not be scaled to the lanes.
- Thickness that encodes converted volume while width also encodes reach (two competing
  scales on one shape), or a minimum-thickness floor that hides the real mix.
- Topic titles ("PATHS TO PURCHASE") or a title that names the biggest lane instead of the
  argument.
- Putting the target inside the ring as the biggest numeral — the ring's largest number is
  the measured one; the target is a tick and caps.
- A legend, arrows between every lane, or leader lines crossing the field: 4 bands with
  direct labels need neither. (The corpus pages that scatter callout arrows read as noise.)
- Ending the lanes at different x to signal "distance travelled" — the taper point is the
  same for all; progress is not encoded here, and if it must be, that's the timeline family.

SOURCE: firms = PwC Strategy& and Accenture. Page 1: p28 of *Global Entertainment & Media
Outlook 2023–2027, Hong Kong summary* (`pwc_strategy__pwc_global_entertainment_media_outlook_2023_2027_hong_kong_s`),
read on `sw_sheets/pwc_strategy__pwc_global_entertainment_media_outlook_2023_2027_hong_kong_s_s02.jpg`
(sheet index floor(28/10)=2; 5col×2row row-major). Catalog row for p28 records the page as
a "2 zone diagram: 4 pink domain bands over 5 orange function columns … use-case text
around, white arrows, magenta→orange gradient bands" — the band architecture and convergence
arrows are ported, the hues are not. Page 2 (device corroboration): Accenture *Accelerating
global companies toward net zero by 2050* p39 on
`sw_sheets/accenture__accenture_accelerating_global_companies_toward_net_zero_by_2_s03.jpg`
(stage cascade with n= per stage and excluded counts off the spine). Funnel-to-target form
factor: catalog S0266 ("4 bars converge arrow / funnel arrows into target ring",
`corpus/sheets/sheet_027.jpg` frame 6), with S0018 (`sheet_002.jpg` frame 8, funnel +
callout arrows) and S0257 (`sheet_026.jpg`, numbered layered funnel). Reviews exist for both
firms' decks; neither lists hexes for this page type, so the palette is the kit default
(DESIGN_PLAYBOOK line 57), stated as such.
