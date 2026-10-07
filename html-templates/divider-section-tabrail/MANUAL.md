# divider-section-tabrail — Display-Title Section Divider with Nav Rail

WHEN: Opening page of a major section in a magazine-paced survey report or annual
outlook, where the deck runs a persistent section rail and wants one owning hue per
chapter. White ground, a giant thin gradient title, an intro, one headline stat with its
claim, a photo strip, and the you-are-here rail on the right edge. From KPMG 2021 CEO
Outlook (`kpmg__kpmg_kpmg_kpmg_2021_ceo_outlook_2021`), section dividers "The road to
renewal" / "Trusted purpose" / "Digital agility" (read in
`sw_sheets/kpmg__kpmg_kpmg_kpmg_2021_ceo_outlook_2021_s00.jpg`, sheet index 0 = floor(3/10));
the opener + stat claim form recurs on KPMG 2020 CEO Outlook COVID-19 Special Edition p5.

ANATOMY (1280×720 stage; `1rem` = 1 stage px; content column 64→1008 = 944 wide,
rail column 1048→1216 = 168 wide, right margin 64):
1. Top hairline rule — `64, 64`, 944×1.
2. Header line — `64, 80` across 944: deck name left, `Section 02 / 05` right.
3. Display title — `64, 116`, width 900, 80px weight 200, line-height 1.08, gradient clip.
4. Mid hairline rule — `64, 312`, 944×1. Title must clear it: two lines at 80px end at
   ~316, so a third line collides. This is the hard gate.
5. Intro / lede — `64, 344`, width 620, 18px, 3 lines max, carries footnote `1`.
6. Headline stat — `758, 340`, width 250: numeral 58px light in `--section-lt`, then a
   2-line claim on a hairline, with its own `1` marker.
7. Photo strip — `64, 460`, three tiles 304×118 at 16px gaps; each tile has a 2px section
   -hue caption rule. Tiles are gradient stand-ins and are labelled as such.
8. Section rail — `1048, 112`, 168 wide: caption + 5 tab rows (1px rules) + legend. Active
   row is filled `--section` with white bold label, a 5px cyan tick at `x=1042`, and page
   refs in the section tint.
9. Source line — `64`, bottom 28, width 820, 11px.
10. Page number — `right:64`, bottom 26, 30px display + "Section 02" label.

SLOTS:
- `title` — **≤ 15 words and ≤ 2 lines** at 900px / 80px. Short beats long: three to five
  words reads as furniture; six-plus starts to look like a body line. It may be a themed
  name ("The road to renewal") rather than a claim — that is what the kicker/stat does.
- `section_index` — "Section 02 / 05". Two numbers, current first. Never "Section 2 of
  chapter four".
- `lede` — 3 lines max at 620px / 18px: ~69 characters per line, so about 200 characters
  / 32 words, plus the footnote marker. The slot carries a `max-height:81rem` clip so a
  fourth line can never walk into photo tile 1 — the clip is a collision guard, not a
  licence to overflow. Set-up plus one number; if it runs long, cut, do not shrink.
- `stat_numeral` — three characters maximum ("69%", "2.4×"). One figure, not a range.
- `stat_claim` — ≤ 26 words / 2 lines, must name WHO and WHAT ("of CEOs plan to…"), with
  the methodology `sup`.
- `tiles[]` — exactly 3. Each caption: `bold locator` + 6–10 words. A photo strip with
  three identical captions is worse than no strip.
- `rail_tabs[]` — 4–6 rows, each `label` ≤ 22 chars (2 lines max) + `pages` like "p6–10".
  Exactly one carries `class="now"`.
- `rail_legend` — one line explaining the active-tab convention. Keep it; the rail is
  meaningless without it.
- `source` — survey window, n, markets, plus the rounding note if percentages don't sum.
- `pageno` — real page number + section label. Both.

