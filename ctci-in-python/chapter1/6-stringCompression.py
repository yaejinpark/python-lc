#Count the repeated characters and compress them
#Example: aabcccccaaa -> a2b1c5a3

def compress(string):
    if len(string) == 0:
        return string

    #Starts at 1 because I still have to "compress" a single char as 1
    repeatCounter = 1
    i = 1
    compressed = []

    while i < len(string):
        #If the current value is the same as the previous value, add to the repeat counter
        if string[i-1] == string[i]:
            repeatCounter += 1
        #If repetition is over, append the final repeat counter and the letter to the compressed array
        else:
            compressed.append(string[i-1]+str(repeatCounter))
            repeatCounter = 1

        #For the very last element to count as a repeat if it is a repeated value
        if i == len(string) - 1:
            if string[i] == string[i-1]:
                compressed.append(string[i-1]+str(repeatCounter))
        i += 1

    #Join all of the compressed array's element into a single string
    newString = "".join(compressed)
    return newString

print(compress("aabcccccaaa")) #Should print a2b1c5a3

#TL;DR
#If I do "".join(list), all of the list's elements will be joined in a single string with whatever is in "".
#If it was " " instead of "", the result would be a2 b1 c5 a3 instead of a2b1c5a3