"""special_bur.py  Mar 7, 2016
  read bur_verbforms1.txt, and write special_bur.txt
  python special_bur.py bur.txt special_bur.txt
"""
import sys,re,codecs

class BUR(object):
 """ from icf.txt (MW In Compound For)
 """
 d = {}
 recs=[]
 def __init__(self,line):
  line=line.rstrip('\r\n')
  (self.dictcode,keylnum,self.note) = re.split(':',line)
  parts = re.split(r',',keylnum)
  self.key1 = parts[0]
  if len(parts) == 2:
   self.L = parts[1]
  else:
   self.L = NOne
  BUR.d[self.key1]=self
  BUR.recs.append(self)

def init_bur(filein="analysis/bur.txt"):
 with codecs.open(filein,"r","utf-8") as f:
  for x in f:
   BUR(x)

if __name__ == "__main__":
 filein = sys.argv[1]  # bur.txt
 fileout = sys.argv[2] # special_bur.txt
 init_bur(filein)
 recs = BUR.recs
 print len(recs)," bur records"
 with codecs.open(fileout,"w","utf-8") as f:
  for rec in recs:
   out = "%s:%s,%s:%s" %(rec.dictcode,rec.key1,rec.L,rec.note)
   f.write('%s\n' % out)

 
