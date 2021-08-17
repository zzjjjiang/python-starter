# 
# File: intro-ex-2.py
# Auth: Martin Burolla
# Date: 8/16/2021
# Desc: Python in a Box
#

def main():
  w = float(input('Enter width: '))
  h = float(input('Enter height: '))
  l = float(input('Enter length: '))
  volume = (w * h * l)
  volume = round(volume, 2)
  print(f'Volume is: {volume}.')

if __name__ == "__main__":  
  main()

  