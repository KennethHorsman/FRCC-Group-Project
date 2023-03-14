"""Design an application that accepts 10 numbers and displays them in descending order."""

data_list = []

while len(data_list) < 10:
    userdata = input("Please enter a number: ")
    if userdata.isnumeric():
        num = int(userdata)
        data_list.append(num)
    else:
        print("Error: Invalid character.")

data_list.sort(reverse=True)

print(data_list)