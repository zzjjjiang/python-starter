# 
# File: intro-ex-19.py
# Auth: Martin Burolla
# Date: 8/18/2021
# Desc: Frame it.
#

def createSeparator(length):
  retval = ''
  for _ in range(length + 4):
    retval += '*'
  return retval

def createTextLine(word, lenLongestWord):
  retval = ''
  endString = ''
  numSpacesToAdd = lenLongestWord - len(word)
  for _ in range(numSpacesToAdd + 1):
    endString += ' '
  endString += '*'
  retval = f'* {word}{endString}'
  return retval

def main():
  myList = ["Hello", "World", "in", "a", "frame"]
  lenLongestWord = max([(len(word)) for word in myList]) # List comprehension
  print(createSeparator(lenLongestWord))
  for word in myList:
    print(createTextLine(word, lenLongestWord))
  print(createSeparator(lenLongestWord))

if __name__ == "__main__":  
  main()
