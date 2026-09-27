---
title: For Institutions
---

# For Institutions

Protocol Manager is a static web application for maintaining and sharing CT imaging protocols within a radiology department. It provides a searchable protocol library organized by body region, a side-by-side comparison tool for selecting between similar protocols, and SVG phase diagrams visualizing contrast injection timing. The site is accessible from any browser with no login required.

The site is built from Markdown files using [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and deployed to GitHub Pages or any internal web server. There is no backend server or database — all data lives in Markdown files with YAML front matter in a Git repository. A CI pipeline regenerates supporting indexes and redeploys the site on every commit to `main`.

## Constraints

- **Requires a developer or IT person** for initial setup and ongoing maintenance. Protocol editing is done by modifying Markdown files directly and committing to Git.
- **Opinionated data format.** Protocols must be structured as Markdown files with a specific YAML front matter schema. A CSV-based import tool is provided for bulk migration from existing documentation.
- **Protocol editing pipeline is a work in progress.** There is no in-browser editor or submission form. Updating a protocol means editing the Markdown file, re-running the comparison index script, and committing.

## Pages in This Section

- [How It Works](how-it-works.md) — System components and data flow
- [Adoption Guide](adoption-guide.md) — Step-by-step setup for a new institution
- [Hosting](hosting.md) — GitHub Pages and local/intranet hosting options
- [Politici Diagnostic Radiology (OHSU)](ohsu-diagnostic-radiology-policies.md) — Ghidul de politici clinice și administrare contrast OHSU
- [Protocoale Clinice & Ghiduri Tehnice Dartmouth Geisel (DHMC)](dartmouth-geisel-protocols.md) — Standarde imagistice, protocoale CT, IRM, US, RX și ghid contrast oral 2026
- [Protocoale Clinice & Standarde Tehnice MCB Radiology](mcb-radiology-protocols.md) — Ghid instituțional Baptist Health / MCB Radiology (CT Scanner Defaults, IRM, US Worksheets, Medicină Nucleară)
- [Protocoale Clinice & Ghiduri Tehnice MIA Radiology](mia-rad-protocols.md) — Manual instituțional Medical Imaging Associates (CT Brain Attack, Fluoroscopie 28 proceduri RF, IRM, US Doppler DVT, MQSA Mamografie, Rezultate Critice 2026)
- [Protocoale Clinice & Suport Imagistic Medford Radiology Group](medford-radiology-protocols.md) — Ghid instituțional The Medford Radiological Group (Anticoagulare ACG 2023, Contrast CT/IRM, TEP în sarcină, mpMRI Prostată, MSK Extremități, 44 proceduri IR)

