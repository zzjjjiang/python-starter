#
# File: ex-10.py
# Auth: Martin Burolla
# Date: 8/11/2021
# Desc: Hello File
#

def createFile(fileName, content):
  fileHandle = open(fileName, "w")
  fileHandle.write(content)
  fileHandle.close()

def main():
  createFile("output.txt", "Hello World!")

if __name__ == "__main__":  
    main()
