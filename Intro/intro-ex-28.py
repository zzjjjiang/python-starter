# 
# File: intro-ex-28.py
# Auth: Martin Burolla
# Date: 8/22/2021
# Desc: Split & Print
#

def splitAndPrint(numList):
  print(f'First half:  { numList[0:len(numList) // 2]}') # https://www.w3schools.com/python/python_operators.asp
  print(f'Second half: { numList[len(numList) // 2:]}')

def main():
  numList = [1,2,3,4,5,6,7,9,10,11]
  splitAndPrint(numList)

if __name__ == "__main__":  
  main()
