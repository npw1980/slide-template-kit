# cover — Full-bleed cover, firm mark bottom-right

WHEN: The page-1 cover of a research/insight report — claim title on a brand field, one duotone
photo, commissioning mark bottom-left, firm mark bottom-right, as-of stamp above the title. Use
it when the report leads with a quantified value claim rather than a topic label. Evidence:
Accenture for nbn Co, *The nbn effect: How the nbn™ network adds value to our lives*, cover p00
(violet field, slanted photo split, giant lowercase wordmark bottom-right) and KPMG, *2021 CEO
Outlook*, cover p00 (full-bleed duotone photo, logo top-left, left-aligned title stack).

ANATOMY: slot map on the 1280×720 stage (coords measured from the rendered file, stage px):

1. `kicker` — 64, 56 · 480×20. Uppercase eyebrow + 26×3 brand rule (chip), letter-spacing 2.6.
2. `as-of` — right 64, 316 · ~197×44. Right-aligned 2 lines: **fieldwork date**, then published date.
3. `title` — 64 → 1216 (width 1152), 368 · 92 high. 38px bold / 46 line-height, tracking −0.5.
   Cap is exactly 2 lines; the slot is sized so the gate cannot be silently broken.
4. `lede` — 64 → 1216, 476 · 52 high (18px / 26). Value statement, 2 lines max.
5. `note` — 64 → 1216, 566 · 16 high. One-line methodology footnote carrying `sup 1`.
6. `hairline` — 64 → 1216, 616, 1px, `--rule`.
7. `commission-mark` — 64, 640 · ~140×50. "COMMISSIONED BY" label 11px + lockup 21px.
8. `firm-mark` — right 64, bottom 26 → occupies 1028–1216 × 632–694. Chevron glyph over the
   wordmark at 38px lowercase. This is the template's signature: the firm mark is big, not a logo strip.
