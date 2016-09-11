# coding=utf-8
"""gram.py  May 19, 2016
  Feb 26, 2016
 Filter the (Gr.) records
"""
import re
import sys,codecs
import transcoder
transcoder.transcoder_set_dir("");
import headword
reHeadword0 = headword.reHeadword
reHeadword = re.compile(reHeadword0)
reHeadword1 = headword.reHeadword + r" \((.*?)\)" 

def as2slp1(x):
 y = re.sub(r'-','',x)
 z = transcoder.transcoder_processString(y,'as','slp1')
 return z
def unused_as2slp1_systematic(x):
 y = re.sub(r'-','',x)
 # nasals
 y = re.sub(r'n3([kg])',r'm3\1',y)
 y = re.sub(r'n5([cj])',r'm3\1',y)
 y = re.sub(r'm([pbm])',r'm3\1',y)
 y = re.sub(r'n([tdn])',r'm3\1',y)
 # visarga
 y = re.sub(r'ss','h2s',y)
 # alternate vant/vat  or mant/mat
 y = re.sub(r'va\(n$','vat',y)
 y = re.sub(r'ma\(n$','mat',y)

 z = transcoder.transcoder_processString(y,'as','slp1')
 return z

slp1_cmp1_helper_data = {
 'k':'N','K':'N','g':'N','G':'N','N':'N',
 'c':'Y','C':'Y','j':'Y','J':'Y','Y':'Y',
 'w':'R','W':'R','q':'R','Q':'R','R':'R',
 't':'n','T':'n','d':'n','D':'n','n':'n',
 'p':'m','P':'m','b':'m','B':'m','m':'m'
}
def slp_cmp1_helper1(m):
 #n = m.group(1) # always M
 c = m.group(2)
 nasal = slp1_cmp1_helper_data[c]
 return (nasal+c)
def normalize_key(a):
 #1. normalize so that M is used rather than homorganic nasal
 a = re.sub(r'(M)([kKgGNcCjJYwWqQRtTdDnpPbBm])',slp_cmp1_helper1,a)
 #2. normalize so that 'rxx' is 'rx' (similarly, fxx is fx)
 a = re.sub(r'([rf])(.)\2',r'\1\2',a)
 #3. ending 'aM' is 'a' (Apte)
 a = re.sub(r'aM$','a',a)
 #4. ending 'aH' is 'a' (Apte)
 a = re.sub(r'aH$','a',a)
 #4a. ending 'uH' is 'u' (Apte)
 a = re.sub(r'uH$','u',a)
 #4b. ending 'iH' is 'i' (Apte)
 a = re.sub(r'iH$','i',a)
 #5. 'ttr' is 'tr' (pattra v. patra)
 a = re.sub(r'ttr','tr',a)
 #6. ending 'ant' is 'at'
 a = re.sub(r'ant$','at',a)
 #7. 'cC' is 'C'
 a = re.sub(r'cC','C',a)
 return a

def main(inlines,hwrecs,fileout,fileout1):
 fout=codecs.open(fileout,"w","utf-8")
 fout1=codecs.open(fileout1,"w","utf-8")
 nsystematic=0
 nout=0
 dictcode='pd'
 ngramsure=0
 for hwrec in hwrecs:
  datalines = inlines[hwrec.linenum1-1:hwrec.linenum2]
  firstline = datalines[0] 
  if  firstline.find('(Gr.)') == -1:
   continue
  # Usually, the (Gr.) occurs very close to the beginning. Check this and set a flag
  if re.search(u'¦ *\([^)]+\) *\(Gr[.]\)',firstline):
   gramsure=""
   ngramsure = ngramsure + 1
  else:
   gramsure="?"
  hw0 = hwrec.hwslp
  # This is the 'normalization' logic of hwnorm1
  hwnorm = normalize_key(hw0)
  page0 = hwrec.pagecol
  l1 = hwrec.linenum1
  l2 = hwrec.linenum2
  #line = "%s:%s:%d,%d:%s" %(page0,hw0,l1,l2,hw0as)
  line = "%s:%s,%s: gram.%s" %(dictcode,hw0,hwrec.lnum,gramsure)
  """
  if re.search(r'[()*\[]',hw1norm) or re.search(r'[()*\[]',hwnorm):
   out = "BADCHAR: %s:%s" % (line,hw1)
   print out.encode('utf-8')
   print '%d old %s' %(hwrec.linenum1,firstline.encode('utf-8'))
   print 'pd:%s,%d:%s:%s:t:' %(hwrec.hwslp,hwrec.linenum1,'X','Y')
   print
   continue
  """
  nout = nout + 1
  # output to fileout
  #out = "%s:%s" %(line,hw1norm)
  out = line
  fout.write("%s\n" % out)
  # output to fileout1
  outarr=[]
  baseurl='http://www.sanskrit-lexicon.uni-koeln.de/scans/awork/apidev/servepdf.php?dict=%s'% dictcode
  url = '%s&page=%s' %(baseurl,page0)
  pageref = "[[%s][page %s]]" %(url,page0)
  outarr.append('* TODO Case %04d:%s %s %s' % (nout, gramsure,hw0,pageref))
  """
  # construct two possible correction 'change' records
  keyref = "%s,%s" %(hwrec.hwslp,hwrec.lnum)
  out = ':'.join([dictcode,keyref,hw1,'n',''])
  outarr.append(';%s' % out)
  out = ':'.join([dictcode,keyref,hw0as,hw0as,'n',''])
  outarr.append(';%s' % out)
  """
  # output up to 10 lines of datalines
  outlines = datalines[0:10]
  for x in outlines:
   outarr.append(';  %s' % x)
  if len(datalines)>10:
   ndiff = len(datalines) - 10
   outarr.append(';   [and %s more lines]' % ndiff)
  # 1 extra blank line
  outarr.append('')
  fout1.write('\n'.join(outarr) + "\n")
  if (nout == 25) and False:
   print "debug",nout
   break
   pass
 fout.close()
 fout1.close()
 print len(hwrecs),"headword records processed"
 print nout,"records written to ",fileout
 print nout,"sections written to ",fileout1
 print (nout - ngramsure),"cases need further examination"

 
class Headword(object):
 def __init__(self,line,n):
  line = line.rstrip('\r\n')
  self.line = line
  self.lnum = n
  (self.pagecol,self.hwslp,linenum12) = re.split('[:]',line)
  (linenum1,linenum2) = re.split(r',',linenum12)
  self.linenum1=int(linenum1)
  self.linenum2=int(linenum2)

def init_headwords(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  recs = []
  lnum=0
  for x in f:
   lnum = lnum+1
   recs.append(Headword(x,lnum))
 return recs

if __name__ == "__main__":
 filein=sys.argv[1] #  pd.txt
 filein1=sys.argv[2] # pdhw2.txt
 fileout =sys.argv[3] #  
 fileout1 =sys.argv[4] #  Emacs Ord Mode listing
 # slurp pd.txt file into list of lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  inlines = [x.rstrip('\r\n') for x in f]
 # construct headword records
 hwrecs=init_headwords(filein1)
 main(inlines,hwrecs,fileout,fileout1)
