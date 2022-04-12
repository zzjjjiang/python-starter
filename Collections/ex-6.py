#
# File: ex-6.py
# Auth: Martin Burolla
# Date: 8/11/2021
# Desc: Create, Sum and Sammy
#

def createList():
  return [*range(1, 11, 1)] # Unpacking operator: https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/

def sumList(list):
  return sum(list)

def main():
  list = createList()
  total = sumList(list)
  print(f"I can't drive {total}.")

if __name__ == "__main__":  
    main()
