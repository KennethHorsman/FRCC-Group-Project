# pylint: disable=line-too-long
# pylint: disable=invalid-name
"""
Project 3A: 
Develop a program that converts feet to inches. 
Your program should ask the user for number of feet and then outputs the converted number of inches. 
In your program, make a function named "feet_to_inches" that accepts number of feet as an argument and 
returns the number of inches in that many feet (ex: 2 feet should return 24 inches). 

Programmer: Horsman, Kenneth. Group Members: Nowak, Stephen. Jimenez-Morales, Destinee.

Course: CSC1019-FBN 
"""

def main():
    "Tells user how many inches are in the number of feet"
    convert_feet_to_inches()

def convert_feet_to_inches():
    "Calculates feet to inches"
    feet = get_number_feet()
    inches = feet * 12
    return print(f"{int(feet) if feet.is_integer() else feet} feet is equivalent to {int(inches) if inches.is_integer() else inches} inches.")

def get_number_feet():
    "Prompts user to input number of feet"
    number_feet_input = get_non_negative_number("Enter the total number of feet: ")
    return number_feet_input

def get_non_negative_number(prompt: str) -> float:
    "Tests if input is a valid number and greater than 0, then returns input as float."
    test_number = True
    while test_number is True:
        user_input = input(prompt)
        if not is_valid_number(user_input):
            print("Error: Invalid character(s) detected.")
        elif float(user_input) < 0:
            print("Error: The number of feet must be a non-negative number.")
        else:
            test_number = False
            return float(user_input)

def is_valid_number(num: str) -> bool:
    "Determines if num can successfully be converted to a float"
    try:
        float(num)
        return True
    except ValueError:
        return False

if __name__=="__main__":
    main()
