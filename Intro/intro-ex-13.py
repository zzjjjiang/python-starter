# 
# File: intro-ex-13.py
# Auth: Martin Burolla
# Date: 8/17/2021
# Desc: Add Only Calculator
#

def main():
  while (True):
    num1 = input("Enter first integer: ")
    if (num1 == "exit"):
      exit()
    num2 = input("Enter second integer: ")
    if (num2 == "exit"):
      exit()
    print(f'Answer: {int(num1) + int(num2)}.')
    
if __name__ == "__main__":  
  main()
