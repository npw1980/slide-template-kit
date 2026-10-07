# exec-summary-ataglance-editorial-spread — Executive summary as a two-column editorial spread

WHEN: The opening summary page of a published-research report (survey + interviews),
where the deck is meant to read like a magazine, not a slide: chapter numeral, heading
under a short brand rule, lead + photo left, justified takeaway prose right. Extracted
from EY | IIF — *Risk management in a time of transformation*
(`ey__ey_risk_management_in_a_time_of_transformation_2024`), Executive summary = p4
(sheet `sw_sheets/ey__ey_risk_management_in_a_time_of_transformation_2024_s00.jpg`,
frame 4).

ANATOMY (px on 1280×720 stage):
1. chapter-num — oversized chapter numeral ("04"), x=88, y=60, 60px light, pale violet.
2. micro-caption — small uppercase context line with violet dot separators, x=88, y=132.
3. title — plain heading "Executive summary", x=88, y=164, 40px regular weight.
4. rule-brand — short yellow brand rule, x=88, y=234, 132×5.
5. lead — single lead paragraph (the page's thesis), x=88, width 520, y=270.
6. figure.photo — grayscale photo block 520×168 + caption, x=88, y=414.
7. article.body — right justified column, x=680, width 512, y=270; 2–3 paragraphs,
   each opening with a bold claim sentence.
8. brandmark — co-brand lockup (placeholder), x=88, y≈662.
9. source — source line bottom-left, y=682, with footnote marker.
10. running — `5 | EXECUTIVE SUMMARY` bottom-right, y=682.

SLOTS:
- chapter-num: the deck's own section number; 2 digits, no leading copy. If the page
  has no chapter, drop the numeral and keep the micro-caption line as the kicker.
- micro-caption: ≤80 chars; three facts max, separated by dots. Bad: a full sentence.
- title: 1–3 words. The MBB ≤15-word/2-line gate is enforced on the *lead*, not this
  label. Do not turn the heading into a claim — the claims live in the paragraph leads.
- lead: ≤ 40 words, 2–4 rendered lines, exactly one bold phrase (the thesis). This
  sentence is what the two columns below support; if it doesn't match the body claims,
  one of them is wrong.
- figure caption: "Figure: who/where", ≤110 chars — never "a picture of …". Replace the
  SVG block with a real grayscale photo of the same 520×168 box (keep one tone family).
- body claims (b.claim): 4–10 words each, declarative ("Transformation is the CRO's
  agenda"); these three bold sentences must stand alone as the takeaways.
- body paragraphs: 28–55 words each; justified; one inline `pullnum` statistic max on
  the page (5 of 10 here) — the rest stay in prose so the page keeps its editorial tone.
- source / running: as specified in TEMPLATE_SPEC footer anatomy; footnotes to an
  appendix page are stated in the source line ("Footnotes continue on p. 41").

FILL:
1. Set chapter numeral + micro-caption from the deck's own numbering.
2. Replace heading; keep "Executive summary" style labels; if the deck titles it
   "Overview"/"At a glance", use that — the slot geometry is unchanged.
3. Rewrite `p.lead` as the page thesis; one `<b>` phrase inside.
4. Replace the photo `<svg>` with either (a) a real photo `<svg><image href>` — only
   if the deck is offline-embeddable, or (b) keep the placeholder frame and hand the
   520×168 box to a designer. Update the figcaption.
5. Replace the three `<p>` blocks in `article.body`; keep the structure
   claim-sentence first, evidence second, footnote marker where a base/weight applies.
   Add a fourth paragraph only if it still clears the column (watch y-overflow at 270 +
   4×(≈63px) + 45px gaps ≈ 690px limit).
6. Recolor for another firm: swap `--violet`/`--violet-pale`/`--violet-deep` as a
   triple (keep the pale step for the numeral) and `--accent` for the brand rule hue.
   If the brand yellow is unavailable, grey the rule (`--gray-2`) — never yellow text.

CHART RECIPE: none — encoding is prose. The single typographic "figure" is the
`pullnum` ratio (numeral + "of N"); if a number needs a chart, it belongs on the
following page in the hbar/vbar family, not here.

VERIFY:
- [ ] lead ≤ 40 words / ≤ 4 lines and matches the three bold claim sentences;
- [ ] claims render as a standalone takeaways list if copied out alone;
- [ ] ≤ 3 hues on the page: brand yellow (rule only), violet (numeral + pullnum),
      grays; body text stays `--gray-1` on white (clears 4.5:1);
- [ ] photo box is grayscale and captioned; no color photography against the violet type;
- [ ] source line present, footnote marker appears next to every weighted/unweighted
      statistic used;
- [ ] running head with page number present;
- [ ] justified columns show no rivers with the fill copy (hyphens are on).

DON'T:
- Stat-callout cards on this page — the corpus page is prose; the harvest's
  "stat-callout" tag for p4 is a mislabel, confirmed absent on the page image. Bullets
  and number tiles turn this into the findings-rail variant: pick one template per page.
- Topic-style paragraph leads ("Risk landscape" as a bold header) — leads assert.
- More than one inline big-numeral per page; it stops being emphasis.
- Full-color photos next to the pale-violet numeral — the page's calm is tonal, not
  chromatic.
- Hard-wrapping the justified text: let `justify` do the work; manual line breaks show.

SOURCE: EY | IIF *Risk management in a time of transformation*
(`ey__ey_risk_management_in_a_time_of_transformation_2024`), Executive summary p4, viewed
on `sw_sheets/ey__ey_risk_management_in_a_time_of_transformation_2024_s00.jpg` (frame 4 =
p4, sheet index floor(4/10)=0); palette and layout facts from
`reviews/ey__ey_risk_management_in_a_time_of_transformation_2024.md` (yellow `#FFE600`,
violet ramp `#7B2FA6`/`#4B1F7D`/`#C8B4DC`, gray `#6E6E73`, wash `#EFEFF2`; the related
takeaway pages p5–p9 confirm the claim-sentence-first habit). EY's real faces are the EY
house sans; body serif is a stated substitute (the sheet's body face was ambiguous), so
decks shipping this template name the substitution in their brand note.
