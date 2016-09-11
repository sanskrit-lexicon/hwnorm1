
The format of 'special' files:
<dictcode>:<key1>[,<L>]:description
where
<dictcode> is lower case
<L> is optional

Preparation:
1. special_icf.txt
 Run this is auxiliary directory
 icf.txt is from MWderivations/step3/icf.txt
 We convert it to the form of the 'special' files
 python special_icf.py ../../MWderivations/step3/auxiliary/icf.txt special_icf.txt
2. special_foreign.txt
Currently, foreignwords.txt is from CORRECTIONS/dictionaries/IEG/foreignwords/
 cp foreignwords.txt special_foreign.txt
3. special_bur.txt
 bur.txt is verbforms1.txt from CORRECTIONS/dictionaries/BUR/verbs
 cp bur.txt special_bur.txt
 Next not needed.
 #python special_bur.py bur.txt special_bur.txt
4. special_bhs.txt
 bhs.txt is verbforms1.txt from CORRECTIONS/dictionaries/BHS/verbs
 cp bhs.txt special_bhs.txt
5. special_nochange.txt
 python special_nochange.py ../../CORRECTIONS/corrections_nochange.txt special_nochange.txt
6. special_pdgram.txt
 in pdgram, redogram.sh constructs gram.txt, and then gram_edit.txt is
 constructed manually (see readme file in pdgram)
 cp pdgram/gram_edit.txt special_pdgram.txt
7. special_mwderiv.txt
 Words which are 'explained' by MWderivations analysis2
 cd mwderivation
 sh redo.sh
 cd ../
 cp mwderivation/deriv1.txt special_mwderiv.txt
99. cat special_*.txt > special.txt
  special.txt is used by whitelist.py

