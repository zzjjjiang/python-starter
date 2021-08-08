# 
# File: app.py
# Auth: Martin Burolla
# Date: 8/8/2021
# Desc: Tests exceptions
#

from NotFoundException import NotFoundException

def main():
  try:
    a = 1
    if not a == 2:
      raise NotFoundException('a not be found')
  except Exception as e:
    print(e)

if __name__ == "__main__":  
    main()
