from typing import Optional

def find_first_invalid_character(num: str) -> Optional[str]:
    """ Find and return the first 'invalid' character (one that causes the float conversion to fail). If it doesn't find one, then it returns None. """
    for i in range(1, len(num)+1):
        try:
            float(num[:i])
        except ValueError:
            return num[i-1]
    return None

def is_valid_number(num: str) ->  bool: # Num is expected to return as a string. '-> bool' is a type hint to say the function returns true or false.
    try: # Tests if it can execute commands below. If it can, it skips the except line.
        float(num) # Tests if the value can be converted to a float (allows decimals and negatives!)
        return True
    except ValueError: #If there's a ValueError exception, it returns false.
        return False

def input_numbers():
    numbers = []
    while True:
        userInput = input("Please provide a number and press ENTER. When you are finished, type \"quit\": ")
        if userInput == '':
            print("No input detected.") 
        elif userInput == 'quit':
            break
        elif not is_valid_number(userInput):
            print(f"Invalid character \"{find_first_invalid_character(userInput)}\" detected in {userInput}.") #Calls the function to find char only if it doesnt pass valid number check
        else:
            numbers.append(float(userInput)) # When dealing with only one value, use append not extend
    return numbers

def print_sum_and_mean(numbers): # Assigns 'numbers' as the parameter to calculate values from
    calcSum = sum(numbers) if len(numbers) > 0 else "Undefined"
    calcMean = calcSum / len(numbers) if len(numbers) > 0 else "Undefined"
    if calcSum == "Undefined":
        summed = calcSum
    else:
        summed = int(calcSum) if calcSum.is_integer() else calcSum
    if calcMean == "Undefined":
        mean = calcMean
    else:
        mean = int(calcMean) if calcMean.is_integer() else calcMean
    print(f"For the numbers {[int(x) if x.is_integer() else x for x in numbers]}:\nSum = {summed}\nMean = {mean}") # Loops through each value in numbers, checking if its an integer
    return

numbers = input_numbers() # Assigns 'numbers' so the below function knows what its parameter value is
print_sum_and_mean(numbers)
input('')
