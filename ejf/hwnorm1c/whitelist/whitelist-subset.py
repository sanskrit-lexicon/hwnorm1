"""whitelist-subset.py  Apr 18, 2016
   Do the logic of whitelist.py, but applied only to the records in a
   given subset of records.  Put all output to the same file.
 python whitelist-subset.py hwnorm1c.txt cae-ccs-only.txt cae-ccs-whitelist.txt
 Revised Mar 18, 2016. See readme.org
"""
import collections
import sys,re,codecs

def whitelist0(rec,code):
 """ in more than one dictionary 
   We do NOT include the records in subset.
 """
 if (len(rec.distinctdicts) > 1) and (not rec.subset):
  rec.code=code
  rec.explain = rec.line

def whitelist1(rec,code):
 """ ends in 'am', word without final 'm' is in some dictionary
 """
 key = rec.hwnorm
 if not key.endswith('am'):
  return
 key1 = key[0:-1] # drop final m
 if key1 not in HWnormc.normd:
  return
 rec1 = HWnormc.normd[key1]
 # found one
 rec.code = code
 rec.explain = "%s@ = %s+m @%s" % (rec.line,key1,rec1.line)

def whitelist2(rec,code):
 """ in SKD, nouns appear in nom. singular form. 
   For nouns whose stems end in vowels, these are handled by the
   logic that generates hwnorm1c (e.g., matiH is already classed with 'mati')
   However, there remain several classes of nouns ending in consonants, and
   this routine deals with those cases.
   For instance, kapinAmA in SKD is same as kapinAman in MW and other
   1. m. nouns in 'an' are shown in nom. singular ending in 'A'
     (example kapinAmA)
   2. m. nouns in 'in' are similar, shown ending in 'I': 
     (example advEtavAdI)
   3. Nouns ending in 'j' and having nom. sing. ending in 'k'
    etc. See logic below for all cases
  For uniform handling, also handle case of SKD ending in 'A' such as:
   akarttA == akarttf
 """
 if (rec.distinctdicts != ['SKD']):
  return
 key = rec.hwnorm
 skd_special = {
 # special cases not currently handled by other skd logic
 # the first arg is the normalized spelling of hwnorm1c (= rec.hwnorm)
 # Sometimes this differs from the un-normalized skd spelling
 'itastata':'itastatas', # skd=itastataH
 'kuwumbOka':'kuwumbOkas', # skd=kuwumbOkaH
 'aGoH':'aGos',
 'kAmAyu':'kAmAyus', # skd = kAmAyuH
 'alpAyu':'alpAyus', # skd = alpAyuH
 'alpIya':'alpIyas', # skd = alpIyaH
 'Ezama':'Ezamas', # skd = EzamaH
 'kAmAyu':'kAmAyus', # skd = kAmAyuH
 'agnisvAttAH':'agnisvAtta', # m. pl. 
 'kIkawAH':'kIkawa', # m. pl.
 'kIrAH':'kIra', # m. pl.
 'agraRIH':'agraRI', # m. noun in I
 'avaSakTika':'avaSakTikA', # skd = avaSakTikaH.  same meaning, diff. gender
 'AbidDa':'AvidDa', # skd = AbidDaH.  b/v confusion
 'AbiDa':'AviDa', # skd = AbiDaH.  b/v confusion. cf. VCP
 'ilvalAH':'ilvalA', # f. pl.
 'uBayedyu':'uBayedyus', #skd = uBayedyuH
 'UDa':'UDas', #skd= UDaH
 'OrdDvaSrotasika':'OrdDvasrotasika',  # vcp has 'srotas', skd confirms as variant
 'kapAlaBfd':'kapAlaBft', # Is 'Bfd' Nom. sing. of 'Bft' ?
 'kambbAtAyI':'kambvAtAyin', # From text, cannot distinguish 'mbb' from 'mbv'
                             # So, am not sure if this is a typo
 'karowI':'karowi', # mw confirms 'karowI as variant f. of 'karowi'.
 'kavI':'kavi',  # mw confirms 'kavI' as variant f. of 'kavi'
 'kARqIrI':'kARqIra', # mw confirms 'kaRqirI' as variant f. of 'kARqIra'
 'kuntalAH':'kuntala', # m. pl. is name of a people, by MW.
 'kfkUlAsa':'kfkalAsa',# skd=kfkUlAsaH.  confirms kfkalAsa as another spelling
 'kolI':'kola', # mw shows kolI as one f. of 'kola', with similar sense (a kind of tree)
 'kozAtakI':'koSAtakI', # mw confirms 'koz' as variant spelling
 'kOverI':'kOvera', # mw72 shows 'I' as f. ending
 'kOzikI':'kOzika', # wil shows 'I' as f. ending of kOzika
 'kratuDruk':'kratudruh', # MW shows 'Druk' as nom. sing. 
 'kruN':'kruYc', # WIL confirms 'kruN' as nom. singular
 'kzuDAvatI':'kzuDAvat', # vatI is f. of 'vat' suffix
 
 }
 lc = key[-1] # last character
 if key in skd_special: #try the 'special' list first
  key1 = skd_special[key]
 elif lc == 'A':
  # search for corresponding 'an' word  
  key1 = key[0:-1] +  'an'
  if key1 not in HWnormc.normd:
   # look for corresponding noun ending in 'f'
   key1 = key1 = key[0:-1] +  'f'
   if key1 not in HWnormc.normd:
    return
 elif lc == 'I':
  # search for corresponding 'in' word  
  key1 = key[0:-1] +  'in'
  if key1 not in HWnormc.normd:
   return
 elif lc == 'k':
  # search for corresponding word ending in 'j','S', 'c'
  newlcs = ['j','S','c']
  found=False
  for newlc in newlcs:
   key1 = key[0:-1] + newlc
   if key1 in HWnormc.normd:
    found=True
    break
  if not found:
   return
 elif lc == 'w':
  # example tfw in SKD = tfz elsewhere
  newlcs = ['z']
  found=False
  for newlc in newlcs:
   key1 = key[0:-1] + newlc
   if key1 in HWnormc.normd:
    found=True
    break
  if not found:
   return
 elif key.endswith('AH'):
  # agOkAH in SKD == agOkas elsewhere
  key1 = key[0:-2]+'as'
  if key1 not in HWnormc.normd:
   return
 elif key.endswith('UH'):
  # anBaHsUH in SKD = abMaHsU elsewhere.  
  # Should this be in hwnorm1c logic ?
  key1 = key[0:-1]
  if key1 not in HWnormc.normd:
   key1 = key[0:-2]+'us'
   if key1 not in HWnormc.normd:
    return
 elif key.endswith('OH'):
  # glOH in SKD = glO elsewhere.  
  # Should this be in hwnorm1c logic ?
  key1 = key[0:-1]
  if key1 not in HWnormc.normd:
   return
 elif lc == 't':
  # example SKD kumut == kumud elsewhere
  key1 = key[0:-1] +  'd'
  if key1 not in HWnormc.normd:
   return
 elif key.endswith('vAn'):
  # Example udanvAn in SKD is udanvat in MW
  key1 = key[0:-3]+'vat'
  if key1 not in HWnormc.normd:
   return  
 elif key.endswith('An'):
  # Example tejIyAn in SKD is tejIyas in MW, tejIyaMs in PW,
  #  tejIyAMs in STC
  # we'll try just the MW form for now
  key1 = key[0:-2]+'as'
  if key1 not in HWnormc.normd:
   return  
 elif key.endswith('an'):
  # Example pacan in SKD is pacat in MW (pres. participle of 'pac')
  key1 = key[0:-2]+'at'
  if key1 not in HWnormc.normd:
   return  
 elif key.endswith('AM'):
  # kintarAM in skd = kintarAm elsewhere, or kiMtarAm in MW
  key1 = key[0:-2]+'Am'
  if key1 not in HWnormc.normd:
   return  
 else:
  # not in any known category for SKD
  return
 rec1 = HWnormc.normd[key1]
 # found one
 rec.code = code
 rec.explain = "%s@ matches %s @%s" % (rec.line,key1,rec1.line)

