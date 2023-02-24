""" This generally looks good! I would split the weekly_pay function into three different ones: get_hourly_wage, get_regular_hours, and get_overtime_hours 
in order to make the program flow a bit more readable. The the actual program would look something like

hourly_wage = get_hourly_wage()
regular_hours = get_regular_hours()
overtime_hours = get_overtime_hours()

weekly_pay = hourly_wage * (regular_hours + 1.5 * overtime_hours)

print(f"\nTotal Weekly Pay: ${weekly_pay}")
input('')

Also, you end up doing basically the same thing (get an input,check that it's a number, check that it's non-negative) quit a few times, both in this program and in the others. 
It might be a good idea to write a general function to abstract this process. Something like:

def get_non_negative_number(prompt: str) -> float:
    while True:
        input_result = input(prompt)
        if not is_valid_number(input_result):
            print("Not valid! (or something)")
            continue
        return str(input_result)
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