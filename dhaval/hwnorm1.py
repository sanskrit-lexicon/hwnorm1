# -*- coding: utf-8 -*-
""" hwnorm1.py
Code Developed by Dhaval Patel in 2014.
Code refactored by Jim Funderburk beginning Jan 16, 2020.

To generate normalization of headwords of sanhw1.txt
Documentation at https://github.com/sanskrit-lexicon/CORRECTIONS/issues/43.

2020 changes:
  change tab to single space, for Python indenting.
  Have a 'main' module. All code run from main module
  Read various file-name parameters at run time
  'global' not needed.
"""
from __future__ import print_function
import sys, re
import codecs
""" ejf removed. not used
import string
from string import maketrans
"""
import datetime

# Function to return timestamp
def timestamp():
 return datetime.datetime.now()

def sanhw1(filein):
 with codecs.open(filein,'r','utf-8') as fin:
  lines = fin.readlines()
 output = []
 for line in lines:
  line = line.strip()
  split = line.split(':')
  word = split[0]
  dicts = split[1].split(',')
  output.append((split[0],dicts)) # Added a tuple of (word,dicts)
 return output

""" ejf move to main
headwithdicts = sanhw1() 
"""
def hw1(headwithdicts):
 #global headwithdicts
 output = []
 for (word,dicts) in headwithdicts:
  output.append(word)
 return output

def rchop(thestring, ending):
 if thestring.endswith(ending):
  return thestring[:-len(ending)]
 else:
  return thestring
 
# See https://github.com/sanskrit-lexicon/CORRECTIONS/issues/43#issuecomment-65781239
""" ejf move to main
log = codecs.open("conv1/log.txt","a","utf-8")
log.write(str(timestamp())+"\n")
anu = [(1,["AP90"]),(2,["AP","BEN","BOP","BUR","CAE","CCS","MD","MW","MW72","PW","PWG","SCH","SHS","STC","VCP","WIL","YAT"]),(3,["SKD","AP90","BHS","WIL","PW","PWG","VCP"]),(4,["YAT"]),(5,["AP","AP90","CAE","CCS","MD","MW","PW","PWG","STC"]),(6,["BUR","MW72","SHS","VCP","WIL","YAT","SKD"])]
"""

def anu(headwithdicts,dictionary,convention):
 if convention == 1:
  anuwords = []
  nasalwords = []
  anun = [] # anusvAra+nasal consecutively
  mn = [] # m+nasal consecutively
  anufile = codecs.open("conv1/"+dictionary+"_anuwords.txt","w","utf-8")
  nasalfile = codecs.open("conv1/"+dictionary+"_nasalwords.txt","w","utf-8")
  anunfile = codecs.open("conv1/"+dictionary+"_anunwords.txt","w","utf-8")
  mnfile = codecs.open("conv1/"+dictionary+"_mnwords.txt","w","utf-8")
  log = codecs.open("conv1/log.txt","a","utf-8")
  for (word,dicts) in headwithdicts:
   #if dictionary in dicts and re.search('M[kKgGcCjJwWqQtTdDpPbB]',word) and not re.search('s[aA]M[kKgGcCjJwWqQtTdDpPbB]',word):
   if dictionary in dicts and re.search('M[kKgGcCjJwWqQtTdDpPbB]',word):
    anuwords.append(word+":"+dictionary)
    anufile.write(word+":"+dictionary+"\n")
   if dictionary in dicts and re.search('[NYRnm][kKgGcCjJwWqQtTdDpPbB]',word):
    nasalwords.append(word+":"+dictionary)
    nasalfile.write(word+":"+dictionary+"\n")
   #if dictionary in dicts and re.search('M[NYRnm]',word) and not re.search('s[aA]M[NYRnm]',word) and not re.search('Mmanya',word):
   if dictionary in dicts and re.search('M[NYRnm]',word):
    anun.append(word+":"+dictionary)
    anunfile.write(word+":"+dictionary+"\n")
   if dictionary in dicts and re.search('[NYRnm][NYRnm]',word):
    mn.append(word+":"+dictionary)
    mnfile.write(word+":"+dictionary+"\n")
  print(len(anuwords), "words with anusvAra+consonant pattern.")
  print(len(nasalwords), "words with m+consonant pattern.")
  print(len(anun), "words with anusvAra+nasal pattern.")
  print(len(mn), "words with m+nasal pattern.")
  log.write(dict+":"+str(len(anuwords))+":"+str(len(nasalwords))+":"+str(len(anun))+":"+str(len(mn))+"\n")

