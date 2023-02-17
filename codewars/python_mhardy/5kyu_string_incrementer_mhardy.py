# Your job is to write a function which increments a string, to create a new string.

# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:

# foo -> foo1

# foobar23 -> foobar24

# foo0042 -> foo0043

# foo9 -> foo10

# foo099 -> foo100

# Attention: If the number has leading zeros the amount of digits should be considered.

# import re
# def increment_string(strng):
#     pattern = r"([a-zA-Z]*)(\d*)([a-zA-Z]*)(\d*)"
#     if not strng:
#         return "1"
#     else:
#         result = re.search(pattern, strng)
        
#         if result.group(len(result.groups())).isnumeric():
#             num = int(result.group(len(result.groups()))) + 1
#         else:
#             num = 1
#     return result.group(1) + str(num).zfill(len(result.group(len(result.groups()))))

#Henry beat me this time
def increment_string(s):
    head = s.rstrip('0123456789')
    tail = s[len(head):]
    if len(tail)==0:newtail ="1"
    else:newtail=str(int(tail)+1).zfill(len(tail))
    return(head+newtail)



import codewars_test as test
# from solution import increment_string

@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(increment_string("foo"), "foo1")
        test.assert_equals(increment_string("foobar001"), "foobar002")
        test.assert_equals(increment_string("foobar1"), "foobar2")
        test.assert_equals(increment_string("foobar00"), "foobar01")
        test.assert_equals(increment_string("foobar99"), "foobar100")
        test.assert_equals(increment_string("foobar099"), "foobar100")
        test.assert_equals(increment_string("fo99obar99"), "fo99obar100")
        test.assert_equals(increment_string(""), "1")