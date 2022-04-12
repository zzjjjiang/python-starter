#
# File: ex-9.py
# Auth: Martin Burolla
# Date: 8/11/2021
# Desc: Joe's Tuple
#

def createTuple(age, name, location):
  retval = (age, name, location)
  return retval

def main():
  myTuple = createTuple(40, 'Joe', 'New York')
  print(myTuple)

if __name__ == "__main__":  
    main()
