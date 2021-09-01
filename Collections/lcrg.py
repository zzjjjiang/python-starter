#
# File: lcrg.py
# Auth: Martin Burolla
# Date: 8/10/2021
# Desc: List Comprehension Reference Guide (LCRG)
#
# Format: 
#  [{REQUIRED: expression for each item} {REQUIRED: iteration} {OPTIONAL: if condition}]
#
# PROTIPs: 
#   If you are filtering and mapping on a list, use a list comprehension 
#   instead of using the filter() and map() functions.
#       

people = [
  { "firstname": "joe", "lastname" : "smith", "age": 30 },
  { "firstname": "peter", "lastname" : "jones", "age": 40 },
  { "firstname": "mary", "lastname" : "jane", "age" : 50 },
  { "firstname": "sue", "lastname" : "anderson", "age" : 51 },
]

def formatName(p):
  return f"{p['firstname'].upper()} {p['lastname'].upper()}"

l1 = [p['firstname'] for p in people]
print(l1) # ['joe', 'peter', 'mary', 'sue']

l2 = [p['firstname'] for p in people if p['age'] > 40]
print(l2) # ['mary', 'sue']

l3 = [formatName(p) for p in people if p['age'] > 40]
print(l3) # ['MARY JANE', 'SUE ANDERSON']
