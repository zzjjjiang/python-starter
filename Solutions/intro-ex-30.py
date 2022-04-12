# 
# File: intro-ex-30.py
# Auth: Martin Burolla
# Date: 8/29/2021
# Desc: Filter
#

def main():

  carList = [
    { 
      'make': 'ford' , 
      'engine' : { 'size' : 3.0, 'type': 'V6' } 
    },
    { 
      'make': 'chevy', 
      'engine' : { 'size' : 5.0, 'type': 'V8' }
    },
    { 'make': 'toyota',
      'engine' : { 'size' : 2.0, 'type': 'Flat 4' } 
    },
    { 
      'make': 'honda',
      'engine' : { 'size' : 5.2, 'type': 'Straight 6' },
    }
  ]

  myList = list(filter(lambda x : x['engine']['size'] > 4.0, carList))
  for car in myList:
    print(f"{ car['make'] } : { car['engine']['size'] }")

if __name__ == "__main__":  
  main()
