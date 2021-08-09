#
# File: app.py
# Auth: Martin Burolla
# Date: 8/9/2021
# Desc: AWS CLI
#

import boto3
from botocore.exceptions import ClientError

def main():
  s3_client = boto3.client('s3')
  file = 'myfile.txt'
  bucketName = 'sia-upload'
  objectName = 'myfile.txt'

  try:
    response = s3_client.upload_file(file, bucketName, objectName)
    print(response) # None.
  except ClientError as e:
    print(e)

if __name__ == "__main__":  
    main()
