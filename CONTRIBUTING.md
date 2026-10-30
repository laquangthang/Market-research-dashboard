# Contributing

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
