# 
# File: intro-ex-40.py
# Auth: Martin Burolla
# Date: 9/1/2021
# Desc: Tiny Movie Theater
#

def printSeats(movieSeats, numRows, numSeats):
  for rowIndex in range(numRows):
    row = ''
    for colIndex in range(numSeats):
      seatIndex = (rowIndex * numSeats) + colIndex
      row += movieSeats[seatIndex]
    print(row)

def validateInput(row, seat, numRows, numSeats):
  if (row > numRows and seat > numSeats):
    raise Exception('ERROR: Not enough rows and seats')
  elif (row > numRows):
    raise Exception('ERROR: Not enough rows')
  elif (seat > numSeats):
    raise Exception('ERROR: Not enough seats')
  elif (seat <= 0 or row <= 0):
    raise Exception('ERROR: Row and seat numbers must greater than 0')

def main():
  totalSales = 0
  numRows = int(input('Enter number of rows: '))
  numSeats = int(input('Enter number of seats: '))
  movieSeats = ['0' for _ in range(numRows * numSeats)]
 
  while True:
    printSeats(movieSeats, numRows, numSeats)
    print("${:,.2f}".format(totalSales))
    row = int(input('Enter row number: '))
    col = int(input('Enter seat number: '))
    try:
      validateInput(row, col, numRows, numSeats)
    except Exception as e:
      print(e)
    else:
      seatIndex = ((row - 1) * numSeats) + (col - 1)
      if movieSeats[seatIndex] == '0':
        totalSales += row
      movieSeats[seatIndex] = 'X'

if __name__ == "__main__":  
  main()
