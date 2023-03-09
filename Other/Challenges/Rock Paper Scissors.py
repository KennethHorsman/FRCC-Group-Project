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

def generate_choice():
    "Generates the programs hand"
    choices = ['rock','paper','scissors']
    return random.choice(choices)

def get_user_choice():
    "Asks for the users hand"
    get_input = True
    while get_input is True:
        user_input = input("Please enter 'rock', 'paper', or 'scissors': ")
        if user_input.lower() not in ('rock','paper','scissors'):
            print("Error: Invalid character(s).")
        else:
            get_input = False
    return user_input.lower()

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

    winner_list = ['rock','paper','scissors'] # Sets up parallel arrays. The value on top beats the corresponding value below.
    loser_list = ['scissors','rock','paper']

    winner_index = winner_list.index(program_hand) # Finds the index of the program's hand on the top list
    loser_index = loser_list.index(program_hand) # And the bottom list too
    winning_hand = winner_list[loser_index] # Sets winning_hand as whichever value would win against the value of program_hand on the bottom list
    losing_hand = loser_list[winner_index] # Sets losing_hand as whichever value would lose against the value of program_hand on the top list

    if user_hand == losing_hand: # If the user_hand is the value that loses against the program_hand value, user loses
        print(f"{program_hand.title()} beats {user_hand}. You lost!")
    elif user_hand == winning_hand: # If the user_hand is the value that wins against the program_hand value, user wins
        print(f"{user_hand.title()} beats {program_hand}. You win!")

def ask_to_play_again():
    "Prompts user to enter if they'd like to play again"
    play_again = None
    while False != play_again != True:
        play_again = input("Would you like to play again? Enter 'YES or 'NO': ")
        if play_again == "YES":
            return True
        if play_again == "NO":
            return False
        print("Error: Invalid character(s) detected.")

if __name__=="__main__":
    main()
