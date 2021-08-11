#
# File: ex-2.py
# Auth: Martin Burolla
# Date: 8/10/2021
# Desc: Remove dupes.
#

def removeDups(list1, list2):
  retval = []
  s1 = set(list1)
  s2 = set(list2)
  retval = list(s1 | s2)
  retval.sort(reverse=True)
  return retval

def main():
  list1 = [7,6,5,4,3,2,1]
  list2 = [10,9,8,7,6,5,4,3]
  newList = removeDups(list1, list2)
  print(newList)

if __name__ == "__main__":  
    main()
