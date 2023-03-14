"""Design an application that accepts 15 words and displays them in alphabetical order."""

word_list = []

while len(word_list) < 15:
    userdata = input("Please enter a word: ")
    if userdata.isalpha():
        word_list.append(userdata)
    else:
        print("Error: Invalid character.")

word_list.sort()

print(word_list)