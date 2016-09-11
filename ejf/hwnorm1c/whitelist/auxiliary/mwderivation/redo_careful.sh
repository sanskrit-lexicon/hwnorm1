echo "Recreate graylist_mw.txt"
GRAY="../../output/20160517/graylist.txt"
echo "Using graylist=$GRAY"
python ../../filterdict.py $GRAY graylist_mw.txt mw
echo "regenerating deriv1.txt"
sh deriv1.sh
