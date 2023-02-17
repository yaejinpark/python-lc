# The Hamming Distance is a measure of similarity between two strings of equal length. 
# Complete the function so that it returns the number of positions where the input strings do not match.

# Examples:
# a = "I like turtles"
# b = "I like turkeys"
# Result: 3

# a = "Hello World"
# b = "Hello World"
# Result: 0

# a = "espresso"
# b = "Expresso"
# Result: 2
# You can assume that the two inputs are ASCII strings of equal length.


def hamming(a,b):
    counter = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            counter += 1

    return counter







import codewars_test as test
# from solution import hamming

@test.describe("Sample tests")
def sample_tests():
    
    @test.it("Sample tests")
    def sample_tests():
        test.assert_equals(hamming("hello world","hello tokyo"),4)
        test.assert_equals(hamming("a man a plan a canal","a man a plan sobanal"),3)
        test.assert_equals(hamming("hamming and cheese","Hamming and Cheese"),2)
        test.assert_equals(hamming("espresso","Expresso"),2)
        test.assert_equals(hamming("old father, old artificer","of my soul the uncreated "),24);