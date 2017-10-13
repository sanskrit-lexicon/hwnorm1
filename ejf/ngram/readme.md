
### ngrams for dictionary headwords.

This continues work begun in the [AE dictionary](https://github.com/sanskrit-lexicon/ApteES/tree/master/ae_saninvert).

Various computations of ngrams can be derived from the hwnorm1c.txt file,
which represents headwords appearing in the various Sanskrit dictionaries of
the Cologne Sanskrit-Lexicon.

### ngram.py
This program computes the n-grams based upon the normalized spellings in
hwnorm1c.txt.  These spellings are in the SLP1 transliteration.
Based on the input parameters, the resulting ngrams are written to an
output file sorted in Sanskrit alphabetical order; the frequency of each
ngram is also written.  The format of each line of the output is:
<ngram> <frequency>

There are two parameters which govern the details of the ngram:
* **n**  The number of characters  (e.g., 2,3) of the ngram. For instance,
 'ka' would be a 2-gram, 'rAm' a 3-gram, etc.
* <position>  a code, one of 
  * **any**   ngram can appear at any position within a headword 
  * **beg**   ngram must appear at the beginning of a headword
  * **end**   ngram must appear at the end of a headword

The third parameter command-line argument of the ngram.py program is the
path to the output file.

For example:
```
python ngram.py 2 any data/2gram.txt
```

### redo.sh
This computes various ngram files
Currently (08-17-2017):
```
python ngram.py 2 any data/2gram.txt      ( 1360)
python ngram.py 3 any data/3gram.txt      (15570)
python ngram.py 2 beg data/2gram_beg.txt  (  770)
python ngram.py 3 beg data/3gram_beg.txt  ( 6697)

```


### Other ways to compute ngrams

One can imagine tweaking the ngram computations in various ways:
* restrict the words to those appearing as headwords in a particular dictionary
   or group of dictionaries.
* Compute ngrams using the individual dictioanary spellings instead of the
  normalized spellings

### consonant-vowel `grams` instead of ngrams 
(speculative)
For Sanskrit words, it might be of interest to slightly different analyses.
One would be to identify consonant-vowel sequences,  where 'consonant' here
would mean a 'consonant-cluster'.  So for a words like 'vizRu' (slp1 spelling),
the consonant-vowel-grams would be 'vi' and 'zRu'. For 'rAma', these cv-grams
would be 'rA', 'ma'.  I'm not sure how words (a) beginning with vowels, or
(b) ending in consonants would handle the 'grams' at the two ends.

#### Revised 10-12-2017
hwnorm1.py was revised to use the `normalize_key` function from
../hwnorm1c/hwnorm1c.py
