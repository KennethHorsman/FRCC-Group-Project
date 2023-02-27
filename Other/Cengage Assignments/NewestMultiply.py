"""
NewestMultiply.py - This program prints the numbers 0 through 10 along with
                     these values multiplied by 2 and by 10.
Input:  None.
Output: Prints the numbers 0 through 10 along with their values multiplied by
        2 and by 10.
"""

head1 = "Number: "
head2 = "Multiplied by 2: "
head3 = "Multiplied by 10:  "
NUM_LOOPS = 0  

print("0 through 10 multiplied by 2 and by 10" + "\n")

while True:
    print(head1 + str(NUM_LOOPS))
    print(head2 + str(NUM_LOOPS * 2))
    print(head3 + str(NUM_LOOPS * 10))
    NUM_LOOPS = NUM_LOOPS + 1
    if NUM_LOOPS > 10:
        break