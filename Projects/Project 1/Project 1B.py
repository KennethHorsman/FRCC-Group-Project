# Project 1B
# Displays a sentence containing the user's name and age.
# Horsman, Kenneth
# Course: CSC1019-FBN

def Name():
    while True: 
        userInput = input("Please enter your name: ")
        if userInput == '':
            print("No input given.")
            continue
        invalidInput = [x for x in userInput.replace(" ","").replace("-","") if not x.isalpha()]
        if len(invalidInput) > 0:
            print(f"Invalid characters detected: {invalidInput}")
            continue
        else:
            name = userInput.title()
            break
    return name

def Age():
    while True:
        userInput = input("Please enter your age: ")
        if userInput == '':
            print("No input given.")
            continue
        invalidInput = [x for x in userInput if not x.isnumeric()]
        if len(invalidInput) > 0:
            print(f"Invalid characters detected: {invalidInput}")
            continue
        else:
            age = userInput
            break
    return age

name = Name()
age = Age()
print(f"Your name is {name} and your age is {age}.")
input('')
