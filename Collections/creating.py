#
# File: creating.py
# Auth: Martin Burolla
# Date: 8/31/2021
# Desc: Creating Reference Guide (CRG)
#

################################################################
# Dictionaries
################################################################
d0 = dict() # An empty dictionary
d1 = {}  # An empty dictionary
d2 = { 'lol' : 'Laugh out loud' } # Dictionary with one key/value pair.
d3 = { 
  'lol' : 'Laugh Out loud', 
  'brb' : 'Be Right Back'  
}
d3['afaik'] = 'As Far As I Know' # Add a new key/value pair to d3
d3['afk'] = 'Away From Keyboard' # Add a new key/value pair to d3
del d3['afk'] # Delete a key
print(f'Dict: {d3}')

################################################################
# Lists
################################################################
l0 = list() # An empty list
l1 = [] # An empty list
l2 = ['red', 'yellow', 'green']
l2.append('orange') # Add item to list
l2.append('purple')
l2.remove('purple') # Remove item from list
print(f'List: {l2}')

################################################################
# Sets
################################################################
s0 = set() # An empty set.
s1 = {'red', 'yellow', 'green'}
s1.add('orange') # Add item to set.
s1.add('purple')
s1.remove('purple') # Remove item from set.
# s1[0] # Not available with Set.
print(f'Set: {s1}')
