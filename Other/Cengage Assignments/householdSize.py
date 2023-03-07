"""
HouseholdSize.py - This program uses a bubble sort to arrange household sizes
                    in descending order and then prints the mean and median
                    household size.
Input:  Interactive.
Output:  Mean and median household size.
"""

# Initialize variables.
householdSizes = []  # Array used to store household sizes.
numSizes = 0
total = 0.0
mean = 0.0
median = 0.0

# Input household size
householdSizeString = input("Enter household size or 999 to quit: ")
householdSize = int(householdSizeString)
# This is the work done in the fillArray() function
while (householdSize != 999):
    # Place value in array.
    householdSizes.append(householdSize)
    # Calculate total of household sizes
    total = sum(householdSizes)

    numSizes += 1  # We have one more house
    householdSizeString = input("Enter household size or 999 to quit: ")
    householdSize = int(householdSizeString)

# Find the mean
mean = total / len(householdSizes)

# This is the work done in the sortArray() function
householdSizes.sort()
# This is the work done in the displayArray() function
import statistics
median = statistics.median(householdSizes)
# Find the median
print(mean)
print(median)
