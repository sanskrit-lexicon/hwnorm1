# -*- coding: utf-8 -*-
""" duplicationstats.py

To generate statistics from rxx.txt
Documentation at https://github.com/sanskrit-lexicon/hwnorm1/issues/1
  
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
alldicts = ["ACC","CAE","AP90","AP","BEN","BHS","BOP","BUR","CCS","GRA","GST","IEG","INM","KRM","MCI","MD","MW72","MW","PD","PE","PGN","PUI","PWG","PW","SCH","SHS","SKD","SNP","STC","VCP","VEI","WIL","YAT"]

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
def duplicatedlist():
	global consonants
	output = []
	for con in consonants:
		output.append("r"+con+con)
	return output

def dictdupstats():
	duplicatelist = duplicatedlist()
	rxxstats = codecs.open('conv2/rxxstats.txt','w','utf-8')
	fin = codecs.open('conv2/rxx.txt','r','utf-8')
	data = fin.readlines()
	fin.close()
	dupdicts = ["SKD","VCP","SHS","WIL","YAT","PD"]
	for entry in duplicatelist:
		for dict in dupdicts:
			counter = 0
			for line in data:
				line = line.strip()
				word, dictionary = line.split(':')
				if re.search(entry,word) and dict == dictionary:
					counter += 1
			print entry, "pattern in", dict, "dictionary is", counter, "/", len(data)
			rxxstats.write(entry+" pattern in "+dict+" dictionary is "+str(counter)+" / "+str(len(data))+"\n")
	rxxstats.close()
dictdupstats()	


def dictnodupstats():
	rxstats = codecs.open('conv2/rxstats.txt','w','utf-8')
	fin = codecs.open('conv2/21violation.txt','r','utf-8')
	data = fin.readlines()
	fin.close()
	dupdicts = ["SKD","VCP","SHS","WIL","YAT","PD"]
	rcon = ['r'+con for con in consonants]
	for entry in rcon:
		for dict in dupdicts:
			counter = 0
			for line in data:
				line = line.strip()
				word, dictionary = line.split(':')
				if re.search(entry,word) and dict == dictionary:
					counter += 1
			print entry, "pattern in", dict, "dictionary is", counter, "/", len(data)
			rxstats.write(entry+" pattern in "+dict+" dictionary is "+str(counter)+" / "+str(len(data))+"\n")
	rxstats.close()
#dictnodupstats()	
