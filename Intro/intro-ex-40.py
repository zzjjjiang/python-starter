# 
# File: intro-ex-40.py
# Auth: Martin Burolla
# Date: 9/15/2021
# Desc: Tiny Movie Theater
#

import boto3

def getFormattedSeats(movieSeats, numRows, numSeats):
  retval = ''
  for rowIndex in range(numRows):
    row = ''
    for colIndex in range(numSeats):
      seatIndex = (rowIndex * numSeats) + colIndex
      row += movieSeats[seatIndex]
    retval += (row + '\n')
  return retval

def validateInput(row, seat, numRows, numSeats):
  if (row > numRows and seat > numSeats):
    raise Exception('ERROR: Not enough rows and seats') # Ideally we would subclass Exception and raise our own Exception.
  elif row > numRows:
    raise Exception('ERROR: Not enough rows')
  elif seat > numSeats:
    raise Exception('ERROR: Not enough seats')
  elif seat <= 0 or row <= 0:
    raise Exception('ERROR: Row and seat numbers must greater than 0')
  elif seat > 1000:
    raise Exception('ERROR: Too many seats')
  elif row > 1000:
    raise Exception('ERROR: Too many rows')

def shouldExit(row):
  return row.lower() == 'exit'

def createFileAndUploadToS3(totalSales, movieSeats, numRows, numSeats):
  # Create file
  f = open("upload.txt", "w")
  f.write(getFormattedSeats(movieSeats, numRows, numSeats))
  f.write("${:,.2f}".format(totalSales))
  f.close()

  # Upload to S3
  s3_client = boto3.client('s3')
  file = 'upload.txt'
  bucketName = 'siua-bucket'
  objectName = 'marty/movies/output.txt'
  s3_client.upload_file(file, bucketName, objectName)

def main():
  totalSales = 0
  numRows = int(input('Enter number of rows: '))
  numSeats = int(input('Enter number of seats: '))
  movieSeats = ['0' for _ in range(numRows * numSeats)]
 
  while True:
    print(getFormattedSeats(movieSeats, numRows, numSeats))
    print("${:,.2f}".format(totalSales))
    row = input('Enter row number: ')
    if shouldExit(row):
      createFileAndUploadToS3(totalSales, movieSeats, numRows, numSeats)
      break
    col = input('Enter seat number: ')
    if shouldExit(col):
      createFileAndUploadToS3(totalSales, movieSeats, numRows, numSeats)
      break

    row = int(row)
    col = int(col)

    try:
      validateInput(row, col, numRows, numSeats)
    except Exception as e: # Ideally we would catch our own custom Exception.
      print(e)
    else:
      seatIndex = ((row - 1) * numSeats) + (col - 1)
      if movieSeats[seatIndex] == '0':
        totalSales += row
      movieSeats[seatIndex] = 'X'

if __name__ == "__main__":  
  main()
