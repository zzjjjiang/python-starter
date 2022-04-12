# 
# File: intro-ex-12.py
# Auth: Martin Burolla
# Date: 8/17/2021
# Desc: Negative to Positive / Positive to Negative
#

def main():
  retval = ''
  inputString = input("Enter integer: ").strip()

  if ("." in inputString): # Validation.
    retval = f'ERROR: {inputString} is not an integer.'
  elif (inputString[0] == "-"):
    retval = inputString[1:len(inputString)] # Return everything after the minus.
  else:
    retval = "-" + inputString

  print(retval)

if __name__ == "__main__":  
  main()