""" ejf move to main
alldicts = ["ACC","CAE","AP90","AP","BEN","BHS","BOP","BUR","CCS","GRA","GST","IEG","INM","KRM","MCI","MD","MW72","MW","PD","PE","PGN","PUI","PWG","PW","SCH","SHS","SKD","SNP","STC","VCP","VEI","WIL","YAT"]
"""
""" move to main
for dict in alldicts:
 print(dict, "is being handled")
 anu(headwithdicts,dict,1)
 print
log.write("-------------------------\n")
log.close()
"""
def notinarray(list,word):
 for member in list:
  if re.search(member,word):
   return False
   break
 else:
  return True

""" ejf move to main
consonants = ['k','K','g','G','N','c','C','j','J','Y','w','W','q','Q','R','t','T','d','D','n','p','P','b','B','m','y','r','l','v','S','z','s','h']
"""

def normduplication(list,word):
 global consonants
 for con in consonants:
  word = word.replace('r'+con+con,'r'+con)
 if word in list:
  return True
 else:
  return False

def duplicatedlist():
 global consonants
 output = []
 for con in consonants:
  output.append("r"+con+con)
 for member in ['rkK','rgG','rcC','rjJ','rwW','rqQ','rtT','rdD','rpP','rbB']: # See https://github.com/sanskrit-lexicon/hwnorm1/issues/1#issuecomment-158735703
  output.append(member)
 return output

def normupasarga(list,word):
 upasarga = ['pr','prati','praty','api','parA','apa','sam','saM','aBi','aBy','anu','anv','ava','nir','niH','niz','dur','duH','duz','vi','vy','A','ni','ny','aDi','aDy','ati','aty','su','sv','ut','ud','ul','prati','praty','pari','pary','upa']
 for upas in upasarga:
  if re.sub("^"+upas,'',word) in list:
   return True
   break
 else:
  return False

def normanusvara(list,word):
 word = re.sub('M([kKgG])','N\g<1>',word)
 word = re.sub('M([cCjJ])','Y\g<1>',word)
 word = re.sub('M([wWqQ])','R\g<1>',word)
 word = re.sub('M([tTdD])','n\g<1>',word)
 word = re.sub('M([pPbB])','m\g<1>',word)
 word = re.sub('M$','m',word)
 if word in list:
  return True
 elif normduplication(list,word):
  return True
 elif normupasarga(list,word):
  return True
 else:
  return False

