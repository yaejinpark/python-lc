# There are no explanations. You have to create the code that 
# gives the following results in Python, Ruby, and Haskell:

# one_two_three(0) == [0, 0]
# one_two_three(1) == [1, 1]
# one_two_three(2) == [2, 11]
# one_two_three(3) == [3, 111]
# one_two_three(19) == [991, 1111111111111111111]


def one_two_three(n):
    if not n:
        return [0, 0]
    if len(str(n)) == 1:
        first_str = n
    elif n > 9:
        first_str = ""
        first_str += "9" * (n//9)
        if n % 9 != 0:
            first_str += str(n%9)
    second_str = ""
    second_str += "1" * int(n)
    return [int(first_str) if first_str else 0, int(second_str)]



import codewars_test as test

test.describe("Example Tests")
test.assert_equals(one_two_three(0), [0, 0])
test.assert_equals(one_two_three(1), [1, 1])
test.assert_equals(one_two_three(2), [2, 11])
test.assert_equals(one_two_three(3), [3, 111])
test.assert_equals(one_two_three(19), [991, 1111111111111111111])
test.assert_equals(one_two_three(220), [9999999999999999999999994, 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111])