

def createList():
  personList = [
      { 'ssn': '222-22-2222' , 'name' : 'charlie', 'weight' : 150 },
      { 'ssn': '333-33-3333' , 'name' : 'bob', 'weight' : 150 },
      { 'ssn': '555-55-5555' , 'name' : 'mary', 'weight' : 140 },
      { 'ssn': '444-44-4444' , 'name' : 'fred', 'weight' : 130 },
      { 'ssn': '111-11-1111' , 'name' : 'alex', 'weight' : 150 }
  ]
  return personList

def sortList(pList):
  pList.sort(key = lambda x : x['name'])
  return pList

def filterList(peopleList):
  return list(filter(lambda x : x['weight'] == 150, peopleList))

def printList(peopleList):
  for p in peopleList:
    print(f"{ p['name']} : {p['weight']}")

def main():
  pList = createList()
  sortedLst = sortList(pList)
  filtered = filterList(sortedLst)
  printList(filtered)

if __name__ == "__main__":  
  main()