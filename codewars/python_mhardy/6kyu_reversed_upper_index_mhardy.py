# In this Golfing Kata, you are going to do simple things:

# Reverse a string; then

# Return the index of first uppercase letter.

# Input:
# You are going to get a string which consists only uppercase and lowercase English letters. It will have at least one uppercase letter.

# Output:
# Return the index of first uppercase letter of reversed string.

# Examples:
# input --> output

# f("HelloWorld") --> 4
# f("Codewars")  --> 7
# f("X") --> 0
# f("findX") --> 0
# Golfing Message:
# The length of your code should be less or equals to 44.

# Your code should be one line.

# The length of the reference solution is 37.

def f(s):
    return [i for i, c in enumerate(s[::-1]) if c.isupper()][0]

# Jin's working lambda function, that fits within the character limit
# f=lambda s:[c<"a"for c in s][::-1].index(1)


# from solution import f
import codewars_test as test

@test.describe("Sample Tests")
def tests():

    
    # with open("/workspace/solution.txt", "r") as file:
    #     sol_code = file.read()
    #     @test.it(f"Test for your code itself: Length is {len(sol_code)}")
    #     def tests():
    #         test.expect(len(sol_code) <= 44, f"{len(sol_code)} should be less or equal to 44.")
    #         test.expect("\n" not in sol_code, "Your code should be one line.")
    
    
    
    @test.it("Basic Tests")
    def tests():
        test.assert_equals(f("HelloWorld"), 4)
        test.assert_equals(f("Codewars"), 7)
        test.assert_equals(f("X"), 0)
        test.assert_equals(f("findX"), 0)