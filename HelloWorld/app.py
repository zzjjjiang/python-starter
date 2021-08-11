# 
# File: app.py
# Auth: Martin Burolla
# Date: 8/3/2021
# Desc: Python 101
#

#r = 22 % 10 
#r = 3 * 2 + 2
#print(r)


# Equality vs Identity
l1 = ['1', '2', '3']
l2 = ['1', '2', '3']
l3 = l1
print(l1 is l2) # False Identity
print(l1 is l3) # True Identity
print(l1 == l2) # True Equality, these are different references but they have an equal value.
print(l1 == l3) # True, same reference to one list





