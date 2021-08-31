numDict = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four'
  }

numList = [1,2,3,4]

print(list(map(lambda x:numDict[x], numList))[::-1])
