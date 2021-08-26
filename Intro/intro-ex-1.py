# 
# File: intro-ex-1.py
# Auth: Martin Burolla
# Date: 8/16/2021
# Desc: Sum of Random Numbers
#

import random

def main():
  myList = []
  for _ in range(0, 10):
    myList.append(random.randint(1, 101))
  total = sum(myList)
  print(f'The sum is: {total}')

if __name__ == "__main__":  
  main()