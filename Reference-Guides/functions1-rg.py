#
# File: functions1-rg.py
# Auth: Martin Burolla
# Date: 10/6/2021
# Desc: Functions Review
#

# Function Name: add
# Parameters: x,y
# Arguments: 1,2
# State: Called by main() function
def add(x,y): # Add() is a function that takes/accepts two parameters and returns a value.
  return x + y

# Function Name: sub
# Parameters: x,y
# Arguments: N/A (Because nothing is calling/consuming this function)
# State: Defined, but not called (not used)
def sub(x,y): # Sub() is a function that takes/accepts two parameters and returns a value.
  return x - y

# Function Name: getMessage
# Parameters: Nothing
# Arguments: Nothing
# State: Defined but not called
def getMessage(): # getMessage() is a function that returns a value.
  return "Hello World"

# Function Name: printMessage
# Parameters: Nothing
# Arguments: Nothing
# State: Defined by not called
# Returns: None
def printMessage(): # printMessage() is a function (AKA subroutine) that accepts nothing and returns nothing.
  print("Hello World")
  return "Hi Jason"

# Function Name: main
# Parameters: Nothing
# Arguments: Nothing
# State: Called by Python 
# Returns: None
def main():
  num = add(1,2) # The main() function is calling the add() function and passing in two arguments.
  print(num)
  #print(printMessage) # Be sure to include parenthesis when calling functions: <function printMessage at 0x111025af0>
  
if __name__ == "__main__":
  main()
