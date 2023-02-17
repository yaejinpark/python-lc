# I want to count from 1 to n. How many times will I use a '9'?

# 9, 19, 91.. will contribute one '9' each, 99, 199, 919.. wil contribute two '9's each...etc

# Note: n will always be a positive integer.

# Examples (input -> output)
# 8  -> 0
# 9  -> 1
# 10 -> 1
# 98 -> 18
# 100 -> 20

# BRUTE FORCE METHOD

def count_nines(n):
    counter = 0
    for i in range(1, n+1):
        counter += (list(str(i))).count('9')
    return counter


# def count_nines(n):

#     return (n//10+((n//100)*10)) + (n%10)//9



import codewars_test as test

@test.describe("Sample tests")
def test_group():
    @test.it("Fixed tests")
    def test_case():
        test.assert_equals(count_nines(1), 0)
        test.assert_equals(count_nines(9), 1)
        test.assert_equals(count_nines(100), 20)
        test.assert_equals(count_nines(200), 40)
        test.assert_equals(count_nines(201), 40)
        test.assert_equals(count_nines(278), 47)
        test.assert_equals(count_nines(279), 48)
        test.assert_equals(count_nines(280), 48)
        test.assert_equals(count_nines(908), 189)
        test.assert_equals(count_nines(909), 191)
        test.assert_equals(count_nines(99999), 50000)
        test.assert_equals(count_nines(565754), 275645)