def unused_whitelist2a(rec,code):
 """ in SKD.  m. nouns in 'f' are shown in nom. singular ending in 'A'
     (example akarttA)
    Require that the 'f' word be found
 """
 if (rec.distinctdicts != ['SKD']):
  return
 key = rec.hwnorm
 if not key.endswith('A'):
  return
 lc = key[-1] # last character (A)
 key1 = key[0:-1] + 'f'
 if key1 not in HWnormc.normd:
  return
 rec1 = HWnormc.normd[key1]
 # found one
 rec.code = code
 rec.explain = "%s@ from %s @%s" % (rec.line,key1,rec1.line)

class Pfxes(object):
 pfxes = []
 def __init__(self,filein):
  # get list of prefixes from filein
  with codecs.open(filein,"r","utf-8") as f:
   Pfxes.pfxes = [x.rstrip('\r\n') for x in f if (not x.startswith(';'))]

def whitelist3a(rec,code):
 """ word is pfx+X for some known pfx and headword X
 """
 key = rec.hwnorm
 found=False
 for pfx in Pfxes.pfxes:
  if key.startswith(pfx):
   l = len(pfx)
   key1 = key[l:] # rest of word
   if key1 in HWnormc.normd:
    found=True
    break #pfx loop
 if not found:
  return
 rec1 = HWnormc.normd[key1]
 # found one
 rec.code = code
 rec.explain = "%s@ = pfx %s+%s @%s" % (rec.line,pfx,key1,rec1.line)

