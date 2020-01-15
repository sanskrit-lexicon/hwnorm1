""" make_hwnorm1c_sql_input.py
   Prepare input for hwnorm1c.sqlite
   Jul 17, 2017
"""
from __future__ import print_function
import sys,re,codecs

def main():
 import sys
 filein = sys.argv[1]
 fileout = sys.argv[2]
 f = codecs.open(filein,'r','utf-8')
 fout = codecs.open(fileout,'w','utf-8')
 n = 0
 for line in f:
  n = n + 1
  line = line.rstrip('\r\n')
  m = re.search(r'^(.*?):(.*)$',line)
  if not m:
   print("error at line # n",line.encode('utf-8'))
   exit(1)
  (key,data) = (m.group(1),m.group(2))
  fout.write('%s\t%s\n' %(key,data))
 f.close()
 fout.close()
 print(n,"lines read from",filein)


if __name__=="__main__":
 main()
