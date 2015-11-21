# -*- coding: utf-8 -*-
""" hwnorm1.py

To generate normalization of headwords of sanhw1.txt
Documentation at https://github.com/sanskrit-lexicon/CORRECTIONS/issues/43.
  
"""
import sys, re
import codecs
import string
import datetime

# Function to return timestamp
def timestamp():
	return datetime.datetime.now()

def sanhw1():
	fin = codecs.open('../CORRECTIONS/sanhw1/sanhw1.txt','r','utf-8');
	lines = fin.readlines()
	output = []
	for line in lines:
		line = line.strip()
		split = line.split(':')
		word = split[0]
		dicts = split[1].split(',')
		output.append((split[0],dicts)) # Added a tuple of (word,dicts)
	return output

headwithdicts = sanhw1()
print len(headwithdicts)

def hw1():
	global headwithdicts
	output = []
	for (word,dicts) in headwithdicts:
		output.append(word)
	return output
hw1 = hw1()
# See https://github.com/sanskrit-lexicon/CORRECTIONS/issues/43#issuecomment-65781239
log = codecs.open("conv1/log.txt","a","utf-8")
log.write(str(timestamp())+"\n")
anu = [(1,["AP90"]),(2,["AP","BEN","BOP","BUR","CAE","CCS","MD","MW","MW72","PW","PWG","SCH","SHS","STC","VCP","WIL","YAT"]),(3,["SKD","AP90","BHS","WIL","PW","PWG","VCP"]),(4,["YAT"]),(5,["AP","AP90","CAE","CCS","MD","MW","PW","PWG","STC"]),(6,["BUR","MW72","SHS","VCP","WIL","YAT","SKD"])]
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
		print len(anuwords), "words with anusvAra+consonant pattern."
		print len(nasalwords), "words with m+consonant pattern."
		print len(anun), "words with anusvAra+nasal pattern."
		print len(mn), "words with m+nasal pattern."
		log.write(dict+":"+str(len(anuwords))+":"+str(len(nasalwords))+":"+str(len(anun))+":"+str(len(mn))+"\n")
alldicts = ["ACC","CAE","AP90","AP","BEN","BHS","BOP","BUR","CCS","GRA","GST","IEG","INM","KRM","MCI","MD","MW72","MW","PD","PE","PGN","PUI","PWG","PW","SCH","SHS","SKD","SNP","STC","VCP","VEI","WIL","YAT"]
"""
for dict in alldicts:
	print dict, "is being handled"
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
			continue
	else:
		return True
consonants = ['k','K','g','G','N','c','C','j','J','Y','w','W','q','Q','R','t','T','d','D','n','p','P','b','B','m','y','r','l','v','S','z','s','h']
def normduplication(list,word):
	global consonants
	for con in consonants:
		word = word.replace('r'+con+con,'r'+con)
	if word in list:
		return True
	else:
		return False
def normanusvara(list,word):
	word = re.sub('M([kKgG])','N\1',word)
	word = re.sub('M([cCjJ])','Y\1',word)
	word = re.sub('M([wWqQ])','R\1',word)
	word = re.sub('M([tTdD])','n\1',word)
	word = re.sub('M([pPbB])','m\1',word)
	if word in list:
		return True
	elif normduplication(list,word):
		return True
	else:
		return False
		
violation11 = codecs.open('proberrors/11violation.txt','w','utf-8')
violation12 = codecs.open('proberrors/12violation.txt','w','utf-8')
violation13 = codecs.open('proberrors/13violation.txt','w','utf-8')
exclusionlist12 = ['[sS][aA][M][kKgGcCjJwWqQtTdDpPbB]','k[iE][M][kKgGcCjJwWqQtTdDpPbB]','aMk[aA]r','BujaMg','yaMdin','aMtap','aMg','MDar','aMBA','Mpac','a[hl]aMk','ahaM','aMBav','h[iu]Mk','oMk','aMDam','annaMBaww','yaMd','aMkf','apAM','dv[Aa]Mdv','aMkaz','[aAiIuU]Mjaya','puraMDr','MGuz','Mdam','Mtud','alaM','Mgat','MBar','MpaSy','Mk[Aa]r','raTaMt','AMpati','AMkf','AsyaMDa','itTaM','idaM','idAnIM','AMd[aA]','^IMkf','ilIMDr','[aA]laMkr','DvaMjAnu','fRaMcaya','evaM','EdaM','kaM[jdD]','kawaMkaw','k[Aa]TaM','karaMDay','p[Aa]raMpar','kAMdiS','puM','k[Uu]laM','ASuMga','karRaM','kAM','kupyaMjara','koyaMpurI','kzudraM','MDa[my]','gAM','gomaRiMda','svayaMB','ciraM','cUMkfta','jIvaM','tadAnIM','timiM','naktaM','tUzRIM','tElaM','zaMDi','tv[aA]M','daM','dayyAM','puraMdar','dAnaM','dAMpaty','devAnAM','devIMDiyaka','dEnaM','dEyAM','dyAM','druhaMtara','D[Aa]naM','DiyaM','DarmaM','DuMDuM','DenuM','naraM','nikftiM','paRyaM','paraM','pAMkt','putraM','p[uO]raM','pfTivIM','prARaM','bAlaMBawwa','B[aA]gaM','makzuM','mahiM','mArtyuM','mitaM','mftyuM','sAyaM','yuDiM','rAtriM','rATaM','lakzmIM','lokaM','varzaM','v[iE]SvaM','vftaM','SataM','S[aA]truM','SayyaM','SarDaM','SAkaM','SunaM','SuBaM','SyEnaM','samaM','samitiM','sarvaM','sahasraM','sAkaM','sAtyaM','suKaM','sEr[ai]M','stanaM','sv[aA]yaM','svarRaM','hUM',]
exclusionlist13 = []
def conventionviolation(word,dict):
	global hw1
	if dict in ["AP90"] and re.search('[NYRnm][kKgGcCjJwWqQtTdDpPbB]',word):
		violation11.write(word+":"+dict+"\n")
	elif dict in ["AP","BEN","BOP","BUR","CAE","CCS","MD","MW","MW72","PW","PWG","SCH","SHS","STC","VCP","WIL","YAT"] and re.search('M[kKgGcCjJwWqQtTdDpPbB]',word):
		if dict in ["AP","AP90","CAE","CCS","IEG","MCI","MD","MW","PD","PW","PWG","SCH","SHS","STC","VEI","WIL"] and notinarray(exclusionlist12,word):
			violation12.write(word+":"+dict+"\n")
	elif dict in ["SKD","AP90","BHS","WIL","PW","PWG","VCP"] and re.search('M$',word) and not normanusvara(hw1,word[:-1]):
		violation13.write(word+":"+dict+"\n")
		
		
for (word,dicts) in headwithdicts:
	for dict in dicts:
		conventionviolation(word,dict)
violation11.close()
violation12.close()

	