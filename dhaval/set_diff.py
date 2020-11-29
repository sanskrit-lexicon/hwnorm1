"""set_diff.py
python set_diff.py A B OUTPUT
A and B are text files.
Consider the lines of A to be a set of strings (A1)
and similarly for B.
take the set difference A1-B1 and also B1-A1.
print the union of these two sets in (normal) sorted order,
labeling each with A or B
"""
import codecs,sys

if __name__=="__main__":
 A = sys.argv[1]
 B = sys.argv[2]
 fileout = sys.argv[3]
 with codecs.open(A,"r","utf-8") as f:
  A1 = [x.rstrip() for x in f]
  print(len(A1),'records from',A)
 with codecs.open(B,"r","utf-8") as f:
  B1 = [x.rstrip() for x in f]
  print(len(B1),'records from',B)
 A2 = set(A1)
 B2 = set(B1)
 print(len(A2),'distinct records from',A)
 print(len(B2),'distinct records from',B)

 A_B = A2.difference(B2)
 B_A = B2.difference(A2)
 print(len(A_B),'records in',A,'but not in',B)
 print(len(B_A),'records in',B,'but not in',A)
 D1 = set(x + ' A' for x in A_B)
 D2 = set(x + ' B' for x in B_A)
 D = D1.union(D2)
 E = sorted(list(D))
 with codecs.open(fileout,"w","utf-8") as f:
  for x in E:
   f.write(x+'\n')
 print(len(E),'records written to',fileout)
