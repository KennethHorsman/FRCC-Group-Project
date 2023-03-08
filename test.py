data_list = []
STOP = False

while STOP is False:
    userdata = input("Please enter a word or \"stop\" to quit: ")
    if userdata == "stop":
        STOP = True
    elif userdata.isalpha():
        data_list.append(userdata)
data_list.sort()
print(data_list)
