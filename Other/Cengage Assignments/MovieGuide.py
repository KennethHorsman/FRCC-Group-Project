"""
MovieGuide.py

This program allows each theater patron to enter a value from
0 to 4 indicating the number of stars that the patron awards
to the Guide's featured movie of the week. The program
executes continuously until the theater manager enters a
negative number to quit. At the end of the program, the
average star rating for the movie is displayed.
"""

totalStars = 0  
numPatrons = 0  
averageStars = 0
numStars = 0

while numStars >= 0:
    totalStars = totalStars + numStars
    numPatrons = numPatrons + 1
    numStarsString = input("Enter rating for featured movie: ")
    numStars = float(numStarsString)

averageStars = totalStars / numPatrons
print("Average Star Value: " + str(averageStars))