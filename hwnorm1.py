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

# See https://github.com/sanskrit-lexicon/CORRECTIONS/issues/43#issuecomment-65781239
anu = [(1,["AP90"]),(2,["AP","BEN","BOP","BUR","CAE","CCS","MD","MW","MW72","PW","PWG","SCH","SHS","STC","VCP","WIL","YAT"]),(3,["SKD","AP90","BHS","WIL","PW","PWG","VCP"]),(4,["YAT"]),(5,["AP","AP90","CAE","CCS","MD","MW","PW","PWG","STC"]),(6,["BUR","MW72","SHS","VCP","WIL","YAT","SKD"])]
def anu(headwithdicts,dictionary):
	anuwords = []
	mwords = []
	anun = [] # anusvAra+nasal consecutively
	mn = [] # m+nasal consecutively
	anufile = codecs.open("conv1/"+dictionary+"_anuwords.txt","w","utf-8")
	mfile = codecs.open("conv1/"+dictionary+"_mwords.txt","w","utf-8")
	anunfile = codecs.open("conv1/"+dictionary+"_anunwords.txt","w","utf-8")
	mnfile = codecs.open("conv1/"+dictionary+"_mnwords.txt","w","utf-8")
	for (word,dicts) in headwithdicts:
		#if dictionary in dicts and re.search('M[kKgGcCjJwWqQtTdDpPbB]',word) and not re.search('s[aA]M[kKgGcCjJwWqQtTdDpPbB]',word):
		if dictionary in dicts and re.search('M[kKgGcCjJwWqQtTdDpPbB]',word):
			anuwords.append(word+":"+dictionary)
			anufile.write(word+":"+dictionary+"\n")
		if dictionary in dicts and re.search('[NYRnm][kKgGcCjJwWqQtTdDpPbB]',word):
			mwords.append(word+":"+dictionary)
			mfile.write(word+":"+dictionary+"\n")
		#if dictionary in dicts and re.search('M[NYRnm]',word) and not re.search('s[aA]M[NYRnm]',word) and not re.search('Mmanya',word):
		if dictionary in dicts and re.search('M[NYRnm]',word):
			anun.append(word+":"+dictionary)
			anunfile.write(word+":"+dictionary+"\n")
		if dictionary in dicts and re.search('[NYRnm][NYRnm]',word):
			mn.append(word+":"+dictionary)
			mnfile.write(word+":"+dictionary+"\n")
	print len(anuwords), "words with anusvAra+consonant pattern."
	print len(mwords), "words with m+consonant pattern."
	print len(anun), "words with anusvAra+nasal pattern."
	print len(mn), "words with m+nasal pattern."
alldicts = ["ACC","CAE","AE","AP90","AP","BEN","BHS","BOP","BOR","BUR","CCS","GRA","GST","IEG","INM","KRM","MCI","MD","MW72","MW","MWE","PD","PE","PGN","PUI","PWG","PW","SCH","SHS","SKD","SNP","STC","VCP","VEI","WIL","YAT"]
for dict in alldicts:
	print dict, "is being handled"
	anu(headwithdicts,dict)	
	print
