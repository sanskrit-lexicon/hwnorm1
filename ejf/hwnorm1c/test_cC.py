"""test_cC.py  10-16-2017
    find entries in hwnorm1c.txt for which there are
    (a) a spelling in some dictionary with 'cC'
    (b) a spelling in some other dictionary with only 'C'
 python test_cC.py hwnorm1c.txt test_cC.txt
"""
import collections
import sys,re,codecs

class HWnormc(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  m = re.search(r'^(.*?):(.*?)$',line)
  self.hwnorm=m.group(1)
  data = m.group(2)
  variants = re.split(r';',data)
  self.keys = []
  self.dicts = []
  self.distinctdicts=[]
  for variant in variants:
   (key,dictstr) = re.split(r':',variant)
   dictlist = re.split(r',',dictstr)
   self.keys.append(key)
   self.dicts.append(dictlist)
   for d in dictlist:
    if d not in self.distinctdicts:
     self.distinctdicts.append(d)

def init_hwnorm1_v1c(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [HWnormc(line) for line in f]
 return recs
def filter_cC(rec):
 if 'C' not in rec.hwnorm:
  return False
 cCkeys = [k for k in rec.keys if 'cC' in k]
 if len(cCkeys) == 0:
  return False
 if len(cCkeys) == len(rec.keys):
  # all have cC
  return False
 return True
 
if __name__ == "__main__":
 filein = sys.argv[1]  # hwnorm1_v1c
 fileout = sys.argv[2]
 recs=init_hwnorm1_v1c(filein)
 recsfound=[]
 for rec in recs:
  if filter_cC(rec):
   recsfound.append(rec)
 with codecs.open(fileout,"w","utf-8") as fout:
  for rec in recsfound:
   fout.write(rec.line + '\n')
 print len(recsfound),"cases filtered out of",len(recs),"total cases"

 
