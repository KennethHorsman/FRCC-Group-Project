def Is_Valid_Number(num: str) -> bool: 
    try: 
        float(num) 
        return True
    except ValueError: 
        return False

def Get_Non_Negative_Number(prompt: str) -> bool:
    while True:
        if not Is_Valid_Number(prompt):
            print("Invalid character(s) detected.")
            return False
        elif float(prompt) < 0:
            print("The value entered must be at least 0.")
            return False
        else:
            return True

def Get_Hourly_Wage():
    while True:
        hourly_wage_input = input("Please enter your hourly wage: ") 
        if not Get_Non_Negative_Number(hourly_wage_input):
            continue
        elif Get_Non_Negative_Number(hourly_wage_input):
            hourly_wage = float(hourly_wage_input)
            break
    return hourly_wage

def Get_Regular_Hours():
    while True:
        regular_hours_input = input("Please enter your hourly wage: ") 
        if not Get_Non_Negative_Number(regular_hours_input):
            continue
        elif Get_Non_Negative_Number(regular_hours_input):
            regular_hours = float(regular_hours_input)
            break
    return regular_hours

def Get_Overtime_Hours():
    while True:
        overtime_hours_input = input("Please enter your hourly wage: ") 
        if not Get_Non_Negative_Number(overtime_hours_input):
            continue
        elif Get_Non_Negative_Number(overtime_hours_input):
            overtime_hours = float(overtime_hours_input)
            break
    return overtime_hours

hourly_wage = Get_Hourly_Wage()
regular_hours = Get_Regular_Hours()
overtime_hours = Get_Overtime_Hours()

weekly_pay = hourly_wage * (regular_hours + (1.5 * overtime_hours))

print(f"\nTotal Weekly Pay: ${weekly_pay}")
input('')