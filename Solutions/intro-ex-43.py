# 
# File: intro-ex-43.py
# Auth: Martin Burolla
# Date: 9/2/2021
# Desc: Moving Company
#

def main():
  costPerBoxDict = {
    'small' : 5.00,
    'medium' : 10.00,
    'large' : 15.00
  }
  customerDict = {
    'living room' : 
      { 
        'small' : 5, 
        'large' : 4
      },
    'bedroom' : 
      { 
        'small' : 1, 
        'medium' : 4,
        'large' : 5
      },
    'bathroom' : 
      { 
        'small' : 2, 
        'large' : 1
      }
  }
  
  totalCost = 0
  for roomKey in customerDict.keys():
    for sizeKey in customerDict[roomKey].keys():
      qty = customerDict[roomKey][sizeKey]
      price = costPerBoxDict[sizeKey]
      totalCost += (qty * price)

  print("${:,.2f}".format(totalCost))
 
if __name__ == "__main__":  
  main()