# 
# File: app.py
# Auth: Martin Burolla
# Date: 8/3/2021
# Desc: Classes
#

from Person import Person

def main():
  p = Person('Marty', 19)
  print(p.speak())

  p2 = Person.fromBirthYear('Marty', 1970)
  print(p2.speak())

  # Static method
  r = Person.isAdult(30)
  print(r)

  print(len(p)) # dunder: __len__
  print(p) # dunder __repr__

if __name__ == "__main__":  
    main()