""" ejf moved to main
#violation11 = codecs.open('proberrors/11violation.txt','w','utf-8')
#violation12 = codecs.open('proberrors/12violation.txt','w','utf-8')
#violation13 = codecs.open('proberrors/13violation.txt','w','utf-8')
#violation14 = codecs.open('proberrors/14violation.txt','w','utf-8')
#violation21 = codecs.open('conv2/21violation.txt','w','utf-8')
#violation31 = codecs.open('conv3/31violation.txt','w','utf-8')
#violation32 = codecs.open('conv3/32violation.txt','w','utf-8')
#violation33 = codecs.open('conv3/33violation.txt','w','utf-8')
#violation34 = codecs.open('conv3/34violation.txt','w','utf-8')
#rxx = codecs.open('conv2/rxx.txt','w','utf-8')
violation41 = codecs.open('proberrors/41violation.txt','w','utf-8')
#violation61 = codecs.open('proberrors/61violation.txt','w','utf-8')
#violation62 = codecs.open('proberrors/62violation.txt','w','utf-8')
exclusionlist12 = ['[sS][aA][M][kKgGcCjJwWqQtTdDpPbB]','k[iE][M][kKgGcCjJwWqQtTdDpPbB]','aMk[aA]r','BujaMg','yaMdin','aMtap','aMg','MDar','aMBA','Mpac','a[hl]aMk','ahaM','aMBav','h[iu]Mk','oMk','aMDam','annaMBaww','yaMd','aMkf','apAM','dv[Aa]Mdv','aMkaz','[aAiIuU]Mjaya','puraMDr','MGuz','Mdam','Mtud','alaM','Mgat','MBar','MpaSy','Mk[Aa]r','raTaMt','AMpati','AMkf','AsyaMDa','itTaM','idaM','idAnIM','AMd[aA]','^IMkf','ilIMDr','[aA]laMkr','DvaMjAnu','fRaMcaya','evaM','EdaM','kaM[jdD]','kawaMkaw','k[Aa]TaM','karaMDay','p[Aa]raMpar','kAMdiS','puM','k[Uu]laM','ASuMga','karRaM','kAM','kupyaMjara','koyaMpurI','kzudraM','MDa[my]','gAM','gomaRiMda','svayaMB','ciraM','cUMkfta','jIvaM','tadAnIM','timiM','naktaM','tUzRIM','tElaM','zaMDi','tv[aA]M','daM','dayyAM','puraMdar','dAnaM','dAMpaty','devAnAM','devIMDiyaka','dEnaM','dEyAM','dyAM','druhaMtara','D[Aa]naM','DiyaM','DarmaM','DuMDuM','DenuM','naraM','nikftiM','paRyaM','paraM','pAMkt','putraM','p[uO]raM','pfTivIM','prARaM','bAlaMBawwa','B[aA]gaM','makzuM','mahiM','mArtyuM','mitaM','mftyuM','sAyaM','yuDiM','rAtriM','rATaM','lakzmIM','lokaM','varzaM','v[iE]SvaM','vftaM','SataM','S[aA]truM','SayyaM','SarDaM','SAkaM','SunaM','SuBaM','SyEnaM','samaM','samitiM','sarvaM','sahasraM','sAkaM','sAtyaM','suKaM','sEr[ai]M','stanaM','sv[aA]yaM','svarRaM','hUM',]
exclusionlist61 = ['kf$','^f$','^[gjdnBnvsh]f$']
exclusionlist62 = ['[GcjJPtvs]ar$','kzar$','antar$','punar$','prAtar','ahar$','kmar$','vaDar$','uzar$','^UDar$','^janar$']
"""

