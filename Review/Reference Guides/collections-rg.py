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

################################################################
# Tuples
################################################################
t = () # Empty tuple
tuple = (1,2,3,4) # Tuples are immutable once created.
tupleList = [(1,2,3,4), (1,2)]
tupleList.append((5,6,7)) # Appending a tuple to a list.
#print(tupleList[1][2]) # Key Error
print(tupleList[0][2]) # Returns 3

#
# File: selecting.py
# Auth: Martin Burolla
# Date: 8/31/2021
# Desc: Selection Reference Guide (SRG)
#

# Collections:
#  - List [] (AKA Arrays)  Selecting syntax is numerical: (e.g. list[2], list[4], etc)
#  - Dictionary {} (AKA Object) Selecting syntax based off of the key: (e.g. dict['lol'])

# Note: Zero is first position.

colors = ['red', 'green', 'blue'] # This is a List(Array) of colors
#print(colors[0])

peopleList = [ # Is a List of dictionary object.
  { 'name' : 'fred', 'age' : 20, 'weight': 160, 'sex' : 'male', 'id' : 1 },
  { 'name' : 'mary', 'age' : 10, 'weight': 130, 'sex' : 'male', 'id' : 2 },
  { 'name' : 'sue', 'age' : 15, 'weight': 120, 'sex' : 'female', 'id' : 3 },
]

# print(peopleList[0])         # Returns: {'name': 'fred', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1}
# print(peopleList[0]['name']) # Returns fred

carList = [
  { 
    'make': 'toyota',
    'cost' : 24000, 
    'engine' : 
      { 
        'size' : 2.0, 
        'type': 'Flat 4' 
      },
  },
  { 
    'make': 'ford',
    'cost' : 25000,
    'engine' : 
      { 
        'size' : 3.0, 
        'type': 'Flat 6' 
      }
  }
]
print(carList[0]) # Returns: {'make': 'toyota', 'cost': 24000, 'engine': {'size': 2.0, 'type': 'Flat 4'}}
print(carList[0]['engine']['size']) # Returns: 2.0
