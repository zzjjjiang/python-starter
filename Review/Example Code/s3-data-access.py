# 
# File: s3-data-access.py
# Auth: Martin Buroll
# Date: 10/6/2021
# Desc: Wraps S3
#

import boto3 # <== Need this to upload to S3.

from time import sleep
from datetime import datetime

def createFileS3(customerList, fileHeader, bucketName, keyPath):
  retval = None
  client = boto3.client('s3')
  
  # Create file contents.
  timeString = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
  fileContents = f'{fileHeader}\nTime: {timeString}\n'
  for customerId in customerList:
    fileContents += f'{customerId}\n'
    
  # Push to S3.
  retval = client.put_object(Body = fileContents, Bucket = bucketName, Key = keyPath) 
  return retval

def main():
  
  # Our customer IDs.
  billableCustomersList = ['123', '456', '789'] # Square brackets indicate a list.

  # Store a file from our customer list into S3.
  createFileS3(customerList = billableCustomersList, fileHeader = '*** Marty was here ***', bucketName = 'siua-bucket', keyPath = 'demo/bill_these_customers.txt' )


if __name__ == "__main__":  
  main()
