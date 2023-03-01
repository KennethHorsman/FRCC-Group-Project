# SuperMarket.py - This program creates a report that lists weekly hours worked 
# by employees of a supermarket. The report lists total hours for 
# each day of one week. 
# Input:  Interactive
# Output: Report. 

# Declare variables.
HEAD1 = "WEEKLY HOURS WORKED"
DAY_FOOTER = "Day Total "
SENTINEL = "done"   # Named constant for sentinel value
hoursWorked = 0     # Current record hours
hoursTotal = 0      # Hours total for a day
prevDay = ""        # Previous day of week
notDone = True      # loop control

# Print two blank lines.
print("\n\n")
# Print heading.
print("\t" + HEAD1)
# Print two blank lines.
print("\n\n")

# Read first record 
dayOfWeek = input("Enter day of week or done to quit: ")
if dayOfWeek  == SENTINEL:
    notDone = False
else:
    hoursWorked = input("Enter hours worked: ")
    prevDay = dayOfWeek
    hoursTotal += int(hoursWorked) 
    print("\t" + DAY_FOOTER + str(hoursTotal))

while notDone == True:
    dayOfWeek = input("Enter day of week or done to quit: ")
    if dayOfWeek  == SENTINEL:
        break
    # Implement control break logic here
    if prevDay != dayOfWeek:
        hoursTotal = 0 
    # Include work done in the dayChange() function
    hoursWorked = input("Enter hours worked: ")
    prevDay = dayOfWeek
    hoursTotal += int(hoursWorked) 
    print("\t" + DAY_FOOTER + str(hoursTotal))
