#
# File: selecting.py
# Auth: Martin Burolla
# Date: 8/31/2021
# Desc: 
#

def printList(filtered):
  for person in filtered:
    print(f"{person['name']} : {person['weight']}")

def filterList(sorted):
  filtered = list(filter(lambda x: x['weight'] == 150, sorted))
  return filtered

def sortList(mylist):
  return mylist.sort(key = lambda x: x['name'])
  # return sorted

def createList():
   personList = [
    { 'ssn': '222-22-2222' , 'name' : 'charlie', 'weight' : 150 },
    { 'ssn': '333-33-3333' , 'name' : 'bob', 'weight' : 150 },
    { 'ssn': '555-55-5555' , 'name' : 'mary', 'weight' : 140 },
    { 'ssn': '444-44-4444' , 'name' : 'fred', 'weight' : 130 },
    { 'ssn': '111-11-1111' , 'name' : 'alex', 'weight' : 150 } 
    ]
   return personList

def main():
   list = createList()
   sorted = sortList(list)
   filtered = filterList(sorted)
   printList(filtered) 

if __name__ == "__main__":
    main()
