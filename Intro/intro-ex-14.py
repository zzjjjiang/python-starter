# 
# File: intro-ex-14.py
# Auth: Martin Burolla
# Date: 8/17/2021
# Desc: Forever Calculator
#

def shouldExit(inStr):
  return inStr == "exit"

def main():
    while (True):
      result = 0
      operand1 = input("Enter first integer: ")
      if shouldExit(operand1):
        break
      operand2 = input("Enter second integer: ")
      if shouldExit(operand2):
        break
      operation = input("Enter operation (add, sub, mul, div): ")
      if shouldExit(operation):
        break

      operand1 = float(operand1)
      operand2 = float(operand2)

      if (operation == 'add'):
        result = operand1 + operand2
      elif (operation == 'sub'):
        result = operand1 - operand2
      elif (operation == 'div'):
        try:
          result = operand1 / operand2
        except ZeroDivisionError:
          result = 0
      elif (operation == 'mul'):
        result = operand1 * operand2

      print(f'Answer: {result}')
      
    exit()

if __name__ == "__main__":  
  main()
