"""
GuessNumber.py - This program allows a user to guess a number
                  between 1 and 10.
Input:  User guesses numbers until they get it right.
Output: Tells users if they are right or wrong.
"""

import random

number = random.randint(1, 10)

keepGoing = input("Do you want to guess a number? Enter Y or N ")

while keepGoing == "N":
    print("Bye!")
    break

while keepGoing == "Y":
    stringNumber = input("I'm thinking of a number. .\n Try to guess by entering a number between 1 and 10 ")
    userNumber = int(stringNumber)
    if stringNumber == "N":
        print("Bye!")
        break
    if userNumber == number:
        keepGoing = "N"
        print("You are a genius. That's correct!")
    else:
        keepGoing = input("That's not correct. Do you want to guess again? Enter Y or N ")
        if keepGoing == "N":
            print("Bye!")
            break        