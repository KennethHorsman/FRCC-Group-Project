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
    "Tests if input is a digit, then returns input as float."
    while True:
        input_result = input(prompt)
        if not input_result.isdigit():
            print("Invalid character(s) detected.")
            continue
        return int(input_result)

def get_dvd_quantity():
    "Prompts user for number of DVDs being rented"
    dvd_input = get_non_negative_number("Number of DVDs:")
    return dvd_input

def get_vhs_quantity():
    "Prompts user for number of VHS tapes being rented"
    vhs_input = get_non_negative_number("Number of VHS Tapes:")
    return vhs_input

def get_number_of_nights():
    "Prompts user for number of rental nights"
    nights_input = get_non_negative_number("Number of Nights:")
    return nights_input

def print_rental_cost(): # pylint: disable=useless-return
    "Calculates and prints the rental cost"
    num_dvds = get_dvd_quantity()
    num_vhs = get_vhs_quantity()
    num_nights = get_number_of_nights()

    rental_cost = ((3 * num_dvds) + (2 * num_vhs)) * (num_nights)
    rental_cost_formatted = f"{rental_cost:,.2f}"

    if rental_cost == 0:
        print("\nNo video rentals are being made.")
    else:
        if num_vhs == 0:
            print(f"The total cost of {num_dvds} DVD{'s' if num_dvds > 1 else ''} for {num_nights} night{'s' if num_nights > 1 else ''} is: ${rental_cost_formatted}")
        elif num_dvds == 0:
            print(f"The total cost of {num_vhs} VHS tape{'s' if num_vhs > 1 else ''} for {num_nights} night{'s' if num_nights > 1 else ''} is: ${rental_cost_formatted}")
        else:
            print(f"The total cost of {num_dvds} DVD{'s' if num_dvds > 1 else ''} and {num_vhs} VHS tape{'s' if num_vhs > 1 else ''} for {num_nights} night{'s' if num_nights > 1 else ''} is: ${rental_cost_formatted}")
    return

print_rental_cost()
