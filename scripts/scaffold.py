"""Scaffold empty market-research dashboard templates.

Safe to re-run: existing template folders and root files are never overwritten.
Usage: python scripts/scaffold.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STUDIES = {
    "bhc": "Brand Health Check",
    "u-and-a": "Usage & Attitude",
    "hut": "Home Use Test",
    "ad-test": "Ad Test",
    "concept-test": "Concept Test",
    "csat": "Customer Satisfaction / NPS",
    "mystery-shopping": "Mystery Shopping",
    "pricing": "Pricing Research",
    "segmentation": "Segmentation",
    "shopper": "Shopper Research",
}
TEMPLATES_PER_STUDY = 5
SECTIONS = [
    "Visual Theme & Atmosphere", "Color Palette & Roles", "Typography Rules",
    "Component Stylings", "Layout Principles", "Depth & Elevation",
    "Do's and Don'ts", "Responsive Behavior", "Data Visualization Rules",
    "Dashboard Structure", "Page Layouts", "Chart Specifications",
    "Agent Prompt Guide",
]
SECTION_NOTES = [
    "Mood, density and design philosophy of the dashboard.",
    "Semantic color names, hex values and their functional roles.",
    "Font families and the full type hierarchy.",
    "Buttons, cards, filters, KPI tiles, tables and their states.",
    "Grid, spacing scale and whitespace rules.",
    "Shadow system and surface hierarchy.",
    "Design guardrails and anti-patterns.",
    "Breakpoints, touch targets and collapsing strategy.",
    "Rules for data viz: chart choice, color encoding, significance marking, base sizes.",
    "List of dashboard pages and navigation.",
    "Where each chart sits on each page.",
    "Detailed design of each chart (type, measures, labels, interactions).",
    "Ready-to-use prompts for AI agents building with this template.",
]


def ids():
    for study, name in STUDIES.items():
        for n in range(1, TEMPLATES_PER_STUDY + 1):
            yield f"{study}-{n:02d}", study, name


def design_md(tid, study, study_name):
    body = "\n".join(f"## {i}. {s}\nTODO\n" for i, s in enumerate(SECTIONS, 1))
    return f"""---
id: {tid}
study: {study}
study_name: {study_name}
name: TODO
style: TODO
status: draft
---

# {tid.upper()} — TODO Template Name

> TODO: one-line description of this template.

{body}"""


def preview(tid, study_name, dark):
    bg, fg, muted = ("#111418", "#e8eaed", "#9aa0a6") if dark else ("#ffffff", "#1f2328", "#656d76")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{tid}</title>
<style>
  body {{ margin: 0; min-height: 100vh; display: grid; place-items: center;
         background: {bg}; color: {fg}; font-family: system-ui, sans-serif; }}
  main {{ text-align: center; }}
  p {{ color: {muted}; }}
</style>
</head>
<body>
<main>
  <h1>{tid.upper()} — TODO Template Name</h1>
  <p>{study_name}</p>
  <p>Preview coming soon</p>
</main>
</body>
</html>
"""


def readme():
    rows = []
    for study, name in STUDIES.items():
        rows.append(f"\n### {name} (`{study}`)\n\n| Template | Study | Name | Status | Links |\n|---|---|---|---|---|")
        for n in range(1, TEMPLATES_PER_STUDY + 1):
            tid, p = f"{study}-{n:02d}", f"design-md/{study}/{study}-{n:02d}"
            rows.append(f"| `{tid}` | {name} | TODO | draft | [DESIGN.md]({p}/DESIGN.md) · [Preview]({p}/preview.html) · [Dark]({p}/preview-dark.html) |")
    sections = "\n".join(f"| {i} | {s} | {d} |" for i, (s, d) in enumerate(zip(SECTIONS, SECTION_NOTES), 1))
    return f"""# Market Research Dashboard Templates

A collection of `DESIGN.md` templates for **market research dashboards**, inspired by
[awesome-design-md](https://github.com/VoltAgent/awesome-design-md).

awesome-design-md captures the design systems of websites. This repo does the same for
MR dashboards, and adds sections on data visualization, page structure and chart specs
for each study type (BHC, U&A, HUT, Ad Test, and more).

## How to use

1. Copy a template folder (e.g. `design-md/bhc/bhc-01/`) into your project.
2. Give its `DESIGN.md` to your AI coding agent and ask it to build the dashboard following it.
3. Open `preview.html` / `preview-dark.html` to see the look.

Each template folder contains:

- `DESIGN.md`: the design system the agent reads
- `preview.html`: visual preview (light)
- `preview-dark.html`: visual preview (dark)

## What's inside each DESIGN.md

Sections 1–8 and 13 follow awesome-design-md. Sections 9–12 are specific to MR dashboards.

| # | Section | Captures |
|---|---|---|
{sections}

## Catalog

{STUDIES.__len__()} study types × {TEMPLATES_PER_STUDY} templates = {len(STUDIES) * TEMPLATES_PER_STUDY} templates.
{chr(10).join(rows)}

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)
"""


CONTRIBUTING = """# Contributing

## Folder naming

Templates live in `design-md/<study>/<study>-NN/`, where `<study>` is the study type slug
(`bhc`, `u-and-a`, `hut`, ...) and `NN` is a two-digit number (`01`, `02`, ...).

Each folder contains exactly `DESIGN.md`, `preview.html` and `preview-dark.html`.

## Adding a new template

1. Copy an existing template folder to the next free number, e.g. `design-md/bhc/bhc-06/`.
2. Update the front-matter in `DESIGN.md` (`id`, `study`, `study_name`, `name`, `style`, `status`)
   and the `<title>` / heading in both preview files.
3. Add a row to the catalog table in `README.md`.

To add a new study type, add it to `STUDIES` in `scripts/scaffold.py` and run
`python scripts/scaffold.py` (existing folders are never overwritten), then add its table to `README.md`.

## Status

Set `status` in the front-matter and in the README table:

- `draft`: empty skeleton, only `TODO`s
- `in-progress`: being written
- `ready`: complete and previews done
"""

LICENSE = """MIT License

Copyright (c) 2026 Market Research Dashboard Templates contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

GITIGNORE = """.DS_Store
Thumbs.db
__pycache__/
*.pyc
.vscode/
.idea/
"""


def write_new(path, text):
    """Write only if the file doesn't exist yet."""
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")
    return True


def main():
    created = skipped = 0
    for tid, study, name in ids():
        folder = ROOT / "design-md" / study / tid
        if folder.exists():  # never touch a template that already exists
            skipped += 1
            continue
        write_new(folder / "DESIGN.md", design_md(tid, study, name))
        write_new(folder / "preview.html", preview(tid, name, dark=False))
        write_new(folder / "preview-dark.html", preview(tid, name, dark=True))
        created += 1
    # ponytail: README is generated once; after that, the catalog table is maintained by hand.
    for fname, text in [("README.md", readme()), ("CONTRIBUTING.md", CONTRIBUTING),
                        ("LICENSE", LICENSE), (".gitignore", GITIGNORE)]:
        write_new(ROOT / fname, text)
    print(f"templates created: {created}, skipped (already exist): {skipped}")


if __name__ == "__main__":
    main()