class Sfxes(object):
 sfxes = []
 def __init__(self,filein):
  # get list of suffixes from filein
  with codecs.open(filein,"r","utf-8") as f:
   # format is <sfx> <whitney-section-number>
   Sfxes.sfxes = [x.rstrip('\r\n').split(' ')[0] for x in f 
    if (not x.startswith(';'))]

def whitelist3b(rec,code):
 """ word is X+sfx for some known sfx and headword X
 """
 # do the test
 key = rec.hwnorm
 found=False
 for sfx in Sfxes.sfxes:
  if key.endswith(sfx):
   l = len(sfx)
   key1 = key[0:-l] # beginning of word
   if key1 in HWnormc.normd:
    found=True
    break #sfx loop
 if not found:
  return
 rec1 = HWnormc.normd[key1]
 # found one
 rec.code = code
 rec.explain = "%s@ = sfx %s+%s @%s" % (rec.line,key1,sfx,rec1.line)

def whitelist3c(rec,code):
 """ word is X+sfx for  sfx = ga or ja, and headword X
 """
 # do the test
 key = rec.hwnorm
 found=False
 sfxes = ['ga','ja']
 for sfx in sfxes:
  if key.endswith(sfx):
   l = len(sfx)
   key1 = key[0:-l] # beginning of word
   if key1 in HWnormc.normd:
    found=True
    break #sfx loop
 if not found:
  return
 rec1 = HWnormc.normd[key1]
 # found one
 rec.code = code
 rec.explain = "%s@ = sfx %s+%s @%s" % (rec.line,key1,sfx,rec1.line)

def whitelist0a(rec,code):
 """ special cases
 """
 key = rec.keys[0]
 if not key in Special.d:
  return
 specialrec = Special.d[key]
 dictcode = rec.distinctdicts[0].lower()
 if dictcode != specialrec.dictcode:
  return
 # found one
 rec.code = code
 rec.explain = "%s@ special @%s" % (rec.line,specialrec.comment)

def whitelist4a(rec,code):
 """ word ends in 'A', and there is a corresponding 'a'-ending word.
    So the given word is probably a feminine form.
 """
 key = rec.hwnorm
 if not key.endswith('A'):
  return
 lc = key[-1] # last character (A)
 key1 = key[0:-1] + 'a'
 if key1 not in HWnormc.normd:
  return
 rec1 = HWnormc.normd[key1]
 # found one
 rec.code = code
 rec.explain = "%s@ fem. from %s @%s" % (rec.line,key1,rec1.line)

