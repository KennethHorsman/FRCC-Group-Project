largest = None
smallest = None

number1 = input("number 1: ")
number2 = input("number 2: ")
number3 = input("number 3: ")

numberList = []

if number1 != "":
    numberList.append(number1)
else:
    number1 = input("number 1: ")
if number1 != "":
    numberList.append(number2)
else:
    number1 = input("number 2: ")    
if number1 != "":
    numberList.append(number3)
else:
    number1 = input("number 3: ")

largest = max(numberList)
smallest = min(numberList)

print("The largest value is " + str(largest))
print("The smallest value is " + str(smallest))