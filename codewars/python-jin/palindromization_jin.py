# https://www.codewars.com/kata/5840107b6fcbf56d2000010b/train/python
def palindromization(element,n):

    # if element string is empty or n is smaller than 2, return Error
    if len(element) == 0 or n < 2:
        return "Error!"

    palindrome_string = ""
    center = n//2 # center index of the completed palindrome string

    i = 0
    for j in range(center):
        if i == len(element): # i is for index of elements. j is not used because of index out or range error.
            i = j - i
        palindrome_string += element[i]
        i += 1
    
    if n % 2 == 0:
        return palindrome_string + palindrome_string[::-1] # if n is even, just return the first half of the palindrome and its reverse concat
    else:
        return palindrome_string + element[center-len(element)] +palindrome_string[::-1] # if n is odd, concat first half of palindrome, center value, and the reverse concat

print(palindromization("123",2)) #"11"
print(palindromization("123",3)) #"121"
print(palindromization("123",4)) #"1221"
print(palindromization("123",5)) #"12321"
print(palindromization("123",6)) #"123321"
print(palindromization("123",7)) #"1231321"
print(palindromization("123",8)) #"12311321"
print(palindromization("123",9)) #"123121321"
print(palindromization("123",10)) #"1231221321"