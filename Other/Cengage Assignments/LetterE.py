# LetterE.py - This program prints the letter E with 3 asterisks

NUM_ACROSS = 3 
NUM_DOWN = 5 

for row in range(NUM_DOWN):
    for column in range(NUM_ACROSS):
        if (row % 2 == 0) or (column == 0):
            print('*', end='')
        else:
            print(' ', end='')
    print()