9. `visual` (photo slot) — 700, 0 · 580×290, `clip-path: polygon(12% 0, 100% 0, 100% 100%, 0 100%)`
   so the left edge slants 769.6 → 700 (the diagonal brand device). Its bottom (290) sits 78px above
   the title band, which is what keeps the white-on-purple contrast guarantee true.
   A hairline at 769.6,0 → 700,290 echoes the same edge (the cover's only graphic gesture).

SLOTS: name → limit → what is good / bad.


- `title` → ≤15 words, ≤2 lines. Measured: the 104-char placeholder fills exactly 2 lines at width 1152 (≈52 chars/line, 38px bold, −0.5 tracking). So the honest ceiling is ~15 words / ~104 chars. GOOD: a claim with a number and a scope ("Reliable Connectivity Adds $1,920¹ a Year in Household Value Across Essential Activities"). BAD: a topic label ("Connectivity study"). If it runs to 3 lines, the number is doing no work — cut, don't shrink.
- `kicker` → 1 line, ≤50 chars, ≤5 words. GOOD: program + market ("Consumer Value Research — Australia"). BAD: a sentence or a stack of 3 lines = kicker wall.
- `as-of` → 2 lines, ≤28 chars each. GOOD: fieldwork date (bold) then published date. BAD: "Confidential — draft for discussion" boilerplate as the first line.
- `lede` → 2 lines, ≤200 chars. GOOD: what the study separates / what it proves. BAD: restating the title.
- `note` → 1 line, ≤185 chars. GOOD: sample size, fieldwork window, weighting, confidence. The `sup 1` here must match the `sup 1` in title/lede.
- `commission-mark` → label ≤22 chars, lockup ≤14 chars. Client, not the authoring firm.
- `firm-mark` → 1 word, lowercase. Replace text only; keep size and corner.
- `visual` → 1 duotone image, purple-tinted at 55–70%, subject kept out of the lower-left. No photo collage.

FILL:

1. Title: edit `h1.title`. Keep `<sup>1</sup>` only if the claim is footnoted. 3 lines → shorten text (see gate).
2. Kicker: edit the second `<span>` inside `.kicker`; the first `<span class="chip">` is brand chrome.
3. As-of: `.meta` → `<b>Fieldwork March 2021</b><br>Report published August 2021`.
4. Lede: edit `p.lede`; keep `<sup>1</sup>` where the sample is cited.
5. Footnote: edit `p.note`. If the claim has no methodology claim, delete the `sup` markers in title/lede AND this line together — never leave a dangling marker.
6. Photo: replace the `<svg>` inside `.visual` with one `<image>` (data URI, so the file stays request-free) keeping `.visual`'s clip and the slant. Or delete `.visual` entirely for a pure-typographic cover (the Accenture-family variant). Keep the photo above y 290.
7. Firm mark: `.firmmark .word` → your firm's word (lowercase). `.chev` is a right-pointing chevron path (`M5 2 L14 8.5 L5 15`); replace the `d` if your brand mark differs, keep the 20×17 box and the bottom-right position (right 64 / bottom 26).
8. Commissioning mark: `.commission .lockup` → client name; swap the concentric-circle `<svg>` for the client's real mark.
9. Recolor: change only the `:root` tokens. Single hue + lightness steps, grey reserved for "the alternative" (never a second hue for a category). The KPMG variant (blue field, logo top-left, full-bleed photo) is already written out in the CSS comment block above the `.stage` rule — swap those seven tokens and make the three layout edits listed there.

VERIFY: every number below was measured on the rendered file, not asserted. Checklist:

- [ ] Title gate: 15 words / 2 lines at the cap. Placeholder passes; your text must.
- [ ] Contrast against the brightest field the text can sit on (#6E00C9): white `--ink` 8.38:1, `--gray-1` 6.46:1, `--gray-2` 4.70:1, `--tint` 6.26:1. On the deep field end (#2E0B66) white reads 15.49:1. All ≥ 4.5:1. Re-run this check after any token swap — the rule is that the gradient stops at `--field-2` for exactly this reason.
- [ ] One emphasis color, ≤2 hues total: violet family + achromes. Grey only ever means "the other thing".
- [ ] Photo never enters the title band: visual bottom 290 < title top 368.
- [ ] Footnote contract: `sup 1` appears in title/lede and in `.note`, once each.
- [ ] No page number (the source decks' covers carry none — the as-of stamp takes that role; page numbers belong on content pages).
- [ ] Self-contained: `grep -o -E "https?://" index.html` returns nothing (0 hits) and `grep -o -c "<script\|<link\|<img\|<iframe"` returns 0. File is 14,009 bytes, inline CSS + inline SVG only.
- [ ] Scaling: `html { font-size: min(100vw/1280, 100vh/720) }` makes 1rem = 1 stage px, so the layout is identical at 1280×720 (scale 0.879 in that headless run), 1440×900 (1.125) and 1920×1080 (1.379); slot coordinates were re-measured at all three and did not move.
- [ ] Fonts: the real display face on the nbn work is a single humanist/geometric sans (Avenir-like, the nbn house type) with no serif or mono, and hierarchy done by weight alone. The stack `"Helvetica Neue", Arial, Liberation Sans` is the honest stand-in, not the brand's face. The KPMG review does not name a typeface — check the actual PDF before claiming a KPMG font here.

DON'T:

- Don't use a topic title ("Connectivity Research 2021") — the corpus cover titles are claims with a number.
- Don't let the photo grow into the title band; white-on-photo at that size is where contrast dies. The source deck's own weak tail was purple-on-purple low-contrast fills.
- Don't stack a kicker wall (3+ lines of eyebrow text), don't run 6pt footnotes, don't spray ™ symbols.
- Don't add a second hue for category coding; distinction rides on lightness steps, not rainbow.
- Don't add amber/yellow glow gradients behind photography (dated, flagged in the review).
- Don't leave the digital-PDF play button / video control on the cover (a KPMG artifact, not a layout decision).
- Don't shrink the title to fit a 3-line story; shorten the claim.

SOURCE: extracted from the live renders of both covers, not from the text reviews alone:
`/home/nathan-white/new projects/deck-research/sw_pages/accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o/pg-01.png`
and `/home/nathan-white/new projects/deck-research/sw_pages/kpmg__kpmg_kpmg_2021_ceo_outlook_2021/pg-01.png`
(cover = page index `p00` in the per-deck slides CSVs, `pg-01.png` on disk). Analyzed in:
`reviews/accenture__accenture_the_nbn_effect_how_the_nbn_network_adds_value_to_o.md` (color section: deep banded purple ≈#6E00C9–#7B1FF0, darker field ≈#3C0A80–#4B0E8F, mid violet #8E24EA/#A45CF0, lavenders #E7D9F8/#D9C6F4, greys #7D7D7D/#B8B8B8; p00 anatomy, footer contract, duotone photo note) and
`reviews/kpmg__kpmg_kpmg_2021_ceo_outlook_2021.md` (navy #00338D, azure #00AEEF–#00B0F0, duotone navy #001E3C, one-hue-per-section mapping, cover description "full-bleed duotone photo, logo top-left, left-aligned title stack"). Spec item: `TEMPLATE_SPEC.md` group A, item 1.
