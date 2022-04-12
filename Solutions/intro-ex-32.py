# 
# File: intro-ex-32.py
# Auth: Martin Burolla
# Date: 8/29/2021
# Desc: Filter & Map
#

def createPeopleList():
  retval = [
    { 
      'name': 'joe', 
      'sex': 'male'
    },
    { 
      'name': 'fred', 
      'sex': 'male' 
    },
    { 
      'name': 'sue', 
      'sex': 'female' 
    } 
  ]
  return retval

def filterPeopleList(peopleList):
  return list(filter(lambda x : x['sex'] == 'male', peopleList))

def main():
  peopleList = createPeopleList()
  filteredPeopleList = filterPeopleList(peopleList)
  
  for person in filteredPeopleList:
    print(f"{ person['name'] }")

if __name__ == "__main__":  
  main()