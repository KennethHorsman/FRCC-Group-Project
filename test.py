import random

def generate_random_number():
    "Generates a random number between 0 and 9"
    generated_number = random.randint(0,10)
    return print(f"{generated_number}")

generate_random_number()