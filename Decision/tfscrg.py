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
# Everything else is truthy
#

# https://www.freecodecamp.org/news/truthy-and-falsy-values-in-python/

b1 = True
b2 = False
n1 = 54 # truthy
n2 = None # falsy
n3 = 0  # falsy
n4 = -1 # truthy
n5 = 1  # truthy
l1 = ['red', 'green', 'blue'] # truthy
l2 = [] # falsy
s1 = "" # falsy
s2 = "test" # truthy

if b1 or n3 or b1:
  print('TRUE')
else:
  print('FALSE')

 