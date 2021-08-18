# 
# File: intro-ex-18.py
# Auth: Martin Burolla
# Date: 8/18/2021

# Desc: Random Number Game
#

from random import randint

def main():
  computerNumber = randint(1,10)

  while(True):
    userNumber = int(input("Enter a number between 1-10: "))
    if (computerNumber == userNumber):
      print('You guessed it!!!!')
      break
    elif (userNumber < computerNumber):
      print('Too low') 
    elif (userNumber > computerNumber):
      print('Too high')

if __name__ == "__main__":  
  main()
