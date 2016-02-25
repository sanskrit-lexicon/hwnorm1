echo "create hwnorm1c.txt from sanhw1.txt"
echo "sanhw1.txt assumed to be in the CORRECTIONS folder, which"
echo "is a 'sibling' of the 'hwnorm1' folder"
python hwnorm1c.py ../../../CORRECTIONS/sanhw1/sanhw1.txt hwnorm1c.txt
echo "create distrib.txt from hwnorm1c.txt"
python distrib.py hwnorm1c.txt distrib.txt
