# Project 1C
# Collects input as a number from the user, then displays the sum and mean of the number(s).
# Horsman, Kenneth
# Course: CSC1019-FBN

def is_valid_number(num: str): # Num is expected to return as a string since input is automatically a string.
    try: # Tests a condition, and returns true or false.
        float(num) # Tests if the value can be converted to a float (allows decimals and negatives, but not things like "2-2", commas or spaces).
        return True
    except ValueError: #If not true, then there must be a 'ValueError' exception (in this case) and it returns false.
        return False

def input_numbers():
    numbers = [] # Creates an empty list.
    while True: #Establishes a loop that requires a condition to be fulfilled in order to exit the loop.
        userInput = input("Please provide a number and press ENTER. When you are finished, type \"quit\": ") # Prompts user for input.
        if userInput == '': # Tests if there was any input provided.
            print("No input detected.") 
        elif userInput == 'quit': # Tests if input was specifically "quit"
            break # If so, ends the loop.
        elif not is_valid_number(userInput): # Runs the is_valid_number function with userInput as num, and checks if it returned false.
            print("Invalid character(s) detected.") 
        else:
            numbers.append(float(userInput)) # Last possibility is userInput returned true in is_valid_number. So, add userInput to list numbers, and repeat the loop.
    return numbers # Returns the final list of numbers as the value of the function.


def print_sum_and_mean(numbers): # Assigns 'numbers' as the parameter to calculate values from. However, this could be anything, such as 'x'.
    calcSum = sum(numbers) if len(numbers) > 0 else "Undefined" # If numbers has at least one input, it calculates the sum. If not, it's "Undefined".
    calcMean = calcSum / len(numbers) if len(numbers) > 0 else "Undefined" # Same here as with above, but for the calculation of the mean.
    if calcSum == "Undefined":
        summed = calcSum # Keeps the value as it is, but with a different name for the print statement because:
    else:
        summed = int(calcSum) if calcSum.is_integer() else calcSum # If the calculated sum is technically an integer (meaning if it's a whole number), then convert it to one. Else, do nothing.
    if calcMean == "Undefined": # The next few lines are exactly the same as 31-34, but for the mean.
        mean = calcMean
    else:
        mean = int(calcMean) if calcMean.is_integer() else calcMean
    print(f"For the numbers {[int(x) if x.is_integer() else x for x in numbers]}:\nSum = {summed}\nMean = {mean}") 
    # F string automatically converts everything within the quotes to a string instead of doing str() for anything that's another data type (use curly brackets for them instead).
    # Loops through each input added to list numbers, checks if it's a whole number, and converts it to an integer if it is. If not, it leaves it as it is.
    # "\n" prints summed and mean values on new lines.
    return # No return is needed because it isn't technically returning a value, it's just executing the print statement above. However, you could instead put the print line here if you wanted.

numbers = input_numbers() # Assigns numbers as whatever value the input_numbers function returns.
print_sum_and_mean(numbers) # Sets the parameter for the sum_and_mean function as numbers, which we just assigned.
input('') # Allows you to view the output if you run the script in Python. Without this, Python will close as soon as everything has completed.
