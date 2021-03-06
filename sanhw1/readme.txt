This was previously on Cologne server in scans/awork/sanhw1 directory.
The redo.sh script does the following:
Note: for a new dictionary, modify the 'dictyear' variable in sanhw1.py.
* remake sanhw1.txt and hwnorm1c.txt
python sanhw1.py sanhw1.txt
python hwnorm1c.py sanhw1.txt hwnorm1c.txt
* TODO remake hwnorm1c.sqlite and move to simple-search
echo "2) hwnorm1c_sql_input.txt"
python make_hwnorm1c_sql_input.py hwnorm1c.txt hwnorm1c_sql_input.txt
echo "3) hwnorm1c.sqlite"
rm hwnorm1c.sqlite
sqlite3 hwnorm1c.sqlite < hwnorm1c.sql
echo "4) Removing intermediate files"
rm hwnorm1c_sql_input.txt
* move  hwnorm1c.sqlite AND commit csl-apidev repository
# in hwnorm1/sanhw1 directory
mv hwnorm1c.sqlite ../../csl-apidev/simple-search/hwnorm1/

* ------------------------------------------------
* Notes from prior work
* ------------------------------------------------
* 01-15-2020  python2/3 conversions 
sanhw1.py and hwnorm1.py now work in either python2 or python3.
The Sanskrit sorting in sanhw1 is modified to use slp_cmp.py module.
sanhw2.py has not been converted to python3.
There is no current need for sanhw2.txt; when the need arises,
sanhw2.py can be adjusted to be python2/3 compatible.
At the same time, sanhw1.py detects where it is being run (either
cologne or xampp); and makes appropriate adjustments.
The assumed location of the 'hwnorm1' parent folder is
- at cologne, in scans directory
- in local installations, in cologne directory.

* Oct 26, 2014 sanhw1.py
python sanhw1.py sanhw1.txt
 Nov 29, 2014 change sort order.
The sorting order was changed, so that
 M+varga -> (homorganic nasal)+varga.
For example, aMga now appears in the
list as if it were spelled aNga.

* Nov 2, 2015.  sanhw2  
Includes first L-number 
* Jan 15, 2020  stop maintenance
No current use of sanhw2.txt.  sanhw2.py would need to be changed
similarly to  sanhw1.py.

* Jul 17, 2017  hwnorm1c
 hwnorm1c.py : ref = https://github.com/sanskrit-lexicon/hwnorm1/tree/master/ejf/hwnorm1c
python hwnorm1c.py sanhw1.txt hwnorm1c.txt
python make_hwnorm1c_sql_input.py hwnorm1c.txt hwnorm1c_sql_input.txt
sqlite3 hwnorm1c.sqlite < hwnorm1c.sql
rm hwnorm1c_sql_input.txt

# Note: hwnorm1c.py is currently (08-17-2017) the same as
#  awork/hwnorm/hwnorm1/hwnorm_v1c.py
#   https://github.com/sanskrit-lexicon/Cologne/issues/171
* redo_hwnorm1c.sh
This script recomputes the hwnorm1c.sqlite database, as described above.
* Oct 12, 2017 Revise hwnorm1c.py
  This now agrees with 
  https://github.com/sanskrit-lexicon/hwnorm1/blob/master/ejf/hwnorm1c/hwnorm1c.py
* Nov 9, 2019. Copy sqlite file to simple-search

* THE END
