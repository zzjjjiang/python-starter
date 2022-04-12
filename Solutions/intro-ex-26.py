# 
# File: intro-ex-26.py
# Auth: Martin Burolla
# Date: 8/22/2021
# Desc: Print Dictionary
#

def printDictionary(dictionary):
  ssns = list(dictionary.keys())
  ssns.sort()
  for ssn in ssns:
    print(f'{ssn} : {dictionary[ssn]}')

def main():
  personDictionary = {
   '222-22-2222' : 'joe',
   '333-33-3333' : 'fred',
   '555-55-5555' : 'mary',
   '444-44-4444' : 'fred',
   '111-11-1111' : 'jane'
  }
  printDictionary(personDictionary)
 
if __name__ == "__main__":  
  main()
