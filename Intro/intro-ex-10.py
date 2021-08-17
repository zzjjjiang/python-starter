# 
# File: intro-ex-10.py
# Auth: Martin Burolla
# Date: 8/16/2021
# Desc: Vs and Cs
#

def main():
  vowelCount = 0
  vowels = ['a','e','i','o','u', 'y']
  instring = input('Enter string: ')
  instring = instring.lower()

  for idx in range(len(instring)):
    if (instring[idx] in vowels):
      vowelCount += 1

  print(f'Vowels: {vowelCount}')
  print(f'Consonants: {len(instring) - vowelCount}')

if __name__ == "__main__":  
  main()
