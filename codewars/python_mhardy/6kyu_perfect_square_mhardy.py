# Task
# Write function which validates an input string. If the string is a perfect square return true,false otherwise.

# What is perfect square?
# * We assume that character '.' (dot) is a perfect square (1x1) * Perfect squares can only contain '.' (dot) and optionally '\n' (line feed) characters.
# * Perfect squares must have same width and height -> cpt.Obvious
# * Squares of random sizes will be tested!
# Function input:
# perfectSquare = "...\n...\n...";    

# // This represents the following Perfect Square:

# `...
#  ...
#  ...`
                               
# notPerfect = "..,\n..\n...";

# // This is not a Perfect Square:

# `..,
#  ..
#  ...`

def perfect_square(square):
    sqr_list = square.split('\n')
    for i in sqr_list:
        if len(i) == len(sqr_list):
            for y in i:
                if y != '.':
                    return False
        else:
            return False
    return True

# JIN'S MORE EFFICIENT ONE-LINER
# def perfect_square(square):
#     parsed = square.split('\n')
#     return all('.'*len(parsed) == i for i in parsed)
    
import codewars_test as test
# from solution import perfect_square

sample_test_cases = [
    ('Perfect squares', [
        ('.', True),
        ('..\n..', True),
        ('...\n...\n...', True),
    ]),
    ('Imperfect squares', [
        ('+', False),
        ('...\n.:.\n...', False),
        ('---\n---\n---', False),
    ]),
    ('Other shapes', [
        ('..', False),
        ('.\n.\n.', False),
        ('...\n....\n...', False),
        ('...\n..\n...', False),
    ]),
]

@test.describe('Sample tests')
def sample_tests():
    for name, test_cases in sample_test_cases:
        @test.it(name)
        def tests():
            for square, expected in test_cases:
                test.assert_equals(perfect_square(square), expected, f'perfect_square({square!r})')