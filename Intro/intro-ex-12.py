# 
# File: intro-ex-12.py
# Auth: Martin Burolla
# Date: 8/17/2021
# Desc: Negative & Positive
#

def main():
  retval = ''
  inputString = input("Enter integer: ").strip()

  if ("." in inputString):
    retval = f'ERROR: {inputString} is not an integer.'
  elif (inputString[0] == "-"):
    retval = inputString[1:len(inputString)] # Slice everything after the minus.
  else:
    retval = "-" + inputString

  print(retval)

if __name__ == "__main__":  
  main()
