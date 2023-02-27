"""
b. Modify the program in Exercise 2a so that the user can enter any amount of numbers up to 20 until a sentinel value is entered.
"""

def is_valid_number(num: str): 
    try: 
        float(num) 
        return True
    except ValueError: 
        return False

def input_numbers():
    numbers = [] 
    while True: 
        userInput = input(f"Please provide a number and press ENTER. When you are finished, type \"quit\": ")
        if userInput == '':
            print("No input detected.") 
        if userInput == 'quit':
            break
        elif not is_valid_number(userInput): 
            print("Invalid character(s) detected.") 
        else:
            numbers.append(float(userInput)) 
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
