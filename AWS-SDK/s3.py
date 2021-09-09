#
# File: s3.py
# Auth: Martin Burolla
# Date: 9/9/2021
# Desc: S3 under the hood
#       S3 is a flat object store, it works much like a Python dictionary.
#

def main():
  s3Dict = {
    'marty/this/is/a/test/myFile.txt' : 'data',
    'joe/testing/directory/joeFile.txt' : 'data',
    'fred/was/here/fredFile.txt' : 'data'
  }
  
  # Get the file from S3...
  print(s3Dict['marty/this/is/a/test/myFile.txt']) # key path (AKA PREFIX)
  
  # Creating a "new directory/folder" in the AWS web console simply "updates" the keypath.
  del s3Dict['marty/this/is/a/test/myFile.txt'] # Remove old key
  s3Dict['marty/this/is/a/test/new directory/myFile.txt'] = 'data' # Add new key
  
  # Get the file from S3...
  print(s3Dict['marty/this/is/a/test/new directory/myFile.txt']) # key path (AKA PREFIX)

if __name__ == "__main__":  
    main()
