# pylint: disable=line-too-long
# pylint: disable=invalid-name
"""
Project 2C:

Write a program that will compute a single filer's income tax.

Programmer: Horsman, Kenneth. Group Members: Nowak, Stephen. Jimenez-Morales, Destinee.

Course: CSC1019-FBN 
"""

def is_valid_number(num: str) -> bool: # uses num as the parameter. Type hints: num is expected to return as a string, and the function returns a boolean expression
    "Determines if num can successfully be converted to a float"
    try: # tests if the below code will result in an error
        float(num) # tries to convert the parameterr to a float
        return True # if successful, function returns true
    except ValueError: # if not-successful, the error will be a ValueError
        return False # so, function returns false

def get_non_negative_number(prompt: str, description: str) -> float: # sets prompt AND description as usable parameters, but these must now be defined when calling function.
    "Tests if input is a valid number and greater than 0, then returns input as float."
    while True: # creates a loop that requires a condition to be fulfilled in order to stop
        user_input = input(prompt) # prompts user for input using the prompt parameter
        if prompt == "Your Gross Income: ": # tests for this specific prompt
            input_result = user_input.replace(",", "").replace(".", "").replace("$","") # if it is, then replace any potential commas or decimals with nothing so those don't trigger the function on line 29
        else:
            input_result = user_input # if it's not that specific prompt, nothing changes except I've assigned user_input to a new variable since I don't want to redefine user_input on line 26
        if not is_valid_number(input_result): # takes input_result from above and uses it as the paramter for the function above this one, and asks if it returned false
            print("Error: Invalid character(s) detected.") # if it is false, it first prints this message
            continue # and then continues the while loop to re-ask for user input
        if float(input_result) < 0: # if the is_valid_number function returned true, it now asks if the input was a number below 0
            error_description = description # if it is, it then takes the description paramater
            print(f"Error: {error_description} must be a non-negative number.") # and uses it for a customized error message
            continue # then continues the loop
        return float(input_result) # one a valid, non-negative number has been given, it returns the users input as a float (because we'll be performing calculations later)

def get_gross_income():
    "Prompts user for their gross income"
    gross_income_input = get_non_negative_number(prompt="Your Gross Income: ", description="Your gross income") # uses above function to get valid user input with a custom prompt and description
    return gross_income_input # returns the result of the above function as this function's value

def get_dependants_over_6():
    "Prompts user for the number of their dependants over 6 years old"
    dependants_over_6_input = get_non_negative_number(prompt="Your Number of Dependants Over 6 Years Old: ", description="Your number of dependants over 6 years old")
    return dependants_over_6_input

def get_dependants_under_6():
    "Prompts user for the number of their dependants under 6 years old"
    dependants_under_6_input = get_non_negative_number(prompt="Your Number of Dependants Under 6 Years Old: ", description="Your number of dependants under 6 years old")
    return dependants_under_6_input

def get_net_income():
    "Calculates the net income from gross income, dependants over/under 6, and standard deduction"
    gross_income = get_gross_income() # calls on the above functions to get the values needed to calculate net income
    dependants_over_6 = get_dependants_over_6()
    dependants_under_6 = get_dependants_under_6()
    STANDARD_DEDUCTION = 13850 # capitalization sets this variable as a constant. It's identical to a normal variable, except it represents a value that will NEVER change.

    dependant_deduction = (3000 * dependants_over_6) + (2000 * dependants_under_6) # calculates dependant deduction based on number of kids and their age
    net_income_calculation = gross_income - dependant_deduction - STANDARD_DEDUCTION # calculates net income based on gross income input, dependant deduction calculation, and standard deduction

    return net_income_calculation # finally, returns net income as the result of all the above functions, to now be used in the next one

def print_income_tax():
    "Calculates and prints the income tax"
    net_income = get_net_income() 

    if net_income < 11000: # once the net income value is obtained, calculates the tax rate based on that value
        tax_rate = 0
    elif 11000 <= net_income < 44725:
        tax_rate = 0.12
    elif 44725 <= net_income < 95375:
        tax_rate = 0.22
    elif 95375 <= net_income < 182100:
        tax_rate = 0.24
    elif 182100 <= net_income < 231250:
        tax_rate = 0.32
    elif 231250 <= net_income < 578125:
        tax_rate = 0.35
    elif net_income >= 578125:
        tax_rate = 0.37

    income_tax_calculation = abs(net_income * tax_rate) # if the net income returns as a negative number, this calculation returns as -0.00. The abs (absolute value) makes it positive.
    income_tax_formatted = f"{income_tax_calculation:,.2f}" # formats the income to have commas as thousands separators, and makes it always have 2 decimal places (rounds up to 2 if it has more)

    return print(f"\nYour Income Tax: ${income_tax_formatted}") # f-string automatically converts non-str values within curly bracks to a string, and prints on a new line

print_income_tax() # in a way, this code reads bottom to top because the ONLY thing the main program actually calls for is this one function, which must call on helper functions.
