# -*- coding: utf-8 -*-
""" proberrors.py

To generate list of potential errors from output of hwnorm1.py
  
"""
import sys, re
import codecs
import string
import datetime

alldicts = ["ACC","CAE","AP90","AP","BEN","BHS","BOP","BUR","CCS","GRA","GST","IEG","INM","KRM","MCI","MD","MW72","MW","PD","PE","PGN","PUI","PWG","PW","SCH","SHS","SKD","SNP","STC","VCP","VEI","WIL","YAT"]
anulist = ["paMqita","annaMBa","laMk","aMkar"]
	
def proberrors(dict,convention):
	if convention == 1:
		fin_anun = codecs.open("conv1/"+dict+"_anunwords.txt","r","utf-8")
		fout_anun = codecs.open("proberrors/anunwords.txt","a","utf-8")
		data = fin_anun.readlines()
		counter1 = 0
		for line in data:
			if not re.search('[sS][aA]M[NYRnm]',line) and not re.search('Mmany[aA][H]*',line) and not re.search('k[Ei]M[NYRmn]',line) and not re.search('puM[NYRmn]',line) and not re.search('idaM[NYRmn]',line) and not re.search('AMniDi',line) and not re.search('ahaM[NYRmn]',line) and not re.search('sAyaM[NYRmn]',line) and not re.search('svayaM[NYRmn]',line) and not re.search('AnAM[NYRmn]',line) and not re.search('apAM[NYRmn]',line) and not re.search('[iE]raM[NYRmn]',line) and not re.search('alaM[NYRmn]',line) and not re.search('evaM[NYRmn]',line) and not re.search('MmAnin',line) and not re.search('AMnetf',line):
				fout_anun.write(line)
				counter1 += 1
		print dict, counter1, "entries written to proberrors/anunwords.txt"
		fin_anun.close()

	
"""	
for dict in alldicts:
	proberrors(dict,1)
"""