def whitelist4b(rec,code):
 """ Inflected form of another headword.
 """
 key = rec.hwnorm
 if key.endswith('At'): 
  key1 = key[0:-2] # without At
  key1 = key1 + 'a'
  if key1 not in HWnormc.normd:
   return
  rec1 = HWnormc.normd[key1]
  rec.code = code
  rec.explain = "%s@ Abl. of %s@%s" % (rec.line,key1,rec1.line)
  return
 if key.endswith(('ena','eRa')):
  key1 = key[0:-3] # without ena
  key1 = key1 + 'a'
  if key1 not in HWnormc.normd:
   return
  rec1 = HWnormc.normd[key1]
  rec.code = code
  rec.explain = "%s@ Instr. of %s@%s" % (rec.line,key1,rec1.line)
  return
 if key.endswith('e'):
  key1 = key[0:-1] # without e
  key1 = key1 + 'a'
  if key1 not in HWnormc.normd:
   return
  rec1 = HWnormc.normd[key1]
  rec.code = code
  rec.explain = "%s@ Loc. of %s@%s" % (rec.line,key1,rec1.line)
  return
 # no luck

def whitelist5a(rec,code):
 """ verb forms ending in 'kf' = 'kar'
 """
 key = rec.hwnorm
 if key.endswith('kar'):
  key1 = key[0:-3]+'kf'
  if key1 not in HWnormc.normd:
   return
  rec1 = HWnormc.normd[key1]
  rec.code = code
  rec.explain = "%s@ %s=%s@%s" % (rec.line,key,key1,rec1.line)
  return
 if key.endswith('kf'):
  key1 = key[0:-2]+'kar'
  if key1 not in HWnormc.normd:
   return
  rec1 = HWnormc.normd[key1]
  rec.code = code
  rec.explain = "%s@ %s=%s@%s" % (rec.line,key,key1,rec1.line)
  return

def whitelist5b(rec,code):
 """ Ikf, IBU, etc
 """
 key = rec.hwnorm
 endings = ['Ikf','IBU','Ikfta','IBUta']
 for ending in endings:
  if not key.endswith(ending):
   continue
  key0 = key[0:len(ending)]
  for key1 in [key0+'a',key0+'i']:
   if key1 in HWnormc.normd:
    rec1 = HWnormc.normd[key1]
    rec.code = code
    rec.explain = "%s@ = %s + %s@%s" % (rec.line,key1,ending,rec1.line)
    return
 # fails
 return

def known_compound_component(x,first=True):
 if x in HWnormc.normd:
  return x
 if first:  # x is a first pada
  if x.endswith(('i','a')):
   # For nouns ending in 'in' or 'an', the compound form drops the 'n'
   # Since we're trying to analyze a compound, and x itself is not known,
   # we see if maybe x+'n' is known.
   y = x + 'n'
   if y in HWnormc.normd:
    return y
 return None

def whitelistcpd1_helper1(key,recursive=False,letters='aiufeo'):
 # require X and Y to be of length at least 3.
 # This to avoid problems (?)
 possibles=[] # return array of possible decompositions
 lenx = 3
 leny = 3
 l = len(key)
 if l < (lenx + leny):
  return possibles
 l1 = l - leny
 for i in xrange(lenx,l1+1): # the +1 is tricky. allows akArya-jYa
  x1 = key[0:i]
  # require break at certain specified letters
  if x1[-1] not in letters: # 'aiufeoA':
   continue
  x1a = known_compound_component(x1,first=True)
  if not x1a:
   continue
  x2 = key[i:]
  x2a = known_compound_component(x2,first=False)
  if x2a:
   possibles.append([x1a,x2a])
   continue # success, keep trying for more
  # x2 not found yet
  if not recursive:  # don't probe further
   continue
  # Try x2 via recursion
  possibles2 = whitelistcpd1_helper1(x2,recursive=True,letters=letters)
  for possible2 in possibles2:
   possible = [x1]+possible2
   possibles.append(possible)
 return possibles

def whitelistcpd1_helper(key,recursive=False,letters='aiufeo'):
 possibles = whitelistcpd1_helper1(key,recursive,letters=letters)
 if len(possibles) == 0:
  return None
 # choose the SHORTEST  possible solution
 s = sorted(possibles,key = lambda x: len(x))
 possible = s[0]  # one of the shortest
 # convert to string
 return '-'.join(possible)

