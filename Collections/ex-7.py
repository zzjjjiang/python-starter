#
# File: ex-7.py
# Auth: Martin Burolla
# Date: 8/11/2021
# Desc: Length of words.
#

def lengthOfWords(wordString):
  retval = []
  #retval = list(map(lambda x: len(x), wordString.split())) # Functional Python.
  wordList = wordString.split() # Iterative Python.
  for word in wordList:
    retval.append(len(word))
  return retval

def main():
  words = "The quick brown fox jumps over the lazy dog"
  resultList = lengthOfWords(words)
  print(resultList)

if __name__ == "__main__":  
    main()
