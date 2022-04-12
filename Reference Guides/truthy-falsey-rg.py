#
# File: truthy-falsey-rg.py
# Auth: Martin Burolla
# Date: 9/2/2021
# Desc: Truthy-Falsy Short-Circuiting Reference Guide
# Overview:
#   Falsy:
#     False
#     None
#     0
#     ""
#     ()
#     []
#     {}
#   Everything else is truthy
#
# Reference: https://www.freecodecamp.org/news/truthy-and-falsy-values-in-python/
#

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
d1 = {} # falsy
d2 = { 'lol' : 'Laugh Out Loud' } # truthy


if b1:
  print('TRUE')
else:
  print('FALSE')

# n6 = 33
# l1 = ['a', 'b', 'c']
# rr =l1.append('d')
# print(rr)

# if (l1.append('d') or l1.append('e') or n6 or l1.append('f')): # l1.append('f') is never called.
#   print('TRUE')
# else:
#   print('FALSE')
# print(l1) # ['a', 'b', 'c', 'd', 'e']
