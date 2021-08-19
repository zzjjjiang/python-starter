# 
# File: intro-ex-20.py
# Auth: Martin Burolla
# Date: 8/19/2021
# Desc: Super Simple File Indexer
#

import string

def removePunctuation(dirtyWord):
  retval = dirtyWord
  return retval

def cleanWordList(dirtyWordList):
  retval = []
  for dirtyWord in dirtyWordList:
    if len(dirtyWord) > 0 and dirtyWord != '\n':
      cleanWord = removePunctuation(dirtyWord)
      retval.append(cleanWord)
  return retval
  
def main():
  wordDictionary = {}

  f = open("input-file-1.txt")
  lines = f.readlines()
  for line in lines:
    wordList = line.split(' ')
    wordList = cleanWordList(wordList)
    for word in wordList:
        if word not in wordDictionary:
          wordDictionary[word] = 1
        else:
          count = wordDictionary[word]
          wordDictionary[word] += count

  for key in wordDictionary:
    print(f'{key}:{wordDictionary[key]}')
  f.close()

if __name__ == "__main__":  
  main()
