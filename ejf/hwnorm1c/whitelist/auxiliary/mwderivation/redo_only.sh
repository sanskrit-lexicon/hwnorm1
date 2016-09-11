echo "Recreate mw_only.txt"
HWNORM1C=~/Documents/GitHub/hwnorm1/ejf/hwnorm1c/hwnorm1c.txt
INPUT=$HWNORM1C
echo "filtering=$INPUT"
python ../../filterdict.py $INPUT mw_only.txt mw
echo "regenerating deriv1_only.txt"
ANALYSIS="../../../MWderivations/step3/analysis2.txt"
python deriv1.py $ANALYSIS mw_only.txt deriv1_only.txt deriv1_only_notfound.txt