def conventionviolation(word,dict,hw1):
 #global hw1
 # ejf uncommmented begin"""
 if dict in ["AP90"] and re.search('[NYRnm][kKgGcCjJwWqQtTdDpPbB]',word):
  print('11', word, dict)
  violation11.write(dict.lower()+":"+word+":"+word+":n:\n")
 if dict in ["AP","BEN","BOP","BUR","CAE","CCS","MD","MW","MW72","PW","PWG","SCH","SHS","STC","VCP","WIL","YAT"] and re.search('M[kKgGcCjJwWqQtTdDpPbB]',word):
  if dict in ["AP","AP90","CAE","CCS","IEG","MCI","MD","MW","PD","PW","PWG","SCH","SHS","STC","VEI","WIL"] and notinarray(exclusionlist12,word):
   print('12', word, dict)
   violation12.write(dict.lower()+":"+word+":"+word+":n:\n")
 if dict in ["SKD","AP90","BHS","WIL","VCP"] and re.search('M$',word) and not normanusvara(hw1,word[:-1]):
  violation13.write(dict.lower()+":"+word+":"+word+":n:\n")
  print('13', word, dict)
 if dict in ["SKD","VCP","SHS","WIL","YAT"] and re.search('r[kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh]',word) and not re.search('r[kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh][kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh]',word): # PD removed
  violation21.write(dict.lower()+":"+word+":"+word+":n:\n")
  print('21', word, dict)
 if dict in ["SKD","VCP","SHS","WIL","YAT"] and re.search('r[kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh][kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh]',word):
  rxx.write(dict.lower()+":"+word+":"+word+":n:\n")
  print('22', word, dict)
 # Convention 3 is too tricky to enter. Leaving it as it is now.
 # ejf uncommented end"""
 if dict in ["AP","AP90","SKD","VCP"] and re.search('[MH]$',word): # and (notinarray(hw1,word[:-1]) ):
  if word[0] == 'a' and (word[1:] in hw1 or normanusvara(hw1,word[1:]) ): # agardaBaH
   #print(word, dict, "passed 0.1")
   pass
  elif word[0:2] == 'an' and (word[2:] in hw1 or normanusvara(hw1,word[2:]) ): # anekaH
   #print(word, dict, "passed 0.2")
   pass
  elif word[:-1] not in hw1 and not normanusvara(hw1,word[:-1]):
   if word[-2] in ["A"] and (word[:-2]+"a" in hw1 or normanusvara(hw1,word[:-2]+"a")): # unmanAH
    #print(word, dict, "passed 1")
    pass
   elif word[-2:] in ["AH"] and (word[:-2]+"as" in hw1 or normanusvara(hw1,word[:-2]+"as")): # ukTaSAH
    #print(word, dict, "passed 2")
    pass
   elif word[-2:] in ["aH"] and (word[:-2]+"as" in hw1 or normanusvara(hw1,word[:-2]+"as")): # akAmataH
    #print(word, dict, "passed 3")
    pass
   elif word[-2:] in ["EH"] and (word[:-2]+"Es" in hw1 or normanusvara(hw1,word[:-2]+"Es")): # uccEH
    #print(word, dict, "passed 4")
    pass
   else:
    print('41', word, dict)
    violation41.write(dict.lower()+":"+word+":"+word+":n:\n")
 """
 # Convention 5 would take much mind. Skipping for now.
 if dict in ["CCS","PW","PWG","SCH",] and re.search('f$',word) and notinarray(exclusionlist61,word):
  violation61.write(dict.lower()+":"+word+":"+word+":n:\n")
  print('61', word, dict)
 if dict in ["AP","AP90","BEN","BOP","BUR","CAE","GRA","MD","MW","MW72","STC"] and re.search('ar$',word) and notinarray(exclusionlist62,word):
  violation62.write(dict.lower()+":"+word+":"+word+":n:\n")
  print('62', word, dict)
 if dict in ["SHS","WIL","GST","MW","MW72","PD","MD"] and re.search('ant$',word) and not re.search('^ant$',word):
  violation31.write(dict.lower()+":"+word+":"+word+":n:\n")
  print('31', word, dict)
 if dict in ["BEN","CAE","CCS","STC","SCH","BHS","PW","PWG","SCH"] and re.search('at$',word) and len(word)>4 and not re.search('[AM]Sat$',word) and not (re.search('[mv]at$',word) and dict in ['PW','PWG']) and not (word.endswith('vat') and rchop(word,'vat') in hw1) and word not in ['pfzat','jagat','camat','avocat','jAgrat','viyat','pawat','mahat','sanat','sarat']:
  violation32.write(dict.lower()+":"+word+":"+word+":n:\n")
  print('32', word, dict)
 """

""" ejf moved to main
for (word,dicts) in headwithdicts:
 for dict in dicts:
  conventionviolation(word,dict)
#violation11.close()
#violation12.close()
#violation14.close()
violation41.close()
#violation61.close()
#violation62.close()
"""   
def norminflection(list,word):
 output = []
 if word not in output:
  word = re.sub('([aA])H','\1',word)
  word = re.sub('[aA]m','\1',word)
  if word in list:
   output.append(word)
 return output
 
def difflist(outputfile,list1,list2):
 fout = codecs.open(outputfile,'w','utf-8')
 difflist = list(set(list1) - set(list2))
 difflist = sorted(difflist);
 fout.write("\n".join(difflist))
 fout.close()

