"""
a. Design the logic for a program that allows a user to enter 20 numbers, then displays each number and its difference from the numeric average of the numbers entered.

"""

def is_valid_number(num: str): 
    try: 
        float(num) 
        return True
    except ValueError: 
        return False

def input_numbers():
    numbers = [] 
    count = 20
    while len(numbers) < 20: 
        userInput = input(f"Please provide a number and press ENTER. You must enter {count} more number(s): ")
        if userInput == '':
            print("No input detected.") 
        elif not is_valid_number(userInput): 
            print("Invalid character(s) detected.") 
        else:
            numbers.append(float(userInput)) 
            count -= 1
    return numbers 

def difference_and_average(numbers):
    numbers2 = [int(x) if x.is_integer() else x for x in numbers]
    calcAvg = sum(numbers2) / len(numbers2)
    average = int(calcAvg) if calcAvg.is_integer() else calcAvg
    print(f"The average of {numbers2} is {average}.")
    for x in numbers2:
        calcDiff = round(float(average - x), 5)
        difference = int(calcDiff) if calcDiff.is_integer() else calcDiff
        print(f"{x} subtracted from {average} is {difference}.")
    return

numbers = input_numbers()
difference_and_average(numbers)
input('')
