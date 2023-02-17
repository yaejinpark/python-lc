# https://www.codewars.com/kata/52a78825cdfc2cfc87000005/train/python


# Given a mathematical expression as a string you must return the result as a number.

# Numbers
# Number may be both whole numbers and/or decimal numbers. The same goes for the returned result.

# Operators
# You need to support the following mathematical operators:

# Multiplication *
# Division / (as floating point division)
# Addition +
# Subtraction -
# Operators are always evaluated from left-to-right, and * and / must be evaluated before + and -.

# Parentheses
# You need to support multiple levels of nested parentheses, ex. (2 / (2 + 3.33) * 4) - -6

# Whitespace
# There may or may not be whitespace between numbers and operators.

# An addition to this rule is that the minus sign (-) used for negating numbers 
# and parentheses will never be separated by whitespace. I.e all of the following are valid expressions.

# 1-1    // 0
# 1 -1   // 0
# 1- 1   // 0
# 1 - 1  // 0
# 1- -1  // 2
# 1 - -1 // 2
# 1--1   // 2

# 6 + -(4)   // 2
# 6 + -( -4) // 10
# And the following are invalid expressions

# 1 - - 1    // Invalid
# 1- - 1     // Invalid
# 6 + - (4)  // Invalid
# 6 + -(- 4) // Invalid
# Validation
# You do not need to worry about validation - you will only receive valid 
# mathematical expressions following the above rules.

# Restricted APIs
# NOTE: eval and exec are disallowed in your solution.

def calc(expression):
    return # evaluated expression






import codewars_test as test

@test.describe("Sample tests")
def _():
    @test.it("Tests")
    def __():
        cases = (
            ("1 + 1", 2),
            ("8/16", 0.5),
            ("3 -(-1)", 4),
            ("2 + -2", 0),
            ("10- 2- -5", 13),
            ("(((10)))", 10),
            ("3 * 5", 15),
            ("-7 * -(6 / 3)", 14)
        )

        for x, y in cases:
            test.assert_equals(calc(x), y)