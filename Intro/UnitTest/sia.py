# 
# File: sia.py
# Auth: Martin Burolla
# Date: 9/5/2021
# Desc: Business Logic
#

def addNumbers(a, b):
   return a + b

def concatStrings(a, b):
   return a + b

def doubleList(list):
   return [item * 2 for item  in list]

# Write test cases for these...

def sortList(list):
   return list.sort() or list

def dedupeList(aList):
   retval = []
   s1 = set(aList)
   retval = list(s1)
   return retval






