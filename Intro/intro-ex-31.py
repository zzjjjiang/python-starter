# 
# File: intro-ex-31.py
# Auth: Martin Burolla
# Date: 8/29/2021
# Desc: Map
#

def main():

  carList = [
    { 
      'make': 'ford' , 
      'engine' : { 'size' : 3.0, 'type': 'V6' },
      'cost' : 20000 
    },
    { 
      'make': 'chevy', 
      'engine' : { 'size' : 5.0, 'type': 'V8' },
      'cost' : 23000 
    },
    { 
      'make': 'toyota',
      'engine' : { 'size' : 2.0, 'type': 'Flat 4' },
      'cost' : 24000 
    },
    { 
      'make': 'honda',
      'engine' : { 'size' : 5.2, 'type': 'Straight 6' },
      'cost' : 24000 
    }
  ]
  
  myList = list(map(lambda x : { x['make'] : x['engine']['type'] }, carList))
  print(myList)

if __name__ == "__main__":  
  main()
