# 
# File: intro-ex-37.py
# Auth: Martin Burolla
# Date: 8/31/2021
# Desc: 
#

def main():
  tuples = [(1,'red'), (2, 'blue'), (3, 'green'), (4, 'green'), (5, 'red')]

  print(set(map(lambda x: x[1], tuples)))

if __name__ == "__main__":  
  main()
