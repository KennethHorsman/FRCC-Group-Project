# Write a function that determines if a word is spelled the same backwards
# as it is forwards. An example of a palindrome: Kayak, because it is spelled the same forwards and backwards. 
# Google a list of palindrome words and sentences to use as test cases.

# In the example above, Kayak was used. Uppercase K and lowercase k are not read the same. 
# Your program should capture characters and either make them all uppercase or all lowercase 
# in order to account for this. 


def isPalindrome(str):
    newString = lowerCaseConverter(str)
    reverseString = ""
    
    for x in reversed(newString):
        reverseString += x
        
    if reverseString == newString:
        return print(str + " is a palindrome.")
    else: return print(str + " is NOT a palindrome")
    
def lowerCaseConverter(str1):
    str2 = ""
    for x in str1:
        str2 += x.lower()
    
    return str2
    
isPalindrome("Kayak")
isPalindrome("Car")
isPalindrome("Racecar")
isPalindrome("Tacos")
isPalindrome("TacoCat")