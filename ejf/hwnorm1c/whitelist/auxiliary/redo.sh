echo "remaking files in whitelist/auxiliary"
echo "1. icf"
 python special_icf.py ../../MWderivations/step3/auxiliary/icf.txt special_icf.txt
echo "2. foreignwords"
 cp foreignwords.txt special_foreign.txt
echo "3. special_bur.txt"
 cp bur.txt special_bur.txt
echo "4. bhs"
 cp bhs.txt special_bhs.txt
echo "5. nochange"
 python special_nochange.py ../../CORRECTIONS/corrections_nochange.txt special_nochange.txt
echo "6. pdgram"
 cp pdgram/gram_edit.txt special_pdgram.txt
echo "7. mwderiv: Skipping this for now: see redo_deriv1.sh"
echo "That's all."
