#
# File: ex-4.py
# Auth: Martin Burolla
# Date: 8/10/2021
# Desc: Cars for the people.
#

def getCarsForPeople(carDictionary, peopleList):
  retval = ''
  for person in peopleList:
    retval += (carDictionary[person]['model']) + ', '
  retval = retval[:len(retval)-2] # Lop off last comma.
  return retval

def main():
  carDictionary = {
     'peter': { 'brand' : 'Ford', 'model' : 'Mustang' },
     'paul': { 'brand' : 'Toyota', 'model' : 'Prius' },
     'mary': { 'brand' : 'Chevy', 'model' : 'Corvette' },
   }
  peopleList = ['peter', 'mary']
  models = getCarsForPeople(carDictionary, peopleList)
  print(models)

if __name__ == "__main__":  
    main()
