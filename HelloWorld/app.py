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
# l1 = ['1', '2', '3']
# l2 = ['1', '2', '3']
# l3 = l1
# print(l1 is l2) # False Identity
# print(l1 is l3) # True Identity
# print(l1 == l2) # True Equality, these are different references but they have an equal value.
# print(l1 == l3) # True, same reference to one list


# a = 1
# b = "string"
# print(a + b)

# acronyms = { 
#   'LOL' : "Laugh out loud",
#   'IDK' : "I don't know",
#   'BRB' : "Be right back"
# }
# print(acronyms[0])


# <class 'list'>
# <class 'set'>
# <class 'dictionary'>

# import hashlib
# result = hashlib.md5(b'GeeksforGeeks')
# print(result.hexdigest())

# Mutable vs Immuatable
# s = "test"  # string
# l = [1,2,3] # list

# print(id(l))
# print(id(s))

# l.append('4')
# s = "test222"

# print(id(l))
# print(id(s))

# a = 1
# b = "string"
# print(a + b)

#print(b + "test" + str(a))






# JSON (Javascript Object Notation)
# List <=> Array
# Dictionary <=> Object
# KEY : VALUE ==> (null, number, string, boolean, list, dict)
# Online JSON Viewers: 
#   http://jsonviewer.stack.hu/
#   https://jsonformatter.org/json-viewer
#

kitchenDictionary = {
    "Fridge" : 1,
    "Stove" : "silver",
    "Trash Compactor" : False,
    "Oven" : [ "silver", "whirlpool", "large" ],
    "Oven2" : [ { "color" : "silver" }, { "make" : "Whirlpool" }, { "size" : "large" } ],
    "Microwave" : { "make" : "whirlpool" }
  }

#print(kitchenDictionary["Fridge"])
#print(kitchenDictionary["Stove"])
#print(kitchenDictionary["Trash Compactor"])
#print(kitchenDictionary["Oven"][2])
#print(kitchenDictionary["Oven2"][2]["size"])
#print(kitchenDictionary["Microwave"]["make"])

# Family room
# Office
# Garage
# Bathroom
# Master Bed
# Home theater
# Gym
# Dining room
# Kids room
# Attic

# def test2(l):
#   l.append(4)

# def test(i):
#   i = 10
#   return i

# i = 0
# l = [1,2,3]
# test(i)
# test2(l)
# print(i)
# print(l)


# a = 1
# b = "string"
# print(a + b)

# a = 1
# b = 2
# print(a == b)