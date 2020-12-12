"""ngram_skipd.py
   Modify ngram.py to skip headwords found in only certain dictionaries.
   Notably, PD. As about 1/4 of the words appear ONLY in PD.
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
  rec = hwnorm1.HWnorm1rec.d[key]
  if not rec.ngramused:
   continue
  ngrams = get_ngrams(key,ngramlen,option)
  for ngram in ngrams:
   if ngramsd[ngram] <= maxinstance:
    rarerecs.append([rec,ngram])
 with codecs.open(filedbg,"w","utf-8") as f:
  for rec,ngram in rarerecs:
   out = "%s:%s:%s" %(ngram,ngramsd[ngram],rec.line)
   f.write(out+'\n')
 print(len(rarerecs),maxinstance,"rare ngram instances written to",filedbg)

if __name__ == "__main__":
 ngramlen = int(sys.argv[1])  # 2,3, etc.
 assert ngramlen>=1,"ngramlen must be >=1"
 option = sys.argv[2] # any,beg,end - location of ngram in word
 # don't count hwnorm1c words appearing ONLY in these dictionaries
 skipdicts0 = sys.argv[3].split(',')
 skipdicts = [x.upper() for x in skipdicts0]
 fileout = sys.argv[4] # "hwnorm1/%sgram.txt"%ngramlen
 filein = "../../sanhw1/hwnorm1c.txt"
 hwnorm1.init_hwnorm1(filein)
 ngramsd = {}
 for key in hwnorm1.HWnorm1rec.d: # normalized headword spelling
  rec = hwnorm1.HWnorm1rec.d[key]
  rec.ngramused = False
  flag = False  # True means we use key for ngrams
  for dictname in rec.dictstrs: # dictname is upper case
   if dictname not in skipdicts:
    flag = True
    # mark so rare_ngrams will know we skipped
    rec.ngramused = True
    break
  if not flag:
   # key occurs only in dictionaries in skipdicts. Don't compute ngrams.
   continue
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
 # it is sometimes of interest to find the words which have 'rare' ngrams
 if False:
  rare_ngrams(fileout,ngramsd)

  
