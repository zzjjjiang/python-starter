# 
# File: intro-ex-13.py
# Auth: Martin Burolla
# Date: 8/17/2021
# Desc: Add Only Calculator
#

def shouldExit(inStr):
  return inStr == "exit"

def main():
  while (True):
    operand1 = input("Enter first integer: ")
    if shouldExit(operand1):
      break
    operand2 = input("Enter second integer: ")
    if shouldExit(operand2):
      break
    print(f'Answer: {int(operand1) + int(operand2)}.')
  exit()
  
if __name__ == "__main__":  
  main()
