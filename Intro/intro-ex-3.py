# 
# File: intro-ex-3.py
# Auth: Martin Burolla
# Date: 8/16/2021
# Desc: First and Last
#

def main():
  retval = False
  inputString = input('Enter list of numbers: ')
  myList = inputString.split(',')
  first = myList[0].strip()
  last = myList[-1].strip()
  if first == last:
    retval = True
  print(retval)

if __name__ == "__main__":  
  main()
