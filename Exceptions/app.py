# 
# File: app.py
# Auth: Martin Burolla
# Date: 8/8/2021
# Desc: Tests exceptions
#

from NotFoundException import NotFoundException

def main():
  try:
    # raise Exception('failure')
    #data = 'Hello World'
    data = ''
    if data == '':
      raise NotFoundException('Hello World could not found.')
  except NotFoundException as nfe:
    print('Caught NotFoundException')
    print(nfe)
  except Exception as e:
    print('Caught Exception')
    print(e)

if __name__ == "__main__":  
    main()
