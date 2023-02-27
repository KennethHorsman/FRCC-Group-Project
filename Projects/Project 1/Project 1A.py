# Project 1A
# Displays the user's name, address, and telephone number.
# Horsman, Kenneth
# Course: CSC1019-FBN

def Name():
    while True: # Creates a loop that requires a condition to be fulfilled in order to break.
        userInput = input("Please enter your name: ") # Prompts user for input.
        if userInput == '': # Checks if there was any input.
            print("No input given.") # Prints this statement, then repeats the loop starting with the prompt for input.
        invalidInput = [x for x in userInput.replace("-","").replace(" ","") if not x.isalpha()] # Creates a list of values that are NOT alphabet letters (if any) after removing any dashes and spaces.
        if len(invalidInput) > 0: # If there is at least one value in the above list:
            print(f"Invalid characters detected: {invalidInput}") # Display the invalid character and repeat the loop.
        else:
            name = userInput.title() # The last possibility is that the input was valid. So, assign name as each word from userInput being capitalized (also includes the letter after a dash).
            break # Then break the loop once a valid name has been given, since we only need one.
    return name # And have the function return the value of name. Remember, this isn't a global variable.

def Address():
    while True:
        userInput = input("Please enter your address: ")
        if userInput == '':
            print("No input given.")
        invalidInput = [x for x in userInput.replace("-","").replace(" ","") if not x.isalnum()] # Everything here is the same as above, but it allows for alphabet letters AND numeric characters.
        if len(invalidInput) > 0:
            print(f"Invalid characters detected: {invalidInput}")
        else:
            address = userInput.title()
            break
    return address

def Telephone():
    while True:
        userInput = input("Please enter your telephone number: ")
        if userInput == '':
            print("No input given.")
        invalidInput = [x for x in userInput.replace("-","") if not x.isnumeric()] # Again, all the same as above (except for no title() below), but this time it only allows numeric characters.
        if len(invalidInput) > 0:
            print(f"Invalid characters detected: {invalidInput}")
        else:
            telephone = userInput
            break
    return telephone

name = Name() # Assigns name as the value returned from the function Name. Same concept for the next two lines.
address = Address()
telephone = Telephone()
print(f"Name: {name}\nAddress: {address}\nTelephone: {telephone}") # F string automatically converts everything to a string, and \n prints out name/address/telephone on separate lines.
input('') # Allows you to view the output if you run the script in Python. Without this, Python will close as soon as everything has completed.
