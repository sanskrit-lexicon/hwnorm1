"""hwnorm1.py
   Sep 5, 2016
   Oct 12, 2017. Revised to use normalize_key from ../hwnorm1c/hwnorm1c.py
"""
import sys,re
#sys.path.append('../hwnorm1c/')
sys.path.append('../../sanhw1/')
import hwnorm1c
class HWnorm1rec(object):
 d = {} # dictionary of normalized keys
 n = 0
 def __init__(self,line):
  line=line.rstrip('\r\n')
  self.line = line
  m = re.search(r'^(.*?):(.*)$',line)
  self.normkey = m.group(1)
  rest = m.group(2)
  parts = rest.split(';')
  self.keys = []
  self.dictstrs = []
  for part in parts:
   (key,s) = part.split(':')
   self.keys.append(key)
   self.dictstrs.append(s)
  HWnorm1rec.d[self.normkey]=self
  HWnorm1rec.n = HWnorm1rec.n + 1

def init_hwnorm1(filein=None):
 if filein == None:
  import os
  dir_path = os.path.dirname(os.path.realpath(__file__))
  filein = os.path.join(dir_path,"hwnorm1c.txt")
 with open(filein,"r") as f:
  recs = [HWnorm1rec(line) for line in f]
 print(len(recs),"read from",filein)


def find(key):
 if HWnorm1rec.n == 0:
  init_hwnorm1()
 normkey = hwnorm1c.normalize_key(key)
 #print key,normkey
 if normkey not in HWnorm1rec.d:
  return None
 return HWnorm1rec.d[normkey]

if __name__ == "__main__":
 key = sys.argv[1]
 rec = find(key)
 if not rec:
  print("key not found")
 else:
  print("key found:",rec.keys)

