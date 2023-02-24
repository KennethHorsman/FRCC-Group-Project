"""
Project 2B:

Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who like to buy LP record albums. The store rents new videos for $3.00 a night, 
and oldies for $2.00 a night. Write a program that the clerks at Five Star Retro Video can use to calculate the total charge for a customer's video rentals. 
The program should prompt the user for the number of each type of video and output the total cost.
"""

def Rental_Cost():
    num_rentals = 0
    while True: 
        new = input("Enter number of new videos: ") 
        if not new.isdigit(): 
            print("Invalid character(s) detected.")
        else:
            new = int(new) 
            num_rentals += new
            break 
            
    while True:
        old = input("Enter number of old videos: ")
        if not old.isdigit():
            print("Invalid character(s) detected.")   
        else:
            old = int(old)
            num_rentals += old
            break

    
    if num_rentals > 1:
        while True:
            nights = input("Enter number of nights for the rentals: ")
            if not nights.isdigit():
                print("Invalid character(s) detected.")
            elif int(nights) == 0:
                print("The number of nights must be at least 1.")
            else:
                nights = int(nights)
                rental_cost = ((3 * new)+(2 * old)) * nights
                break
    elif num_rentals == 1:
        while True:
            nights = input("Enter number of nights for the rental: ")
            if not nights.isdigit():
                print("Invalid character(s) detected.")
            elif int(nights) == 0:
                print("The number of nights must be at least 1.")
            else:
                nights = int(nights)
                rental_cost = ((3 * new)+(2 * old)) * nights
                break
    else:
        rental_cost = 0

    return rental_cost, new, old, nights 

rental_cost, new, old, nights = Rental_Cost() 
rental_cost = "{:,.2f}".format(rental_cost)

if rental_cost == 0:
    print("No video rentals are being made.")
else:
    if nights == 1:
        if new > 0 and old == 0:
            print(f"\nThe total cost of {new} new videos for 1 night is ${rental_cost}")
        elif old > 0 and new == 0:
            print(f"\nThe total cost of {old} old videos for 1 night is ${rental_cost}")
        else:
            print(f"\nThe total cost of {new} new videos and {old} old videos for 1 night is: ${rental_cost}") 
    else:
        if new > 0 and old == 0:
            print(f"\nThe total cost of {new} new videos for {nights} nights is ${rental_cost}")
        elif old > 0 and new == 0:
            print(f"\nThe total cost of {old} old videos for {nights} nights is ${rental_cost}")
        else:
            print(f"\nThe total cost of {new} new videos and {old} old videos for {nights} nights is: ${rental_cost}")
input('') 