def whitelistcpd1(rec,code):
 """ Given word = X + Y, where X and Y are known
 """
 decomp=whitelistcpd1_helper(rec.hwnorm,recursive=False,letters='aiufeo')
 if not decomp:
  return
 rec.code = code
 rec.explain = "%s@ = %s @" % (rec.line,decomp)

def whitelistcpd1a(rec,code):
 """ Given word = X + Y, where X and Y are known
 """
 decomp=whitelistcpd1_helper(rec.hwnorm,recursive=False,letters='AI')
 if not decomp:
  return
 rec.code = code
 rec.explain = "%s@ = %s @" % (rec.line,decomp)

def whitelistcpd2(rec,code):
 """ Given word = X + Y + ... Z, where X,Y,...,Z are known. 
     Like whitelistcp1, but permits multiple parts, rather than just 2
 """
 decomp=whitelistcpd1_helper(rec.hwnorm,recursive=True,letters='aiufeo')
 if not decomp:
  return
 rec.code = code
 rec.explain = "%s@ = %s @" % (rec.line,decomp)

def whitelistcpd2a(rec,code):
 """ Given word = X + Y + ... Z, where X,Y,...,Z are known. 
     Like whitelistcp1, but permits multiple parts, rather than just 2
 """
 decomp=whitelistcpd1_helper(rec.hwnorm,recursive=True,letters='aiufeoA')
 if not decomp:
  return
 rec.code = code
 rec.explain = "%s@ = %s @" % (rec.line,decomp)

def splitwordat(key,letter,minlen):
 """ Search for letter in spelling of key.
  Return pairs (X,Y), where
   key == X+Y (string concatenation)
   X ends with the given letter,
   and X and Y have length >= minlen
 """
 # ref. http://code.activestate.com/recipes/499314-find-all-indices-of-a-substring-in-a-given-string/
 offsets = [m.start() for m in re.finditer(letter,key)]
 ans = []
 for offset in offsets:
  j = offset + len(letter)
  x = key[0:j]
  y = key[j:]
  if (minlen <= len(x)) and (minlen <= len(y)):
   ans.append((x,y))
 return ans

presandhi_hash = {} # dictionary
presandhi_hash["A"] = (("a","a"),("a","A"),("A","a"),("A","A"))
presandhi_hash["U"] = (("u","u"),("u","U"),("U","u"),("U","U"))
presandhi_hash["I"] = (("i","i"),("i","I"),("I","i"),("I","I"))
presandhi_hash["o"] = (("a","u"),("a","U"),("A","u"),("A","U"))
presandhi_hash["e"] = (("a","i"),("a","I"),("A","i"),("A","I"))
presandhi_hash["O"] = (("a","o"),("a","O"),("A","o"),("A","O"))
presandhi_hash["E"] = (("a","e"),("a","E"),("A","e"),("A","E"))

def whitelistcpdsrs1(rec,code):
 """ Given word = X +'A' Y,  try possible sandhis for A
 """
 letters = 'AIUoeEO'  # split places
 minlen = 3
 key = rec.hwnorm
 for letter in letters:
  for (x,y) in splitwordat(key,letter,minlen):
   x0 = x[0:-1] # drop 'letter' from the end of x
   for (u,v) in presandhi_hash[letter]:
    x1 = x0+u
    y1 = v + y
    if (x1 in HWnormc.normd) and (y1 in HWnormc.normd):
     # success. Take the first possibility, at least for now
     rec.code = code
     rec.explain = "%s@ = %s+%s @" % (rec.line,x1,y1)
     return


class Special(object):
 """ from auxiliary/special.txt 
 """
 d = {}
 recs=[]
 def __init__(self,line):
  line=line.rstrip('\r\n')
  (self.dictcode,temp,self.comment) = line.split(':')
  parts = temp.split(',')
  self.key1=parts[0]
  if len(parts) == 2:
   self.L = parts[1]
  else:
   self.L = "?"
  Special.d[self.key1]=self
  Special.recs.append(self)

def init_special(filein="auxiliary/special.txt"):
 with codecs.open(filein,"r","utf-8") as f:
  for x in f:
   Special(x)

