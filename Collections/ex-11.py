#
# File: ex-11.py
# Auth: Martin Burolla
# Date: 8/16/2021
# Desc: People in space
#

import requests

def main():
  # Get the data.
  url = 'http://api.open-notify.org/astros.json'
  peopleList = requests.get(url).json()["people"]

  # Write the data to file.
  f = open("output.txt", "w")
  for person in peopleList:
    f.write(f'{person["name"]} is in {person["craft"]}.\n')
  f.close()

  # Close.
  print('Finished.')

if __name__ == "__main__":  
  main()
