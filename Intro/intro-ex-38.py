# 
# File: intro-ex-38.py
# Auth: Martin Burolla
# Date: 8/31/2021
# Desc: Carpets
#

PRICE_PER_SQUARE_FEET = 7.89

def main():
  roomsList = [
    { 
      'room' : 
      { 
        'name' : 'kitchen',
        'color' : 'blue',
        'dimensions' : 
        { 
          'width' : 10, 'length' : 10, 'height' : 8 
        }
      }
    },
    { 
      'room' : 
      { 
        'name' : 'living room',
        'color' : 'blue',
        'dimensions' : 
        { 
          'width' : 10, 'length' : 20, 'height' : 10 
        }
      }
    },
    { 
      'room' : 
      { 
        'name' : 'family room',
        'color' : 'tan',
        'dimensions' : 
        { 
          'width' : 10, 'length' : 20, 'height' : 8 
        }
      }
    },
    { 
      'room' : 
      { 
        'name' : 'bathroom',
        'color' : 'blue',
        'dimensions' : 
        { 
          'width' : 5, 'length' : 8, 'height' : 10 
        }
      }
    }
  ]

  # Map & Filter...
  # filterRoomList = list(filter(lambda x: x['room']['color'] == 'blue', roomsList))
  # areaForRoomsList = list(map(lambda x: x['room']['dimensions']['length'] * x['room']['dimensions']['width'], filterRoomList))
  
  # List comprehension...
  areasOfRoomsList = [calcAreaForRoom(r) for r in roomsList if r['room']['color'] == 'blue']
  totalCost = sum(areasOfRoomsList) * PRICE_PER_SQUARE_FEET
  print("${:,.2f}".format(totalCost))

def calcAreaForRoom(r):
  return r['room']['dimensions']['length'] * r['room']['dimensions']['width']

if __name__ == "__main__":  
  main()
