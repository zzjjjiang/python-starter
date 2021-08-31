# 
# File: intro-ex-36.py
# Auth: Martin Burolla
# Date: 8/31/2021
# Desc: Map Number Lookup
#

def main():

  numDict = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four'
  }
  numList = [1,2,3,4]
  
  numList.sort(reverse=True)
  print(list(map(lambda x: numDict[x], numList)))

if __name__ == "__main__":  
  main()
