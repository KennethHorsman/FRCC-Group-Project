"""
Project 2A:

Write a program that takes as inputs the hourly wage, total regular hours, and total overtime hours and displays an employee's total weekly pay.

Overtime pay equals the total overtime hours multiplied by 1.5 times the hourly wage.
An employee's total weekly pay equals the hourly wage multiplied by the total number of regular hours plus any overtime pay. 
"""

def is_valid_number(num): 
    try: 
        float(num) 
        return True
    except ValueError: 
        return False

def Weekly_Pay():
    while True:
        hourly_wage = input("Please enter your hourly wage: ") 
        if not is_valid_number(hourly_wage): 
            print("Invalid character(s) detected.") 
        elif float(hourly_wage) < 0:
            print("Your hourly wage must be a positive number.")
        else:
            hourly_wage = float(hourly_wage)
            break

    while True:
        total_regular_hours = input("Please enter your total regular hours: ")
        if not is_valid_number(total_regular_hours): 
            print("Invalid character(s) detected.") 
        elif float(total_regular_hours) < 0:
            print("Your total regular hours must be a positive number.")
        else:
            total_regular_hours = float(total_regular_hours)
            break

    while True:
        total_overtime_hours = input("Please enter your total overtime hours: ")
        if not is_valid_number(total_overtime_hours): 
            print("Invalid character(s) detected.") 
        elif float(total_overtime_hours) < 0:
            print("Your total overtime hours must be a positive number.")
        else:
            total_overtime_hours = float(total_overtime_hours)
            break

    overtime_pay = total_overtime_hours * (1.5 * hourly_wage)
    total_weekly_pay = (hourly_wage * total_regular_hours) + overtime_pay
    return total_weekly_pay

weekly_pay = Weekly_Pay()
weekly_pay = "{:,.2f}".format(round(weekly_pay,2))

print(f"\nTotal Weekly Pay: ${weekly_pay}")
input('')
