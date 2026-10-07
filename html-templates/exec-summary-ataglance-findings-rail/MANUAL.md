# exec-summary-ataglance-findings-rail — Executive summary, numbered findings + methodology rail

WHEN: The opening "at a glance" page of a survey-led research deck: what leadership
should take away, stated as numbered findings whose load-bearing statistic sits inside
the sentence, with the survey credibility block (n, population, fieldwork, dates) kept
visible in a right rail. Extracted from KPMG — *GenAI Survey 2024, Key insights*
(`kpmg__kpmg_genai_survey_2024_key_insights_2024`), Executive summary = p2
(sheet `sw_sheets/kpmg__kpmg_genai_survey_2024_key_insights_2024_s00.jpg`, frame 2);
the numbered (rather than dotted) marker is the playbook's takeaway-column standard.

ANATOMY (px on 1280×720 stage):
1. rule-top — hairline across the top, `88..1192` at y=64.
2. kicker — deck context line, x=88, y=78, width 840.
3. title — label title "Executive summary", x=88, y=104, 44px display, navy.
4. edition — right-aligned context block, x ends 1192, y=112, width 330.
5. thesis — one bold positioning sentence, x=88 (right edge 1024), y=178, 17.5px.
6. findings — numbered `<ol>`, x=88, width 800, first item y=256, item pitch ≈ 61px
   (13.5px body at 1.5 line-height + 16px gap). Each item: number column 44px + text.
7. method — methodology rail, right edge 1192, width 256, y=256; cyan 4px cap, wash
   field, heading + prose + `<dl>` of survey facts.
8. brandmark — placeholder SVG mark + firm wordmark, x=88, y≈662.
9. source — source line bottom-left, x=88, y=682, with footnote marker.
10. running — running head `03 | EXECUTIVE SUMMARY` bottom-right, y=682.

SLOTS:
- kicker: ≤70 chars, uppercase, "report name · section". Bad: a full sentence.
- title: 1–3 words ("Executive summary"). The ≤15-word/2-line gate is trivially
  satisfied here; do not let a marketing title creep in.
- edition: company / audience / series line; one bold line max.
- thesis: the page's so-what, ≤ 33 words and ≤ 2 lines (the MBB title gate applies to
  it — it is the claim this page makes). One accent phrase max via `.turn`.
- finding lead (strong): 2–4 words, a stance ("Investment is accelerating"), never a
  topic label ("Investment"). 
- finding text: 18–40 words, exactly one bold `.stat` per sentence pair; percentages
  as three-digit-safe bold accent. If an item needs 3 lines, shorten it or cut an item.
- method heading: "Methodology" (fixed).
- method prose / dl: respondent count, population cut, fieldwork window, market count.
  Keep 4 facts; a fifth fact belongs on the appendix page.
- source: "Source: …" sentence, ≤ 110 chars, with sup footnote where bases apply.
- running: "N | SECTION" — page number is part of the slot, not decoration.

FILL:
1. Replace kicker, title, edition text.
2. Rewrite `.thesis` as one declarative sentence; wrap at most one clause in
   `<span class="turn">` (renders accent).
3. Replace the five `<li>` blocks; keep one `<span class="num">` per item (renumber
   1–5, no skipping — a missing number reads as an error). Keep one `<strong>` lead
   and one or two `b.stat` per item.
4. Rail: replace paragraph + all four `<dl>` rows (`dt` = fact name, `dd` = value).
   If your survey has dates/counts that differ, only text changes — structure is fixed.
5. Footer: source line + running head number; swap the brandmark SVG letter/fill
   (`rect` fill = `--accent`) and wordmark span.
6. Recoloring for another firm: set `--accent` and keep `--cyan`/`--wash` as the
   derived lightness pair (8% tint); if the brand has no cyan, set `--cyan` to
   `--accent` and `--wash` to its 8% tint — never introduce a second hue for the rail.

CHART RECIPE: none — this is a text-and-numbers page. The "figure" is each sentence's
bold statistic; if you need bars, use the `hbar-*` family on the following page rather
than converting findings into charts.

VERIFY:
- [ ] thesis ≤15 words and ≤2 rendered lines (MBB gate);
- [ ] every finding has exactly one bold lead and its stat bolded;
- [ ] one emphasis color: navy for numbers/titles, cyan only as the rail cap;
- [ ] no more than 3 hues on the page (navy, cyan cap, grays);
- [ ] accent type on white clears 4.5:1 (verify any recolored `--accent`);
- [ ] source line present bottom-left with sup marker where bases apply;
- [ ] running head bottom-right with page number;
- [ ] rail facts match the numbers quoted inside the findings (83/78/61/55/16/69/13/24/52 here).

DON'T:
- Topic-style leads ("Investment: overview") — leads must assert.
- Three or more stats per sentence (stacks become unreadable; split into two findings).
- A methodology rail stuffed with a paragraph wall — facts as dl pairs, prose one line.
- Recreating KPMG's trademark wordmark — ship your own mark on the placeholder frame.
- Dropping the page number so the summary floats free of the deck numbering.

SOURCE: KPMG *GenAI Survey 2024, Key insights* (`kpmg__kpmg_genai_survey_2024_key_insights_2024`),
Executive summary p2, viewed on `sw_sheets/kpmg__kpmg_genai_survey_2024_key_insights_2024_s00.jpg`
(frame 2 = p2, sheet index floor(2/10)=0); review `reviews/kpmg__kpmg_genai_survey_2024_key_insights_2024.md`
(font fact: one geometric corporate sans throughout). Palette hexes cited from sibling KPMG
reviews: navy `#00338D` (`reviews/kpmg__kpmg_kpmg_our_impact_plan_2024_update_2024.md`),
cyan `#019cde` (`reviews/kpmg__kpmg_kpmg_2020_ceo_outlook_covid_19_special_edition_2020.md`);
rail wash `#E8F5FB` is a derived 8% tint of the cyan, not sampled. The real KPMG face is the
house sans (Arial/Sharp-Sans family per the review); the Arial/Helvetica stack stands in.