def triming(lst):
 output = []
 for member in lst:
  member = str(member)
  output.append(member.strip())
 return output

def exam(test,control,step,outfile):
 examinableentries = []
 fout = codecs.open(outfile,'w','utf-8')
 ok = []
 test = sorted(test)
 print("Writing suspect entries to", outfile)
 test1 = list(set(test)-set(control))
 test1 = sorted(test1)
 if step == 4:
  for member in test:
   if member in test1 and member not in control:
    if member+"H" in control:
     fout.write(member+"H\n")
    elif member+"m" in control:
     fout.write(member+"m\n")
    else:
     print("Something is wrong")
     exit(1)
    examinableentries.append(member)
   else:
    ok.append(member)
 fout.close()
 ok = list(set(ok))
 ok = sorted(ok)
 examinableentries = list(set(examinableentries))
 examinableentries = sorted(examinableentries)
 return [ok,examinableentries]

def countlen():
 global sanhw1
 global hw1
 global headwithdicts
 hw1file = codecs.open('normalization/hw1.txt','w','utf-8')
 hw1 = sorted(hw1)
 hw1file.write("\n".join(hw1))
 hw1file.close()
 print("Total entries without normalization are", len(hw1))
 output = []
 for word in hw1:
  word = re.sub('N([kKgG])','M\g<1>',word)
  word = re.sub('Y([cCjJ])','M\g<1>',word)
  word = re.sub('R([wWqQ])','M\g<1>',word)
  word = re.sub('n([tTdD])','M\g<1>',word)
  word = re.sub('m([pPbB])','M\g<1>',word)
  word = re.sub('m([Szs])','M\g<1>',word)
  word = re.sub('M$','m',word)
  output.append(word)
 hw2 = list(set(output))
 hw2 = sorted(hw2)
 print("Total entries with anusvAra normalization are", len(hw2))
 hw2file = codecs.open('normalization/hw2.txt','w','utf-8')
 hw2file.write("\n".join(hw2))
 hw2file.close()
 # Do duplication normalization
 duplicates = duplicatedlist()
 singles = ['r'+con for con in consonants]
 output1 = []
 for member in ['rK','rG','rC','rJ','rW','rQ','rT','rD','rP','rB']:
  singles.append(member)
 for word in hw2:
  for i in xrange(len(duplicates)):
   word = word.replace(duplicates[i],singles[i])
  output1.append(word)
 hw3 = list(set(output1))
 hw3 = sorted(hw3)
 print("Total entries with duplication normalization are", len(hw3))
 hw3file = codecs.open('normalization/hw3.txt','w','utf-8')
 hw3file.write("\n".join(hw3))
 hw3file.close()
 # Do 'ant$' normalization
 output3 = []
 for word in hw3:
  if re.search('aMt$',word): # Because it was already converted from 'nt'->'Mt'
   output3.append(re.sub('aMt$','at',word))
  else:
   output3.append(word)
 hw4 = list(set(output3))
 hw4 = sorted(hw4)
 hw4file = codecs.open('normalization/hw4.txt','w','utf-8')
 hw4file.write("\n".join(hw4))
 hw4file.close()
 print("Total entries with 'ant' normalization are", len(hw4))
 # Do inflection normalization
 output4 = []
 exclist = ['$aDi.*\m','pUrvam$','pUrvakam$','^a[BD][iy].*m$','^aMta[rH]','naMtaram$','^anati','^an[vu].*m$','tum$','[aA]rTam$','^[ua]pa.*m$','^at[yi].*m$','aSaH$','^ni[rzH].*m$','^par[i].*m','^pr[aA].*m$','^up[aAo].*m','sa[nMm].*m$','^u[td].*m$','^v[iy].*m$','^y[aA]TA.*m$','^zw.*m$','^A.*am$','ataH$','AH$','agr[ae].*m$','ta[mr]am$','^an[AiIU].*m$','^ana[BD][iy].*m$','^ana[vp][ae].*m$','^apra.*m$','^av[aAio].*m$','^ayaTA.*m$','^bahi[rzH].*m$','^bahu.*m$','^catu[rHz].*m$','dv[iy].*m$','SiraH$','AyAm$','^s[aA].*m$','[DQ]um$','^kiM','^kiya[tc].*m','^maDye.*m','^nAti.*m$','^niSc.*m$','^pAre.*m$','dyuH$','^uccEH.*m$','^yAva[tcd].*m$','^yaT[Aeo].*m$','^yat.*m$']
 for word in hw3:
  if not notinarray(exclist,word) or len(word) < 5:
   output4.append(word)
  else:
   word1 = re.sub('([aAiIuU])H$','\g<1>',word)
   word1 = re.sub('([aAiIuU])m$','\g<1>',word1)
   output4.append(word1)
  
 hw5 = list(set(output4))
 hw5 = sorted(hw5)
 hw5file = codecs.open('normalization/hw5.txt','w','utf-8')
 hw5file.write("\n".join(hw5))
 hw5file.close()
 print("Total entries with inflection normalization are", len(hw5))

