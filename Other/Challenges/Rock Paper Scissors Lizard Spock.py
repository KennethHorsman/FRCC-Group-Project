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

    winner_list = ['rock', 'paper', 'scissors', 'lizard', 'spock'] # Sets up parallel arrays. The value on top beats the corresponding value below.
    loser_list1 = ['scissors','spock','lizard','paper','rock']
    loser_list2 = ['lizard','rock','paper','spock','scissors']

    winner_index = winner_list.index(program_hand) # Finds the index of the program's hand on the top list
    loser_index1 = loser_list1.index(program_hand) # Finds the index of the programs hand if it were a losing value
    loser_index2 = loser_list2.index(program_hand) # Finds second losing value

    winning_hand1 = winner_list[loser_index1] # Sets one winning_hand as whichever value would win against the value of program_hand on the first losing list
    winning_hand2 = winner_list[loser_index2] # Finds the second winning hand

    losing_hand1 = loser_list1[winner_index] # Sets one losing_hand as whichever value would lose against the value of program_hand on the top list
    losing_hand2 = loser_list2[winner_index] # Finds the second losing hand

    if user_hand in (losing_hand1, losing_hand2): # If the user_hand is one of the value that loses against the program_hand value, user loses
        print(f"{program_hand.title()} beats {user_hand}. You lost!")
        return
    if user_hand in (winning_hand1, winning_hand2): # If the user_hand is one of the value that wins against the program_hand value, user wins
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
            get_input = False
    return user_input.lower()

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
