#
# File: ex-9.py
# Auth: Martin Burolla
# Date: 8/11/2021
# Desc: 
#

def createTuple(age, name, location):
  retval = (age, name, location)
  return retval

def main():
  r = createTuple(40, 'Joe', 'New York')
  print(r)

if __name__ == "__main__":  
    main()
