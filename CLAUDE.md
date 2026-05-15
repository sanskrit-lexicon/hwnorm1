# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**hwnorm1** normalizes Sanskrit headword spellings across all CDSL dictionaries, producing `sanhw1.txt` (the master list of all distinct Sanskrit headwords with their dictionary affiliations) and `hwnorm1c.txt` / `hwnorm1c.sqlite` (a normalization map used by the API's autocomplete and simple-search features).

The output `hwnorm1c.sqlite` is deployed to `csl-apidev/simple-search/hwnorm1/` and also copied into the `cologne-stardict` pipeline.

Assumed local directory layout:
```
cologne/
  hwnorm1/          ← this repo
  csl-orig/         ← source digitization files (read-only)
  CORRECTIONS/      ← sanhw1/sanhw1.txt cross-reference data
  csl-apidev/       ← deployment target for hwnorm1c.sqlite
```

## Architecture

| Directory/File | Purpose |
|---|---|
| `sanhw1/` | Primary pipeline: generates `sanhw1.txt` and `hwnorm1c.txt/sqlite` |
| `normalization/` | Research artifacts: multi-generation headword lists (`hw1.txt`–`hw5.txt`) for analysis |
| `conv1/`–`conv3/` | Legacy conversion experiments (historical) |
| `ejf/` | Earlier EJF-contributed normalization prototypes |
| `dhaval/` | Dhaval-contributed normalization experiments |
| `proberrors.py` | Identifies probable digitization errors in headwords |
| `hwnorm1.py` | Headword normalization logic (reads `CORRECTIONS/sanhw1/sanhw1.txt`) |
| `hwnorm1.sh` | Shell wrapper for `hwnorm1.py` |

### `sanhw1/` Pipeline

The main workflow (run from `sanhw1/`):
```
python sanhw1.py sanhw1.txt
python hwnorm1c.py sanhw1.txt hwnorm1c.txt
python make_hwnorm1c_sql_input.py hwnorm1c.txt hwnorm1c_sql_input.txt
sqlite3 hwnorm1c.sqlite < hwnorm1c.sql
rm hwnorm1c_sql_input.txt
mv hwnorm1c.sqlite ../../csl-apidev/simple-search/hwnorm1/
```

After this, commit both `hwnorm1` and `csl-apidev`, then pull on the Cologne server.

`sanhw1.py` detects its execution environment (Cologne server vs. XAMPP local) and adjusts paths accordingly. For a new dictionary, update the `dictyear` variable in `sanhw1.py`.

## Common Commands

### Full rebuild (from `sanhw1/`)
```bash
sh redo.sh
```

### Identify headword errors
```bash
python proberrors.py
```

## Dependencies

- **Python 3** (`sanhw1.py`, `hwnorm1c.py` are Python 2/3 compatible; `sanhw2.py` is Python 2 only)
- **sqlite3** CLI
- **CORRECTIONS** sibling repo — `../CORRECTIONS/sanhw1/sanhw1.txt`
- **csl-orig** sibling repo — source digitization files
