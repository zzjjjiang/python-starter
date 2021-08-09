#
# File: app.py
# Auth: Martin Burolla
# Date: 8/9/2021
# Desc: Data access
#

from AuroraDBProxy import AuroraDBProxy

def main():
  with AuroraDBProxy() as auroraDBProxy:
    data = auroraDBProxy.getAllPeople()
  print(data)

if __name__ == "__main__":  
  main()
