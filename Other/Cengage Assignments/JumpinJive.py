addIns = ["Cream", "Cinnamon", "Chocolate", "Amaretto", "Whiskey"]

addInPrices = [.89, .25, .59, 1.50, 1.75]
orderTotal = 2.00

while True:
    addIn = input("Enter coffee add-in or XXX to quit: ")
    if addIn == "XXX":
        print(f"Order Total: {orderTotal}")
        break
    if addIn in addIns:
        index = addIns.index(addIn)
        orderTotal = orderTotal + addInPrices[index]
        print(addIn + " Price is $" + str(addInPrices[index]))
    else:
        print("Sorry, we do not carry that.")