# pylint: disable=line-too-long
# pylint: disable=invalid-name
"""
Project 2A

Write a program that takes as inputs the hourly wage, total regular hours, 
and total overtime hours and displays an employee's total weekly pay.

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
        input_result = input(prompt)
        if not is_valid_number(input_result):
            print("Error: Invalid character(s) detected.")
            continue
        if float(input_result) < 0:
            error_description = description
            print(f"Error: {error_description} must be a non-negative number.")
            continue
        return float(input_result)

def get_hourly_wage():
    "Prompts user for hourly wage"
    hourly_wage_input = get_non_negative_number(prompt="Your Hourly Wage: ", description="Your hourly wage")
    return hourly_wage_input

def get_regular_hours():
    "Prompts user for regular hours"
    regular_hours_input = get_non_negative_number(prompt="Your Regular Hours: ", description="Your regular hours")
    return regular_hours_input

def get_overtime_hours():
    "Prompts user for overtime hours"
    overtime_hours_input = get_non_negative_number(prompt="Your Overtime Hours: ", description="Your overtime hours")
    return overtime_hours_input

def print_weekly_pay():
    "Calculates and prints weekly pay"
    hourly_wage = get_hourly_wage()
    regular_hours = get_regular_hours()
    overtime_hours = get_overtime_hours()

    overtime_pay = (hourly_wage * 1.5) * overtime_hours
    weekly_pay = (hourly_wage * regular_hours) + overtime_pay
    weekly_pay_formatted = f"{weekly_pay:,.2f}"

    return print(f"\nTotal Weekly Pay: ${weekly_pay_formatted}")

print_weekly_pay()
