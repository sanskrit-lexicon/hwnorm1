#rm -rf proberrors
#rm -rf conv1
#mkdir proberrors
#mkdir conv1
#python hwnorm1.py
#python proberrors.py
cd proberrors
shopt -s nullglob
array=(*.txt)
for VALUE in "${array[@]}"
do
	php ../link.php $VALUE $VALUE".html"
done
