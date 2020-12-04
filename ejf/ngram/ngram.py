"""ngram.py
   Aug 18, 2017
   Generate n-grams from hwnorm1
   python ngram.py <n> 
"""
import sys,re,codecs
#sys.path.append('hwnorm1')
import hwnorm1
#from sansort import slp_cmp
slp_from = "aAiIuUfFxXeEoOMHkKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh"
slp_to =   "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvw"
slp_from_to = str.maketrans(slp_from,slp_to)

def get_ngrams(x,n,option="all"):
 ans=[]
 nx = len(x)
 if option == "any":
  ibeg = 0
  iend = nx - n + 1
  for i in range(ibeg,iend):
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
def rare_ngrams(fileout,ngramsd):
 filedbg = fileout.replace('.txt','_rare.txt')
 maxinstance = 1
 rarerecs = []
 for key in hwnorm1.HWnorm1rec.d:
  ngrams = get_ngrams(key,ngramlen,option)
  for ngram in ngrams:
   if ngramsd[ngram] <= maxinstance:
    rec = hwnorm1.HWnorm1rec.d[key]
    rarerecs.append([rec,ngram])
 with codecs.open(filedbg,"w","utf-8") as f:
  for rec,ngram in rarerecs:
   out = "%s:%s:%s" %(ngram,ngramsd[ngram],rec.line)
   f.write(out+'\n')
 print(len(rarerecs),maxinstance,"rare ngram instances written to",filedbg)

if __name__ == "__main__":
 ngramlen = int(sys.argv[1])  # 2,3, etc.
 assert ngramlen>=1,"ngramlen must be >=1"
 option = sys.argv[2] # any,beg,end
 fileout = sys.argv[3] # "hwnorm1/%sgram.txt"%ngramlen
 filein = "../../sanhw1/hwnorm1c.txt"
 hwnorm1.init_hwnorm1(filein)
 ngramsd = {}
 for key in hwnorm1.HWnorm1rec.d: # normalized headword spelling
  ngrams = get_ngrams(key,ngramlen,option)
  for ngram in ngrams:
   if ngram not in ngramsd:
    ngramsd[ngram]=0
   ngramsd[ngram] = ngramsd[ngram] + 1
  
 keys = list(ngramsd.keys())
 #keys.sort(cmp=slp_cmp)
 keys.sort(key = lambda x: x.translate(slp_from_to))
 with codecs.open(fileout,"w","utf-8") as f:
  for key in keys:
   out = "%s:%s"%(key,ngramsd[key])
   f.write(out + "\n")
 print(len(keys),"ngrams written to",fileout)
 # it is of interest to find the words which have 'rare' ngrams
 if True:
  rare_ngrams(fileout,ngramsd)

  
