from collections import defaultdict

wordDictionary = defaultdict(lambda:0)

file = open("input.txt", "r")
for x in file:
  if len(x) > 1: 
    wordList = x.split()
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

# s = sorted(wordDictionary.items(), key=lambda x: x)

# print(s)

# # l = []
# # for key, value in wordDictionary.items():
# #     temp = [key,value]
# #     l.append(temp)
# # print(l[0])
