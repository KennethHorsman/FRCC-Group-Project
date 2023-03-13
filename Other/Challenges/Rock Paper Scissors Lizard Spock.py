#pylint: disable=invalid-name
#pylint: disable=line-too-long
#pylint: disable=inconsistent-return-statements
"""
From Big Bang Theory: Rock Paper Scissors, but with two added variables: Lizard and Spock!
"""

import random

def main():
    "Plays Rock Paper Scissors with the user"
    total_wins = 0
    total_losses = 0
    play_again = True

    print("Welcome to Rock-Paper-Scissors-Lizard-Spock!")
    match_length = get_match_length()
    
    if match_length > 0:
        while total_wins < match_length and total_losses < match_length:
            if did_user_win_rpsls() is True:
                total_wins += 1
            else:
                total_losses += 1
        if total_wins == match_length:
            print(f"You were the first to {match_length} round{'s' if match_length > 1 else ''} won. You win the game!")
        if total_losses == match_length:
            print(f"The computer was the first to {match_length} round{'s' if match_length > 1 else ''} won. You lose the game!")

    else:
        while play_again is True:
            if did_user_win_rpsls() is True:
                total_wins += 1
            else:
                total_losses += 1
            play_again = ask_to_play_again()
        print(f"Total Wins: {total_wins}\nTotal Losses: {total_losses}")

    print("Thanks for playing!")

def get_match_length():
    "Determines if match is indefinite or until a certain number of wins"
    match_length = 0
    get_length = True

    while get_length is True:
        length_input = input("To play indefinitely, type \"A\". To play until a certain number of wins, type \"B\": ")
        if length_input == "A":
            match_length = 0
            get_length = False
        elif length_input == "B":
            while match_length < 1:
                num_wins_input = input("Please enter the number of wins that will end the game: ")
                if not num_wins_input.isnumeric():
                    match_length = 0
                    print("Error: Invalid character(s) detected.")
                else:
                    match_length = int(num_wins_input)
            get_length = False
        else:
            print("Error: Invalid character(s) detected.")

    return match_length

def did_user_win_rpsls():
    "Determines if the user was the winner or loser in rock-paper-scissors-lizard-spock"
    user_hand, program_hand = compare_hands()

    game_rules = {'rock': ['scissors', 'lizard'],
                'paper': ['spock','rock'],
                'scissors': ['lizard','paper'],
                'lizard': ['paper','spock'],
                'spock': ['rock','scissors']}

    lose_to_program = game_rules[program_hand]
    lose_to_user = game_rules[user_hand]

    if program_hand in lose_to_user:
        print(f"{user_hand.title()} beats {program_hand}. You won that round!")
        return True
    if user_hand in lose_to_program:
        print(f"{program_hand.title()} beats {user_hand}. You lost that round!")
        return False

def compare_hands():
    "Compares computer vs users hands"
    get_hands = True

    while get_hands is True:
        program_hand = generate_choice()
        user_hand = get_user_choice()
        if program_hand == user_hand:
            print(f"You both chose {user_hand}!")
        else:
            print(f"You chose {user_hand}. Computer chose {program_hand}.")
            get_hands = False
            return user_hand, program_hand

def generate_choice():
    "Generates the programs hand"
    choices = ['rock','paper','scissors','lizard','spock']
    return random.choice(choices)

def get_user_choice():
    "Asks for the users hand"
    get_input = True
    while get_input is True:
        user_input = input("Please enter 'rock', 'paper', 'scissors', 'lizard', or 'spock': ").lower()
        if user_input not in ('rock','paper','scissors','lizard','spock'):
            print("Error: Invalid character(s).")
        else:
            return user_input

def ask_to_play_again():
    "Prompts user to enter if they'd like to play again"
    play_again = None
    while play_again not in (True, False):
        play_again = input("Would you like to play again? Enter 'YES or 'NO': ").upper()
        if play_again == "YES":
            return True
        if play_again == "NO":
            return False
        print("Error: Invalid character(s) detected.")

if __name__=="__main__":
    main()
    input('')
