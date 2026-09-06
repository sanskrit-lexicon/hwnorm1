# hwnorm1

_Created: 05-07-2026 · Last updated: 11-07-2026_

Headword **normalization** across the Cologne Digital Sanskrit Lexicon (CDSL)
dictionaries — a `processing-tool` repository in the
[sanskrit-lexicon](https://github.com/sanskrit-lexicon) project.

The tool reads the union headword list (`sanhw1.txt`, headword + the dictionaries
it appears in) and derives a normalized key so that spelling variants across
dictionaries collapse to one lookup form. That normalized key powers the
simple-search entry lookup in
csl-apidev
(the `hwnorm1c.sqlite` database this repo generates is moved there and served).

Origin discussion:
[CORRECTIONS#43](https://github.com/sanskrit-lexicon/CORRECTIONS/issues/43).

## What it does — normalization pipeline

[`normalization/readme.md`](https://github.com/sanskrit-lexicon/hwnorm1/blob/main/normalization/readme.md)
documents the staged reduction (responsible code: `countlen()` in
[`hwnorm1.py`](https://github.com/sanskrit-lexicon/hwnorm1/blob/main/hwnorm1.py)):

1. `hw1.txt` — headwords of `sanhw1.txt`, sorted (Python order, not Sanskrit order).
2. `hw2.txt` — anusvāra normalized (`[NYRnm][consonant] → M[consonant]`; terminal `M → m`).
3. `hw3.txt` — post-`r` duplication removed (`r[consonant][consonant] → r[consonant]`).
4. `hw4.txt` — terminal `ant` normalized (`aMt$ → at`).
5. `hw5.txt` — terminal `m`/`H` dropped (`[aA][mH]$ → [aA]$`).

Difference files (`hw1minushw2.txt` … `hw3minushw4.txt`) and an `examine`
file capture entries changed or needing manual review at each stage.

## Normalization conventions

The full set of spelling conventions the standard normalization targets —
anusvāra treatment, post-`r` duplication, `-at`/`-vat`/`-mat` vs `-ant`/`-vant`/`-mant`,
inflected vs uninflected forms, verb anusvāra, terminal `f` (ṛ), and `-yas`/`-vas`
vs `-yaṁs`/`-vaṁs` — are catalogued option-by-option, with per-dictionary
assignments and examples, in
[`readme_old.md`](https://github.com/sanskrit-lexicon/hwnorm1/blob/main/readme_old.md).

## Key files

| File | Purpose |
|---|---|
| [`hwnorm1.py`](https://github.com/sanskrit-lexicon/hwnorm1/blob/main/hwnorm1.py) | Main normalizer; reads `../CORRECTIONS/sanhw1/sanhw1.txt`, emits the staged `hw*.txt` and violation logs |
| [`hwnorm1.sh`](https://github.com/sanskrit-lexicon/hwnorm1/blob/main/hwnorm1.sh) | Driver: runs the normalizer + `proberrors.py`, then `link.php` over the probe output |
| [`proberrors.py`](https://github.com/sanskrit-lexicon/hwnorm1/blob/main/proberrors.py) | Emits the per-convention `*violation.txt` files under [`proberrors/`](https://github.com/sanskrit-lexicon/hwnorm1/tree/main/proberrors) |
| [`duplicationstats.py`](https://github.com/sanskrit-lexicon/hwnorm1/blob/main/duplicationstats.py) | Statistics on the post-`r` duplication convention |
| [`link.php`](https://github.com/sanskrit-lexicon/hwnorm1/blob/main/link.php) | Renders violation lists to browsable HTML |
| [`sanhw1/`](https://github.com/sanskrit-lexicon/hwnorm1/tree/main/sanhw1) | Rebuilds `sanhw1.txt` + `hwnorm1c.txt` + `hwnorm1c.sqlite` (see its [`readme.txt`](https://github.com/sanskrit-lexicon/hwnorm1/blob/main/sanhw1/readme.txt)) |
| [`normalization/`](https://github.com/sanskrit-lexicon/hwnorm1/tree/main/normalization) | The staged `hw1`–`hw5` output and its [`readme.md`](https://github.com/sanskrit-lexicon/hwnorm1/blob/main/normalization/readme.md) |
| [`conv1/`](https://github.com/sanskrit-lexicon/hwnorm1/tree/main/conv1), [`conv2/`](https://github.com/sanskrit-lexicon/hwnorm1/tree/main/conv2), [`conv3/`](https://github.com/sanskrit-lexicon/hwnorm1/tree/main/conv3) | Per-convention working files (anusvāra / duplication / `-ant`) per dictionary |
| [`normalization.pdf`](https://github.com/sanskrit-lexicon/hwnorm1/blob/main/normalization.pdf) | Written write-up of the normalization approach |

## Rebuilding the SQLite database

[`sanhw1/readme.txt`](https://github.com/sanskrit-lexicon/hwnorm1/blob/main/sanhw1/readme.txt)
is the canonical procedure (`redo.sh` remakes `sanhw1.txt` + `hwnorm1c.txt`;
`hwnorm1c.sqlite` is regenerated and then moved to
`csl-apidev/simple-search/hwnorm1/`, and is **not** tracked by git). Both this
repo and csl-apidev are then synced and pulled on the Cologne server. For a new
dictionary, update the `dictyear` variable in
[`sanhw1/sanhw1.py`](https://github.com/sanskrit-lexicon/hwnorm1/blob/main/sanhw1/sanhw1.py).

## GitHub issue conventions

This repository follows the
[Cologne tooling-repo taxonomy](https://github.com/sanskrit-lexicon/csl-observatory/blob/main/runbook/cologne-tooling-runbook.md).
Every issue carries exactly one **type** label, one **severity**
(`trivial` · `minor` · `major` · `critical`), and one **milestone**
(API Stability · User Experience · Data Quality · Developer Experience · Community),
plus domain labels scoped to normalization work. Cross-repo tool work is tracked
in the org [Tooling Roadmap](https://github.com/orgs/sanskrit-lexicon/projects/9).
As of 11-07-2026: **21 issues total — 17 open, 4 closed** (nearly all
`domain:normalization`). See
[`CLAUDE.md`](https://github.com/sanskrit-lexicon/hwnorm1/blob/main/CLAUDE.md)
for the full label definitions.

_Dr. Mārcis Gasūns_
