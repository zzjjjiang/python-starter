# def download():
#   print('*** Downloading file from S3 ***')
#   s3_client = boto3.client('s3')
#   with open('marty_myfile.txt', 'wb') as f:
#     s3_client.download_fileobj('siua-bucket', 'marty/myfile.txt', f)

# s3 = boto3.resource('s3')
# s3.Object('your-bucket', 'your-key').delete()