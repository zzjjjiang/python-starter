# 
# File: s3-data-access.py
# Auth: Martin Buroll
# Date: 10/6/2021
# Desc: Wraps S3
#

import boto3

from time import sleep
from datetime import datetime


def main():
  client = boto3.client('s3')

  # Our customer IDs.
  billableCustomersList = ['123', '456', '789']
  
  # Create file contents.
  timeString = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
  fileContents = f'*** BILLABLE CUSTOMERS ***\nTime: {timeString}\n'
  for customerId in billableCustomersList:
    fileContents += f'{customerId}\n'
  
  # Push to S3.
  client.put_object(Body=fileContents, Bucket='siua-bucket', Key='bill_these_customers.txt')
  print(fileContents)

if __name__ == "__main__":  
  main()
