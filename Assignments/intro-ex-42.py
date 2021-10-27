# 
# File: intro-ex-42.py
# Auth: Martin Burolla
# Date: 9/2/2021
# Desc: Access Denied
#

def main():
  peopleList = [
    { 'ssn' : '222-22-2222' , 'name' : 'joe' },
    { 'ssn' : '333-33-3333' , 'name' : 'bob' },
    { 'ssn' : '555-55-5555' , 'name' : 'tim' },
  ]
  accessDict = {
    '222-22-2222' : True,
    '333-33-3333' : False,
    '555-55-5555' : False,
  }

  while True:
    userName = input('Enter Username: ').lower()
    try:
      ssn = [p['ssn'] for p in peopleList if p['name'] == userName][0]
    except IndexError:
      print('Username does not exist.')
    else:
      if accessDict[ssn]:
        print('Access granted.')
      else:
        print('Access denied.')
  
if __name__ == "__main__":  
  main()