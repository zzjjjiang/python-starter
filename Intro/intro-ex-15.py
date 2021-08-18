# 
# File: intro-ex-15.py
# Auth: Martin Burolla
# Date: 8/17/2021
# Desc: Forever Calculator Logger
#

from datetime import datetime

def shouldExit(inStr):
  return inStr == "exit"

def main():
    f = open("output.txt", "w")
  
    while (True):
      result = 0
      operand1 = input("Enter first integer: ")
      if shouldExit(operand1):
        break
      operand2 = input("Enter second integer: ")
      if shouldExit(operand2):
        break
      operation = input("Enter operation (add, sub, mul, div): ")
      shouldExit(operation)

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

      todaysDate = datetime.today().strftime('%m/%d/%Y %I:%M:%S %p')
      f.write(f"{todaysDate}: {operand1} {operation} {operand2} = {result}\n")
      print(f'Answer: {result}')

    f.close()
    exit()

if __name__ == "__main__":  
  main()
