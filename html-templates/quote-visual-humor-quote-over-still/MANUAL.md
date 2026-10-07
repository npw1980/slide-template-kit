# quote-visual-humor-quote-over-still — MANUAL

One line of dialogue, set over a full-bleed film still, with an attribution under it and nothing
else. The photograph runs edge to edge, a scrim keeps the type readable, and the joke is that the
speaker is a fictional character while the page's argument is completely serious. This is the
quietest page in the kit: if the line needs a body paragraph, the line is wrong.

## WHEN
- A voice-of-customer or leadership-voice page where a single quoted sentence lands harder than a
  paraphrase: expert interview, customer verbatim, a line from a film/sport/history that frames the
  section. Usually a section opener or a closing page — not a content page.
- Use when you have one sentence and one face. Two quotes = two pages, or use
  `quote-visual-humor-still-checks` (which is the multi-point variant of the same device).
- Evidence: corpus S1089 (`catalog_101-134.csv` line 90 — content / "quote-slide" / charts none /
  typography "bold-italic-quote-center" / colour "blur-bokeh-photo-bg" / layout
  "full-bleed-photo-with-center-quote" / device "quote over movie still"). The catalog also notes
  S1092, a title-slide variant of the same device ("Quotes And Leadership Lessons From Toy Story").

## ANATOMY (px on the 1280×720 stage)
1. **Photograph** — `figure.still` is the whole canvas: (0, 0) 1280×720, svg clips with
   `preserveAspectRatio="xMidYMid slice"`. One chip inside: `.stamp` bottom-RIGHT (1186 right edge,
   bottom 12), `position:absolute` — bottom-left is reserved for the caption line.
2. **Scrim** — `div.scrim` covering the canvas, flat `--scrim` (rgba(9,14,18,.50)) plus a soft
   centre band via `::after` (top 150, height 420, fades in/out — never a hard-edged box).
3. **Kicker** — (64, 56), 12.5px bold, tracking 2.1px, uppercase, ink-dim.
4. **Quote** — `blockquote.quote`, box (190, 286) width 900, centred, 52px bold italic, 1.2 line
   height, two `<span class="l">` lines. Real quotation marks are typed into the text (opening
   `“`, closing `”`), so no decorative quote glyph is needed.
5. **Rule** — `div.rule`, 84×1px at (598, 452), centred, `--accent-on-dark`. The only accent on the
   page.
6. **Attribution** — `p.attrib`, full-width centred, top 470, 20px italic, ink-dim.
7. **Footer** — `p.mark` (1216, bottom 50); `p.caption` (64, bottom 30); `p.pagestamp` (1216,
   bottom 30).

## SLOTS
- **kicker** — ≤24 chars: "IN THEIR OWN WORDS". Good: a section-ish label. Bad: the page's thesis —
  the quote IS the thesis.
- **quote** — 1 sentence, ≤15 words, ≤2 lines, ≤38 chars/line. Must be spoken by someone with a
  name (real or fictional) — the attribution slot requires a speaker. Bad: a paraphrasable
  platitude ("quality matters most") or a two-clause thesis; that is a claim title, and claims have
  their own template.
- **attribution** — "— Firstname Lastname" plus (optionally) a two-word aside, ≤38 chars total.
  The aside is where the dry humour lives ("— Buzz Lightyear, toy, self-appointed"). Keep the em
  dash.
- **caption / still credit** — film or subject + year, ≤80 chars, states where the frame is from.
- **page stamp** — "N | SECTION". **mark** — firm wordmark placeholder.

## FILL (step-by-step)
1. Replace kicker, both quote lines, attribution, caption, page stamp, mark. The quotation marks
   are characters, not a pseudo-element — keep them if you replace the text.
2. **Drop in the real still.** Delete every child of the still `<svg>` and put
   `<img src="frame.jpg" alt="…">` inside the `figure` (set `left:0; top:0; width:1280rem;
   height:720rem; object-fit:cover` — or keep the existing `slice` clipping by giving the img
   `object-fit:cover`). If the source frame is not 16:9, crop, do not letterbox: the page's whole
   trick is edge-to-edge.
