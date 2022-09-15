# In this kata you should simply determine, whether a given year is a leap year or not. 
# In case you don't know the rules, here they are:

# years divisible by 4 are leap years
# but years divisible by 100 are not leap years
# but years divisible by 400 are leap years

def isLeapYear(year):
    if (int(year) % 4 == 0) and (int(year) % 100 != 0) or (int(year) % 400 == 0):
        return True
    elif (int(year) % 100 == 0) and (int(year) % 400 != 0):
        return False
    else:
        return False


# Jin's optimized 1 liner
# def isLeapYear(year):
    # return year % != 0 and year % 4 == 0 or year % 400 == 0

# clever lambda solution:
# isLeapYear = lambda y: (not y%4) * bool(y%100+(not y%400))

import codewars_test as test

test.describe('Leap years (should equal True)')
test.assert_equals(isLeapYear(1984), True, 'Year 1984 was a leap year!')
test.assert_equals(isLeapYear(2000), True, 'Year 2000 was a leap year!')

test.describe('Normal years (should equal False)')
test.assert_equals(isLeapYear(1234), False, 'Year 1234 was NOT a leap year!')
test.assert_equals(isLeapYear(1100), False, 'Year 1100 was NOT a leap year!')