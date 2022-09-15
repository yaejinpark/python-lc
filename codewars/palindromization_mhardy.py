def reverse(num):
    return str(num)[::-1]

def palindromization(element, n):
    if len(element) == 0 or n < 2:
        return "Error!"
    palindrome_string = ""
    center = n//2
    i = 0
    for j in range(center):
        if i == len(element):
            i = j - i
        palindrome_string += element[i]
        i += 1

    if n % 2 == 0:
        return palindrome_string + palindrome_string[::-1]
    else:
        return palindrome_string + element[center-len(element)] + palindrome_string[::-1]


import codewars_test as test

test.describe("Examples")

# Use "it" to identify the conditions you are testing for
test.it("Description examples")
# using assert_equals will report the invalid values to the user
test.assert_equals(palindromization("123",2), "11");
test.assert_equals(palindromization("123",3), "121");
test.assert_equals(palindromization("123",4), "1221");
test.assert_equals(palindromization("123",5), "12321");
test.assert_equals(palindromization("123",6), "123321");
test.assert_equals(palindromization("123",7), "1231321");
test.assert_equals(palindromization("123",8), "12311321");
test.assert_equals(palindromization("123",9), "123121321");
test.assert_equals(palindromization("123",10), "1231221321");

test.it("Description error")

test.assert_equals(palindromization("", 2), "Error!");
test.assert_equals(palindromization("123", 1), "Error!");
