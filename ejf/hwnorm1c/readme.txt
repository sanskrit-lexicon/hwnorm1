python extract.py ../../sanhw1/hwnorm1c.txt hwlist.txt extract.txt

hwlist is a file with one headword per line. Headword assumed to be
spelled in slp1 transliteration.
For each input headword:
a) apply the normalization function normalize_key
b) look up the normalized key in the hwnorm1c list of such
c) write what is found.
