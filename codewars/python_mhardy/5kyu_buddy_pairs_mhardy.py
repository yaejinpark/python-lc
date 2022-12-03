# You know what divisors of a number are. The divisors of a positive integer n are said to be proper 
# when you consider only the divisors other than n itself. In the following description, divisors 
# will mean proper divisors. For example for 100 they are 1, 2, 4, 5, 10, 20, 25, and 50.

# Let s(n) be the sum of these proper divisors of n. Call buddy two positive integers such that 
# the sum of the proper divisors of each number is one more than the other number:

# (n, m) are a pair of buddy if s(m) = n + 1 and s(n) = m + 1

# For example 48 & 75 is such a pair:

# Divisors of 48 are: 1, 2, 3, 4, 6, 8, 12, 16, 24 --> sum: 76 = 75 + 1
# Divisors of 75 are: 1, 3, 5, 15, 25 --> sum: 49 = 48 + 1
# Task
# Given two positive integers start and limit, the function buddy(start, limit) should return the 
# first pair (n m) of buddy pairs such that n (positive integer) is between start (inclusive) and 
# limit (inclusive); m can be greater than limit and has to be greater than n

# If there is no buddy pair satisfying the conditions, then return "Nothing" or (for Go lang) nil 
# or (for Dart) null; (for Lua, Pascal, Perl, D) [-1, -1]; (for Erlang {-1, -1}).

# Examples
# (depending on the languages)

# buddy(10, 50) returns [48, 75] 
# buddy(48, 50) returns [48, 75]
# or
# buddy(10, 50) returns "(48 75)"
# buddy(48, 50) returns "(48 75)"


def div_sum(n):
    divs = set()
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            divs.add(x)
            divs.add(n // x)
    return sum(divs)

def buddy(start, limit):
    for n in range(start, limit+1):
        buddy = div_sum(n)
        
        if buddy > n and div_sum(buddy) == n:
            return [n, buddy]
    
    return "Nothing"



import codewars_test as test
# from solution import buddy

@test.describe("Buddy Pairs")
def buddy_pairs():
    @test.it("Sample tests")
    def sample_tests():
        test.assert_equals(buddy(10, 50), [48, 75])
        test.assert_equals(buddy(2177, 4357), "Nothing")
        test.assert_equals(buddy(57345, 90061), [62744, 75495])
        test.assert_equals(buddy(1071625, 1103735), [1081184, 1331967])