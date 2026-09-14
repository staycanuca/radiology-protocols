---
title: How It Works
---

# How It Works

## Protocol Pages

Each protocol is a Markdown file under `docs/ct/<body-area>/`. For example:

```
docs/ct/chest/ct-pulmonary-embolism.md
docs/ct/cardiac/coronary-cta.md
docs/ct/abdomen/ct-renal-mass-protocol.md
```

Each file has two parts:

**YAML front matter** — machine-readable structured data at the top of the file, delimited by `---`. This stores contrast agent, injection rate, kV/mAs, series list, timing, and other parameters used by the comparison tool and acquisition diagrams.

**Markdown body** — the human-readable protocol document with sections for clinical summary, patient preparation, contrast parameters, acquisition series, technical parameters, and post-processing notes.

Front matter can be added to existing Markdown files using `scripts/extract_to_frontmatter.py`, or generated from scratch using `scripts/build_from_csv.py`.

## Comparison Tool

The comparison tool at `/ct/compare/` loads two or more protocols side-by-side. It reads from `docs/javascripts/protocol-comparison-index.json`, a pre-generated JSON file that aggregates key fields from all protocol YAML front matter. This index is regenerated automatically by CI on every push to `main`.

Deep linking is supported: the URL query string encodes selected protocol file paths (e.g. `?p=ct/chest/ct-pulmonary-embolism&p=ct/chest/non-contrast-ct-chest-routine`), so comparison views can be bookmarked and shared.

The comparison tool is vanilla JavaScript. No server is involved at runtime.

## SVG Acquisition Diagrams

Each protocol page renders an SVG timeline showing the contrast injection phases, scan delays, and acquisition windows. This is generated at page load time by `acquisition-diagram.js`, which reads the series data from the page's YAML front matter and draws inline SVG.

The diagrams support multi-phase protocols, split boluses, and multiple fields of view.

## CI Pipeline

The GitHub Actions workflow at `.github/workflows/deploy.yml` runs on every push to `main`:

1. `python scripts/generate_comparison_index.py` — reads all YAML front matter and writes `docs/javascripts/protocol-comparison-index.json`
2. `python scripts/generate_sitemap.py` — writes `docs/javascripts/sitemap.json`
3. `mkdocs gh-deploy --force` — builds the site and pushes to the `gh-pages` branch

For local/intranet hosting, these scripts are run manually before `mkdocs build`.

## Chrome Extension Integration (Optional)

`scripts/generate_sitemap.py` outputs `docs/javascripts/sitemap.json` — a list of all protocol URLs and titles derived from YAML front matter and `config/institution.yml`. This file is used by the [radiology-agent](https://github.com/dfergs93/radiology-agent) Chrome extension to discover protocol pages for AI-assisted queries.

This is optional. Institutions not using the Chrome extension can ignore the sitemap output — it has no effect on the site itself.
