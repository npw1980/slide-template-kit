# quote-pull-bubble-cluster — Stakeholder-coloured speech-bubble cluster

WHEN: A qualitative finding is made credible by many voices at once — the
evidence is that several different stakeholder groups independently say the
same kind of thing. From the Deloitte Accelerated Access Review UK Mapping
(2015): the "Illustrative Quotes" pages, p25 (Development) measured and
p30 (Regulation) with identical geometry; the review counts the device
~12 times deck-wide. Use it for interview/stakeholder programmes with a real
speaker taxonomy. If you only have ONE quote, use `quote-pull-claim-rail`.

ANATOMY (1280×720 stage; coords are stage px. The exhibit is one inline SVG
with `viewBox="64 134 1152 478"`, so SVG user units ARE stage px):
1. title — left 64, top 36, width 1060, 30px bold green; the run-in word is plain green, the italic part `--green-deep`.
2. message line — left 64, top 80, width 1000, 15px/1.45, 1-2 lines. This is where the claim lives (Monitor-style: short topic title + claim subhead).
3. stage chevron strip — right 64, top 36, 150×20, 4 chevrons, stage 1 active; label `1/4`.
4. exhibit panel — left 64, top 134, 1152×478, `--panel` #F4F4F4 with 1px `--panel-line` edge; caption `COMMENTS ON DEVELOPMENT` at 88/160.
5. speaker pair — two silhouettes centred on x≈700-798, y 330-430 (the person the quotes come from).
6. bubbles ×9 — rects `rx=6`, 1.8px stroke in the speaker's identity colour, white fill, 11px text (2-4 `tspan` lines), plus a tail triangle pointing at the silhouettes.
7. key — inside the panel, bottom-left at 88/470: `Key:` + 4 colour rules + labels.
8. footer rule 636; source line 64/648 (left); `25 | DEVELOPMENT` right 64/648; colophon right 64/666.

SLOTS:
- `title` — ≤6 words (topic label only). Good: `Stage: Illustrative Quotes`. Bad: a full claim sentence — the message line below already is the claim, and double claims double the word count.
- `message_line` — ≤26 words / 2 lines. Good: says what the cluster proves. Bad: "Quotes summarise some of the challenges" boilerplate with no finding in it.
- `bubble_text` ×9 — 2-4 lines × ≤44 chars, first line carrying the point. Good: verbatim spoken phrasing with one concrete number or named object. Bad: summarised corporate language (then the page is just a bullet list wearing costumes), and bad: any bubble over 4 lines — it collides with its neighbours.
- `bubble_speaker` — one of the four identity colours; the geometry (left/right/top) is free, the colour is not.
- `key_labels` — the same 4 names used in the bubble strokes; never more than 4 groups (5+ groups is the point where the encoding stops being readable).
- `source_line` — n= + method + the honest disclosure that quotes were edited (the review flags this deck's "wording unverified").
- `running_head` / `colophon` — page | section, and the firm's confidentiality line.

FILL:
1. Title: edit `<div class="title">Development: <i>...</i></div>` — keep the `<i>`.
2. Message: replace the `.message` text; keep 2 lines.
3. Bubbles: each is a `<g>` with a `<rect>` + `<path>` tail + a `<text>` of `tspan`s. Swap only the `tspan` text; keep `x`/`dy`. To add a bubble copy a `<g>` block and place it in the free ring (the corners are free: upper-left, right, lower-left, bottom).
4. Change the speaker set: edit the four `--navy/--cyan/--charity/--hmg` tokens AND their key entries together; the bubbles reference the tokens, so recolouring both is one edit per identity.
5. A different stage: change the filled chevron `<path fill/stroke>` and the `1/4` text; leave the other three gray.

CHART RECIPE: The figure encodes **who is speaking**, not how much. Colour = identity (4 classes, semantic, not decorative), spatial position = free, and there is no quantity channel — do not size bubbles by "importance", that is chart-junk the corpus rejects. Rules: white fill on the gray field; one stroke weight (1.8px); tails must terminate within 60px of the figure so the attribution reads as pointing at a person; the key is mandatory because 4 hues is exactly the readable limit for unlabelled colour. Text on white must stay ≥11px. The green `--green` (#6F8F2A) is darkened from the brand's ~#86BC90 family so 30px title text clears 3:1 — if you set body text on the bright brand green, contrast fails, keep bright green for fills only.

VERIFY:
- [ ] title ≤6 words and the message line ≤2 lines (the gate for the claim text).
- [ ] every bubble's stroke colour appears in the key, and every key colour is used at least once.
- [ ] only one green (title/caption) + the 4 identity hues; no fifth hue anywhere.
- [ ] key present inside the panel; `Key:` in bold, labels gray.
- [ ] source line bottom-left with n= and method; `PAGE | SECTION` bottom-right; colophon present.
- [ ] no bubble overlaps the key or the panel edge; text inside bubbles not touching stroke.
- [ ] render check: 0 non-file requests, 0 overflowing elements.

DON'T (corpus failure modes):
- Do not let the bubbles become a decorative halo with generic praise — each one needs a finding or a number.
- Do not put the key outside the panel or below the figure; the review's praise of this deck is that colour is a data dimension read inside the exhibit.
- Do not keep 9 bubbles when you have 4 good quotes; empty bubbles are worse than a sparser page.
- Do not add a photo of a person behind the silhouettes; the device is schematic on purpose.
- Do not re-use the bright brand green for bubble strokes — colour must mean "who", not "brand".

SOURCE: firm Deloitte (Monitor lineage) · deck `deloitte__deloitte_accelerated_access_review_uk_mapping_2015` · page 25 measured on contact sheet `sw_sheets/deloitte__deloitte_accelerated_access_review_uk_mapping_2015_s02.jpg` (tile 5) and re-cropped for palette: panel #F2F2F2 with #DC-#E5 edges, silhouette cyan #6CC9EB/#72C6E8, navy bubble stroke #3F4A68-#525D7B (rendered as navy #1F4E79 on white), title green sampled #8EAB3C-#99B744; chevron strip cyan/green/gray/yellow. Same geometry on p30 (same sheet, bottom row). Device and semantic-colour claims (stage colours, stakeholder colours "repeated in quote bubbles", ~12 uses, "colour used as a data dimension far more than as decoration") from `reviews/deloitte__deloitte_accelerated_access_review_uk_mapping_2015.md` §Color system / §Layout archetypes #5. Real fonts: Deloitte's proprietary brand sans + Monitor house face → substituted by the Helvetica Neue / Arial stacks.
