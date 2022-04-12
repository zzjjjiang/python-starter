# 
# File: intro-ex-20.py
# Auth: Martin Burolla
# Date: 8/19/2021
# Desc: Super Simple File Indexer
#

import string

def cleanWordList(dirtyWordList):
  '''
  Accepts a list of dirty words and returns a list of clean words.
  '''
  retval = []
  for dirtyWord in dirtyWordList:
    if dirtyWord != '\n' and dirtyWord != '':
      cleanerWord = dirtyWord.replace('\n', '')
      cleanWord = cleanerWord.strip(string.punctuation)
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

  for key in sorted(wordDictionary.keys()):
    print(f'{key}:{wordDictionary[key]}')
  f.close()

if __name__ == "__main__":  
  main()
