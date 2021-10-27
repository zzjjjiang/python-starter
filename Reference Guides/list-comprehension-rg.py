#
# File: list-comprehension-rg.py
# Auth: Martin Burolla
# Date: 8/10/2021
# Desc: List Comprehension Reference Guide
#
# Format: 
#  [{REQUIRED: expression for each item} {REQUIRED: iteration} {OPTIONAL: if condition}]

# PROTIP:
#   If you are filtering and mapping a list, use a list comprehension instead of using the filter() and map() functions.
#       

people = [
  {"firstname": "joe", "lastname": "smith", "age": 30},
  {"firstname": "peter", "lastname": "jones", "age": 40},
  {"firstname": "mary", "lastname": "jane", "age": 50},
  {"firstname": "sue", "lastname": "anderson", "age": 51},
]


def format_name(p):
    return f"{p['firstname'].upper()} {p['lastname'].upper()}"

# Return a list that only contains the first names: ['joe', 'peter', 'mary', 'sue']
l1 = [p['firstname'] for p in people]
print(l1)

# Return a list that only contains the firat names for people over 40: ['mary', 'sue']
l2 = [p['firstname'] for p in people if p['age'] > 40]
#  print(l2)

# Return a list of captialized first names for people over 40: ['MARY JANE', 'SUE ANDERSON']
l3 = [format_name(p) for p in people if p['age'] > 40]
#  print(l3)
