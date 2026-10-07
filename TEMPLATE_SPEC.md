# HTML Slide-Template Kit — Build Spec

Read this before building any template. The evidence base for every rule here: `DESIGN_PLAYBOOK.md` (rules + confidence labels), `reviews/*.md` (per-deck teardowns), `catalog_*.csv` (per-slide cataloging).

## Output layout (create exactly this)

```
deck-research/html-templates/
├── README.md                  # index table: template id, archetype, source firm evidence, status
├── manifest.json              # [{id, title, archetype, path, source, slots:[names]}]
└── <template_id>/
    ├── index.html             # self-contained, ONE file, no external requests
    └── MANUAL.md              # the instruction manual (schema below)
```

## Template rules (every index.html)

- Stage: 1280×720 fixed stage, scaled to viewport with a CSS transform wrapper; everything laid out on that exact canvas.
- Self-contained: inline CSS, inline SVG for diagrams/charts, zero CDN/network calls, zero JS unless the interaction is load-bearing (none is, for slides).
- Fonts: no webfonts. Use stacks that degrade honestly:
  - display/titles: `"Helvetica Neue", Arial, sans-serif` with tight letter-spacing on big text (or Georgia serif stack where the source is an editorial system like PwC);
  - body/axis/footnotes: Arial/Calibri stack.
  - Every MANUAL must state the firm's real font (e.g. McKinsey Bower/GT) and what the stack stands in for.
- Data: realistic placeholder content that demonstrates the slot at its worst plausible fill (2-line claim title, three-digit percentages, long-ish source string) — lorem ipsum is FORBIDDEN; a template must not hide overflow behind fake brevity.
- Color: tokens as CSS custom properties at `:root` with the playbook's roles: `--accent` (emphasis), `--ink` (text), `--gray-*` (secondary + "the rest"), `--rule` (hairlines), `--bg`. Non-accent series render in gray ramp + one lightness of accent.
- Footer anatomy on every content page: source line bottom-left, `1 | SECTION` running head or page number bottom-right, superscript footnote markers where methodology claims exist.
- MBB gate that the render itself must pass: claim title ≤ 15 words and ≤ 2 lines (if the placeholder breaks the gate, the template is wrong — fix the slot sizing, not the text).

## MANUAL.md schema (the actual deliverable — the "instruction manual")

```
# <Template id> — <Title>
WHEN: 2-3 lines, what this template is for, which firm evidence it comes from (deck name + page ref).
ANATOMY: numbered slot map — 1 title, 2 kicker, ... — with px coords for each slot on the 1280×720 stage.
SLOTS: one line per editable slot: name, max chars/lines, what makes it good/bad (e.g. action title = quantitative claim, not topic).
FILL: step-by-step build instructions: which text nodes to replace, which SVG numbers to swap (chart series arrays: give the exact array/attr), which tokens to recolor for a different accent.
CHART RECIPE (chart templates only): how the figure encodes data — scales, label placement, emphasis rules, the "one accent + gray" rule, axis/unit rules.
VERIFY: checklist — title gate (≤15w/2 lines), source line present, one emphasis color, no more than N hues, contrast (text on accent must clear 4.5:1), page number.
DON'T: the failure modes seen in the corpus (e.g. topic titles, 10-hue pies, chart-junk legends, kicker walls of text).
SOURCE: where this was extracted from — firm, deck filename, page number(s) in sw_sheets/ or corpus sheet, and which review file analyzed it.
```

## Template inventory (24 templates, 3 groups)

### Group A — deck spine masters
1. `cover` — full-bleed cover, firm-mark bottom-right (Accenture violet / KPMG blue variants in comments)
2. `exec-summary-at-a-glance` — SCQA opener, numbered takeaways column (McKinsey "At a Glance")
3. `agenda-roadmarkers` — TOC reused as divider with you-are-here marker (KPMG nav-strip variant)
4. `section-divider` — full-bleed "N. SECTION" with progress marker
5. `content-action-title` — THE core page: 2-line claim title slot, 70% canvas exhibit, so-what kicker box, source line
6. `two-column-lead` — lead-in column + body exhibit (McKinsey kicker-rail pattern)
7. `pull-quote` — interview / expert quote page with attribution block (KPMG quote-panel)
8. `methodology` — label title, sample/fieldwork/N table
9. `data-appendix` — dense table page with per-column stats discipline
10. `closing-contacts` — regional contacts + back-matter (PwC 4-col close)

### Group B — chart-card templates (one accent + gray ramp, value labels on elements)
11. `hbars-end-labels` — horizontal bars, % labels on bar ends, one highlighted bar
12. `paired-bars-deltas` — before/after or 2021/2022 pairs with delta pills
13. `stacked-100-columns` — 100% stacks with segment share labels + respondent sub-row (n=)
14. `small-multiples-lines` — 3–6 sparkline panels, shared scale, emphasis line in accent
15. `donut-claim-center` — donut with the argument sentence centered (not a bare %)
16. `waffle-matrix` — dot/waffle percentage grid, 1 dot = 1%
17. `heat-matrix` — 5-step heat ramp table/heatmap (Advanced→Developing ladders)
18. `from-to-bridge` — waterfall / from-to with delta markers

### Group C — content-diagram patterns (custom-drawn, not SmartArt)
19. `custom-2x2` — real-axis quadrants with plotted points + callouts (NOT static 2x2 labels)
20. `issue-tree` — hypothesis tree, node numbering, dimming rule for unexamined branches
21. `process-flow-numbered` — 3–5 step chevron/numbered flow with owners + outputs row
22. `timeline-milestones` — dated roadmap with milestone chips + today-marker
23. `persona-cards` — survey persona row (photo circle + stats + verbatim)
24. `org-hub-map` — capability hub / org map, custom SVG with real labels

## Build notes

- Extract every template from what the reviews actually praised. Provenance examples: Accenture NBN effect (claim-band title system, KPI numerals, donut-with-claim) — `accenture__accenture_the_nbn_effect...` p03-p09; EY Risk Management (takeaway page + Figure-N caption convention) — `ey__ey_risk_management...`; KPMG AI report (nav strip, donut/progress rows) — `kpmg__kpmg_ai...`; PwC EV sales (small multiples, persona cards) — `strategy_electric_vehicle...`; Accenture net-zero (deliberate anti-SmartArt, prose-forward claim pages).
- If a template needs a real palette anchor, cite the hexes from the matching review md (they list them), don't invent.
- The MANUAL is the point. A reader must be able to turn the template into their deck's page without opening index.html.
