# 
# File: intro-ex-19.py
# Auth: Martin Burolla
# Date: 8/18/2021
# Desc: Frame it.
#

from hashlib import md5


def createSeparator(length):
  retval = ''
  for _ in range(length + 4):
    retval += '*'
  return retval

def createTextLine(word, lenLongestWord):
  retval = ''
  endString = ''
  numSpacesToAdd = (lenLongestWord - len(word)) + 1
  for _ in range(numSpacesToAdd):
    endString += ' '
  endString += '*'
  retval = f'* {word}{endString}'
  return retval

def main():
  wordList = ["Hello", "World", "in", "a", "frame"]
  #lenLongestWord = max([(len(word)) for word in wordList]) # Functional Python: List comprehension
  lenLongestWord = 0 # Iterative Python
  for word in wordList:
    if len(word) > lenLongestWord:
      lenLongestWord = len(word)
  print(createSeparator(lenLongestWord))
  for word in wordList:
    print(createTextLine(word, lenLongestWord))
  print(createSeparator(lenLongestWord))

if __name__ == "__main__":  
  main()
