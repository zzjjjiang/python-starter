# 
# File: intro-ex-40.py
# Auth: Martin Burolla
# Date: 9/1/2021
# Desc: Tiny Theater
#

NUM_ROWS = 3
NUM_SEATS_IN_ROW = 10

def printSeats(movieSeats):
  for rowIndex in range(NUM_ROWS):
    row = ''
    for colIndex in range(NUM_SEATS_IN_ROW):
      pos = (rowIndex * NUM_SEATS_IN_ROW) + colIndex
      row += movieSeats[pos]
    print(row)

def validate(row, seat):
  if (row > NUM_ROWS and seat > NUM_SEATS_IN_ROW):
    raise Exception('ERROR: Not enough rows and seats!!!')
  elif (row > NUM_ROWS):
    raise Exception('ERROR: Not enough rows!!!')
  elif (seat > NUM_SEATS_IN_ROW):
    raise Exception('ERROR: Not enough seats!!!')

def main():
  movieSeats = ['0' for _ in range(NUM_ROWS * NUM_SEATS_IN_ROW)]
  
  while True:
    printSeats(movieSeats)
    row = int(input('Enter row number: '))
    col = int(input('Enter seat number: '))
    try:
      validate(row, col)
      pos = ((row - 1) * NUM_SEATS_IN_ROW) + (col - 1)
      movieSeats[pos] = 'X'
    except Exception as e:
      print(e)

if __name__ == "__main__":  
  main()
