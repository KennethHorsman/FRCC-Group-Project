# pylint: disable=line-too-long
# pylint: disable=invalid-name
"""
Project 2B:

Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who like to buy LP record albums. 
The store rents new videos for $3.00 a night, and oldies for $2.00 a night. Write a program that the clerks 
at Five Star Retro Video can use to calculate the total charge for a customer's video rentals. 
The program should prompt the user for the number of each type of video and output the total cost.
"""

def get_non_negative_number(prompt: str) -> float:
    "Tests if input is a valid number and greater than 0."
    while True:
        input_result = input(prompt)
        if not input_result.isdigit():
            print("Invalid character(s) detected.")
            continue
        if float(input_result) < 0:
            prompt_message = prompt.lower().strip(": ")
            print(f"The {prompt_message} must be at least 0.")
            continue
        return int(input_result)

def get_dvd_quantity():
    "Prompts user for number of DVDs being rented"
    dvd_quantity = get_non_negative_number("Number of DVDs:")
    return dvd_quantity

def get_vhs_quantity():
    "Prompts user for number of VHS tapes being rented"
    vhs_quantity = get_non_negative_number("Number of VHS Tapes:")
    return vhs_quantity

def get_number_of_nights():
    "Prompts user for number of rental nights"
    num_nights = get_non_negative_number("Number of Nights:")
    return num_nights

dvds = get_dvd_quantity()
vhs_tapes = get_vhs_quantity()
nights = get_number_of_nights()

rental_cost_calculation = ((3 * dvds) + (2 * vhs_tapes)) * (nights)
rental_cost = "{:,.2f}".format(rental_cost_calculation) # pylint: disable=consider-using-f-string

if rental_cost == 0 or nights == 0:
    print("No video rentals are being made.")
else:
    if nights == 1:
        if dvds > 1 and vhs_tapes == 0:
            print(f"\nThe total cost of {dvds} DVDs for 1 night is ${rental_cost}")
        elif dvds == 1 and vhs_tapes == 0:
            print(f"\nThe total cost of 1 DVD for 1 night is ${rental_cost}")
        elif vhs_tapes > 1 and dvds == 0:
            print(f"\nThe total cost of {vhs_tapes} VHS tapes for 1 night is ${rental_cost}")
        elif vhs_tapes == 1 and dvds == 0:
            print(f"\nThe total cost of 1 VHS tape for 1 night is ${rental_cost}")
        else:
            print(f"\nThe total cost of {dvds} DVDs and {vhs_tapes} VHS tapes for 1 night is: ${rental_cost}")
    else:
        if dvds > 1 and vhs_tapes == 0:
            print(f"\nThe total cost of {dvds} DVDs for {nights} nights is ${rental_cost}")
        elif dvds == 1 and vhs_tapes == 0:
            print(f"\nThe total cost of 1 DVD for {nights} nights is ${rental_cost}")
        elif vhs_tapes > 1 and dvds == 0:
            print(f"\nThe total cost of {vhs_tapes} VHS tapes for {nights} nights is ${rental_cost}")
        elif vhs_tapes == 1 and dvds == 0:
            print(f"\nThe total cost of 1 VHS tape for {nights} nights is ${rental_cost}")
        else:
            print(f"\nThe total cost of {dvds} DVDs and {vhs_tapes} VHS tapes for {nights} nights is: ${rental_cost}")