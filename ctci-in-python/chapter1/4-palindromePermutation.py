#If a string is a palindrome there are two cases
#1. String length is odd: only one letter can have an odd number of frequency
#2. String length is even: All letters should appear twice or some even number

def palindrome(input):
    dict = {}
    #Get rid of blank spaces or they will be included in the dictionary
    newInput = input.replace(' ','')

    #Include all characters and their frequencies in a dictionary
    for i in range(0,len(newInput)):
        if newInput[i] not in dict:
            dict[newInput[i]] = 1
        else:
            dict[newInput[i]] += 1
    # print(dict)

    #If the string's length is even, check that no letters' frequencies are odd
    #If odd, then not a palindrome
    if len(newInput) % 2 == 0:
        for letters in dict:
            if dict.get(letters) % 2 != 0:
                print("Even String: Not a palindrome")
                return False
        return True

    #If the string's length is odd, check that no more than one letter's frequencies are odd
    #If not, then not a palindrome
    elif len(newInput) % 2 == 1:
        oddCounter = 0
        for letters in dict:
            if dict.get(letters) % 2 != 0:
                oddCounter += 1
        if oddCounter > 1:
            print("Odd String: Not a palindrome")
            return False
        return True

palindrome1 = "taco cat"
palindrome2 = "anna"
palindrome3 = "obviously this is not a palindrome"


print(palindrome(palindrome1)) #True
print(palindrome(palindrome2)) #True
print(palindrome(palindrome3)) #Should print a message and say False

#TL;DR
#It will be useful in the future to memorize the definition of a palindrome
#This is indicated on the top of this script