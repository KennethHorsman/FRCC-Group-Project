# pylint: disable=line-too-long
# pylint: disable=invalid-name
"""
Project 3A: 
Develop a program that converts feet to inches. 
Your program should ask the user for number of feet and then outputs the converted number of inches. 
In your program, make a function named "feet_to_inches" that accepts number of feet as an argument and 
returns the number of inches in that many feet (ex: 2 feet should return 24 inches). 

Programmer: Horsman, Kenneth. Group Members: Nowak, Stephen. Jimenez, Destinee.

Course: CSC1019-FBN 
"""

def is_valid_number(num: str) -> bool:
    "Determines if num can successfully be converted to a float"
    try:
        float(num)
        return True
    except ValueError:
        return False

def get_non_negative_number(prompt: str, description: str) -> float:
    "Tests if input is a valid number and greater than 0, then returns input as float."
    while True:
        user_input = input(prompt)
        if prompt == "Your Gross Income: ":
            input_result = user_input.replace(",", "")
        else:
            input_result = user_input
        if not is_valid_number(input_result):
            print("Error: Invalid character(s) detected.")
            continue
        if float(input_result) < 0:
            error_description = description
            print(f"Error: {error_description} must be a non-negative number.")
            continue
        return float(input_result)

def get_number_feet():
    "Prompts user to input number of feet"
    number_feet_input = get_non_negative_number(prompt="Enter the total number of feet: ", description="The number of feet")
    return number_feet_input

def convert_feet_to_inches():
    "Calculates how many inches are in the number of feet"
    number_feet = get_number_feet()

    inches_calculation = number_feet * 12
    inches_to_integer = int(inches_calculation) if inches_calculation.is_integer() else inches_calculation
    number_feet_to_integer = int(number_feet) if number_feet.is_integer() else number_feet
    return print(f"{number_feet_to_integer} feet is equivalent to {inches_to_integer} inches.")

convert_feet_to_inches()
