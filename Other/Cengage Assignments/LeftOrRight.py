"""
LeftOrRight.py - This program calculates the total number of left-handed and
                   right-handed students in a class.
Input:  L for left-handed; R for right handed; X to quit.
Output: Prints the number of left-handed students and the number of right-handed students.
"""

rightTotal = 0  
leftTotal = 0  

while True:
    leftOrRight = input("Enter an L if you are left-handed,a R if you are right-handed or X to quit.")
    if leftOrRight == "L":
        leftTotal += 1
        continue
    elif leftOrRight == "R":
        rightTotal += 1
        continue
    elif leftOrRight == "X":
        break

print("Number of left-handed students: " + str(leftTotal))
print("Number of right-handed students: " + str(rightTotal))