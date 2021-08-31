# 
# File: intro-ex-32.py
# Auth: Martin Burolla
# Date: 8/30/2021
# Desc: Create, Sort, Filter, Print
#

def createList():
  personList = [
    { 'ssn': '222-22-2222' , 'name' : 'charlie', 'weight' : 150 },
    { 'ssn': '333-33-3333' , 'name' : 'bob', 'weight' : 150 },
    { 'ssn': '555-55-5555' , 'name' : 'mary', 'weight' : 140 },
    { 'ssn': '444-44-4444' , 'name' : 'fred', 'weight' : 130 },
    { 'ssn': '111-11-1111' , 'name' : 'alex', 'weight' : 150 }
  ]
  return personList

def sortList(list):
  list.sort(key = lambda x: x['name']) # Update the list that is currently in memory.
  return list
  #return sorted(list, key = lambda x: x['name']) # Create a new list in memory.

def filterList(peopleList):
  return list(filter(lambda x: x['weight'] == 150, peopleList)) # Creates a new list in memory.

def printList(peopleList):
  for p in peopleList:
    print(f"{ p['name'] } : {p['weight']} ")

def main():
  list = createList()
  sortedList = sortList(list)
  filtered = filterList(sortedList)
  printList(filtered)

  # Print IDs of list.
  # print(id(list))
  # print(id(sortedList))
  # print(id(filtered))

if __name__ == "__main__":  
  main()
