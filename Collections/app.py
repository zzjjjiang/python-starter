# 
# File: app.py
# Auth: Martin Burolla
# Date: 8/3/2021
# Desc: Collections
#

from collections import namedtuple

def main():
  listExample()
  #dictionaryExample()
  #tupleExample()
  #setExample()
  #namedTupleExample()
  #deepCopyVsShallowCopy()

def deepCopyVsShallowCopy():
  # Shallow Copy
  colorList1 = ['red', 'yellow', 'green']
  colorList2 = colorList1
  colorList2.append('black')
  print(colorList1)
  print(colorList2)

  # Deep Copy
  # colorList1 = ['red', 'yellow', 'green']
  # colorList2 = colorList1.copy()
  # colorList2.append('black')
  # print(colorList1)
  # print(colorList2)

def listExample():
  fruitList = ['apple', 'orange', 'grape']
  colorList = ['red', 'yellow', 'green']
  c = colorList.count('red')
  colorList.append('white')
  fruitList.remove('apple')
  fruitListCopy = fruitList.copy() # Deep Copy
  fruitListShallowCopy = fruitList # Shallow Copy
  len(fruitList)

def dictionaryExample():
  dict1 = {
    1: 'one',
    2: 'two',
    3: 'three'
  }
  print(dict1[2])

  # dict2 = {
  #   1: {'brand' : 'Ford', 'model' : 'Mustang'},
  #   2: {'brand' : 'Toyota', 'model' : 'Prius'},
  #   3: {'brand' : 'Chevy', 'model' : 'Corvette'},
  # }
  # dict2[4] = {'brand' : 'Nissan', 'model' : 'Ultima'}
  # dict2[5] = {'brand' : 'BMW', 'model' : 'M5'}

  # print(dict2[4])
  # print(dict2[4]['brand'])
  # print(dict2[4]['model'])

  #del dict2[3]
  #print(dict2[3])

  # for key in dict1:
  #   print(key)

def tupleExample():
  myColorTuple1 = ('red', 'yellow', 'green')
  myColorTuple2 = ('orange', 'purple', 'black')
  t = myColorTuple1 + myColorTuple2
  # Cannot add or remove.
  print(t)

def setExample():
  colorSet = {'red', 'yellow', 'green'}
  colorSet = {'red', 'yellow', 'green', 'red', 'red', 'red'}
  print(colorSet)

def namedTupleExample():
  Point = namedtuple("Point", "x y") # immutable structs
  p1 = Point(1,2)
  p2 = Point(2,3)
  print(p1, p2)

if __name__ == "__main__":  
    main()
