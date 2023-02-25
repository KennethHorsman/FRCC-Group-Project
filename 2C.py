# pylint: disable=line-too-long
# pylint: disable=invalid-name
"""
Project 2C:

Write a program that will compute a single filer's income tax.

1. Significant constants:
       tax rate
       standard deduction
       deduction per dependent
2. The inputs are:
       gross income 
       number of dependents 
3. Computations:
       net income = gross income - the standard deduction - a deduction for each dependent 
       income tax = is a fixed percentage of the net income 
4. The outputs are:
       the income tax, rounded to two decimals.
"""

def is_valid_number(num: str) -> bool:
    "Determines if num can successfully be converted to a float"
    try:
        float(num)
        return True
    except ValueError:
        return False

def get_non_negative_number(prompt: str) -> float:
    "Tests if input is a valid number and greater than 0, then returns input as float."
    while True:
        user_input = input(prompt)
        if prompt == "Your Gross Income: ":
            input_result = user_input.replace(",", "")
        else:
            input_result = user_input
        if not is_valid_number(input_result):
            print("Invalid character(s) detected.")
            continue
        if float(input_result) < 0:
            first_letter_prompt = prompt[0]
            lowered_prompt = prompt.lower().strip(": ")
            error_description = first_letter_prompt + lowered_prompt[1:]
            print(f"Error: {error_description} must be a non-negative number.")
            continue
        return float(input_result)

def get_gross_income():
    "Prompts user for their gross income"
    gross_income_input = get_non_negative_number("Your Gross Income: ")
    return gross_income_input

def get_dependants_over_6():
    "Prompts user for the number of their dependants over 6 years old"
    dependants_over_6_input = get_non_negative_number("Your Number of Dependants Over 6 Years Old: ")
    return dependants_over_6_input

def get_dependants_under_6():
    "Prompts user for the number of their dependants under 6 years old"
    dependants_under_6_input = get_non_negative_number("Your Number of Dependants Under 6 Years Old: ")
    return dependants_under_6_input

def get_net_income():
    "Calculates the net income from gross income, dependants over/under 6, and standard deduction"
    gross_income = get_gross_income()
    dependants_over_6 = get_dependants_over_6()
    dependants_under_6 = get_dependants_under_6()
    STANDARD_DEDUCTION = 13850

    dependant_deduction = (3000 * dependants_over_6) + (2000 * dependants_under_6)
    net_income_calculation = gross_income - dependant_deduction - STANDARD_DEDUCTION

    return net_income_calculation

def print_income_tax():
    "Calculates and prints the income tax"
    net_income = get_net_income()

    if net_income < 11000:
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
        tax_rate = 0.37
    elif net_income >= 578125:
        tax_rate = 0.37

    income_tax_calculation = abs(net_income * tax_rate)
    income_tax_formatted = f"{income_tax_calculation:,.2f}"

    return print(f"\nYour Income Tax: ${income_tax_formatted}")

print_income_tax()