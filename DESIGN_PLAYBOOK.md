# Consulting Deck & Market-Research Report Design Playbook

Extracted from the visual corpus (1,819 master-corpus slides cataloged page-by-page + 3,043 reviewed firm-deck pages across all 75 archived decks), three expert-team research tracks (evidence synthesis, product trends, build-vs-buy), and per-deck reviews of real firm deliverables downloaded from public archives. Review method: contact sheets built from downloaded PDFs and image harvests, every slide cataloged for archetype, chart types, typography, color, and layout, with an explicit SMARTART-GENERIC flag where a page is just default PowerPoint shape art with filler text (per Nathan: those aren't high-quality templates; skip them).

This is the synthesis. Per-slide evidence lives in `catalog_*.csv`, `reviews/*.md`, `slides_manifest.json`.

---

## 1. What "McKinsey style" actually is — and isn't

The Google Images result that started this search is mostly an SEO artifact, not a style. Roughly four in five hits under "mckinsey style consulting slide deck" are marketplace recreations — SlideUpLift openly sells "recreations of the twelve slide types." Real McKinsey/BCG/Bain decks run on internal systems nobody sells. The style that is real is a **page system**, not a look:

- **Action titles are the defining convention.** Every content page carries a full-sentence takeaway as its title: ≤15 words, ≤2 lines, active voice, ideally quantitative. Test: read only the titles, and they should form the argument. Topic titles ("Market Overview") mark amateur work. Source: deckary guide 2025, slideworks how-to, corroborated across practitioner threads. Practitioner lore, not firm doctrine.
- **Parallel grammar across the deck.** Same structure and tense for every title.
- **One idea per page, every page.** Data on most pages, sources on all pages.
- **Per-page "so what" kicker** — a boxed implication under the exhibit, not optional.
- **TOC re-inserted as section road-markers**; cover → agenda → "At a Glance" exec summary with SCQA opener → 40–60 body exhibits → recommendations → appendix.
- **Chart hygiene:** direct value labels in/on bars, one emphasis color plus gray, source line bottom-left, no 3D, no clipart, axis units stated.

An independent review of a real 39-page McKinsey-USPS deck (2010, consultantsmind 2024) is the closest thing to a teardown of a real firm deck and confirms all of the above. Weight it above vendor blogs. Caveat: it is 16 years old; the practices may have drifted.

**Implication for our library:** build the page system (title slot sized for 2-line claims, kicker box, source-footer, road-marker dividers), and treat any specific "McKinsey template" purchase as decorative filler.

## 2. Page anatomy (the slot schema to encode in our masters)

Observed on real consulting pages (slideworks-rendered McKinsey slide + EY/Accenture decks):

| Slot | Rule |
|---|---|
| Action title | full-sentence claim, 2-line max, top-left, serif or grotesque bold |
| Date / "as of" line | top-right ghost-header style, small gray |
| Kicker / lead-in column | optional left rail framing the question |
| Body exhibit | chart or diagram, ~70% of canvas |
| So-what kicker box | boxed implication under the exhibit |
| Footnotes | superscript markers + sampling/method note, small |
| Source line | bottom-left "Source: …" |
| Footer | firm name + slide number, bottom-right |
| Section divider | full-bleed, "N. SECTION" centered, you-are-here marker |

Claim-title rule with one deliberate exception, observed in an EY ICO study: summary pages, contents, and methodology pages get **label** titles ("Executive summary", "Methodology") because their job is being a known page type, not arguing. Takeaways pages should still carry a claim.

## 3. Typography and color — documented facts, with confidence labels

Firm-specific specs are firm-specific; do not generalize one firm's guide to "consulting type."

| Firm | Documented | Source / confidence |
|---|---|---|
| McKinsey | Deep blue #051C2C + electric #2251FF + cyan accent; Bower serif display + McKinsey Sans. Bower impractical in shared decks → substitute Georgia | Identity: mckinsey.com blog 2019-02 (Wolff Olins), primary. Hexes: 3 agreeing tertiary scrapers + visual check — medium |
| **Gartner** | **The most actionable exact spec found anywhere: News Gothic Bold 14/18 titles, subheads 11/15 orange, captions 12/15 with rule above, grays 2D2D2D/464646/7D7D7D/DEDEDE, Arial+Georgia Office fallback.** 2017 internal style-guide PDF | Primary; high. Use as the model for our own written standard |
| PwC | Arial body / Georgia headers; accents #FFB600 #EB8C00 #D04A02 #DB536A #E0301E + grays | Australian VI PDF 2020, primary; high |
| BCG | Chart green ≈#29BA74 vs dark logo-green — unresolved; the "blue #0000C1" circulating in briefs is unsourced | code/tertiary; medium-low |
| Bain | Red ≈#CC0000 (±1), echoed secondary sources, no primary brand PDF | medium-low |
| Deloitte | Pentagram-built Insights system with 20+ chart/infographic templates, treated as brand; Open Sans + Verdana fallback; green-dot hexes disagree across regional toolkits | Pentagram project page primary for the system; hexes unresolved |
| EY | Yellow #FFE600 commonly cited, unconfirmed; survey decks run near-mono blue with dark data panels | tertiary; low |
| Statista | Blues #0666E5 / #82B2F2 / near-black #000913 | tertiary; low |

**Palette ruling for our own masters:** deep navy #051C2C + one accent (electric blue or the client's) + grays 2D2D2D/464646/7D7D7D/DEDEDE. One emphasis color; everything else gray. This is what real decks converge on when they're good.

## 4. What the visual review found, block by block

**Real firm decks — all 75 Slideworks-archived decks reviewed page-by-page** (Accenture, Deloitte, EY, KPMG, L.E.K., PwC Strategy&; 3,048 pages cataloged, 2,721 content): the strongest evidence, since these are actual deliverables, not templates:

- The good firm decks contain **zero filler-text SmartArt pages**. Where pages get flagged, it's Deloitte's 12-node donut rings and radial hubs (default-shape arrangements) and one nested-oval org map. High-achieving pages are chart pages: horizontal bars with end-value labels, 100% stacks, small multiples, heatmap/waffle grids.
- Accenture's net-zero research deck "deliberately avoids process-SmartArt idioms — no 2×2s, no chevrons, no donut lifecycles — which is why it reads as analysis, not framework theater." The 2×2/chevron/cycle grammar so many templates sell is a marketplace invention.
- EY's engine: dark-navy data panels floating on white, native charts inside, claim-sentence titles on evidence pages, label titles on front/back matter. A survey-report chart-card system worth porting directly.
- Accenture survey-report skeleton worth copying for MR work: numbered TOC → full-bleed section dividers (N. TITLE + index chip) → summary slide per section → data slides keyed to survey question numbers (Q1…Q16) → open-ends and verbatims last.
- Common flaws to design away in our masters: topic titles (Deloitte Tillsonburg), gray-on-gray low contrast (Accenture IAC), segment-soup pies with 10+ hues, double-punchline kicker text, dividers that eat pages without marking progress.
- Coverage is now complete: 75/75 archived decks reviewed, 3,043 pages, 2,713 content, only 12 pages SMARTART-GENERIC-flagged across every real firm deck — confirming the thesis that generic shape-art is a template-marketplace phenomenon, not a firm one. Tier verdicts (from the review md files) land overwhelmingly at B: coherent house systems, real exhibits, zero filler, but action-titles only partial — topic-label titles on setup/divider pages and over-length claims keep nearly every deck out of the A tier. Genuine outliers noted per deck (e.g. donut-only chart vocabularies, missing pagination/source lines in KPMG pulse decks).

**Umbrex block (the user-vetted high-quality source):** the honest picture is more nuanced than "high quality" — it splits into two populations (149 slides; 116 / 78% flagged SMARTART-GENERIC, 33 genuine). The flagged majority are stock "Template - <chart>" PowerPoint/SmartArt pages with lorem/Text/XXX placeholders — polished but generic by the skip rule. The real value sits in sheets 175–179: ~33 named-framework slides with authentic ex-MBB structure — hypothesis/issue trees (S1752–53), Plan Analyses table (S1754), six-box problem statement (S1786), stakeholder grid (S1787), SIPOC (S1779), Porter Five Forces (S1765), BCG/GE/Ansoff matrices (S1765–70), 7-S (S1771), profitability tree (S1775), Three Horizons (S1782), SBAR (S1744). House system is consistent and transferable: dark navy ≈#1F2A65 + teal/cyan + cornflower blue + dimming gray, white canvas, bold sans titles, universal "Your logo here / Source: / page" footer strip. Data-chart templates (waffle, heat map, 100% stacks, delta-brace clustered bars, growth curves) are well-drawn but placeholder-filled — the chart grammar ports, the pages themselves are SmartArt-class. Minor provenance noise flagged: two gallery-tagged cells, Spanish leftover labels (Rama/Hoja/Valores) on four slides, one off-palette red-ribbon slide (S1776). 15 ranked template picks in `reviews/umbrex_patterns.md`.

**Bing block:** mixed. The densest hits were 2×2 matrices with callout bubbles, parallel 3-step timelines, funnels, org charts, orange/blue value-stack pyramids, staircase journeys, commodity/differentiator chevrons — but the later harvest range degraded into stock photos and clipart (Pikachu and lizards under market queries); anything not obviously a slide layout was flagged and dropped.

**Gallery/marketplace block (slidesgo, SlideModel, SlidesPilot, sites):** nearly all title-slide archetypes and cover designs — polished device mockups, flat illustrations, photo overlays, big-type titles. Good pattern bank for covers/agendas/dividers (title placement, kicker/eyebrow, card styles, KPI rings), not for content pages. Per the skip rule, most content pages here were flagged SMARTART-GENERIC; they are not template candidates. Preview "beauty" decomposes to: one dominant palette, icon-chip consistency, generous whitespace, numbered thumbnail grids, device mockups.

## 5. Market-research report templates (report ≠ deck)

Canonical structure, confirmed by three semi-independent sources: title page → disclaimer → TOC → executive summary (findings + implications) → methodology (sample, fieldwork, N) → results by research question → discussion → recommendations → appendix (data tables, questionnaire).

The stable exhibit formula across NIQ, PwC, EY, Deloitte Insights report pages: **chart + insight box + methodology/source footnote**, on a repeating grid. Deloitte Insights is the strongest documented case of report design treated as a brand system (Pentagram, 2017). Gartner's page spec is the model for exactness.

For our shell, that means: k-dense-style spine (cover, disclaimer, TOC, exec summary, methodology, market sizing TAM/SAM/SOM, segmentation, trends, landscape, recommendations, appendix) + per-page exhibit card (title claim / chart / insight box / source line) + divider template with you-are-here marker + a Q-numbered survey-report variant (Accenture pattern) for survey-driven MR work.

## 6. Build vs buy

Practitioner consensus and this corpus point one way: the value is in **structure-first masters**, not purchased decks.

- Build (core recommendation): in-house master set — deck anatomy masters (title/road-marker/one-idea/divider/summary/methodology) + chart-card system (the direct-label bar/stack/small-multiple/heatmap/waffle family that real firm decks use) + report shell per §5. Written style spec per firm modeled on the Gartner one-pager: fonts, sizes, grays, one accent, chart rules.
- Buy (donor kit only): Slideworks Full Access is the only bundle with verifiable MBB-ex-consultant provenance (3,523 slides + Excel model files; also ~$129 toolkit tier, 205 slides / 171 layouts / 15 frameworks). Purpose: layout raw material to port into masters, not end decks. Marketplace subs (SlideModel, Slidesgo, Envato) stay trial-scoped filler: keep-after-cancel tactics known; Slidesgo free tier carries attribution; license terms matter more than the slide count.
- Don't buy as backbone: firm consultants keep saying "buying templates ≠ firm quality" (r/consulting), and this corpus shows why — real decks are argument systems; the templates are shapes without arguments. AI generators (Gamma-class, $2.1B/$100M ARR wave 2024-26) shift premium toward narrative + branded masters; not trusted as the skeleton.
- think-cell (or PowerPoint-native equivalents with direct labeling) buys more than any template purchase.

## 7. Template set to build (the deliverable this playbook points at)

1. **Deck masters ×12**: cover / road-marker TOC / exec-summary "at a glance" / claim-title content page + kicker / divider with you-are-here / 2-column compare / process timeline / matrix (with callout layer) / funnel-value stack / KPI number page / summary-recommendations / appendix source-dense.
2. **Chart cards ×10**: labeled horizontal bar / 100% stack / small multiples grid / line w/ milestone markers / waffle-pictogram / heat grid / donut with in-segment % / from-to arrow / growth curve with % bubbles / clustered bars with delta braces. One accent + grays; direct labels; source slot.
3. **MR report shell ×8**: cover / disclaimer / TOC / exec summary / methodology (N, fieldwork, sampling note) / exhibit page (chart + insight box + footnote) / survey Q-block / appendix tables.
4. **One-page variant**: the one-page-strategy stack (objectives → choices → capabilities → metrics with side-question callouts) and the "win/now/next"-style single page; Gartner's one-page strategy deck pages are the reference.
5. **Written spec page** per brand: like the Gartner guide — title font/size, body, grays, accent, chart rules.

## 8. Evidence ledger (load-bearing claims)

| Claim | Source | Tier | Conf |
|---|---|---|---|
| Action-title rule (2 lines, active, quantitative) | deckary 2025 + slideworks | practitioner | High (consistent) |
| 39pg real-McKinsey-deck practices (roadmarkers, parallel titles, kicker boxes) | consultantsmind 2024 | practitioner review | Med-High |
| McKinsey 2019 identity | mckinsey.com blog | primary | High |
| #051C2C / #2251FF hexes | 3 tertiary + visual | tertiary, consistent | Med |
| Gartner exact page spec | Gartner brand PDF 2017 | primary | High |
| PwC fonts/hexes | PwC AU VI 2020 PDF | primary | High |
| Deloitte Insights chart system | Pentagram project page | primary (project) | High |
| BCG/Bain/Deloitte hex conflicts | mixed | — | flagged above |
| Firm decks carry zero filler SmartArt (13/3,048 pages); templates = shapes without arguments | 75 per-deck reviews + r/consulting | observed + practitioner | High |
| Slideworks bundle provenance (ex-MBB, 3,523 slides) | vendor page, verifiable artifacts | vendor | Med |
| "McKinsey style" Google results mostly SEO recreations | task-2 trend work (SlideUpLift admissions) | vendor-admitted | High |

Gaps stated honestly: no primary brand PDFs surfaced for Bain/BCG/Deloitte-global; most gallery SKU prices unverifiable (JS pages); the 2010 USPS teardown predates the current slide era. Corpus-side, the review contract is closed: 182/182 master-corpus sheets + 75/75 firm-deck sheets read and cataloged.

## 9. The HTML template kit (buildout record)

Spec: `TEMPLATE_SPEC.md`. Layout-family provenance: `TEMPLATE_HARVEST.json` (3,294 content/non-smartart slides → 50 families). Built kit: `html-templates/` — **101 templates across 51 family dirs**, each one self-contained `index.html` (1280×720 stage that scales to viewport with zero JS/network; inline CSS/SVG; marked data arrays) + `MANUAL.md` build manual (WHEN / ANATOMY / SLOTS / FILL / CHART-RECIPE / VERIFY / DON'T / SOURCE). Extraction streams: A spine/text 17 families, B chart exhibits 17, C diagrams/frameworks 16 (+ cover probe). Every template cites the source deck and page(s) it was read off; honest stand-ins (fonts, illustrative numbers) are labeled in the manual, source-deck defects recorded as DON'T items. Index: `html-templates/gallery.html` (+ `README.md`, `manifest.json`, `manifest.jsonl`). Integrity: 101/101 dirs carry index+manual with all seven sections, zero external URLs, zero duplicate ids.

