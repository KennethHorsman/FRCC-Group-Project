# NewMultiply.py - This program prints the numbers 0 through 10 along with these values multiplied by 2 and by 10.

head1 = "Number: "
head2 = "Multiplied by 2: "
head3 = "Multiplied by 10: "

NUM_LOOP_START = 0  
NUM_LOOP_END = 11 

print("0 through 10 multiplied by 2 and by 10.")

for x in range(NUM_LOOP_START, NUM_LOOP_END):
    print(head1 + str(x))
    print(head2 + str((x * 2)))
    print(head3 + str((x * 10)))