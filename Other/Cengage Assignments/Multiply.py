"""
Multiply.py - This program prints the numbers 0 through 10 along
              with these values multiplied by 2 and by 10.
Input:  None.
Output: Prints the numbers 0 through 10 along with their values multiplied by
        2 and by 10.
"""

head1 = "Number: "
head2 = "Multiplied by 2: "
head3 = "Multiplied by 10:  "
NUM_LOOPS = 10  

print("0 through 10 multiplied by 2 and by 10" + "\n")

numberCounter = 0

while numberCounter <= 10:
    byTen = numberCounter * 10
    byTwo = numberCounter * 2
    print(head1 + str(numberCounter))
    print(head2 + str(byTwo))
    print(head3 + str(byTen))
    numberCounter += 1
    continue