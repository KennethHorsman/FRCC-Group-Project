# pylint: disable=line-too-long
# pylint: disable=invalid-name
# pylint: disable=too-many-statements
"""
Project 3C:
Develop a program that simulates a slot machine. When the program runs, it should do the following:
Ask the user to enter the amount of money they want to insert
Instead of displaying images, the program will randomly select a word from the following list: 
Cherry, Orange, Plums, Bell, Melon, Bar. 
The program will select and display a word from this list three times. 
If none of the randomly selected words match, the program will inform the user that they've won $0. 
If two words match, the program will inform the user that he or she has won two time the amount entered. 
If three words match, the program will inform the user that they've won three times the amount entered.
The program will ask whether the user wants to play again. If so, the steps are repeated. 
If not, the program displays the total amount of money entered into the slot machine and the total amount won.

Programmer: Horsman, Kenneth. Group Members: Nowak, Stephen. Jimenez-Morales, Destinee.

Course: CSC1019-FBN 
"""

import random

def main():
    "Program that simulates a slot machine"
    print("Welcome to the slot machine!")
    slot_machine()
    print("Thanks for playing. Come again!")

def slot_machine():
    "Determines if the user won money from the slot machine game"
    total_money_won = 0
    total_money_lost = 0
    roll_slot_machine = True

    while roll_slot_machine is True:
        images = get_random_images()
        money_inserted = get_user_money()

        total_length = sum(len(x) for x in images)+10 # Calculates the total length of line 42
        print("-" * total_length) # Prints the number of dashes that will perfectly cover line 42
        print(f"| {images[0]} | {images[1]} | {images[2]} |") # Prints each image that was randomly generated in 3 separated boxes
        print("-" * total_length)

        image_dict = {} # Creates an empty dictionary
        for x in images: # Loops through each item in list images
            image_dict[x] = image_dict.get(x,0)+1 # Creates key in dict as x, assigns value as 0 if not already in dict, and adds 1 for that occurance of the key
        num_matches = max(image_dict.values()) # Finds the highest value in the dict, which is the number of matches (occurances) of the key

        if num_matches == 3:
            amount_won = 3 * money_inserted
            print(f"You've won ${amount_won:,.2f}!")
        elif num_matches == 2:
            amount_won = 2 * money_inserted
            print(f"You've won ${amount_won:,.2f}!")
        else:
            amount_won = 0
            print("Oh no! You didn't win anything that time.")

        total_money_won += amount_won
        total_money_lost += money_inserted
        grand_total = total_money_won - total_money_lost

        if ask_to_play_again() is False: # Performs the ask_to_play function, and only if it returns False does the while loop end up breaking on line 67
            roll_slot_machine = False # Completely useless line of code but it's helpful to indicate that roll_slot_machine has stopped
            display_total(grand_total) # Uses the calculated grand total as the parameter in the display_total function
            return

def get_random_images():
    "Determines the images rolled by the slot machine"
    images = ["Cherry", "Orange", "Plums", "Bell", "Melon", "Bar"]
    return [random.choice(images) for x in range(3)] # randomly selects an item from images 3 times and puts them in a list

def get_user_money():
    "Prompts the user to enter how much money they'd like to insert"
    money_input = get_non_negative_number("Enter the amount of money you'd like to insert: ")
    return money_input

def get_non_negative_number(prompt: str) -> float:
    "Tests if input is a valid number and greater than 0, then returns input as float."
    test_number = True
    while test_number is True:
        user_input = input(prompt).strip("$").replace(",","")
        if not is_valid_number(user_input):
            print("Error: Invalid character(s) detected.")
        elif float(user_input) < 0:
            print("Error: The amount of money inserted must be a non-negative number.")
        else:
            test_number = False
            return float(user_input)

def is_valid_number(num: str) -> bool:
    "Determines if num can successfully be converted to a float"
    try:
        float(num)
        return True
    except ValueError:
        return False

def ask_to_play_again() -> bool:
    "Prompts user to enter if they'd like to play again"
    play_again = None
    while play_again not in (True, False):
        play_again = input("Would you like to play again? Enter 'YES or 'NO': ").upper()
        if play_again == "YES":
            return True
        if play_again == "NO":
            return False
        print("Error: Invalid character(s) detected.")

def display_total(total):
    "Displays total amount of money won or lost"
    if total > 0:
        print(f"You gained a total of ${total:,.2f}!")
        return
    if total == 0:
        print("You did not gain or lose any money!")
        return
    if total < 0:
        abs_total = abs(total)
        print(f"You lost a total of ${abs_total:,.2f}!")
        return

if __name__=="__main__":
    main()
