# pylint: disable=line-too-long
# pylint: disable=invalid-name
"""
Project 2C:

Write a program that will compute a single filer's income tax.

1. Significant constants:
       tax rate -
              37% for above $578,125 
              35% for above $231,250 
              32% for above $182,100
              24% for above $95,375 
              22% for above $44,725 
              12% for above $11,000 
       standard deduction -
              $13,850 
       deduction per dependent -
              $2,000 for <=5 or $3,000 for 6-17 (not over 17)
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
    "Determines if the num can successfully be converted to a float"

    try:
        float(num)
        return True
    except ValueError:
        return False

def get_non_negative_number(prompt: str) -> float:
    "Tests if input is a valid number and greater than 0."

    while True:
        input_result = input(prompt)
        if not is_valid_number(input_result):
            print("Invalid character(s) detected.")
            continue
        if float(input_result) < 0:
            prompt_message = prompt.lower().strip(": ")
            print(f"The value of {prompt_message} must be at least 0.")
            continue
        return float(input_result)

def get_gross_income():
    "Prompts user for their gross income"

    gross_income_input = get_non_negative_number("Your Gross Income: ")
    return gross_income_input

def get_dependants_over_6():
    "Prompts user for the number of their dependants over 6 years old"

    dependants_over_6_input = get_non_negative_number("Number of Dependants Over 6 Years Old: ")
    return dependants_over_6_input

def get_dependants_under_6():
    "Prompts user for the number of their dependants under 6 years old"

    dependants_under_6_input = get_non_negative_number("Number of Dependants Under 6 Years Old: ")
    return dependants_under_6_input

gross_income = get_gross_income()
dependants_over_6 = get_dependants_over_6()
dependants_under_6 = get_dependants_under_6()

def get_net_income():
    "Calculates the net income from gross income, dependants over/under 6, and standard deduction"

    STANDARD_DEDUCTION = 13850
    dependant_deduction = (2000 * dependants_under_6) + (3000 * dependants_over_6)
    net_income = gross_income - dependant_deduction - STANDARD_DEDUCTION

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

    income_tax_result = int(net_income * tax_rate)
    # I had to add int() here because it would return -0.00 with certain values???

    return income_tax_result

income_tax = get_net_income()

income_tax_formatted = "{:,.2f}".format(income_tax) # pylint: disable=consider-using-f-string

print(f"Your Income Tax: ${income_tax_formatted}")
