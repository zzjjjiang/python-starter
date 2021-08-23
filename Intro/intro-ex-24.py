# 
# File: intro-ex-24.py
# Auth: Martin Burolla
# Date: 8/22/2021
# Desc: Diagon Alley
#

def printDiagonally(word):
  for idx in range(len(word)):
    padding = ''
    for _ in range(idx):
      padding += ' '
    print(f'{padding}{word[idx]}')

def main():
  inputString = input('Enter text: ' )
  myWordList = inputString.split(' ')
  for word in myWordList:
    printDiagonally(word)

if __name__ == "__main__":  
  main()
