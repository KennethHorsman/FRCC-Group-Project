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
    "Tests if input is a valid number and at least 0."
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

num_dvds = get_dvd_quantity()
num_vhs = get_vhs_quantity()
num_nights = get_number_of_nights()

rental_cost = ((3 * num_dvds) + (2 * num_vhs)) * (num_nights)
rental_cost_formatted = "{:,.2f}".format(rental_cost) # pylint: disable=consider-using-f-string

if rental_cost == 0 or num_nights == 0:
    print("\nNo video rentals are being made.")
else: # Completely unecessary but I felt like doing it anyways
    if num_nights == 1:
        if num_dvds > 1 and num_vhs == 0:
            print(f"\nThe total cost of {num_dvds} DVDs for 1 night is ${rental_cost_formatted}")
        elif num_dvds == 1 and num_vhs == 0:
            print(f"\nThe total cost of 1 DVD for 1 night is ${rental_cost_formatted}")
        elif num_vhs > 1 and num_dvds == 0:
            print(f"\nThe total cost of {num_vhs} VHS tapes for 1 night is ${rental_cost_formatted}")
        elif num_vhs == 1 and num_dvds == 0:
            print(f"\nThe total cost of 1 VHS tape for 1 night is ${rental_cost_formatted}")
        else:
            print(f"\nThe total cost of {num_dvds} DVDs and {num_vhs} VHS tapes for 1 night is: ${rental_cost_formatted}")
    else:
        if num_dvds > 1 and num_vhs == 0:
            print(f"\nThe total cost of {num_dvds} DVDs for {num_nights} nights is ${rental_cost_formatted}")
        elif num_dvds == 1 and num_vhs == 0:
            print(f"\nThe total cost of 1 DVD for {num_nights} nights is ${rental_cost_formatted}")
        elif num_vhs > 1 and num_dvds == 0:
            print(f"\nThe total cost of {num_vhs} VHS tapes for {num_nights} nights is ${rental_cost_formatted}")
        elif num_vhs == 1 and num_dvds == 0:
            print(f"\nThe total cost of 1 VHS tape for {num_nights} nights is ${rental_cost_formatted}")
        else:
            print(f"\nThe total cost of {num_dvds} DVDs and {num_vhs} VHS tapes for {num_nights} nights is: ${rental_cost_formatted}")
