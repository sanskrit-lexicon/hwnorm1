"""deriv1.py  May 19, 2016
"""
import codecs,re,sys

class Analysis(object):
 def __init__(self,line,option):
  line = line.rstrip('\r\n')
  self.line = line
  parts = re.split('\t',line)
  nparts=len(parts)
  if (option == 'init') and (nparts == 5):
   pass
  elif (option != 'init') and (nparts == 8):
   pass
  else:
   print "Analysis ERROR. %s and %s inconsistent" %(option,nparts)
   print "line=",line.encode('utf-8')
   exit(1)
  (self.H,self.L,self.key1,self.key2,self.lex) = parts[0:5]
  # use self.lex to get self.type (type of record)
  m = re.search(r'^(m|f|n|ind|LEXID|INFLECTID|LOAN|NONE|VERB|ICF|SEE)',self.lex)
  if not m:
   print "Analysis. UNEXPECTED lex:",self.lex.encode('utf-8')
   print "  line=",line.encode('utf-8')
   exit(1)
  code=m.group(1)
  if code in ('m','f','n','ind'):
   self.type='S' # normal Substantive or indeclineable 
  elif code in ('LEXID','INFLECTID','LOAN'):
   self.type='S1' # special substantive
  else:
   self.type=code
  if nparts == 5:  # form of all.txt
   self.analysis='' 
   self.note='init'
   if self.type in ('S','S1'):
    self.status = 'TODO'
   else:
    self.status = 'NTD' # Nothing To Do
  elif nparts == 8:
   (self.analysis,self.status,self.note) = parts[5:]
  else:
   print "Analysis, INTERNAL ERROR:",nparts
   print "Should be either 5 or 8 tab-delimited parts"
   print "line=",line.encode('utf-8')
   exit(1)
  self.parent = None  # determined by init_parents. 
  self.parenta = None # determined by init_parentsa.

 def __repr__(self):
  note=self.note
  if self.status == 'TODO':
   if self.parent:
    note = '%s:parent=%s'%(self.note,self.parent.key1)
    if self.parent.type == 'VERB':
     note = "%s:VERB"%note
  parts=(self.H,self.L,self.key1,self.key2,self.lex,self.analysis,self.status,note) 
  return '\t'.join(parts)

 def substantiveP(self):
  #return self.type not in ('VERB','SEE','NONE')
  #return self.type not in ('VERB','SEE')
  return self.type not in ('VERB')


def init_analysis(filein,option=None):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [Analysis(x,option) for x in f]
 print len(recs),"records read from",filein
 # generate dictionary on key1.  val is a list of records
 d = {}
 for rec in recs:
  key1 = rec.key1
  if key1 not in d:
   d[key1]=[]
  d[key1].append(rec)
 return (recs,d)

class HWnormc(object):
 normd = {} 
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line=line
  m = re.search(r'^(.*?):(.*?)$',line)
  self.hwnorm=m.group(1)
  self.code=None # modified later
  self.explain = None # modified later
  data = m.group(2)
  variants = re.split(r';',data)
  self.keys = []
  self.dicts = []
  self.distinctdicts=[]
  for variant in variants:
   (key,dictstr) = re.split(r':',variant)
   dictlist = re.split(r',',dictstr)
   self.keys.append(key)
   self.dicts.append(dictlist)
   for d in dictlist:
    if d not in self.distinctdicts:
     self.distinctdicts.append(d)
  if self.hwnorm in HWnormc.normd:
   print "HWnormc: unexpected duplicate",self.hwnorm
  HWnormc.normd[self.hwnorm] = self

def init_hwnorm1c(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [HWnormc(line) for line in f]
 print len(recs),"records from",filein
 return recs

def init_graylist(filein):
 return init_hwnorm1c(filein)

def acceptrec(rec):
 status = rec.status
 note = rec.note
 analysis=rec.analysis
 lex = rec.lex
 if (status == 'DONE') and (note.startswith('cpd')):
  return (note+'='+analysis)
 if (status == 'NTD') and lex.startswith('VERB:'):
  return lex
 if (status == 'DONE') and note.startswith('gender:'):
  note = re.sub('^gender:','',note)
  return note
 if (status == 'DONE') and note.startswith('pfxderiv:'):
  note = re.sub(r':',' of ',note)
  return note
 if (status == 'DONE') and note.startswith('pfx1:'):
  note = analysis
  return note
 if (status == 'DONE') and note.startswith('inflected:'):
  note =  re.sub(r'inflected:','',note)
  return note
 if (status == 'DONE') and note.startswith('srs2'):
  note = analysis
  return note
 return None

def main(hwrecs,drecs,fileout,fileout1):
 fout = codecs.open(fileout,"w","utf-8")
 fout1 = codecs.open(fileout1,"w","utf-8")
 n1 = 0
 n2 = 0
 for hwrec in hwrecs:
  hwnorm=hwrec.hwnorm
  hw = hwrec.keys[0]
  # NOTE: we write out hw (rather than hwnorm) since that is the
  # spelling used in whitelist01a function.
  thedict = hwrec.dicts[0][0]
  thedict = thedict.lower()  # whitelist needs lower case
  if hw not in drecs:
   print "NOT FOUND: %s"%hwrec.line
   continue
  recs = drecs[hw]
  noteXtra=''
  if hw!=hwnorm:
   noteXtra = ' (hwnorm=%s)' % hwnorm
  for rec in recs:
   note = acceptrec(rec)
   if note:
    note = note.replace(':',' ') # colon has special meaning to whitelist.py
    out = "%s:%s:%s\n" %(thedict,hw,note+noteXtra)
    fout.write(out)
    n1 = n1 + 1
    break  # take first rec accepted, if there is more than one
  if not note:
   rec = recs[0]
   if (rec.status == 'DONE') and (rec.note == 'noparts'):
    out = "%s:%s:TODO%s = %s\n" %(thedict,hw,noteXtra,rec.note)
   else:
    out = "%s:%s:TODO%s = %s\n" %(thedict,hw,noteXtra,rec)
   fout1.write(out)
   n2=n2+1
 fout.close()
 fout1.close()
 print n1,"solved, but",n2,"unsolved"

if __name__ == "__main__":
 filein  = sys.argv[1] # mwderivatsion/analysis2.txt
 filein1 = sys.argv[2] # graylist_mw.txt
 fileout = sys.argv[3]
 fileout1 = sys.argv[4] # not found
 (recs,drecs) = init_analysis(filein,option=None) 
 hwrecs = init_graylist(filein1)
 main(hwrecs,drecs,fileout,fileout1)
