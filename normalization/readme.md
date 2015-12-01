Right now the output is placed in normalization subdirectory.

Responsible code is function countlen() in hwnorm1.py.

Let me document the steps.

1. hw1.txt - headwords of sanhw1.txt sorted alphabetically (python order. Not Sanskrit order).

2. hw2.txt - hw1.txt after normalization of anusvAra ([NYRnm][consonant] -> M[consonant]. Also terminal 'M' converted to 'm')

3. hw3.txt - hw2.txt after normalization of duplication ( r[consonant][consonant] -> r[consonant] conversion).

4. hw4.txt - hw3.txt after normalization of terminal 'm' and 'H' ( [aA][mH]$ -> [aA]$ )

There are three difference files generated in the process.

1. hw1minushw2.txt - hw1.txt entries not found in hw2.txt

2. hw2minushw3.txt - hw2.txt entries not found in hw3.txt

3. hw3minushw4.txt - hw3.txt entries not found in hw4.txt

There is also one subsidiary file generated in step 4, which requires manual examination

1. examine.txt - The words in hw3 whose word[:-1] (removal of last letter) form is not found in hw3. This at least beacons that the word is not found in other dictionaries. Have a closer look.


I hope someone would cursorily examine the files and decide whether we are on right track or not.
