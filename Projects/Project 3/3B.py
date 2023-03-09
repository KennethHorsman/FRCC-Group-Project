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

def main():
    "Simulates a number guessing game"
    print("Welcome to the number guessing game!")
    play_again = True
    while play_again is True:
        guess_random_number()
        play_again = ask_to_play_again()
    print("Thanks for playing!")

def guess_random_number():
    "Determines if users guess was correct"
    random_number = generate_random_number()
    guess_dict = {}
    user_guess = None

    while user_guess != random_number:
        user_guess = get_users_guess()
        if user_guess > random_number:
            print("That number is too high.")
        elif user_guess < random_number:
            print("That number is too low.")
        guess_dict[user_guess] = guess_dict.get(user_guess,0)+1

    guess_dict[user_guess] = guess_dict.get(user_guess,0)+1
    print("That's correct!")
    print(f"Number of guesses: {len(guess_dict)}")
    return

def generate_random_number():
    "Generates a random number between 0 and 9"
    generated_number = random.randint(0,9)
    return generated_number

def get_users_guess():
    "Prompts user to guess a number"
    user_guess_input = get_digit_in_range("Guess a number between 0 and 9: ")
    return user_guess_input

def get_digit_in_range(prompt: str) -> int:
    "Tests if input is a valid number and greater than 0, then returns input as an integer."
    test_number = True
    while test_number is True:
        user_input = input(prompt)
        if not user_input.isdigit():
            print("Error: Invalid character(s) detected.")
        elif float(user_input) > 9:
            print("Error: Your guess is out of bounds.")
        else:
            test_number = False
            return int(user_input)

def ask_to_play_again():
    "Prompts user to enter whether they would like to play again"
    play_again_input = None
    while play_again_input not in (True, False):
        play_again_input = input("Would you like to play again? Enter 'YES' or 'NO': ")
        if play_again_input == "YES":
            return True
        if play_again_input == "NO":
            return False
    print("Error: Invalid character(s) detected.")

if __name__=="__main__":
    main()
