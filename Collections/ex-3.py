#
# File: ex-2.py
# Auth: Martin Burolla
# Date: 8/10/2021
# Desc: Add ages.
#

def addAges(peopleList):
  retval = 0
  #retval = sum(list(map(lambda x: x['age'], peopleList))) # Functional Python.
  for person in peopleList: # Iterative Python.
    retval += person['age']
  return retval

def main():
  peopleList = [
    { 'name':'Peter', 'age': 20 },
    { 'name':'Paul',  'age': 30 },
    { 'name':'Mary',  'age': 40 },
  ]
  total = addAges(peopleList)
  print(total)

if __name__ == "__main__":  
    main()
