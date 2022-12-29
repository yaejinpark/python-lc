# Create a function that takes a string as a parameter and does the following, in this order:

# Replaces every letter with the letter following it in the alphabet (see note below)
# Makes any vowels capital
# Makes any consonants lower case
# Note:

# the alphabet should wrap around, so Z becomes A
# in this kata, y isn't considered as a vowel.
# So, for example the string "Cat30" would return "dbU30" (Cat30 --> Dbu30 --> dbU30)


def changer(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output_str = ''
    for i in list(s.lower()):
        if i.isalpha():
            if i == 'z':
                output_str += 'A'
            elif chr(ord(i)+1) in vowels:
                output_str += chr(ord(i)+1).upper()
            else:
                output_str += chr(ord(i)+1)
        elif i.isnumeric() or ord(i) == 32:
                output_str += i
    return output_str


# from solution import changer
import codewars_test as test

@test.describe('Changer tests...')
def _():

    @test.it("Basic tests")
    def _():
        test.assert_equals(changer('Cat30'), 'dbU30')
        test.assert_equals(changer('Alice'), 'bmjdf')
        test.assert_equals(changer('sponge1'), 'tqpOhf1')
        test.assert_equals(changer('Hello World'), 'Ifmmp xpsmE')
        test.assert_equals(changer('dogs'), 'Epht')
        test.assert_equals(changer('z'), 'A')