def difflister():
 hw1text = codecs.open('normalization/hw1.txt','r','utf-8')
 hw2text = codecs.open('normalization/hw2.txt','r','utf-8')
 hw3text = codecs.open('normalization/hw3.txt','r','utf-8')
 hw4text = codecs.open('normalization/hw4.txt','r','utf-8')
 hw5text = codecs.open('normalization/hw5.txt','r','utf-8')
 hw1 = hw1text.readlines()
 hw2 = hw2text.readlines()
 hw3 = hw3text.readlines()
 hw4 = hw4text.readlines()
 hw5 = hw5text.readlines()
 hw1 = triming(hw1)
 hw2 = triming(hw2)
 hw3 = triming(hw3)
 hw4 = triming(hw4)
 hw5 = triming(hw5)
 difffiles = [('normalization/hw1minushw2.txt',hw1,hw2),('normalization/hw2minushw3.txt',hw2,hw3),('normalization/hw3minushw4.txt',hw3,hw4),('normalization/hw4minushw5.txt',hw4,hw5)]
 for (file,list1,list2) in difffiles:
  difflist(file,list1,list2)
 hw1text.close()
 hw2text.close()
 hw3text.close()
 hw4text.close()
 hw5text.close()
""" moved to main
#countlen()
#difflister()
"""
def anu_main(headwithdicts,hw1,conv1dir,alldicts):
 log = codecs.open("conv1/log.txt","a","utf-8")
 log.write(str(timestamp())+"\n")
 #anu = [(1,["AP90"]),(2,["AP","BEN","BOP","BUR","CAE","CCS","MD","MW","MW72","PW","PWG","SCH","SHS","STC","VCP","WIL","YAT"]),(3,["SKD","AP90","BHS","WIL","PW","PWG","VCP"]),(4,["YAT"]),(5,["AP","AP90","CAE","CCS","MD","MW","PW","PWG","STC"]),(6,["BUR","MW72","SHS","VCP","WIL","YAT","SKD"])]

 for dict in alldicts:
  print(dict, "is being handled by 'anu'")
  anu(headwithdicts,dict,1)
  print()
 log.write("-------------------------\n")
 log.close()

