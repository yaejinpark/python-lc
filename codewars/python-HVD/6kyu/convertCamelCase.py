def to_camel_case(text):
    # return ''.join(c if c.isalpha() else c for c in s)
    x=0
    for char in text:
        if char.isalpha():            
            x+=1
        else:
            text=text[:x] + text[x+1:].capitalize()   
    return text

import codewars_test as test

@test.describe("Sample Tests")
def sample_tests():
    @test.it("Tests")
    def _():
        test.assert_equals(to_camel_case(""), "", "An empty string was provided but not returned")
        test.assert_equals(to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
        test.assert_equals(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
        test.assert_equals(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")