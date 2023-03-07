"""
HouseholdSize.py - This program uses a bubble sort to arrange household sizes
                    in descending order and then prints the mean and median
                    household size.
Input:  Interactive.
Output:  Mean and median household size.
"""

import statistics

householdSizes = []
SENTINEL = False

while SENTINEL is False:
    householdSize = int(input("Enter household size or 999 to quit: "))
    if householdSize != 999:
        householdSizes.append(householdSize)
    else:
        SENTINEL = True

total = sum(householdSizes)
mean = total / len(householdSizes)

householdSizes.sort()
median = statistics.median(householdSizes)

print(mean)
print(median)
