"""special_icf.py  Mar 2, 2016
  read icf.txt, and write special_icf.txt
  python special_icf.py icf.txt special_icf.txt
"""
import sys,re,codecs

class ICF(object):
 """ from icf.txt (MW In Compound For)
 """
 d = {}
 recs=[]
 def __init__(self,line):
  line=line.rstrip('\r\n')
  (self.Hcode,self.L,self.key1,self.key2,temp) = re.split('\t',line)
  (dummy,self.refkey1) = re.split(r':',temp)
  ICF.d[self.key1]=self
  ICF.recs.append(self)

def init_icf(filein="analysis/icf.txt"):
 with codecs.open(filein,"r","utf-8") as f:
  for x in f:
   ICF(x)

if __name__ == "__main__":
 filein = sys.argv[1]  # icf.txt
 fileout = sys.argv[2] # graylist.txt
 init_icf(filein)
 recs = ICF.recs
 print len(recs)," icf records"
 dictcode='mw'
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in recs:
   out = "%s:%s,%s:in compound for %s" %(dictcode,rec.key1,rec.L,rec.refkey1)
   f.write('%s\n' % out)

 
