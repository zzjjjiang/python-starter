# 
# File: intro-ex-21.py
# Auth: Martin Burolla
# Date: 8/18/2021
# Desc: Blast Off!!!
#

import time

def main():
  countDown = int(input('Enter countdown (sec): '))

  if countDown < 0:
    print("Countdown cannot be negative.")
    exit()

  for x in range(countDown, 0, -1):
    time.sleep(1)
    print(x)
  time.sleep(1)
  print('Blast off!!!')

if __name__ == "__main__":  
  main()