class HWnormc(object):
 normd = {} 
 def __init__(self,line,updateDict=True):
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
  if updateDict:
   if self.hwnorm in HWnormc.normd:
    print "HWnormc: unexpected duplicate",self.hwnorm
   HWnormc.normd[self.hwnorm] = self
   self.subset = False  # filled in later

def init_subset(filein):
 with codecs.open(filein,"r","utf-8") as f:
  for line in f:
   arec = HWnormc(line,False)
   if arec.hwnorm in HWnormc.normd:
    rec = HWnormc.normd[arec.hwnorm]
    rec.subset=True
   else:
    print "init_subset ERROR.",arec.hwnorm

def init_hwnorm1c(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [HWnormc(line) for line in f]
 print len(recs),"records from",filein
 return recs

def function_from_code(code):
 localdict = globals()
 fcnname = "whitelist%s" % code
 if fcnname in localdict:
  fcn = localdict[fcnname]
  return fcn
 else:
  print "ERROR: whitelist code not implemented:",code
  exit(1)

def graylist(recs,fout):
 for rec in recs:
  if rec.code == None:
   fout.write("%s\n" % rec.line)
   rec.code='gray'

codedocs = {
 '0':"In two or more dictionaries",
 #1:"In AP, ends in 'am'  (probable neuter noun)", 
 #2:"In PD, ends in 'am' (probable adverb)",
 #'_bur':'Burnouf verb form',
 '1':"key1=X+am and X+a is found",
 '2':"SKD nouns shown in nominative singular",
 #'2a':"SKD nouns ending in 'f' shown as ending in 'A'",
 '3a':"prefix of known word",
 '3b':"suffix of known word",
 '3c':"words ending in pseudo-suffix ga, ja",
 '0a':"special words (icf, foreign, etc.)",
 '4a':"probable f. nouns ending in 'A'",
 '4b':"inflected form",
 'cpd1':"simple compound of 2 parts, first ending in 'aiufeo'",
 'cpd1a':"simple compound of 2 parts, first ending at 'A,I'",
 'cpd2':"simple compound of 3 or more parts, each part ending in 'aiufeo'",
 'cpd2a':"simple compound of 3 or more parts, each part ending in 'aiufeoA'",
 'cpdsrs1':"Simple compound with vowel sandhi at 'AoeEO'",
 '5a':"kar<->kf",
 '5b':'Ikf, IBU, Ikfta, IBUta',
}
if __name__ == "__main__":
 filein = sys.argv[1]  # hwnorm1c
 # subset of records of hwnorm1c, constructed elsewhere, such 
 # as by filterdict
 filesubset = sys.argv[2]  
 fileout = sys.argv[3]  # all output goes here

 recs=init_hwnorm1c(filein)
 # Mark the 'subset' parameter of records
 init_subset(filesubset)
 init_special()
 Pfxes("auxiliary/pfx.txt")
 Sfxes("auxiliary/wsfx.txt")
 #codes = sys.argv[3:]
 codekeys = sorted(codedocs.keys())
 for rec in recs:
  for code in codekeys:
   # check code is implemented
   fcn = function_from_code(code)
   fcn(rec,code)
   if rec.code == code:  
    # be satisfied with first solution
    break
 # Now print results 
 fout = codecs.open(fileout,"w","utf-8")
 recs_subset = [rec for rec in recs if rec.subset]
 for code in codekeys:
   fout.write("; --------------------------------------\n")
   fout.write("; code=%s: %s\n" %(code,codedocs[code]))
   for rec in recs_subset:
    if rec.code == code:
     out = rec.explain
     fout.write('%s\n' % out)
 fout.write("; --------------------------------------\n")
 fout.write("; Not explained\n")
 for rec in recs_subset:
  if rec.code == None:
   fout.write("%s\n" % rec.line)
   rec.code='gray'
 # summary
 c = collections.Counter()
 for rec in recs_subset:
  #n = len(rec.distinctdicts)
  c.update([rec.code])
 keys = sorted(c.keys())
 codedocs['gray']="Not yet whitelisted"
 for key in keys:
  doc = codedocs[key]
  count = c[key]
  out = "%6d headwords coded as %s: %s" %(count,key,doc)
  print out

