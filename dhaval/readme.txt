
This attempts to recreate Dhaval's work of 2016.
Begun 01-16-2020 by ejf.
hwnorm1  Dhaval's code refactored.
python hwnorm1.py ../sanhw1/sanhw1.txt nasal > hwnorm1_nasal_log.txt
  results for dictionary XXX are in 4 files in 'conv1' directory:
   XXX_nasalwords.txt nasal-varga + non-nasal-varga
   XXX_mnwords.txt    nasal-varga + nasal-varga
   XXX_anuwords.txt   M + non-nasal-varga
   XXX_anunwords.txt  M + nasal-varga
File hwnorm1_log_nasal.txt has counts for each of these files.
There are 33 dictionaries (values of XXX), so 4*33 = 132 files in conv1/.


python hwnorm1.py ../sanhw1/sanhw1.txt violation
[compute time ~ 105 minutes!]

2:11: AP90:  homorganic nasal + non-nasal-consonant:
28:12: --?:  M + non-nasal-consonant, excluding exclusionlist12:
216:13:SKD,AP90,BHS,WIL,VCP  : ending M 'not normanusvara(hw1,word[:-1])':
13253:21:SKD,VCP,SHS,WIL,YAT : r + one-consonant:
11859:22:SKD,VCP,SHS,WIL,YAT :r + two-consonants:   
771:41:AP,AP90,SKD,VCP: cond41:
32:61:CCS,PW,PWG,SCH:ends in 'f' and not in exclusionlist61:
19:62:AP,AP90,BEN,BOP,BUR,CAE,GRA,MD,MW,MW72,STC: ends in 'ar' and not in exclusionlist62:
4:31:SHS,WIL,GST,MW,MW72,PD,MD:ends in 'ant' (but != 'ant'):
236:32:BEN,CAE,CCS,STC,SCH,BHS,PW,PWG,SCH: word ends in 'at' with several exceptions:

cond41:  very complicated
  a + word1 OR a + normanusvara(hw1,word[1:])  
  etc, etc

There are no tests in hwnorm1.py for 14, 33, 34  
 In Dhaval's original work, also these files are empty.
 So, this was probably from a prior version.


--------------------------------------------------------
normalization results

python hwnorm1.py ../sanhw1/sanhw1.txt normalize_all normalization/hw1.txt
# Total entries without normalization are 431510

python hwnorm1.py ../sanhw1/sanhw1.txt normalize_nasal normalization/hw2.txt
# Total entries with anusvAra normalization are 420864 

python hwnorm1.py ../sanhw1/sanhw1.txt normalize_nasal_rxx normalization/hw3.txt
# Total entries with duplication normalization are 416910

python hwnorm1.py ../sanhw1/sanhw1.txt normalize_nasal_rxx_ant normalization/hw4.txt
# Total entries with nasal, rxx, ant normalization are 414623

python hwnorm1.py ../sanhw1/sanhw1.txt normalize_nasal_rxx_ant_infl normalization/hw5.txt
# Total entries with nasal, rxx, ant, infl normalization are 383576

 compare hw5.txt  to 384885 words in ../sanhw1/hwnorm1c.txt
 compare hw5.txt to  389841 words in ../normalization/hw5.txt


../sanhw1/temp_hwnorm1c_word_sorted.txt   
   (first word of each line, sorted in English alphabetical order)
normalization/temp_hw5.txt  : use homorganic nasals , sorted.

python set_diff.py ../sanhw1/temp_hwnorm1c_words_sorted.txt normalization/temp_hw5.txt set_diff_hwnorm1c_hw5.txt

384885 records from hwnorm1c
383576 records from hw5
384884 distinct records from hwnorm1c
383186 distinct records from hw5
7158 records in hwnorm1c but not in hw5
  4987  *am 
    95  *M
   325  *cC*
   412  *patr*
   249  *H
    94  *m  preceding letter not an 'a'
   813  *a
    11  *A
   238 *RW*  see note below re *MW*
     2 *ms*
    17 *u
    26 *i
     8 *I
     6 [the hwnorm1c version of *aa* - see below]
     1 tarirE  (see below)
     1 putrO
    21 various -- all that remain
5460 records in hw5 but not in hwnorm1c
  2681 *a 
    86 *A
  1167 *m
   575 *XC*  X!=c
   303 *pattr*
   134 *ttr*
   580 *H
   239 *MW*  I thought these were handled by construction of temphw5
     4 *Ms*
    15 *U
    11 *i
    10 *I
     8 *u
     6 *aa*  In each case, an hwnor1c version with one 'a'
     1 tariirE

Surely errors:
greek B
grek A

12618 records written to set_diff_hwnorm1c_hw5.txt

