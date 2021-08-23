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

import hashlib

password = 'SongA.mp3'
passwordHash = hashlib.md5(password.encode()).hexdigest()
print(passwordHash)

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
  
# Lambda functions
# def add(x,y):
#   return x + y

# add = lambda x,y : x + y # "lambda" <INPUT> : <EXPRESSION> 
# print(add(1,2))

peopleList = [
  { 'name': 'fred', 'age' : 20, 'weight': 160 },
  { 'name': 'mary', 'age' : 10, 'weight': 130 },
  { 'name': 'sue', 'age' : 15, 'weight': 120 },
]

peopleList.sort(key = lambda x : x['weight'])
print(peopleList)

# l = list(filter(lambda x : x['age'] >= 15, peopleList))
# print(l)


 