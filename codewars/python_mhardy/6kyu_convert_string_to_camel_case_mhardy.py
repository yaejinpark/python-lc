# Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized only if the original word was capitalized 
# (known as Upper Camel Case, also often referred to as Pascal case).

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

import re

def to_camel_case(text):
    if text:
        split_string = re.split('-|_', text)
        new_string_list = [split_string[0]]
        cap_list = [word.capitalize() for word in split_string[1:]]
        for x in cap_list:
            new_string_list.append(x)
        new_string = "".join(new_string_list)
        return new_string
    else:
        return ""




import codewars_test as test


@test.describe("Sample Tests")
def sample_tests():
    @test.it("Tests")
    def _():
        test.assert_equals(to_camel_case(""), "", "An empty string was provided but not returned")
        test.assert_equals(to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
        test.assert_equals(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
        test.assert_equals(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")