# 
# File: intro-ex-17.py
# Auth: Martin Burolla
# Date: 8/18/2021
# Desc: Easy Authentication, Not Authorization
#

import hashlib

def shouldExit(inStr):
  return inStr == "exit"

def main():
  print("Type exit at anytime to end program...")

  userPwdDict = {}
  while (True):

    mode = input("Enter mode (add|login): ")
    if shouldExit(mode): 
        break

    if (mode == "add"):
      username = input("Enter username: ")
      if shouldExit(username): 
        break
      password = input("Enter password: ")
      if shouldExit(password):
        break
      userPwdDict[username] = hashlib.sha256(password.encode()).hexdigest() # Add our key/value pair to dictionary.

    if (mode == "login"):
      username = input("Enter username: ")
      if shouldExit(username): 
        break
      password = input("Enter password: ")
      enteredPasswordHash = hashlib.sha256(password.encode()).hexdigest()

      if (username in userPwdDict):
        savedPasswordHash = userPwdDict[username]  # Lookup password hash for this user from dictionary.
        if (savedPasswordHash == enteredPasswordHash):
          print('Password is correct.')
        else:
          print("Incorrect password.")
      else:
        print('User does not exist.')

  # Print contents of dictionary.
  for key in userPwdDict:
    print(f'{key} : {userPwdDict[key]}')

  exit()

if __name__ == "__main__":  
  main()
