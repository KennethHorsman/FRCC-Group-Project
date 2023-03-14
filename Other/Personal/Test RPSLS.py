import random
from enum import Enum

class Choice(Enum):
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'
    LIZARD = 'lizard'
    SPOCK = 'spock'

def main():
    "Plays Rock Paper Scissors with the user"
    total_wins = 0
    total_losses = 0
    play_again = True

    while play_again is True:
        win, loss = play_round()
        total_wins += win
        total_losses += loss
        play_again = ask_to_play_again()

    print(f"Total Wins: {total_wins}\nTotal Losses: {total_losses}")
    print("Thanks for playing!")

def play_round():
    "Plays a single round of Rock Paper Scissors"
    win = 0
    loss = 0

    program_hand = generate_choice()
    user_hand = get_user_choice()

    if program_hand == user_hand:
        print(f"You both chose {user_hand.value}!")
    elif program_hand.beats(user_hand):
        print(f"{program_hand.value.title()} beats {user_hand.value}. You lost!")
        loss += 1
    else:
        print(f"{user_hand.value.title()} beats {program_hand.value}. You win!")
        win += 1

    return win, loss

def generate_choice():
    "Generates the program's hand"
    return random.choice(list(Choice))

def get_user_choice():
    "Asks for the user's hand"
    while True:
        user_input = input(f"Please enter {', '.join([c.value for c in Choice])}: ").lower()
        try:
            choice = Choice(user_input)
        except ValueError:
            print("Error: Invalid character(s).")
        else:
            return choice

def ask_to_play_again():
    "Prompts user to enter if they'd like to play again"
    while True:
        play_again = input("Would you like to play again? Enter 'YES' or 'NO': ").upper()
        if play_again == "YES":
            return True
        elif play_again == "NO":
            return False
        elif play_again not in ('YES', 'NO'):
            print("Error: Invalid character(s) detected.")
            return False

if __name__ == "__main__":
    main()
    input('')
