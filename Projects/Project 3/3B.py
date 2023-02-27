# pylint: disable=line-too-long
# pylint: disable=invalid-name
# pylint: disable=useless-return
"""
Project 3B: 
Develop a number guessing game. The program should generate a random number and then 
ask the user to guess the number. Each time the user enters a guess, the program should 
indicate whether it was too high or too low. The game is over when the user correctly guesses 
the number. When the game ends, the program should display the number of guesses the user made. 
Break your program into functions where appropriate.

Programmer: Horsman, Kenneth. Group Members: Nowak, Stephen. Jimenez-Morales, Destinee.

Course: CSC1019-FBN 
"""

import random

def get_non_negative_number(prompt: str) -> int:
    "Tests if input is a valid number and greater than 0, then returns input as float."
    while True:
        user_input = input(prompt)
        if not user_input.isdigit():
            print("Error: Invalid character(s) detected.")
            continue
        if float(user_input) > 9:
            print("Error: Your guess is out of bounds.")
            continue
        return int(user_input)

def generate_random_number():
    "Generates a random number between 0 and 9"
    generated_number = random.randint(0,10)
    return generated_number

def get_users_guess():
    "Prompts user to guess a number"
    user_guess_input = get_non_negative_number("Guess a number between 0 and 9: ")
    return user_guess_input

def guess_random_number():
    "Determines if users guess was correct"
    random_number = generate_random_number()
    count = 1
    while True:
        user_guess = get_users_guess()
        if user_guess > random_number:
            print("That number is too high.")
            count += 1
        elif user_guess < random_number:
            print("That number is too low.")
            count += 1
        else:
            print("That's correct!")
            print(f"Number of guesses: {count}")
            break
    return None

def ask_to_play_again():
    "Prompts user to enter whether they would like to play again"
    while True:
        play_again = input("Would you like to play again? Enter 'YES' or 'NO': ")
        if play_again == "YES":
            guess_random_number()
        elif play_again == "NO":
            break
        else:
            print("Error: Invalid character(s) detected.")
    return None

guess_random_number()
ask_to_play_again()
