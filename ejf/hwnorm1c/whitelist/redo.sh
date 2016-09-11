#echo "copying hwnorm1c.txt..."
#cp ~/Documents/GitHub/hwnorm1/ejf/hwnorm1c/hwnorm1c.txt .
echo "Recreating auxiliary/special.txt"
cd auxiliary
cat special_*.txt > special.txt
cd ../
echo "regenerating graylist.txt and all whitelistX.txt files"
#HWNORM1C=~/Documents/GitHub/hwnorm1/ejf/hwnorm1c/hwnorm1c.txt
HWNORM1C=../hwnorm1c.txt
OUTDIR=output/all
python whitelist.py $HWNORM1C graylist.txt $OUTDIR
