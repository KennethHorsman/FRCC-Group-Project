# Declare two dimensional list here

# Declare other variables
QUIT = 99

age = int(input("Enter the age of the child or 99 to quit: "))

# Perform a priming read to get the age of the child
while age != QUIT:

    # Ask the user to enter the number of days
    days = int(input("Enter number of days per week: "))
    # Print the weekly rate
    rate = [[30.0,60.0,88.0,115.0,140.0],
            [26.0,52.0,70.0,96.0,120.0],
            [24.0,46.0,67.0,89.0,110.0],
            [22.0,40.0,60.0,75.0,88.0],
            [20.0,35.0,50.0,66.0,84.0]]
    if age == 0:
         weekly_rate = rate[0][days-1]
    if age == 1:
         weekly_rate = rate[1][days-1]
    if age == 2:
         weekly_rate = rate[2][days-1]
    if age == 3:
         weekly_rate = rate[3][days-1]
    if age >= 4:
         weekly_rate = rate[4][days-1]
    print(weekly_rate)
    # Ask the user to enter the next child's age
    age = int(input("Enter the age of the child or 99 to quit: "))


