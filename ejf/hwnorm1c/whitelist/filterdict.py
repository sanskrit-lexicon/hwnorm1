"""filterdict.py
   Apr 15, 2016
   Filter hwnorm1c.txt for all words appearing only in a certain
   subcollection of dictionaries
   python filterdict.py hwnorm1c.txt <outputfile> dict1 [dict2 ...]
"""
import re,sys,codecs
import whitelist   # for init_hwnorm1c

if __name__ == "__main__":
 filein = sys.argv[1] #hwnorm1c.txt
 recs = whitelist.init_hwnorm1c(filein)
 fileout = sys.argv[2]
 dictlist = [x.upper() for x in  sys.argv[3:]]
 dictset = set(dictlist)
 fout = codecs.open(fileout,"w","utf-8")
 nout = 0
 for rec in recs:
  if set(rec.distinctdicts) == dictset:
   fout.write("%s\n" % rec.line)
   nout = nout + 1
 fout.close()
 print nout,"lines from",filein,"written to",fileout
