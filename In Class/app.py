# 
# File: app.py
# Auth: Martin Burolla
# Date: 8/3/2021
# Desc: In class notes.
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

##############################################################################
# 8/16/2021
##############################################################################

# JSON (Javascript Object Notation)
# List <=> Array
# Dictionary <=> Object
# KEY : VALUE ==> (null, number, string, boolean, list, dict)
# Online JSON Viewers: 
#   http://jsonviewer.stack.hu/
#   https://jsonformatter.org/json-viewer
#

from os import killpg
from typing import Dict


kitchenDictionary = {
    "Fridge" : 1,
    "Stove" : "silver",
    "Trash Compactor" : False,
    "Oven" : [ "silver", "whirlpool", "large" ],
    "Oven2" : [ { "color" : "silver" }, { "make" : "Whirlpool" }, { "size" : "large" } ],
    "Microwave" : { "make" : "whirlpool" }
  }

# # Get all the keys in a dictionary.
# for k in kitchenDictionary.keys():
#   print(k)

# # Check if a key exists in a dictionary.
# if "Thing" in kitchenDictionary:
#   print('YES')
# else: 
#   print('NO')

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

# import requests
# print(requests.get('http://www.google.com').content) 

# import random
# print(random.randint(0, 10))

##############################################################################
# 8/17/2021
##############################################################################

# Three ways of creating stings...
# s1 = "Marty's test"
# s2 = 'test'
# s3 = '''
#   this is a test
#   this is another string
#   and here we are
#   **********
#   ##$I&(*&)
# '''

# Hashing
# YT: https://youtu.be/2BldESGZKB8
# NOT Encryption
# "One way hash"
#  - PWD
#  - Signing 
#  - DeDupe

# import hashlib

# password = 'SongA.mp3'
# passwordHash = hashlib.md5(password.encode()).hexdigest()
# print(passwordHash)

#
# My computer test.py ==> Internet ==>  AWS
#
# Boto3 (Python lib)
# - private secret: 123
#
# Request
# - Type: PUT
# - Body: Hello World
# - Signature: 446bad0cc3cf4ab377e655db3d11d382

#
# My Computer    ===>  AWS S3
# Marty: SongA.mp3     hash: 58b5428a6dd575ae154e9704303e871c 
# Jason: SongA.mp3     hash: 58b5428a6dd575ae154e9704303e871c   
# 
# Table:
# Marty SongA.mp3 58b5428a6dd575ae154e9704303e871c resides: 0X2323
# Jason SongA.mp3 58b5428a6dd575ae154e9704303e871cSongA.



# AWS HASH: 446bad0cc3cf4ab377e655db3d11d382

# a6309881d9962e3eac73ae456351aac5
# cb6e3360990811e6eb0cdc9c556e24a7

# MD5: 9c87baa223f464954940f859bcf2e233
# SHA1: 1cf4c502ddd89b918c4bfefea76dadd590693b48
# SHA256: 6e659deaa85842cdabb5c6305fcc40033ba43772ec00d45c2a3c921741a5e377
# SHA512: f58d2a3eea606202c580591f1af9bed15298576c44094d579aa18df2defa6e1eb3b749783a551af5b619a32758fe0e9b0fcd30ffd0ca8a34ca5b7907055a1c36


# myDictionary = {
#   "LOL" : "Laugh out loud",
#   "BRB" : "Be right back", 
#   "IDK" : "I don't know"
# }

# # Adding to dictionary:
# myDictionary["AFAIK"] = "As far as I know"

# # Print key/values from dictionary:
# for key in myDictionary:
#   print(f"{key}:{myDictionary[key]}")
  


# print ('')

# def printWords(wordlist):
#     size = max(len(word) for word in wordlist)
#     print('*' * (size + 4))
    
#     for word in wordlist:
#        print('* {:<{}} *'.format(word, size)) # :<{}
#     print('*' * (size + 4))

# def main():
#    wordlist = ["Hello", "World", "in", "a", "frame"]
#    printWords(wordlist)

# if __name__ == "__main__":
#     main()

#####################################################################################
# LAMBDA
#####################################################################################

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

#peopleList.sort(key = lambda p : p['weight']) # Inline Lambda, in-place sort.
# peopleList.sort(key = sortLambdaFunc) # Lambda function defined elsewhere, in-place sort.
# peopleList.sort(key = mySortFunction) # No lambda, native python function, in-place sort.
# print(peopleList)

# Declarative programming is a programming paradigm … that expresses the logic of a computation without describing its control flow.
# Imperative programming is a programming paradigm that uses statements that change a program’s state.

#myList = list(filter(lambda p : p['age'] >= 15, peopleList))
# print(myList)


# [{'name': 'fred', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1}, 
# {'name': 'mary', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2}, 
# {'name': 'sue', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3}]

#l = list(map(lambda x : { 'short_name' : x['name'], 'new_age': x['age'] + 1 }, peopleList))
#l = sum(list(map(lambda x : x['age'], peopleList)))
#print(l)


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
print(l)

# [{'short_name': 'fred', 'new_age': 21, 'the_weight': 160, 'sex': 'M', 'nick_name': 'Freddy'}, 
# {'short_name': 'mary', 'new_age': 11, 'the_weight': 130, 'sex': 'M', 'nick_name': 'Mary Jane'}, 
# {'short_name': 'sue', 'new_age': 16, 'the_weight': 120, 'sex': 'F', 'nick_name': 'Suzie Q'}]

# [
#   {'short_name': 'fred', 'new_age': 21, 'the_weight': 160, 'sex': 'M', 'nick_name': 'Freddy'}, 
#   {'short_name': 'mary', 'new_age': 11, 'the_weight': 130, 'sex': 'M', 'nick_name': 'Mary Jane'}, 
#   {'short_name': 'sue', 'new_age': 16, 'the_weight': 120, 'sex': 'F', 'nick_name': 'Suzie Q'}
# ]

#############################################################################
# Exceptions
#############################################################################

# https://www.youtube.com/watch?v=NIWwJbo-9_8

# try:
#   r = 8 / 0

# except ZeroDivisionError as z:  # More specific exception towards the top.
#   # pass DO NOT DO THIS.
#   print(f"Zero Division Error: {z}")

# except Exception as e: # Make sure this is last.
#   print(f"Exception: {e}")

# finally:
#   print("Done")

# Key messages:
# - Do not swallow exceptions
# - Put more specific message at the top
# 