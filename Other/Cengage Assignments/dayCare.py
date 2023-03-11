QUIT = 99

rate = [[30.0,60.0,88.0,115.0,140.0],
        [26.0,52.0,70.0,96.0,120.0],
        [24.0,46.0,67.0,89.0,110.0],
        [22.0,40.0,60.0,75.0,88.0],
        [20.0,35.0,50.0,66.0,84.0]]

while True:
    age = input("Enter the age of the child or 99 to quit: ")
    if age == "99":
        break
    age = int(age)
    if age < 0 or age > 4:
        print("Invalid age. Please enter an age between 0 and 4.")
        continue
    days = int(input("Enter number of days per week: "))
    weekly_rate = rate[age][days-1]
    print(weekly_rate)

