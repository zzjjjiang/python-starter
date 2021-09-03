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

    sPrice = 0
    mPrice = 0
    lPrice = 0
    smallBoxes = 0
    medBoxes = 0
    largeBoxes = 0

    for room in customerDict:
        for box in customerDict[room].keys():
            if box == 'small':
                sPrice = costPerBoxDict[box]
                smallBoxes += customerDict[room][box]
            elif box == 'medium':
                mPrice = costPerBoxDict[box]
                medBoxes += customerDict[room][box]
            elif box == 'large':
                lPrice = costPerBoxDict[box]
                largeBoxes += customerDict[room][box]

    totalPrice = (sPrice * smallBoxes ) + (mPrice * medBoxes) + (lPrice * largeBoxes)
    totalPrice = "${:,.2f}".format(totalPrice)
    print(f"Small boxes: {smallBoxes}\nMedium Boxes: {medBoxes}\nLarge Boxes: {largeBoxes}\nTotal price: {totalPrice}")


if __name__ == "__main__":
    main() 