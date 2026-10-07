# divider-section-outline — Outline-Type Chapter Divider

WHEN: Opening page of a numbered chapter in a long-form survey or thought-leadership
report, where the deck wants one owning device per chapter. Full-bleed duotone
photograph, a giant hairline-outlined "CHAPTER n" letterform as page furniture, and a
small block of copy inside it. From the EY | IIF Global Insurance Risk Management
Survey 2024 spine (chapter dividers p10 / p17 / p30; the half-bleed p18 form is visible
in `sw_sheets/ey__ey_risk_management_in_a_time_of_transformation_2024_s01.jpg`).

ANATOMY (1280×720 stage; `1rem` = 1 stage px, everything absolute):
1. Photo field — full bleed, `0,0` → `1280×720`, z-index 0. Duotone SVG stand-in.
2. Photo stand-in tag — rotated 90° down the right edge at `x=1269`, `y=290`, z-5.
3. Header eyebrow — `64, 44`, uppercase 12/1.2em, one line.
4. Brand lockup — `1152, 38`, 46×46 SVG mark, right margin 64.
5. Chapter furniture "Chapter n" — `52, 112`, 190px display, hairline-stroked, z-2.
6. Kicker chip — `64, 284`, filled accent, 14px uppercase, auto width (cap 660).
7. Section title — `64, 336`, box 740×~110, 40px light display, 2 lines max.
8. Accent rule — `64, 444`, 96×4 px.
9. Subtitle / claim line — `64, 466`, width 690, 19px, 2 lines max.
10. Intro paragraph — `64, 544`, width 640, 14px, 2–3 lines, carries the `1` footnote.
11. "In this chapter" index — `800, 284`, width 196, header + 3 items, left hairline.
12. Progress strip — `64, 612`, caption + 3 bars (144×4 each, 4px gaps) + names row;
    the names row ends at ~646 and the source line begins at ~659, so 3 bars is the
    ceiling — a 4th chapter name would collide with the footer.
13. Source line — `64`, bottom 28, width 780, 11px.
14. Page number — `right:64`, bottom 24, 34px display + "Section" label under it.

SLOTS:
- `furniture` — "Chapter 1". One word + one digit. Never a sentence; it is a shape.
- `eyebrow` — deck name / programme line, ≤ 70 chars, sentence-case → uppercased in CSS.
- `kicker` — "Chapter n · <section name>", ≤ 46 chars. If it wraps, shorten the name.
- `title` — **≤ 15 words and ≤ 2 lines** at 740px width. A descriptive section title is
  allowed here (this is a divider, not a content page) but it must still be a statement
  about the chapter's scope, not a bare noun. "Industry risk" is weak; "The big picture
  across emerging and familiar risk types" is right.
- `subtitle` — ≤ 26 words / 2 lines. One quantified observation that makes the chapter
  worth reading.
- `intro` — ≤ 34 words / 2 lines, with one superscript methodology marker.
- `index_items[]` — exactly 3 (2–4 allowed). Pattern: `Figure N · what it answers` +
  a bold count line. Bold line is the base, not a caption.
- `progress` — 1 active bar + N−1 inactive, names one per chapter, ≤ 22 chars each
  (they ellipsis — do not let them wrap).
- `source` — survey / fieldwork window / n / markets, one line. Keep the `1` marker pair.
- `pageno` — real page number + "Section". Both, never just one.

FILL:
1. Replace `.furniture` text (`Chapter 1` → `Chapter 2` …). Keep the same two-word
   shape so the stroke stays one line at 190px.
2. Replace the three `<stop>` values in `#g1` (`#150A21`, `#3A0F4B`, `#7B2FA6`) plus the
   `#C8B4DC` in `#v` to move the duotone to your brand ramp; the whole page re-tones.
   Or replace the whole `.photo > svg` block with the real photograph:
   draw it as `<image>` only if you can also inline the base64 data — otherwise keep the
   SVG field and print a note. The on-page `photo-tag` line is the honesty marker: delete
   it once a real image is in place.
3. Swap text: `.eyebrow`, `.kicker`, `.title`, `.subtitle`, `.intro` (and its `<sup>1</sup>`,
   which must stay paired with the `1` in `.source`).
4. Index: edit the three `<li>` spans; each `<em>` is the base/count.
5. Progress: set one `<i class="now">` and one `<b class="now">` per chapter — that pair
   IS the you-are-here marker. Add or delete bars to match the chapter count and keep
   `width:144rem` as `(600 − 4·(n−1)) / n`.
6. Recolor for another accent: change `--accent` only. Text on the chip is `#150A21` and
   must stay dark — yellow ground takes dark type.

CHART RECIPE: none — this is a divider. The only data-bearing objects are the index
counts (index 11) and the progress bars (index 12), both counts, not measurements.

VERIFY:
- [ ] Title ≤ 15 words and ≤ 2 lines inside its 740px box (`overflow` must not trigger).
- [ ] Source line present bottom-left, with the footnote definition after the `sup` marker.
- [ ] One emphasis colour only: yellow. Everything else is white / lilac / black ground.
- [ ] ≤ 2 hues on the page (purple ramp + yellow). No blue, no teal, no "brand photo" cast.
- [ ] Text on the yellow chip clears 4.5:1 — dark ink `#150A21` on `#FFE600` ≈ 13:1 ✓;
      white on yellow does NOT, never do that.
- [ ] Exactly one `now` marker is active in the progress pair.
- [ ] Page number bottom-right with its "Section" label.
- [ ] Zero network calls: no `img`, `link`, `script`, `iframe`, no `@import`, no webfonts.

DON'T (corpus failure modes, EY + neighbours):
- Topic-title dividers with no claim ("Industry risks"). The review's own knock on this
  deck is "dividers and figure headers lean on descriptive/topic titles" — this template
  is where you fix that, in the `subtitle` slot.
- Kicker chip carrying a sentence. It is a label; the sentence belongs in `subtitle`.
- Photos placed without checking contrast: outline type over photos is legible only by
  contrast (the deck has pages that are legible-only-because-of-contrast). Keep a dark
  duotone stop behind the copy block.
- Palette drift mid-chapter: the deck switched bar hue around figure 26. A divider is the
  chance to set the hue — set it in tokens, not per shape.
- More than 4 index items — it turns a divider into a contents page; use `agenda-contents`.

SOURCE: EY | IIF Global Insurance Risk Management Survey 2024 (`ey__ey_risk_management_in_a_time_of_transformation_2024`),
chapter dividers p10 / p17 / p30 — p18 half-bleed form read in
`sw_sheets/ey__ey_risk_management_in_a_time_of_transformation_2024_s01.jpg` (sheet index 1 = floor(16/10));
device wording and palette hexes from `reviews/ey__ey_risk_management_in_a_time_of_transformation_2024.md`
("Dividers (p10, p17, p30) = full-bleed photo + giant outline 'CHAPTER n' + one-line
descriptive title beneath"; "1 deck archetype… half-page photo / half-page content").
Typography note: EY's real face is its house humanist sans with an outline display layer;
the stacks here (Helvetica Neue / Arial) stand in for it — outline type still reads at
190px, but letterforms will not match EY's. No webfonts per spec.
