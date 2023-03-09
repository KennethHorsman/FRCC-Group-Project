#pylint: disable=invalid-name
#pylint: disable=line-too-long
"""
Rock, Paper, Scissors game - 
Take in a user input for rock, paper, or scissors and have code that runs the 
user input vs a randomly generated rock, paper, or scissors to see if the user wins or the computer wins.
"""

import random

def main():
    "Plays Rock Paper Scissors with the user"
    play_again = True
    while play_again is True:
        rock_paper_scissors()
        play_again = ask_to_play_again()
    print("Thanks for playing!")

def rock_paper_scissors():
    "Determines game winner"
    get_hands = True
    while get_hands is True:
        program_hand = generate_choice()
        user_hand = get_user_choice()
        if program_hand == user_hand:
            print(f"You both chose {user_hand}!")
        else:
            print(f"You chose {user_hand}. Computer chose {program_hand}.")
            get_hands = False

    game_rules = {'rock': ['scissors', 'lizard'],
                'paper': ['spock','rock'],
                'scissors': ['lizard','paper'],
                'lizard': ['paper','spock'],
                'spock': ['rock','scissors']}

    lose_to_program = game_rules[f"{program_hand}"]
    lose_to_user = game_rules[f"{user_hand}"]

    if user_hand in lose_to_program: # If the user_hand is one of the value that loses against the program_hand value, user loses
        print(f"{program_hand.title()} beats {user_hand}. You lost!")
        return
    if program_hand in lose_to_user: # If the user_hand is one of the value that wins against the program_hand value, user wins
        print(f"{user_hand.title()} beats {program_hand}. You win!")
        return

def generate_choice():
    "Generates the programs hand"
    choices = ['rock','paper','scissors','lizard','spock']
    return random.choice(choices)

def get_user_choice():
    "Asks for the users hand"
    get_input = True
    while get_input is True:
        user_input = input("Please enter 'rock', 'paper', 'scissors', 'lizard', or 'spock': ")
        if user_input.lower() not in ('rock','paper','scissors','lizard','spock'):
            print("Error: Invalid character(s).")
        else:
            return user_input.lower()

def ask_to_play_again():
    "Prompts user to enter if they'd like to play again"
    play_again = None
    while False != play_again != True:
        play_again = input("Would you like to play again? Enter 'YES or 'NO': ").upper()
        if play_again == "YES":
            return True
        if play_again == "NO":
            return False
        print("Error: Invalid character(s) detected.")

if __name__=="__main__":
    main()
