# 
# File: intro-ex-41.py
# Auth: Martin Burolla
# Date: 9/1/2021
# Desc: Mask SSN
#

def maskSSN(person):
  person.update({'ssn' : 'xxx-xx-xxxx'}) # in-place update.
  return person

def main():
  peopleList = [
    { 'ssn' : '222-22-2222' , 'name' : 'charlie' },
    { 'ssn' : '333-33-3333' , 'name' : 'bob' },
    { 'ssn' : '555-55-5555' , 'name' : 'mary' },
    { 'ssn' : '444-44-4444' , 'name' : 'fred' },
    { 'ssn' : '111-11-1111' , 'name' : 'alex' }
  ]
  #print(list(map(maskSSN, peopleList)))
  print(list(map(lambda x: x.update({ 'ssn' : 'xxx-xx-xxxx' }) or x, peopleList))) # short-circuit.

if __name__ == "__main__":  
  main()
