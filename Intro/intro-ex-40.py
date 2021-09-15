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
  retval = retval[:-1] # Lop off the last \n
  return retval

def validateInput(row, seat, numRows, numSeats):
  if (row > numRows and seat > numSeats):
    raise Exception('ERROR: Not enough rows and seats') # Ideally we would subclass Exception and raise our own custom Exception.
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
  elif seat > 1000 and row > 1000:
    raise Exception('ERROR: Too many rows and seats')

def createFile(totalSales, movieSeats, numRows, numSeats):
  with open('upload.txt', 'w') as file: # Python context manager.
    file.write(getFormattedSeats(movieSeats, numRows, numSeats))
    file.write("\n${:,.2f}".format(totalSales))

def uploadToS3():  
  s3_client = boto3.client('s3')
  file = 'upload.txt'
  bucketName = 'siua-bucket'
  objectName = 'marty/movies/output.txt'
  s3_client.upload_file(file, bucketName, objectName)

def shouldExit(row, totalSales, movieSeats, numRows, numSeats):
  retval = row.lower() == 'exit'
  if retval:
    createFile(totalSales, movieSeats, numRows, numSeats)
    uploadToS3()
  return retval

def main():
  totalSales = 0
  numRows = int(input('Enter number of rows: '))
  numSeats = int(input('Enter number of seats: '))
  movieSeats = ['0' for _ in range(numRows * numSeats)]
 
  while True:
    print(getFormattedSeats(movieSeats, numRows, numSeats))
    print("${:,.2f}".format(totalSales))
    row = input('Enter row number: ')
    if shouldExit(row, totalSales, movieSeats, numRows, numSeats):
      break
    col = input('Enter seat number: ')
    if shouldExit(row, totalSales, movieSeats, numRows, numSeats):
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
