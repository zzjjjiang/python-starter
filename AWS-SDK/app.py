#
# File: app.py
# Auth: Martin Burolla
# Date: 9/8/2021
# Desc: Interact with S3.
#
#       AWS-SDK:
#         https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html
#         https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html
#       AWS-CLI:      
#         https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html
#

import boto3
from botocore.exceptions import ClientError

def upload():
  print('*** Uploading file to S3 ***')
  s3_client = boto3.client('s3')
  file = 'myfile.txt'
  bucketName = 'siua-bucket'
  objectName = 'marty/myfile.txt'

  try:
    response = s3_client.upload_file(file, bucketName, objectName)
    print(response) # No news is good news.
  except ClientError as e:
    print(e)

def download():
  pass

def main():
  upload()
  download()
  
if __name__ == "__main__":  
    main()