if __name__ == "__main__":
 filein = sys.argv[1] # sanhw1.txt
 option = sys.argv[2]
 headwithdicts = sanhw1(filein)
 hw1 = hw1(headwithdicts)
 alldicts = ["ACC","CAE","AP90","AP","BEN","BHS","BOP","BUR","CCS","GRA","GST","IEG","INM","KRM","MCI","MD","MW72","MW","PD","PE","PGN","PUI","PWG","PW","SCH","SHS","SKD","SNP","STC","VCP","VEI","WIL","YAT"]
 if option == 'nasal':
  anu_main(headwithdicts,hw1,"conv1",alldicts)
  exit()
 #print('exiting after step 1')
 #exit(1)
 consonants = ['k','K','g','G','N','c','C','j','J','Y','w','W','q','Q','R','t','T','d','D','n','p','P','b','B','m','y','r','l','v','S','z','s','h']

 #violation11 = codecs.open('proberrors/11violation.txt','w','utf-8')
 #violation12 = codecs.open('proberrors/12violation.txt','w','utf-8')
 #violation13 = codecs.open('proberrors/13violation.txt','w','utf-8')
 #violation14 = codecs.open('proberrors/14violation.txt','w','utf-8')
 #violation21 = codecs.open('conv2/21violation.txt','w','utf-8')
 #violation31 = codecs.open('conv3/31violation.txt','w','utf-8')
 #violation32 = codecs.open('conv3/32violation.txt','w','utf-8')
 #violation33 = codecs.open('conv3/33violation.txt','w','utf-8')
 #violation34 = codecs.open('conv3/34violation.txt','w','utf-8')
 #rxx = codecs.open('conv2/rxx.txt','w','utf-8')
 violation41 = codecs.open('proberrors/41violation.txt','w','utf-8')
 #violation61 = codecs.open('proberrors/61violation.txt','w','utf-8')
 #violation62 = codecs.open('proberrors/62violation.txt','w','utf-8')
 exclusionlist12 = ['[sS][aA][M][kKgGcCjJwWqQtTdDpPbB]','k[iE][M][kKgGcCjJwWqQtTdDpPbB]','aMk[aA]r','BujaMg','yaMdin','aMtap','aMg','MDar','aMBA','Mpac','a[hl]aMk','ahaM','aMBav','h[iu]Mk','oMk','aMDam','annaMBaww','yaMd','aMkf','apAM','dv[Aa]Mdv','aMkaz','[aAiIuU]Mjaya','puraMDr','MGuz','Mdam','Mtud','alaM','Mgat','MBar','MpaSy','Mk[Aa]r','raTaMt','AMpati','AMkf','AsyaMDa','itTaM','idaM','idAnIM','AMd[aA]','^IMkf','ilIMDr','[aA]laMkr','DvaMjAnu','fRaMcaya','evaM','EdaM','kaM[jdD]','kawaMkaw','k[Aa]TaM','karaMDay','p[Aa]raMpar','kAMdiS','puM','k[Uu]laM','ASuMga','karRaM','kAM','kupyaMjara','koyaMpurI','kzudraM','MDa[my]','gAM','gomaRiMda','svayaMB','ciraM','cUMkfta','jIvaM','tadAnIM','timiM','naktaM','tUzRIM','tElaM','zaMDi','tv[aA]M','daM','dayyAM','puraMdar','dAnaM','dAMpaty','devAnAM','devIMDiyaka','dEnaM','dEyAM','dyAM','druhaMtara','D[Aa]naM','DiyaM','DarmaM','DuMDuM','DenuM','naraM','nikftiM','paRyaM','paraM','pAMkt','putraM','p[uO]raM','pfTivIM','prARaM','bAlaMBawwa','B[aA]gaM','makzuM','mahiM','mArtyuM','mitaM','mftyuM','sAyaM','yuDiM','rAtriM','rATaM','lakzmIM','lokaM','varzaM','v[iE]SvaM','vftaM','SataM','S[aA]truM','SayyaM','SarDaM','SAkaM','SunaM','SuBaM','SyEnaM','samaM','samitiM','sarvaM','sahasraM','sAkaM','sAtyaM','suKaM','sEr[ai]M','stanaM','sv[aA]yaM','svarRaM','hUM',]
 exclusionlist61 = ['kf$','^f$','^[gjdnBnvsh]f$']
 exclusionlist62 = ['[GcjJPtvs]ar$','kzar$','antar$','punar$','prAtar','ahar$','kmar$','vaDar$','uzar$','^UDar$','^janar$']
 
 for (word,dicts) in headwithdicts:
  for dict in dicts:
   conventionviolation(word,dict)
 #violation11.close()
 #violation12.close()
 #violation14.close()
 violation41.close()
 #violation61.close()
 #violation62.close()
 
 #countlen()
 #difflister()
