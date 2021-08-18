# 
# File: intro-ex-11.py
# Auth: Martin Burolla
# Date: 8/17/2021
# Desc: Write Today's Date
#

from datetime import datetime

def main():
  todaysDate = datetime.today().strftime('%m/%d/%Y')
  f = open("output.txt", "w")
  f.write(f"Today's date is: {todaysDate}.")
  f.close()

if __name__ == "__main__":  
  main()
