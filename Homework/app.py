from collections import defaultdict

wordDictionary = defaultdict(lambda:0)

file = open("input.txt", "r")
for line in file:
  if len(line) > 1: 
    wordList = line.split()
    for word in wordList:
      if (word[-1] == '.'):
        word = word[:-1]
      word = word.lower()
      count = wordDictionary[word]
      count += 1
      wordDictionary[word] = count

for key in wordDictionary:
  count = wordDictionary[key]
  print(f'{key}:{count}')
