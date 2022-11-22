# In this example you have to validate if a user input string is alphanumeric. 
# The given string is not nil/null/NULL/None, so you don't have to check that.

# The string has the following conditions to be alphanumeric:

# At least one character ("" is not valid)
# Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
# No whitespaces / underscore

import re

def alphanumeric(password):
    bad_chars =  re.compile(r"[\W_]")
    if password:
        if bad_chars.search(password):
            return False
        else:
            return True
    else:
        return False


# BEST PRACTICES FROM CODEWARS:

# def alphanumeric(string):
#     return string.isalnum()



import codewars_test as test

@test.describe("Sample Tests")
def sample_tests():
    tests = [
        ("hello world_", False),
        ("PassW0rd", True),
        ("     ", False)
    ]
    for s, b in tests:
        @test.it('alphanumeric("' + s + '")')
        def sample_test():
            test.assert_equals(alphanumeric(s), b)