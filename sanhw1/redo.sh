echo "1a) remake sanhw1.txt"
python sanhw1.py sanhw1.txt
echo "1b) remake hwnorm1c.txt"
python hwnorm1c.py sanhw1.txt hwnorm1c.txt
#
echo "2) hwnorm1c_sql_input.txt"
python make_hwnorm1c_sql_input.py hwnorm1c.txt hwnorm1c_sql_input.txt
echo "3) hwnorm1c.sqlite"
rm hwnorm1c.sqlite
sqlite3 hwnorm1c.sqlite < hwnorm1c.sql
echo "4) Removing intermediate files"
rm hwnorm1c_sql_input.txt
echo "If your are ready, move hwnorm1c.sqlite to csl-apidev by this command:"
echo "mv hwnorm1c.sqlite ../../csl-apidev/simple-search/hwnorm1/"
