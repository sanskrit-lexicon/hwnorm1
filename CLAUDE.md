# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**hwnorm1** is a Sanskrit Lexicon **processing-tool** repository — part of the Cologne Digital Sanskrit Lexicon (CDSL) infrastructure.

## Repo Category

`processing-tool` — see the [tooling runbook](https://github.com/sanskrit-lexicon/csl-observatory/blob/main/runbook/cologne-tooling-runbook.md) for category-specific conventions.

## GitHub Issue Conventions

This repository uses the **Cologne tooling-repo taxonomy**. All issues must have:
- **Exactly one type label** (9 options)
- **Exactly one severity label** (4 levels)
- **One milestone** (5 options)

### Type Labels
- `bug` — Code defect (wrong output, broken contract)
- `feature` — Net-new capability
- `enhancement` — Improvement to existing capability
- `performance` — Speed, memory, throughput optimization
- `tech-debt` — Refactoring, cleanup, dependency updates
- `security` — CVE, auth issue, credential exposure
- `documentation` — Prose docs, API docs, comments
- `infrastructure` — CI/CD, deploy, data pipelines, build tooling
- `question` — Research, proposals, open discussions

### Severity Labels
- `trivial` — Cosmetic, < 1 hour
- `minor` — Single function/component
- `major` — Multiple files, design decision
- `critical` — Blocks users, data loss/security CVE

### Milestones
- **API Stability** — performance, security, regressions
- **User Experience** — bugs, features, enhancements
- **Data Quality** — data-pipeline issues, integrity
- **Developer Experience** — tech-debt, infrastructure, docs
- **Community** — questions, proposals, discussions

## Cross-Repo Coordination

The org-level project [Tooling Roadmap](https://github.com/orgs/sanskrit-lexicon/projects/9) tracks tool work across all repositories.

## Key files

| Path | Purpose |
|---|---|
| `hwnorm1.py` | Main script — classifies headwords by normalization convention |
| `sanhw1/sanhw1.txt` | Input: cross-dictionary headword list (`headword:dict1,dict2,...`) |
| `conv1/{DICT}_{TYPE}.txt` | Output: per-dictionary normalization reports |
| `normalization.pdf` | Analysis documentation |
| `hwnorm1_log_violation.txt` | Headwords that violated expected patterns |

## Input / output contract

**Input:** `sanhw1/sanhw1.txt` — SLP1-encoded headwords, each with a comma-separated list
of CDSL dictionary short names.  
**Output:** `conv1/`, `conv2/`, `conv3/` — per-dictionary text files, one `headword:dict`
per line, grouped by normalization pattern (anusvāra, nasals, etc.).  
**Encoding:** SLP1 throughout.

## Common commands

```bash
# Run normalization analysis (generates conv1/ output)
python hwnorm1.py

# Run error probe
python proberrors.py

# Generate HTML reports (from conv1/ .txt files)
bash hwnorm1.sh

# Check for duplicates
python duplicationstats.py
```

## Dataset profile

See [`DATASET_PROFILE.md`](DATASET_PROFILE.md) for the full schema, coverage table, and
usage examples.
