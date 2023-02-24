def Is_Valid_Number(num: str) -> bool: 
    try: 
        float(num) 
        return True
    except ValueError: 
        return False

def Get_Non_Negative_Number(prompt: str) -> float:
    while True:
        input_result = input(prompt)
        if not Is_Valid_Number(input_result):
            print("Invalid character(s) detected.")
            continue
        return float(input_result)

def Get_Hourly_Wage():
    hourly_wage = Get_Non_Negative_Number("Please enter your hourly wage: ")
    return hourly_wage

def Get_Regular_Hours():
    regular_hours = Get_Non_Negative_Number("Please enter your regular hours: ")
    return regular_hours

def Get_Overtime_Hours():
    overtime_hours = Get_Non_Negative_Number("Please enter your overtime hours: ")
    return overtime_hours

hourly_wage = Get_Hourly_Wage()
regular_hours = Get_Regular_Hours()
overtime_hours = Get_Overtime_Hours()

weekly_pay = hourly_wage * (regular_hours + (1.5 * overtime_hours))

print(f"\nTotal Weekly Pay: ${weekly_pay}")
input('')