"""slp_cmp.py
 Sanskrit sorting. Works for both python2 and python3
 Assumes words to be sorted are in slp1 transliteration of Sanskrit
"""
from __future__ import print_function
import string,sys
pyversion2 = (sys.version_info[0] == 2)
# Note 'L' and '|' and 'Z' and 'V' are not present
# Not sure where they go 
tranfrom="aAiIuUfFxXeEoOMHkKgGNcCjJYwWqLQ|RtTdDnpPbBmyrlvSzsh"
tranto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxy"
# ref: https://stackoverflow.com/questions/41708770/translate-function-in-python-3
if pyversion2:
 trantable = string.maketrans(tranfrom,tranto)
else: #version3 of python
 trantable = str.maketrans(tranfrom,tranto)

def translate_one(a):
 if pyversion2:
  a1 = string.translate(a,trantable)
 else:
  a1 = a.translate(trantable)
 return a1

def slp_cmp(a,b):
 try:
  #a1 = string.translate(a,trantable)
  #b1 = string.translate(b,trantable)
  a1 = translate_one(a)
  b1 = translate_one(b)
 except:
  print("slp_cmp error: a=",a,"b=",b)
  exit(1)
 return cmp(a1,b1)

def unused_slp_sorted_python2(keys,keyFcn=None):
 # for slp_cmp to work (namely, string.translate, need array of ascii keys
 newkeys=[]
 for key in keys:
  if keyFcn != None:
   newkey = keyFcn(key)
  else:
   newkey = key
  try:
   newkey = newkey.decode("utf-8").encode("ascii","ignore")
  except:
   print('slp_sorted_python2 error: key=',key,newkey)
   exit(1)
  newkeys.append(newkey)
 sorted_keys = sorted(newkeys,cmp=slp_cmp)
 return sorted_keys

def slp_sorted_python2(keys,keyFcn=None):
 # for slp_cmp to work (namely, string.translate, need array of ascii keys
 newkeys=[]
 for key in keys:
  if keyFcn != None:
   newkey = keyFcn(key)
  else:
   newkey = key
  try:
   newkey = newkey.decode("utf-8").encode("ascii","ignore")
  except:
   print('slp_sorted_python2 error: key=',key,newkey)
   exit(1)
  newkeys.append(newkey)
 sorted_keys = sorted(newkeys,cmp=slp_cmp)
 return sorted_keys

def slp_sorted_python3(keys,keyFcn=None):
 if keyFcn == None:
  sorted_keys = sorted(keys,key=lambda x: translate_one(x))
 else:
  sorted_keys = sorted(keys,key=lambda x: translate_one(keyFcn(x)))  
 return sorted_keys

def slp_sorted(keys,keyFcn=None):
 if pyversion2:
  return slp_sorted_python2(keys,keyFcn)
 else:
  return slp_sorted_python3(keys,keyFcn)
