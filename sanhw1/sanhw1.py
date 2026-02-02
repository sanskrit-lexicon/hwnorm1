"""sanhw1.py
 Oct 26, 2014
 Construct merge of all Cologne Sanskrit-Lexicon dictionaries 
   with Sanskrit headwords.
 Merge the raw headwords into one list.
 The output file contains two fields, separated by colon
  hw  =  the headword spelled in SLP1
  dicts = the Cologne dictionary codes having this hw; separated by 'comma'.
 NO spelling normalization is done, though this may be useful in future
 revisions.
 The output is sorted into Sanskrit alphabetical order by headword.
 Nov 28, 2014  Modified to place M+consonant in the order of 
     [homorganic nasal of consonant]+consonant.
     e.g., aMka  would be (for purpose of ordering) thought of as aNka.
     This is when the consonant is among the 5 vargas.  For other consonants
     (  yrlvSzsh), the ordering remains as M.
 Dec 29, 2014. Revised to make the sort faster.
     Checked it gives same result as prior version.
 Apr 13, 2015. Added specialized dictionaries
 Oct 20, 2016.  Use revised key2 format.
   Currently, SKD has extra fields  (see skd/2012/pywork/make_xml.py)
   This program is changed to parse both this (new) format, and the
   old formats
 Jan 15, 2020.  Use /2020/ instead of /2014
 Jan 27, 2020. Use mwhw2.txt for MW, no longer use mwkeys/extract_keys_b.txt
 Feb 1,2025 FRI dictionary
"""
from __future__ import print_function
import sys,re
import codecs
pyversion2 = (sys.version_info[0] == 2)
from slp_cmp import slp_sorted
from slp_cmp import translate_one
# dictyear has all dictionary codes, with the 'year'.
# This 'year' is required to locate the files
# This is a Python dictionary data structure, quite like a PHP associative array
dictyear={"ACC":"2020" , "AE":"2020" , "AP":"2020" , "AP90":"2020",
       "BEN":"2020" , "BHS":"2020" , "BOP":"2020" , "BOR":"2020",
       "BUR":"2020" , "CAE":"2020" , "CCS":"2020" , "GRA":"2020",
       "GST":"2020" , "IEG":"2020" , "INM":"2020" , "KRM":"2020",
       "MCI":"2020" , "MD":"2020" , "MW":"2020" , "MW72":"2020",
       "MWE":"2020" , "PD":"2020" , "PE":"2020" , "PGN":"2020",
       "PUI":"2020" , "PWG":"2020" , "PW":"2020" , "SCH":"2020",
       "SHS":"2020" , "SKD":"2020" , "SNP":"2020" , "STC":"2020",
       "VCP":"2020" , "VEI":"2020" , "WIL":"2020" , "YAT":"2020",
       "LAN":"2020","ARMH":"2020","LRV":"2022","ABCH":"2023",
       "ACPH":"2023", "ACSJ":"2023","PWKVN":"2020", "FRI":"2025",}
# sandicts is list of dictionaries with Sanskrit Headwords
# only the 'general' dictionaries are included.
san_en_dicts = ["WIL","YAT","GST","BEN","MW72","AP90","CAE","MD",
               "MW","SHS","BHS","AP","PD","LAN","LRV"]
san_fr_dicts = ["BUR","STC"]
san_de_dicts = ["PWG","GRA","PW","CCS","SCH","PWKVN"]
san_lat_dicts = ["BOP"]
san_san_dicts = ["SKD","VCP","ARMH","ABCH","ACPH","ACSJ"]
san_spc_dicts = ["INM","VEI","PUI","ACC","KRM","IEG","SNP","PE","PGN","MCI","FRI"]
sandicts = san_en_dicts + san_fr_dicts + san_de_dicts + san_lat_dicts +san_san_dicts + san_spc_dicts

def unused_extracthw_mw(filein):
 try: 
  f = codecs.open(filein,"r","utf-8")
 except:
  print("ERROR extracthw_mw file not found:",filein)
  exit(1)
 hws = []
 for line in f:
  line = line.rstrip('\r\n')
  (hw,dummy,dummy) = re.split('\t',line)
  hws.append(hw)
 f.close()
 return hws

class HW2(object):
 def __init__(self,line,n):
  line = line.strip() # remove starting or ending whitespace
  self.line = line
  self.n = n
  parts = re.split(':',line)
  if len(parts) == 5:
   (self.pagecol,self.hw,self.line12,self.L,self.type) = parts
  elif len(parts) == 4:
   (self.pagecol,self.hw,self.line12,self.L) = parts
   self.type='n' # default 'normal'
  elif len(parts) == 3:
   (self.pagecol,self.hw,self.line12) = parts
   self.L = n  # default, line number within hw2 file
   self.type='n'

def init_hw2(filein):
 recs=[]
 with codecs.open(filein,'r','utf-8') as f:
  n = 0
  for line in f:
   n = n + 1
   rec = HW2(line,n)
   recs.append(rec)
 #print(len(recs),"records from",filein)
 return recs

