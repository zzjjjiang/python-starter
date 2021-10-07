#
# File: cron.py
# Auth: Martin Burolla
# Date: 10/4/2021
# Desc: CRPON template boilerplate code
#       Runs forever until Control+C is entered on the console.
#

from time import sleep
from datetime import datetime

INTERVAL_SECONDS = 10 # Number of seconds to sleep.

def businessLogic():
  # Do some real work here...
  pass

def main():
  while True:
    businessLogic()
    timestamp = datetime.today().strftime('%m/%d/%Y %I:%M:%S %p')
    print(f'Last run: {timestamp}.')
    sleep(INTERVAL_SECONDS)

if __name__ == "__main__":  
  main()