3. **If the speaker is off-centre:** move the subject mass in the placeholder by editing the two
   `ellipse` centres (cx 835/815) and the floor rect; if you need the type over a busy area, raise
   `--scrim` alpha (see step 5), don't add a box.
4. **Resize the quote block (the slot that actually stretches):**
   - 1 line: keep font 52px, set `.quote` `top:318rem`, delete the second `<span class="l">`;
     move `.rule` to 484 and `.attrib` to 502 so the block stays centred on 402.
   - 2 lines: current build (top 286, rule 452, attrib 470) — this is the calibrated default.
   - 3 lines: drop size to **46px**, set `.quote` `top:252rem`, keep `.rule` 452 / `.attrib` 470
     unchanged only if you also drop line-height to 1.14 — at 46/1.14 a 3-line block ends at ~
     434, so the rule still clears. Long quotes go to 3 lines max; past that the still has no room
     to breathe and you should cut the quote.
   - The block never widens past 900: at 52px, 900px is ~38 chars/line, so widening means
     shrinking, not gaining.
5. **Legibility dials.** `--scrim` (flat, .50) and `--scrim-band` (centre, .32) are the knobs. If
   white text fails on a bright frame, raise both; do not add a second scrim layer, a border, or a
   blurred box — a visible panel is the tell that gives away "template".
6. **Recolour.** The page takes one hue. On a dark photo the accent must be a light lightness, so
   the rule uses `--accent-on-dark` (#79B6EE — a lightness of #1F7CCE), and `--accent` is otherwise
   unused; all type is white/ink-dim. If the frame is light (sky, product shot), raise the scrim
   rather than darkening the type.
7. **Do not put the accent inside the photograph** (no coloured duotone). The grayscale ramp
   `--photo-1/2/3` exists to keep the default render one-hue.

## VERIFY
- White quote on the scrim: with `--scrim` at .50 over the placeholder ramp the contrast is ≈13:1;
  re-check after the real frame lands — text must clear 4.5:1 over every glyph it crosses.
- One emphasis hue: `--accent-on-dark` used exactly once (the rule). No second hue.
- Quote ≤15 words / ≤2 lines (or 3 lines at 46px), real quotation marks present, attribution has an
  em dash and a named speaker.
- Still is truly full-bleed: no white border, no letterbox, no drop shadow around the frame.
- Source/caption bottom-left, page stamp bottom-right, mark present. No chart, no legend, no bullets.
- Squint test: at thumbnail size you should see an image plus a white two-line block and nothing
  else.

## DON'T
- Do not add a "so what" paragraph, kicker wall, or three takeaways under the quote — that is the
  other template. The page must be explainable as "picture + one line".
- Do not pull a quote from a source you cannot credit; the caption slot is mandatory, which is the
  honesty gate for this device.
- Do not use a stock-photo placeholder and call it a still. Use the actual frame; this template
  only works if the audience recognises it.
- Do not stack a coloured translucent box behind the text — the centre band is soft-edged on
  purpose. A visible box reads as a text box, not as atmosphere.
- Do not run two of these back to back in one deck.

## SOURCE
- Corpus page: S1089 — `catalog_101-134.csv`, content / "quote-slide" / "bold-italic-quote-center" /
  "blur-bokeh-photo-bg" / "full-bleed-photo-with-center-quote" / "quote over movie still".
  Image: `corpus/images3/slideuplift_0025_91a72c04.jpg` (2400×1200 frame, tagged
  `slideuplift`; kind `bing` in `slides_manifest.json`, i.e. a web-sourced reference, not a firm
  deck page).
- No `reviews/*.md` or firm attribution exists for this page, so the palette is kit-default:
  one hue (`--accent` #1F7CCE, the value used across this kit's families) with the light lightness
  used on dark ground. The grayscale photo ramp is the playbook's one-accent rule applied to a
  photograph.
- The source frame is 2:1; geometry was re-derived for 16:9 — the quote block sits centred on the
  optical middle of the stage (y≈402) with attribution ~15% below, which is where the reference's
  own centred quote/attribution pair lands proportionally.
- Fonts: the reference is bold-italic display sans; `--font-display` (Helvetica Neue/Arial) stands
  in for it. No webfonts.
