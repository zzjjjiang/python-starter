# 
# File: intro-ex-25.py
# Auth: Martin Burolla
# Date: 8/22/2021
# Desc: Count Case
#

def main():
  inputString = input('Enter text: ')
  numUppercase = 0
  numLowercase = 0
  for char in inputString:
    if char.isupper():
      numUppercase += 1
    elif char.islower():
      numLowercase += 1
    else:
        pass
  print(f'Upper case: {numUppercase}')
  print(f'Lower case: {numLowercase}')

if __name__ == "__main__":  
  main()
