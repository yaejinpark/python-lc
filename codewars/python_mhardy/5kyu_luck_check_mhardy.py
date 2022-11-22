# In some countries of former Soviet Union there was a belief about lucky tickets. 
# A transport ticket of any sort was believed to posess luck if sum of digits on 
# the left half of its number was equal to the sum of digits on the right half. 
# Here are examples of such numbers:

# 003111    #             3 = 1 + 1 + 1
# 813372    #     8 + 1 + 3 = 3 + 7 + 2
# 17935     #         1 + 7 = 3 + 5  // if the length is odd, you should ignore the middle number when adding the halves.
# 56328116  # 5 + 6 + 3 + 2 = 8 + 1 + 1 + 6
# Such tickets were either eaten after being used or collected for bragging rights.

# Your task is to write a funtion luck_check(str), which returns true/True if argument is 
# string decimal representation of a lucky ticket number, or false/False for all other numbers. 
# It should throw errors for empty strings or strings which don't represent a decimal number.

def luck_check(string):
    digits = list(string)
    divider = len(digits)//2
    sum1 = 0
    sum2 = 0
    middle = 0
    if len(digits)%2 != 0:
        middle += int(digits[divider])
    for i in digits[:divider]:
        sum1 += int(i)
    for i in digits[-divider:]:
        sum2 += int(i)
    if sum1 == sum2:
        return True
    else:
        return False



import codewars_test as test

test.assert_equals(luck_check('683179'),True, "The function doesn't recognise a lucky ticket number")
test.assert_equals(luck_check('683000'),False, 'The function doesn\'t return true for a wrong number')
test.it("should raise an error for string with illegal characters")
test.expect_error("It should give an error for invalid input",lambda: luck_check('6F43E8'))