def extracthw(filein):
 recs = init_hw2(filein)
 hws = [rec.hw for rec in recs]
 """
 for hw in hws:
  if type(hw) != str:
   print('extracthw error',filein)
   print('hw=',hw,'has type',type(hw))
   exit(1)
 """
 return hws

def whichinstall():
 import os
 path = os.path.realpath(__file__) 
 if path.startswith('/nfs/'):
  which = 'cologne'
 else: 
  which = 'xampp'
 return which

def get_dirmain(code):
 try:
  year = dictyear[code]
 except:
  print("ERROR dictyear has no code",code)
  exit(1)
 # depends whether we are running at Cologne or in local installation
 if whichinstall() == 'cologne':
 # dirmain example:  PWGScan/2020/  if code == PWG
  dirmain = "%sScan/%s/" %(code,year)
 else:
  dirmain = code.lower() + '/'  # e.g. pwg/
 return dirmain

def addhw(code,d):
 """ Uses global dictyear to locate codehw2.txt file 
 """
 # assume this directory is a subdiretory of hwnorm1 repository (folder)
 dirmain = get_dirmain(code)
 # "../../"  due to relative location of this program file
 dirbase = dirin = "../../" + dirmain
 if False: # and (code == 'MW'):  test to use mwhw2 for mw
  # revised 2018-11-27
  #filein = dirbase + "mwaux/mwkeys/extract_keys_b.txt"
  #filein = dirbase + "pywork/mwkeys/extract_keys_b.txt"
  #hws = extracthw_mw(filein)
  pass
 else:
  # hw2name = pwghw2.txt  for code = PWG
  hw2name = "%shw2.txt" % code.lower()
  filein = dirbase + "pywork/" + hw2name
  hws = extracthw(filein)
 print("%s hws extracted from dict %s" %(len(hws),filein))
 # add these to 'd'
 for ihw0,hw0 in enumerate(hws):
  if hw0 == '':  # should not happen 12-24-2023
   continue
  # hw0 is a unicode string. Convert.
  #hw = hw0.encode('ascii','replace')
  # this may be un-needed in python3
  try:
   if pyversion2:
    hw = hw0.encode('ascii','replace')
   else:
    hw = hw0
  except:
   out = "HEADWORD ERROR: ihw0=%s" %ihw0
   print(out.encode('utf-8'))
   print("dict code =",code)
   exit(1)
  if not hw in d:
   d[hw] = [code]
  else:
   if code not in d[hw]:
    d[hw].append(code)

slp1_cmp1_helper_data = {
 'k':'N','K':'N','g':'N','G':'N','N':'N',
 'c':'Y','C':'Y','j':'Y','J':'Y','Y':'Y',
 'w':'R','W':'R','q':'R','Q':'R','R':'R',
 't':'n','T':'n','d':'n','D':'n','n':'n',
 'p':'m','P':'m','b':'m','B':'m','m':'m'
}
def slp_cmp1_helper1(m):
 #n = m.group(1) # always M
 c = m.group(2)
 nasal = slp1_cmp1_helper_data[c]
 return (nasal+c)
def slp_cmp1_helper(a):
 try:
  a1 = re.sub(r'(M)([kKgGNcCjJYwWqQRtTdDnpPbBm])',slp_cmp1_helper1,a)
 except:
  print('slp_cmp1_helper error:a=',a)
  exit(1)
 return a1

def sanhw1(fileout):
 # d is a dictionary
 # key is headword
 # value is list of dict codes
 d = {}
 dicts = ["MW","PW"] # for testing
 dicts = sandicts
 for code in dicts:
  addhw(code,d)
 # sort hws
 hws = d.keys()
 opt=2 # controls which way
 if opt==1:
  # previous way
  sortedhws = sorted(hws,cmp=slp_cmp1)
 else:
  # new way - 
  hwpairs = [(hw,slp_cmp1_helper(hw)) for hw in hws]
  #sorted_hwpairs = sorted(hwpairs,cmp=slp_cmp_pairs)
  sorted_hwpairs = sorted(hwpairs,key=lambda x:translate_one(x[1]))
  #sorted_hwpairs = slp_sorted(hwpairs,keyFcn = (lambda x: x[1]))
  sortedhws = [hw for (hw,hwadj) in sorted_hwpairs]
 # output 
 fout = codecs.open(fileout,"w","utf-8")
 for hw in sortedhws:
  codes = sorted(d[hw])
  codestr = ','.join(codes)
  fout.write("%s:%s\n"%(hw,codestr))
  #hw1=slp_cmp1_helper(hw)
  #fout.write("%s,%s:%s\n"%(hw,hw1,codestr))
 fout.close()
 print("%s hws written to %s" %(len(hws),fileout))
if __name__=="__main__":
 fileout = sys.argv[1] # output path
 sanhw1(fileout)

