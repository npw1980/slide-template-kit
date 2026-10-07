# quote-visual-humor-still-checks — MANUAL

The movie-still joke page: a reference tag as the kicker, one witty claim title, a photograph
bleeding down the LEFT edge, and the argument carried entirely by three check-marked takeaways in
the right column. No chart, no legend, no boxes. The humour is the pairing of a pop-culture frame
with a straight-faced consulting claim; the checks are what keeps it a business page instead of a
meme.

## WHEN
- When one image says the "so what" better than three bullets would: an unexpected reference (a
  heist film, a sports photo, a historical painting) made to argue a serious point. Classic on
  innovation / competition / "read the room" pages in firm decks that want warmth without losing
  the claim.
- Use when the takeaway count is 2–4 short items and you have NOTHING to plot. If you have numbers,
  take the chart-card templates instead — this page cannot hold an exhibit.
- Evidence: corpus S0009 (`catalog_1-20.csv`, archetype "humor text plus still", device "movie still
  joke slide", layout "photo left; checks right", typography "blue checkmark callouts"), page 9 of a
  Firms Mazars / forvs mazars deck. There is no `reviews/*.md` entry for that deck, so nothing about
  the palette comes from a review — see SOURCE.

## ANATOMY (px on the 1280×720 stage)
1. **Kicker** — (64, 44), 13px bold, tracking 1.1px, uppercase, gray-2. `p.kicker`.
2. **Claim title** — block starts (64, 66), width 700, two `<span class="l">` lines at 31px bold
   ink. The photo's top edge is at y=176, so a third title line collides — do not add one.
3. **Photograph** — `figure.still` at (0, 176), 756×452. Bleeds to the canvas left edge; 1px
   `--rule` along its bottom. Two chips sit inside it (`.credit` bottom-left, `.stamp` bottom-right,
   both `position:absolute`).
4. **Check column** — an `<svg class="checks" viewBox="0 0 1280 720">` overlaying the whole stage.
   Each takeaway is one `<g class="check" transform="translate(X,Y)">` with X=**836** fixed and
   Y = the item's block top. Inside a group, local coords: plate circle (16,14,r17), tick polyline,
   lead text x=46 (first line y=21, second line y=49), sub text x=46 (y=47 when one lead line, y=75
   when two). Current block tops: **206, 306, 426** — i.e. 100px pitch for a 1-line item and 120px
   for a 2-line item.
5. **Footer** — `p.source` (64, bottom 26); `p.pagestamp` right-anchored (1216, bottom 26);
   `p.mark` right-anchored (1216, bottom 46).

## SLOTS
- **kicker** — the reference, ≤26 chars: "THE DEPARTED · 2006". Good: title + year so the joke is
  identifiable. Bad: a sentence, or a joke-only kicker ("funny picture!") that names nothing.
- **claim title** — ≤15 words, ≤2 lines, ≤58 chars/line. Must be a **claim** that the checks
  support ("Organized crime is strategic because…"), not a caption of the photo ("Two men talking").
  The second half carries the argument; the photo is the wink, not the thesis.
- **check lead** — 1–2 lines, ≤30 chars/line, 21.5px bold accent. Good: "Looks outside the /
  organization". Bad: a full sentence — that is what the sub line is for.
- **check sub** — one line ≤46 chars, 13.5px gray-2. Good: the 6-word gloss that makes the lead
  defensible. Bad: 2 lines; the block pitch then breaks the column rhythm.
- **still credit** — the film/subject + year, ≤44 chars. It is a caption, not a joke.
- **source line** — ≤95 chars, states where the still is from and what analysis is behind it.
- **page stamp** — "N | SECTION". **mark** — the firm wordmark placeholder.

## FILL (step-by-step)
1. Replace kicker, both title lines, the three lead/sub text pairs, the still credit, the source
   line, the page stamp and the mark text. All are plain `<text>`/`<p>` content; nothing is
   computed.
2. **Drop the photograph in.** Delete every child of `<figure class="still"><svg …>…</svg>` and put
   `<img src="frame.jpg" alt="…">` in its place, or keep it a single inline SVG if the deck must be
   network-free. The chips need `position:absolute` (already in the CSS) to stay pinned; if you
   replace the svg with an `<img>`, keep the two `<span>` chips. If the still is not 5:3, change
   `height` on `.still` (the svg clips via `preserveAspectRatio="xMidYMid slice"` either way).
3. **Add a takeaway (3 → 4):** copy the third `<g class="check">` block, set the four tops to
   **188, 276, 364, 452** (88px pitch, block vertically centred against the photo, which spans
   176–628) and shrink `lead` to 19px / `sub` to 12.5px. Reflow rules: the lead column width is
   1216 − 882 = 334px, so at 19px a lead wraps at ~28 chars — keep one line per item. Do not go past
   4 items: below the 4th the column runs off the photo's bottom edge.
4. **Remove a takeaway (3 → 2):** delete one group and re-space the survivors to 88px pitch
   centred on y=402: for 2 items use tops **290, 378**. With 1 item, put it at y=384.
5. **Recolour.** The single emphasis hue is `--accent` (#1F7CCE, read off the frame). Check leads,
   tick strokes and the plate fill (`--accent-soft`, a light tint of it) all derive from it, so
   changing `--accent` + `--accent-soft` in `:root` recolours the whole column. Keep the title and
   body in grays: any hue added to the title competes with the checks and the page stops reading as
   one argument.
6. **Photo tone:** `--photo-1/2/3` are placeholder-only grays; they exist so the default render
   cannot accidentally carry a second hue. Set them to zero/omit them when the real still lands.

## VERIFY
- Title is a claim, ≤15 words, ≤2 lines, and does not touch the photo (photo top = 176).
- Source line bottom-left, page stamp bottom-right, firm mark present.
- One emphasis hue (blue) + grays; no second hue anywhere including the photo placeholder.
- Text contrast: leads #1F7CCE on white = 4.36:1, which passes because they render ≥19px bold
  (large-text threshold 3:1). Sub lines and source must be gray-2/gray-3 on white — never render
  sub-line-size text in the accent.
- Check column vertical rhythm: 88 or 100/120px pitch, tops inside 176–628.
- Squint test: title + three leads should read as a sentence with no photo.

## DON'T
- Do not caption the photo as the thesis. The claim belongs in the title; the still is the wink.
- Do not add SmartArt chevrons, numbered boxes or a legend — three checks and three ticks is the
  whole system, and furniture is what kills the joke's timing.
- Do not run 5+ checks, or two-line leads on every item; the column collides with the photo's bottom.
- Do not use emoji ✓ / ✗ glyphs — they render inconsistently across viewers. The tick is a stroked
  polyline on purpose.
- Do not let the still be decorative-only: pick a frame whose content actually maps to the claim
  ("thinks outside the org chart" → the frame, not a random scene).

## SOURCE
- Corpus page: S0009, `catalog_1-20.csv` line 10 — content / "humor text plus still" / charts none /
  typography "blue checkmark callouts" / colour "photo tones plus blue checks" / layout "photo
  left; checks right" / device "movie still joke slide". Image:
  `corpus/pdfpages/4890_49c9_a1ee_77b0f75a86c7_St_-09.png` (page 9 of the deck; also frame 9 of
  `corpus/sheets/sheet_001.jpg`).
- The rendered frame is a Firms Mazars / forvs mazars page (© 2020 line, "forvs mazars" mark
  bottom-right). No `reviews/*.md` exists for this deck and no `catalog_*.csv` row names the firm, so
  the blue is taken from the frame itself: mean RGB of its blue callout pixels (31,124,206) =
  **#1F7CCE**. That is a measurement, not an invented brand hex.
- Fonts: the firm deck is a plain office sans; `--font-display` (Helvetica Neue/Arial, tight on the
  title) stands in for it, body is the standard Arial/Calibri stack.
- Layout numbers (photo 0→756 × 176→628, check column 836→1216) were measured from that same frame
  with a pixel occupancy scan, then redrawn on the kit's 1280×720 grid.
