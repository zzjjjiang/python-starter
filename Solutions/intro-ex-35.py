# 
# File: intro-ex-35.py
# Auth: Martin Burolla
# Date: 8/30/2021
# Desc: Map Weight Loss
#

def main():
  personList = [
    { 'ssn': '222-22-2222' , 'name' : 'charlie', 'weight' : 150 },
    { 'ssn': '333-33-3333' , 'name' : 'bob', 'weight' : 150 },
    { 'ssn': '555-55-5555' , 'name' : 'mary', 'weight' : 140 },
    { 'ssn': '444-44-4444' , 'name' : 'fred', 'weight' : 130 },
    { 'ssn': '111-11-1111' , 'name' : 'alex', 'weight' : 150 }
  ]
  
  print(list(map(lambda x: { x['name'] : ['weight'] - 10 }, personList)))

if __name__ == "__main__":  
  main()
