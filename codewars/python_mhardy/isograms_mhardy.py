# An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
# Implement a function that determines whether a string that contains only letters is 
# an isogram. Assume the empty string is an isogram. Ignore letter case.


def is_isogram(string):
    char_list = []
    for i in string:
        if i.lower() in char_list:
            return False
        else:
            char_list.append(i.lower())
            continue
    return True

# Jin's optimized one liner


import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():      
        test.assert_equals(is_isogram("Dermatoglyphics"), True )
        test.assert_equals(is_isogram("isogram"), True )
        test.assert_equals(is_isogram("aba"), False, "same chars may not be adjacent" )
        test.assert_equals(is_isogram("moOse"), False, "same chars may not be same case" )
        test.assert_equals(is_isogram("isIsogram"), False )
        test.assert_equals(is_isogram(""), True, "an empty string is a valid isogram" )