# 
# File: app.py
# Auth: Martin Burolla
# Date: 8/8/2021
# Desc: Functions
#

# If you pass a mutable object into a method, the method gets a reference to that 
# same object and you can mutate it, but if you rebind the reference in the method, 
# the outer scope will know nothing about it, and after you're done, 
# the outer reference will still point at the original object.

# If you pass an immutable object to a method, you still can't rebind the outer reference, 
# and you can't mutate the object.

def main():
  # mutableTest()
  immutableTest()

def mutableTest():
  list1 = ['red', 'yellow', 'green']
  print(list1)
  list2 = foo(list1)
  print(f'List 1: {list1}')
  print(f'List 2: {list2}')

def immutableTest():
  s1 = 'Hello World'
  s2 = foo2(s1)
  print(s1)
  print(s2)

def foo(list): # Pass by reference
  #list.append('orange')
  list2 = list.copy()
  list2.append('purple')
  return list2

def foo2(s1): # Pass by copy
  s1 = 'test'
  return s1

if __name__ == "__main__":  
    main()