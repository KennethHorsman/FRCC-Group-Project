"""
EmployeeBonus.py - This program calculates an employee's productivity bonus.
"""

BONUS_1 = 50.00
BONUS_2 = 75.00
BONUS_3 = 100.00
BONUS_4 = 200.00

employeeName = input("Enter employee's name: ")
shiftString = input("Enter number of shifts: ")
transactString = input("Enter number of transactions: ")
dollarString = input("Enter transactions dollar value: ")

numShifts = float(shiftString)
numTransactions = float(transactString)
dollarValue = float(dollarString)

productivity = (dollarValue / numTransactions) / numShifts
if productivity >= 0:
    bonus = BONUS_1
    if productivity >= 31:
        bonus = BONUS_2
        if productivity >= 70:
            bonus = BONUS_3
            if productivity >= 200:
                bonus = BONUS_4
else:
    bonus = "0.00  No soup for you!"


print("Employee Name: " + employeeName)
print("Employee Bonus: $" + str(bonus))
print("Productivity: " + str(productivity))
"""
if productivity <= 30:
    bonus = BONUS_1
elif 30 < productivity <= 69:
    bonus = BONUS_2
elif 69 < productivity <= 199:
    bonus = BONUS_3
elif productivity >= 200:
    bonus = BONUS_4
"""