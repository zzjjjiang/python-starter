#
# File: ex-5.py
# Auth: Martin Burolla
# Date: 8/11/2021
# Desc: Find longest list
#

def lenLongestList(list1, list2, list3):
  retval = 0
  lenList1 = len(list1)
  lenList2 = len(list2)
  lenList3 = len(list3)
  retval = max(lenList1, lenList2, lenList3)
  return retval

def main():
  list1 = [1,2,3,4,5]
  list2 = ['a', 'b', 'c']
  list3 = ['red', 'yellow', 'green']
  length = lenLongestList(list1, list2, list3)
  print(length)

if __name__ == "__main__":  
    main()
