#
# File: ex-10.py
# Auth: Martin Burolla
# Date: 8/11/2021
# Desc: Oven List
#

def main():
  kitchenDictionary = {
    "Fridge" : 1,
    "Stove" : "silver",
    "Trash Compactor" : False,
    "Oven1" : [ "silver", "whirlpool", "large" ],
    "Oven2" : [ { "color" : "silver" }, { "make" : "Whirlpool" }, { "size" : "small" } ],
    "Microwave" : { "make" : "whirlpool" }
  }

  oven1Size = (kitchenDictionary["Oven1"][2])
  oven2Size = (kitchenDictionary["Oven2"][2]["size"])
  sizeList = [oven1Size, oven2Size]
  print(sizeList)

if __name__ == "__main__":  
    main()
