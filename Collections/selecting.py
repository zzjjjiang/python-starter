#
# File: selecting.py
# Auth: Martin Burolla
# Date: 8/31/2021
# Desc: 
#

# Collections:
#  - List [] (AKA Arrays)  Selecting syntax is numerical: (e.g. list[2], list[4], etc)
#  - Dictionary {} (AKA Object) Selecting syntax based off of the key: (e.g. dict['lol'])

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
