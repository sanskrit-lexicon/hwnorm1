# Dataset Profile — hwnorm1

*Authoritative schema and usage reference for the `hwnorm1` normalized-headword dataset.*

---

## Overview

| Fact | Value |
|---|---|
| Full name | Headword Normalization Dataset — hwnorm1 |
| Maintainer | Cologne Digital Sanskrit Lexicon project |
| Version | see CITATION.cff |
| Format | Plain text (one record per line) |
| Encoding | SLP1 (headwords); ASCII (dictionary short names) |
| License | GPL-3.0 (scripts); output data: public domain |
| DOI | `10.5281/zenodo.XXXXXXX` *(update after Zenodo deposit)* |

---

## Purpose

hwnorm1 analyses headword normalization conventions across CDSL dictionaries,
focusing on anusvāra, nasal, and related spelling variants in SLP1-encoded headwords.
It reads the canonical cross-dictionary headword list (`sanhw1/sanhw1.txt`) and
produces per-dictionary reports of which headwords follow each normalization convention.

Downstream consumers: `csl-pywork` pipeline; researchers comparing cross-dictionary
headword forms; CORRECTIONS project for systematic headword alignment.

---

## Primary data files

### Input: `sanhw1/sanhw1.txt`

Canonical cross-dictionary headword list. One entry per line.

| Field | Type | Required | Description |
|---|---|---|---|
| headword | SLP1 string | yes | Headword in SLP1 encoding (no accents) |
| dict_list | comma-separated short names | yes | Dictionaries in which this headword appears |

**Format:** `headword:dict1,dict2,...`  
**Example:** `a:ABCH,AP,AP90,BEN,BHS,BOP,BUR,CAE,...`

Approximately 186,000 unique headwords across ~34 CDSL dictionaries.

### Output: `conv1/{DICT}_{TYPE}.txt`

Per-dictionary normalization reports. One headword per line.

| File pattern | Content |
|---|---|
| `{DICT}_anuwords.txt` | Headwords with anusvāra + following consonant (SLP1: `M[kKg…]`) |
| `{DICT}_nasalwords.txt` | Headwords with nasal + following consonant (`[NYRnm][kKg…]`) |
| `{DICT}_anunwords.txt` | Headwords with anusvāra + following nasal (`M[NYRnm]`) |
| `{DICT}_mnwords.txt` | Headwords with double nasal (`[NYRnm][NYRnm]`) |

**Format:** `headword:dict_short`  
**Example:** `saMskfta:MW`

Dictionaries covered (28 as of 2026-05-22): ACC, AP, AP90, BEN, BHS, BOP, BUR, CAE, CCS,
GRA, GST, IEG, INM, KRM, MCI, MD, MW, MW72, PD, PE, PGN, PUI, PW, PWG, SCH, SHS, SKD,
SNP, STC, VCP, VEI, WIL, YAT.

### Output: `sanhw1/hwnorm1c.txt`

Canonical normalized headword table (one entry per headword across all dicts).

---

## Schema: `sanhw1/sanhw1.txt`

```
a:ABCH,AP,AP90,BEN,BHS,BOP,BUR,CAE,CCS,FRI,GRA,GST,...
aicadeva:PD
afRa:PD
afRin:AP,AP90,GST,LRV,MW,MW72,PD,PW,PWG,SHS,STC,VCP,WIL
```

SLP1 quick reference: vowels `a A i I u U f F x X e E o O M H`; consonants as in standard SLP1.

---

## Usage examples

### Python — load sanhw1.txt

```python
headwords = {}
with open("sanhw1/sanhw1.txt", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        word, dicts = line.split(":", 1)
        headwords[word] = dicts.split(",")
print(len(headwords), "headwords")  # ~186,000
```

### Shell — count MW anusvāra words

```bash
grep ':MW$' conv1/MW_anuwords.txt | wc -l
```

---

## Derivation / provenance

**Source:** `sanhw1/sanhw1.txt` — compiled by the CORRECTIONS project from all CDSL
dictionary headword lists.  
**Method:** Script `hwnorm1.py` applies regex pattern matching to classify headwords
by anusvāra/nasal convention per dictionary. See [normalization.pdf](normalization.pdf)
for the full normalization analysis.  
**Reference:** [CORRECTIONS issue #43](https://github.com/sanskrit-lexicon/CORRECTIONS/issues/43).

Regeneration command:
```bash
python hwnorm1.py    # writes conv1/, conv2/, conv3/ output dirs
```

---

## Known limitations

- Headwords are in SLP1 only; no IAST or Devanagari output.
- The normalization conventions tracked (anusvāra, nasals) represent one dimension
  of headword variation; other variation types (vowel length, aspirates) are not covered.
- `hwnorm1_log_violation.txt` captures headwords that violate expected patterns — see that
  file for known anomalies [to be reviewed by maintainer].

---

## Citation

If you use this dataset in research, please cite:

```bibtex
@software{hwnorm1,
  title     = {hwnorm1 — Headword Normalization for Cologne Dictionaries},
  author    = {Cologne Digital Sanskrit Lexicon project contributors},
  year      = {2020},
  publisher = {Cologne Digital Sanskrit Lexicon},
  url       = {https://github.com/sanskrit-lexicon/hwnorm1}
}
```

See also [`CITATION.cff`](CITATION.cff).
