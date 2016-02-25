"""distrib.py  Feb 54, 2016
   count the number of dictionaries represented in the hwnorm1_v1c.txt 
     headwords
 python distrib.py hwnorm1c.txt distrib.txt
"""
import collections
import sys,re,codecs

class HWnormc(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
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
if __name__ == "__main__":
 filein = sys.argv[1]  # hwnorm1_v1c
 fileout = sys.argv[2]
 recs=init_hwnorm1_v1c(filein)
 c = collections.Counter()
 for rec in recs:
  #dicts = rec.dicts
  #n = sum([len(dicts[i]) for i in xrange(0,len(dicts))])
  n = len(rec.distinctdicts)
  c.update([n])
 fout = codecs.open(fileout,"w","utf-8")
 keys = sorted(c.keys())
 for key in keys:
  fout.write("%6d headwords occur in %02d dictionaries\n"%(c[key],key))
 tot = sum(c.values())
 fout.write("%6d headwords in total\n"% tot)
 fout.close()

 
