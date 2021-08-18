# 
# File: intro-ex-16.py
# Auth: Martin Burolla
# Date: 8/18/2021
# Desc: Hash It, Print It
#

import hashlib

def shouldExit(inStr):
  return inStr == "exit"

def main():
  print("Type exit at anytime to end program...")

  userPwdDict = {}
  while (True):
    username = input("Enter username: ")
    if shouldExit(username): 
      break
    password = input("Enter password: ")
    if shouldExit(password):
      break
    userPwdDict[username] = hashlib.sha256(password.encode()).hexdigest() # Add our key/value pair to dictionary.
 
  # Print contents of dictionary.
  for key in userPwdDict:
    print(f'{key} : {userPwdDict[key]}')

  exit()

if __name__ == "__main__":  
  main()
