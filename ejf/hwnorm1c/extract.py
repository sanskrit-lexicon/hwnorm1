"""extract.py July 6, 2021
 Extract records from a list of headwords.
 python extract.py ../../sanhw1/hwnorm1c.txt hwlist.txt extract.txt

"""
import collections
import sys,re,codecs
sys.path.append('../../sanhw1') # form hwnorm1c.py
from hwnorm1c import normalize_key

class HWnormc(object):
 dnorm = {}
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
  # update dnorm
  if self.hwnorm in HWnormc.dnorm:
   print('WARNING. Unexpected duplicate (%s)\n%s' %(self.hwnorm,line))
  HWnormc.dnorm[self.hwnorm] = self
  
def init_hwnorm1_v1c(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [HWnormc(line) for line in f]
 return recs

def write_hwrecs(fileout,hwrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  nmiss = 0
  nfound = 0
  for hw,normhw,hwrec in hwrecs:
   if hwrec == None:
    nmiss = nmiss + 1
    out = '%s = %s:%s' %(hw,normhw,'None')
   else:
    nfound = nfound + 1
    line = hwrec.line
    out = '%s = %s'%(hw,line)
   f.write(out+'\n')
 print(nmiss+nfound,"records written to",fileout)
 print(nmiss,"headwords not found")

def find_hw(hw,d):
 normhw = normalize_key(hw)
 if normhw in d:
  hwrec = d[normhw]
  return normhw,hwrec
 # Try some additional 'normalizations'
 if normhw.endswith('m'):
  normhw1 = normhw[:-1] # remove ending 'm' (neuters)
  if normhw1 in d:
   hwrec = d[normhw1]
   return normhw1,hwrec
  else:
   return normhw,None
 return normhw,None
 

if __name__ == "__main__":
 filein = sys.argv[1]  # hwnorm1c.txt
 filehw = sys.argv[2]  # headword list, one per line. slp1
 fileout = sys.argv[3]
 recs=init_hwnorm1_v1c(filein)
 with codecs.open(filehw,"r","utf-8") as f:
  hws = [x.rstrip('\r\n') for x in f if not x.startswith(';')]
  print(len(hws),"headwords read from",filehw)
 hwrecs = []
 d = HWnormc.dnorm

 for hw in hws:
  normhw,hwrec = find_hw(hw,d)
  hwrecs.append((hw,normhw,hwrec))
 write_hwrecs(fileout,hwrecs)

 
