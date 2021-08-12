#
# File: ex-8.py
# Auth: Martin Burolla
# Date: 8/11/2021
# Desc: Peter's Ford
#

def main():
  carDictionary = {
     'peter': { 'brand' : 'Ford', 'model' : 'Mustang' },
     'paul': { 'brand' : 'Toyota', 'model' : 'Prius' },
     'mary': { 'brand' : 'Chevy', 'model' : 'Corvette' },
  }
  print(f"Peter drives a {carDictionary['peter']['brand']} {carDictionary['peter']['model']}.")

if __name__ == "__main__":  
    main()
