# Count the vowels in a string
# Create a function in Python that accepts a single word and returns the number of vowels in that word. In this function, only a, e, i, o, and u will be counted as vowels — not y.
# Then create your own test case words and see if it’s counting the correct amount of vowels from your test cases

def vowelCounter(word):
    count = 0
    for vowels in word:
        if (vowels in "aeiouAEIOU"):
            count += 1

    print("There are " + str(count) + " vowels in the word " + "\"" + word + ".\"")

vowelCounter("Australia")