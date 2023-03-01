# pylint: disable=line-too-long
# pylint: disable=invalid-name
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

def is_valid_number(num: str) -> bool:
    "Determines if num can successfully be converted to a float"
    try:
        float(num)
        return True
    except ValueError:
        return False

def get_non_negative_number(prompt: str) -> float:
    "Tests if input is a valid number and greater than 0, then returns input as float."
    while True:
        user_input = input(prompt).replace("$","").replace(",","")
        if not is_valid_number(user_input.replace(".","")):
            print("Error: Invalid character(s) detected.")
            continue
        if float(user_input) < 0:
            print("Error: The amount of money inserted must be a non-negative number.")
            continue
        return float(user_input)

def get_random_images():
    "Determines the images rolled by the slot machine"
    images = ["Cherry", "Orange", "Plums", "Bell", "Melon", "Bar"]
    roll_1 = random.choice(images)
    roll_2 = random.choice(images)
    roll_3 = random.choice(images)
    return roll_1, roll_2, roll_3

def get_user_money():
    "Prompts the user to enter how much money they'd like to insert"
    money_input = get_non_negative_number("Enter the amount of money you'd like to insert: ")
    return money_input

def ask_to_play_again() -> bool:
    "Prompts user to enter if they'd like to play again"
    while True:
        play_again = input("Would you like to play again? Enter 'YES or 'NO': ")
        if play_again == "YES":
            return True
        if play_again == "NO":
            return False
        print("Error: Invalid character(s) detected.")

def display_total(total):
    "Displays total amount of money won or lost"
    if total > 0:
        return print(f"You gained a total of: ${total:,.2f}!")
    if total == 0:
        return print("You did not win or lose any money!")
    if total < 0:
        abs_total = abs(total)
        return print(f"You lost a total of ${abs_total:,.2f}!")

def slot_machine():
    "Simulates a slot machine"
    total_money_won = 0
    total_money_lost = 0
    while True:
        image_1, image_2, image_3 = get_random_images()
        money_inserted = get_user_money()

        total_length = len(image_1)+len(image_2)+len(image_3)+10
        for i in range(0, total_length): # pylint: disable=unused-variable
            print("-", end="")
        print("")
        print(f"| {image_1} | {image_2} | {image_3} |")
        for i in range(0, total_length):
            print("-", end="")
        print("")

        if image_1 == image_2 == image_3:
            amount_won = 3 * money_inserted
            print(f"You've won ${int(amount_won) if amount_won.is_integer() else amount_won}!")
            total_money_won += amount_won
            total_money_lost += money_inserted
            total = total_money_won - total_money_lost
            if ask_to_play_again() is False:
                return display_total(total)
        elif image_1 == image_2 or image_1 == image_3 or image_2 == image_3:
            amount_won = 2 * money_inserted
            print(f"You've won ${int(amount_won) if amount_won.is_integer() else amount_won}!")
            total_money_won += amount_won
            total_money_lost += money_inserted
            total = total_money_won - total_money_lost
            if ask_to_play_again() is False:
                return display_total(total)
        else:
            print("Oh no! You didn't win anything that time.")
            total_money_lost += money_inserted
            total = total_money_won - total_money_lost
            if ask_to_play_again() is False:
                return display_total(total)


print("Welcome to the slot machine!")
slot_machine()
print("Thanks for playing. Come again!")
