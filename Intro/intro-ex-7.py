# 
# File: intro-ex-7.py
# Auth: Martin Burolla
# Date: 8/16/2021
# Desc: Winner Winner
#

from random import randint

def main():
  retval = ""
  num = randint(1, 100)
  if (num < 10):
    retval = f'{num}: You lose.'
  elif (num > 10 and num < 50):
    retval = f'{num}: Try again.'
  elif (num > 50):
    retval = f'{num}: You win!'
  print(retval)

if __name__ == "__main__":  
  main()
