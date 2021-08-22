# 
# File: intro-ex-27.py
# Auth: Martin Burolla
# Date: 8/22/2021
# Desc: Print Person
#

def _lambda(x):
  return x['age']

def printPersonList(peopleList):
  peopleList.sort(key = lambda x : x['age']) # Lambda functions: https://www.youtube.com/watch?v=Ob9rY6PQMfI
  for person in peopleList:
    name = person['name']
    age = person['age']
    print(f'{ name } : { age } ')

def main(): 
  personList = [
    { 'name' : 'joe', 'age' : 20 },
    { 'name' : 'fred', 'age' : 10 },
    { 'name' : 'sally', 'age' : 30},
    { 'name' : 'sue', 'age' : 15},
  ]

  printPersonList(personList)
 
if __name__ == "__main__":  
  main()
