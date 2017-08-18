"""ngram.py
   Aug 18, 2017
   Generate n-grams from hwnorm1
   python ngram.py <n> 
"""
import sys
#sys.path.append('hwnorm1')
import hwnorm1
from sansort import slp_cmp

def get_ngrams(x,n,option="all"):
 ans=[]
 nx = len(x)
 if option == "any":
  ibeg = 0
  iend = nx - n + 1
  for i in xrange(ibeg,iend):
   ans.append(x[i:i+n])
 elif option == "beg":
  ibeg = 0
  iend = n
  if iend <= nx:
   ans.append(x[ibeg:iend])
 elif option == "end":
  ibeg = nx - n
  iend = nx
  if ibeg >= 0:
   ans.append(x[ibeg:iend])
 return ans

if __name__ == "__main__":
 ngramlen = int(sys.argv[1])  # 2,3, etc.
 assert ngramlen>=1,"ngramlen must be >=1"
 option = sys.argv[2] # any,beg,end
 fileout = sys.argv[3] # "hwnorm1/%sgram.txt"%ngramlen
 hwnorm1.init_hwnorm1("../hwnorm1c/hwnorm1c.txt")
 ngramsd = {}
 for key in hwnorm1.HWnorm1rec.d: # normalized headword spelling
  ngrams = get_ngrams(key,ngramlen,option)
  for ngram in ngrams:
   if ngram not in ngramsd:
    ngramsd[ngram]=0
   ngramsd[ngram] = ngramsd[ngram] + 1
  
 keys = ngramsd.keys()
 keys.sort(cmp=slp_cmp)
 with open(fileout,"w") as f:
  for key in keys:
   out = "%s:%s"%(key,ngramsd[key])
   f.write(out + "\n")
 print len(keys),"ngrams written to",fileout

