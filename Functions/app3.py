# 
# File: app3.py
# Auth: Martin Burolla
# Date: 8/30/2021
# Desc: Functions Review
#

def add(x, y): # This is the function signature.
  return x + y # This is the implementation of this function.

def sub(number1, number2): # This function is not called.
  return number1 - number2

def mySubroutine(): # This function takes nothing, returns nothing (sometimes called a subroutine).
  print('Hello World')

def main():
  r1 = add(1, 3)
  r2 = add(x = 1, y = 3) # Named parameters.
  add(x = 2, y = 5) # Not storing return value into a variable.

  mySmallNumber1 = 4
  mySmallNumber2 = 5
  r3 = add(mySmallNumber1, mySmallNumber2)
  r4 = add(x = mySmallNumber1, y = mySmallNumber2) # Named parameters.

  mySubroutine() 
  
  # Print results.
  print(r1)
  print(r2)
  print(r3)
  print(r4)

if __name__ == "__main__":  
  main()
