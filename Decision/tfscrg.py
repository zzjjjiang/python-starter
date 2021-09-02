#
# File: tfrg.py
# Auth: Martin Burolla
# Date: 9/2/2021
# Desc: Truthy-Falsy Short-Circuiting Reference Guide (TFSCRG)
#
# Falsy: 
#   False    
#   None    
#   0    
#   ""    
#   ()    
#   []     
#   {}

# https://www.freecodecamp.org/news/truthy-and-falsy-values-in-python/

b1 = True
b2 = False
n1 = 54
n2 = None
n3 = 0
l1 = ['red', 'green', 'blue']
l2 = []
s1 = ""
s2 = "test"

if b1:
  print('TRUE')
else:
  print('FALSE')
