"""special_nochange.py  May 16, 2016
 read CORRECTIONS/corrections_nochange.txt and write
  special_nochange.txt
  python special_nochange.py ../../CORRECTIONS/corrections_nochange.txt special_nochange.txt
"""
import sys,re,codecs

class NOCHG(object):
 """ from  CORRECTIONS/corrections_nochange.txt
 """
 d = {}
 recs=[]
 def __init__(self,dictcode,hw):
  self.dict = dictcode
  self.key1 = hw
  NOCHG.d[self.key1]=self
  NOCHG.recs.append(self)

def init_nochg(filein):
 with codecs.open(filein,"r","utf-8") as f:
  n=0
  for x in f:
   x = x.strip()
   n = n + 1
   if x.startswith(';'): # comment
    continue
   parts = x.split(r':')
   if len(parts) == 4:
    # ben:SAstravant:Sastravant:SAstra and Sastra both are valid words.
    # issue number missing. insert 000
    parts.insert(1,'000')
    parts.insert(4,'n')
   elif len(parts) == 5:
    # yat:295:AkzEvajYa,4387:AkzEvajYa->AkzEvajYa:zE
    # standardize to
    # yat:295:AkzEvajYa,4387:AkzEvajYa->AkzEvajYa:n:zE
    parts.insert(4,'n')
   if (len(parts) == 6) and (parts[4]=='n'):
    # ccs:201:suMbrahman:subrahman:n: PREVIOUSLY CORRECTED to subrahman
    #print 'Irregular line %s (#parts=%s)='%(n,len(parts)),x.encode('utf-8')
    pass
   else:
    print 'Irregular line %s (#parts=%s)='%(n,len(parts)),x.encode('utf-8')
    continue
   (dictcode,issuenum,hw1,hw2,code,comment) = parts
   if ',' in hw1:
    (hw,L) = hw1.split(',')
   else:
    hw = hw1
   NOCHG(dictcode,hw)

if __name__ == "__main__":
 filein = sys.argv[1]  # corrections_nochange.txt
 fileout = sys.argv[2] # special_nochange.txt
 init_nochg(filein)
 recs = NOCHG.recs
 print len(recs)," nochg records"

 with codecs.open(fileout,"w","utf-8") as f:
  for rec in recs:
   out = "%s:%s: nochange " %(rec.dict,rec.key1)
   f.write('%s\n' % out)

 
