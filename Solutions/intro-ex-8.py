# 
# File: intro-ex-8.py
# Auth: Martin Burolla
# Date: 8/16/2021
# Desc: Shortest Straw
#

def main():
  smallestNumber = None
  myList = [6,2,7,3,77,7]
  for number in myList:
    if smallestNumber == None or number < smallestNumber:
      smallestNumber = number
  print(smallestNumber)

if __name__ == "__main__":  
  main()
