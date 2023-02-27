"""
b. Modify the reverse-display program so that the user can enter any amount of numbers up to 20 until a sentinel value is entered.
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
        elif userInput == 'quit':
            break 
        elif not is_valid_number(userInput): 
            print("Invalid character(s) detected.") 
        else:
            numbers.append(float(userInput)) 
    return numbers 

def reverse_numbers(numbers):
    numbers.reverse()
    print(f"The numbers you entered in reverse order are: {[int(x) if x.is_integer() else x for x in numbers]}.")
    return

numbers = input_numbers()
reverse_numbers(numbers)
input('')
