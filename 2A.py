# pylint: disable=line-too-long
# pylint: disable=invalid-name
"""
Project 2A:

Write a program that takes as inputs the hourly wage, total regular hours, 
and total overtime hours and displays an employee's total weekly pay.

Overtime pay equals the total overtime hours multiplied by 1.5 times the hourly wage.
An employee's total weekly pay equals the hourly wage multiplied by the total number 
of regular hours plus any overtime pay. 
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

def get_hourly_wage():
    "Prompts user for hourly wage"
    hourly_wage_input = get_non_negative_number("Your Hourly Wage: ")
    return hourly_wage_input

def get_regular_hours():
    "Prompts user for regular hours"
    regular_hours_input = get_non_negative_number("Your Regular Hours: ")
    return regular_hours_input

def get_overtime_hours():
    "Prompts user for overtime hours"
    overtime_hours_input = get_non_negative_number("Your Overtime Hours: ")
    return overtime_hours_input

hourly_wage = get_hourly_wage()
regular_hours = get_regular_hours()
overtime_hours = get_overtime_hours()

weekly_pay = hourly_wage * (regular_hours + (1.5 * overtime_hours))
weekly_pay_formatted = "{:,.2f}".format(weekly_pay) # pylint: disable=consider-using-f-string

print(f"\nTotal Weekly Pay: ${weekly_pay_formatted}")
