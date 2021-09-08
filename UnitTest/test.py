
def main():
  try: 
    x = 1
    y = 2
    assert x + y == 4, 'An error has occurred...' # Assert throws!
  except AssertionError as e:
    print(e)

if __name__ == "__main__":  
  main()