FILL:
1. Re-theme for the next chapter: change **`--section`**, `--section-lt`, `--section-tint`
   only. The title gradient, the active rail tab, the stat numeral and the tile caption
   rules all follow those three tokens. (KPMG's system is literally "1 chapter = 1 brand
   hue applied consistently to headers, bubbles, bars, photo frames".)
2. Title: replace the `.title` text. Keep the weight at 200 and the letter-spacing at
   −.015em — the thinness is the design.
3. Move the you-are-here marker: cut `class="now"` off one `<li>` and put it on the next.
   Nothing else changes; the rail order is the deck order.
4. Stats: replace `.stat .n` and `.stat .c`; keep the `sup` pair with the `.source` line.
5. Photo strip: replace each tile's `<svg>` — inline the photo as a base64 `<image>` if
   you must stay self-contained, else keep a duotone SVG and leave the "placeholder"
   caption wording honest. Frame the strip with the section hue.
6. Footer: page number + section label, source line + footnote definition.

CHART RECIPE: none — the only figure is the single stat numeral (slot 6), which is
displayed as a numeral, not a chart. If the section's headline evidence is a chart, that
belongs on the following content page (`content-action-title` / the group-B chart cards),
not on the divider.

VERIFY:
- [ ] Title ≤ 15 words and ≤ 2 lines; check it against the `312` rule — third line = fail.
- [ ] Source line present bottom-left; footnote `sup` pairs resolved.
- [ ] One emphasis hue: `--section` + its own light step. Grey is the only other thing.
- [ ] ≤ 2 hues (section ramp) + achromes. No second brand colour beside the rail.
- [ ] Contrast: white tab label on `#00338D` ≈ 11:1 ✓; `#16202B` body on white ≈ 14:1 ✓;
      grey `#5B6773` on white ≈ 5.6:1 ✓; do NOT use `--gray-2` for body text (2.5:1).
- [ ] Exactly one active rail tab, and the rail covers every section in the deck.
- [ ] Page number + section label present bottom-right.
- [ ] Zero network calls: no `img`, `link`, `script`, `iframe`, `@import`, no webfonts.
- [ ] Gradient-title fallback verified by hard-coding the fallback colour once: if it
      disappears entirely, the clip rules are in the wrong order.

DON'T (corpus failure modes, KPMG + neighbours):
- Kicker walls of text — the review's recurring knock. The intro is 3 lines; the rail
  carries no prose. If you need more, it is a content page.
- Topic titles with no numbers anywhere. The divider's job is scope + one reason.
- A second rail: do not stack a chapter rail and a topic rail. One axis only.
- Filling inactive tabs with the section hue — "the rest" is grey, one fill is the marker.
- Ten-hue photo strip: one duotone preset across all three tiles, framed in the section hue.
- Letting the title touch the rail: rail starts at x 1048, title box ends at 964. Never
  widen the title into the rail.

SOURCE: KPMG 2021 CEO Outlook (`kpmg__kpmg_kpmg_kpmg_2021_ceo_outlook_2021`), section
dividers — pages read in `sw_sheets/kpmg__kpmg_kpmg_kpmg_2021_ceo_outlook_2021_s00.jpg`
(sheet 0, pages p1–p10) and the opener/stat form in
`sw_sheets/kpmg__kpmg_kpmg_kpmg_2020_ceo_outlook_covid_19_special_edition_2020_s00.jpg`
(p5); archetype + palette wording from
`reviews/kpmg__kpmg_kpmg_kpmg_2021_ceo_outlook_2021.md` ("giant gradient title left, short
intro, thin rules, photo strip"; "right-edge vertical section tab rail"; hexes #00338D,
#001E3C, #0099DA/#00AEEF/#00B0F0, teal family) and
`reviews/kpmg__kpmg_kpmg_kpmg_2020_ceo_outlook_covid_19_special_edition_2020.md`
("section opener (outlined word + themed lead)"). Typography note: KPMG's real divider
face is an ultra-thin high-contrast display (close to a thin Didone/stencil) in brand
gradients; "Helvetica Neue" at weight 200 stands in for it and keeps the geometry, not
the letterforms. No webfonts per spec.
