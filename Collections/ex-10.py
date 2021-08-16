#
# File: ex-10.py
# Auth: Martin Burolla
# Date: 8/11/2021
# Desc: Oven List
#

def main():
  partsDictionary = {
    "Screw" : [ { "inStock": True }, { "color" : "silver" }, { "partNumber" : "123" }, { "cost" : 1.00 } ],
    "Hammer" : [ { "inStock": True }, { "color" : "silver" }, { "cost" : 10.00 } ],
    "Bolt" : [ { "inStock": True }, { "color" : "silver" }, { "cost" : 1.00 } ],
    "Nail" : [ { "inStock": False }, { "color" : "silver" }, { "cost" : .10 } ],
    "Wood" : [ { "inStock": True }, { "cost" : 3.00 } ],
  }

  totalCost = 0
  for key in partsDictionary.keys():
    myList = partsDictionary[key]
    if myList[0]["inStock"]:
      for dictionary in myList:
        if "cost" in dictionary:
          totalCost += dictionary["cost"]

  currency = "${:,.2f}".format(totalCost)
  print(f"Total Cost: {currency}.")

if __name__ == "__main__":  
    main()
