# framework-named-five-forces — Porter's Five Forces (1280×720)

WHEN: Industry-structure page drawn by hand, not SmartArt: four force panels around a central
competition-intensity disc, each force carrying a LOW/MODERATE/HIGH assessment and one line of
evidence. This is the page that says "we named the framework and committed to a rating on each
force." Source form: Umbrex template deck S1765 "Template — Porter's Five Forces"
(`corpus/sheets/sheet_177.jpg`, ceil(1765/10)=177, row 1 col 5), discipline from
`reviews/umbrex_patterns.md` §9 (four corners + central intensity, "Low/moderate/high" prompt
lines). For a generic 2×2 (no named framework), use `matrix-2x2-scenario` / `matrix-2x2-panels`.

ANATOMY (slot map, stage px; `1rem = 1 stage px` via the html rule):
1. `kicker` — x64 y36, 12/1 bold uppercase ls .15em, `12 | Market structure — Porter` (numeral in accent).
2. `title` — x64 y58, width 1152, 30/38 bold navy, 2-line box.
3. `lead` — x64 y143, 13/18 bold, one sentence naming the verdict; `<sup>1</sup>` for the methodology claim.
4. `force-1` — SVG group, translate(64,168), local rect 516×196. Top-left corner (threat of entry).
5. `force-2` — translate(700,168), 516×196. Top-right (buyer power). Binding corner: rating in accent.
6. `force-3` — translate(64,404), 516×196. Bottom-left (supplier power).
7. `force-4` — translate(700,404), 516×196. Bottom-right (substitutes).
8. `center` — SVG group translate(640,387): disc r104, 3px navy ring + r112 hairline halo, white fill; drawn AFTER the four panels so it overlaps their inner corners (the figure's whole grammar).
9. `foot-src` — bottom-left x64, 9.5 gray-3, superscripted; `foot-page` — bottom-right x1216, 10 bold `12 | STRATEGY`.
Panel grid: cols x 64 / 700, rows y 168 / 404 — the cross-gutters are 120px wide, which is what lets the center disc sit on top without burying any panel text.

SLOTS:
- `title`: action title. ≤15 words / 2 lines at 30/38 (gate). Good: names both the binding forces and the verdict. Bad: "Five Forces Analysis" (topic title, zero information).
- `lead`: ≤16 words one line; must state how many forces bind and what the assessment rests on. Never a kicker-wall second paragraph.
- per-force `fhead` (15.5 bold): exact force name — "Threat of new entrants", "Bargaining power of buyers", "Bargaining power of suppliers", "Threat of substitutes". 28 chars max before wrap risk.
- per-force `frate` (13 bold caps): exactly one of LOW / MODERATE / HIGH. It is an assessment, not a hedge — "LOW-TO-MODERATE" is forbidden (that's the prompt text from the blank template, keep it only in a template you leave unanswered).
- per-force `fnote` (11.5 gray): max 2 lines × ~48 chars of *evidence* (a number or mechanism), not a restatement of the rating.
- `center.chead` / `crate` / `cnote`: the rivalry disc — name (2 lines), one rating word (accent, 16), one evidence line (2 lines × ~34 chars).
- `foot-src`: full method string with dates; `foot-page`: `NN | SECTION`.
- Dimming rule: a force you did not assess gets `fill:var(--gray-5)` on its rect and `fill:var(--gray-3)` on all its text — say in the title that it was not assessed, don't fabricate a rating.

FILL:
1. Titles/labels: replace the `<text>` contents in `h1.title`, `.lead`, `.foot`. The claim title keeps the gate — if it breaks 2 lines, shorten the claim, never shrink the font.
2. Per-force copy: each force is one `<g id="force-N">`. Inside, lines live at fixed local baselines y=34 (head), y=66 (rating), y=94/110 (evidence ×2). Edit only the text; the rect and all coordinates stay.
3. Swap which force is binding: toggle the `bind` class on the `.frate` of that group (`.frate` → `.frate bind`). The accent must appear on ≤2 force ratings + the center — never all five (then it stops meaning "binds").
4. ADD/REMOVE/RESHAPE NODES:
   - A corner panel = one group; moving one corner = editing its single `transform="translate(x,y)"`. Corner anchors are the four values above; keep panel size 516×196 so gutters (120 × 40px) don't collide with the disc (dia 208 at cx 640 cy 387).
   - A 6th force (complements / government, as some Porter variants add) cannot share this frame honestly: shrink panels to 510×176 and use 3 rows (y 160 / 368 / 576 — bottom row h=124) or drop to 3 corners + disc. Do NOT overlap text with the disc: a panel overlaps only its blank inner corner.
   - Inner-corner clearance: the disc (dia 208 + halo) overlaps the inner corner of every panel, but text must stay 130px clear of it. force-1/2/3 keep x=24 because their inner corner faces AWAY from the disc; force-4 is the mirror case — its heading/rating/notes all sit at local x=150. If you move a panel so its blank corner no longer faces the disc, move that x-offset back to 24.
   - Rename a force (Five Forces → PEST/PESTLE boxes, etc.) is the ONLY safe node swap: text-only, same geometry. For anything needing arrows or weights between nodes, this is the wrong template.
   - To leave a corner blank-but-present (unexamined branch), keep the group, gray it per the dimming rule above.
5. Recolor for another accent: change `--accent` only (e.g. PwC red #D60A2C). `--accent-2` does not exist here by design — there is nothing to wash out. Keep `--ink` navy; the ring stays ink, never accent.
6. No chart-series arrays here — all data lives in text nodes.

DIAGRAM RECIPE:
- Scale: qualitative 3-point assessment (LOW/MODERATE/HIGH), same word list on all four panels + disc — encoding is lexical (the word) plus color (accent = binds), no numeric mapping.
- Emphasis rule: exactly one hue; non-binding forces render in gray-2; binding forces render their rating in accent; everything structural (panels, rings, text) is ink/rule/gray-4.
- The disc must float on top of the panels (SVG order: force-1..4, then center) — flat-quadrant behind-disc rendering is the tell of a drawn-by-SmartArt version of this figure.
- Rating word sits above evidence lines in every panel; never stack rating + note without the y-rhythm 34/66/94/110.

VERIFY:
- [ ] Title ≤15 words / ≤2 lines (the current placeholder is 11 words).
- [ ] Every force carries exactly one LOW/MODERATE/HIGH — none missing, none hedged.
- [ ] Accent on ≤2 force ratings + disc rating only; contrast 6.3:1 for accent text on white.
- [ ] Source line present bottom-left with fieldwork dates + sup marker on the methodology claim.
- [ ] Page running head `NN | SECTION` bottom-right; exactly 2 hues (ink navy + one accent) + grays.
- [ ] Center disc drawn after the four panels and its text ends before r104.

DON'T: topic titles ("Five Forces Overview"); the blank template's own "Low, moderate, or high"
prompt text shipped verbatim (the corpus template literally says that — a built deck commits to
one word per force); ratings without evidence lines; 5-accent rainbow panels; arrows between
corners (none in the source grammar); a sixth force bolted on without fixing the grid.

SOURCE: `catalog_umbrex.csv` S1765 (arch "Porter's Five Forces", prompt-line form noted in
`reviews/umbrex_patterns.md` §9) — image read in `corpus/sheets/sheet_177.jpg`
(ceil(1765/10)=177, zero-padded, row 1 col 5 of the 5×2 sheet). Palette: umbrex house navy
~#1F2A65/#1F2A4F + teal highlight (#00D4C8, too neon for text — normalized to house
`--accent #2251FF`) per `reviews/umbrex_patterns.md` §palette line 29. Fonts: deck faces unknown/
unlicensed — Helvetica Neue / Arial stacks stand in.
