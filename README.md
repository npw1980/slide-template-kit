# Slide Template Kit

**101 HTML slide templates that come with build manuals.** Every template is a single
self-contained HTML file on a 1280×720 stage — no JavaScript, no network calls, no CDN — and
every template ships a `MANUAL.md` that tells you exactly when to use it, what each slot is,
how to fill it, how to resize it, how to verify the result, and what not to do.

Built from a research pass over consulting decks and market-research reports: 4,867 slides
were visually reviewed page by page (firm decks from Accenture, Deloitte, EY, KPMG, L.E.K.,
PwC Strategy& plus vetted template archives), clustered into 50 layout families, and each
family's genuinely distinct subtypes were encoded as templates that cite the exact source
pages they were read off.

## Start here

Open [`html-templates/gallery.html`](html-templates/gallery.html) in any browser: a browsable
index of all templates, grouped by layout family, with live thumbnails and source citations.
No server needed — the gallery and every template it links to are plain files that work from
`file://`.

Or go straight to a template: copy `html-templates/<template-id>/` and fill it per its
`MANUAL.md`.

## What's inside

| Path | What it is |
|---|---|
| `html-templates/` | 101 templates across 51 directories. Each directory: `index.html` + `MANUAL.md` |
| `html-templates/gallery.html` | Browsable index of the whole kit |
| `html-templates/manifest.json` | Machine-readable list of all templates (family, slots, sources) |
| `TEMPLATE_SPEC.md` | The kit spec the build followed (stage rules, manual schema, title gate) |
| `DESIGN_PLAYBOOK.md` | The design principles extracted from the review, with an evidence ledger |
| `TEMPLATE_HARVEST.json` | Layout-family census: 3,294 content slides clustered into 50 families, with ranked exemplars |
| `scripts/assemble_kit.py` | Regenerates the gallery/README/manifest after you add templates |

## House rules the templates follow

- One page = one argument. Claim titles within 15 words and two lines (the MBB rule).
- One accent color plus a gray ramp per page; emphasis is a budget, not a habit.
- Every page carries a source line and, where numbers come from placeholders, the manual says so.
- Direct labels over legends; zero-based axes for bars; honest grids for charts.
- Fonts are honest stand-ins for the firms' licensed typefaces — the manuals label every
  substitute, so nothing pretends to be a brand match.

## Using it

- **Build one:** open a template, replace the slots per the manual, render it (the manual's
  VERIFY section says what to check), export or screenshot the 1280×720 stage.
- **Extend the kit:** build new templates per `TEMPLATE_SPEC.md`, then run
  `python3 scripts/assemble_kit.py` to regenerate the gallery, README, and manifest.
- **The manuals are the product.** If you only read one thing per template, make it the
  `DON'T` section — it records the source decks' own defects, deliberately kept out.

## Notes and disclaimers

- This kit is an independent research project. It is not affiliated with, endorsed by, or
  sponsored by any of the firms named in the source citations.
- All cited material is from public reports and decks; each template lists its evidence
  pages so you can check the provenance.
- Placeholder copy and numbers are labeled as illustrative. Swap them for your own data.
- License: MIT (see `LICENSE`). Attribution of this repo is appreciated, not required.

## Stats

- 4,867 slides reviewed · 3,294 content slides clustered · 50 layout families
- 101 templates · 1280×720 · zero external requests anywhere in the kit
- Built with headless-render verification per template (no unviewed templates shipped)
