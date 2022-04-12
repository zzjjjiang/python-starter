# 
# File: intro-ex-38.py
# Auth: Martin Burolla
# Date: 8/31/2021
# Desc: 
#

def main():
  numList = [1,2,3,4,5,6,7,8,9,10]
  evenList = list(filter(lambda x: x % 2 == 0, numList))
  doubleList = list(map(lambda x: x * 2, evenList))
  print(doubleList)

  doubleList2 = [n * 2 for n in numList if n % 2 == 0]
  print(doubleList2)

if __name__ == "__main__":  
  main()
