# 
# File: lambda-filter-map.py
# Auth: Martin Burolla
# Date: 10/6/2021
# Desc: 
#

def add5(x):
  return x + 5

r = add5(5)

def add(x,y,z):
  return x + y + z

# r = add(1,2)
#print(r)
#print(add(1,2))

# https://youtu.be/Ob9rY6PQMfI

add = lambda x, y, z : x + y + z
# r = add(1,2)
# print(r)
# FORMAT: lambda <INPUT ARGS> : <OUTPUT EXPRESSION> ONE

peopleList = [
  { 'name' : 'fred', 'age' : 20, 'weight': 160, 'sex' : 'male', 'id' : 1 },
  { 'name' : 'mary', 'age' : 10, 'weight': 130, 'sex' : 'male', 'id' : 2 },
  { 'name' : 'sue', 'age' : 15, 'weight': 120, 'sex' : 'female', 'id' : 3 },
]

# [] = List => Selecting is done by index (e.g. myList[1])
# {} = Dictionary (or set) => selecting is done by key (e.g. myDict['theKey'])

sortLambdaFunc = lambda p : p['weight']

def mySortFunction(x):
  return x['weight']

# peopleList.sort(key = lambda p : p['weight']) # Inline Lambda, in-place sort.
# peopleList.sort(key = sortLambdaFunc) # Lambda function defined elsewhere, in-place sort.
# peopleList.sort(key = mySortFunction) # No lambda, native python function, in-place sort.
# print(peopleList)

# Declarative programming is a programming paradigm … that expresses the logic of a computation without describing its control flow.
# Imperative programming is a programming paradigm that uses statements that change a program’s state.

# myList = list(filter(lambda p : p['age'] >= 15, peopleList))
# print(myList)

# [{'name': 'fred', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1}, 
# {'name': 'mary', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2}, 
# {'name': 'sue', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3}]

# l = list(map(lambda x : { 'short_name' : x['name'], 'new_age': x['age'] + 1 }, peopleList))
# l = sum(list(map(lambda x : x['age'], peopleList)))
# print(l)

# [{'short_name': 'fred', 'new_age': 21}, 
# {'short_name': 'mary', 'new_age': 11}, 
# {'short_name': 'sue', 'new_age': 16}]

def getNickname(id):
  retval = ''
  nnDict = {
    1 : "Freddy",
    2 : "Mary Jane",
    3 : "Suzie Q"
  }
  retval = nnDict[id]
  return retval

def transformPerson(person):
  retval = { 
    'short_name' : person['name'], 
    'new_age' : person['age'] + 1,
    'the_weight' : person['weight'],
    'sex' : 'M' if person['sex'] == 'male' else 'F' # inline if
    }
  retval['nick_name'] = getNickname(person['id'])
  return retval


l = list(map(transformPerson, peopleList))
#print(l)

# [{'short_name': 'fred', 'new_age': 21, 'the_weight': 160, 'sex': 'M', 'nick_name': 'Freddy'}, 
# {'short_name': 'mary', 'new_age': 11, 'the_weight': 130, 'sex': 'M', 'nick_name': 'Mary Jane'}, 
# {'short_name': 'sue', 'new_age': 16, 'the_weight': 120, 'sex': 'F', 'nick_name': 'Suzie Q'}]

# [
#   {'short_name': 'fred', 'new_age': 21, 'the_weight': 160, 'sex': 'M', 'nick_name': 'Freddy'}, 
#   {'short_name': 'mary', 'new_age': 11, 'the_weight': 130, 'sex': 'M', 'nick_name': 'Mary Jane'}, 
#   {'short_name': 'sue', 'new_age': 16, 'the_weight': 120, 'sex': 'F', 'nick_name': 'Suzie Q'}
# ]
