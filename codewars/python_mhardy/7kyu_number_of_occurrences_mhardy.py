# Write a function that returns the number of occurrences of an element in an array.

# Examples
# sample = [0, 1, 2, 2, 3]
# number_of_occurrences(0, sample) == 1
# number_of_occurrences(4, sample) == 0
# number_of_occurrences(2, sample) == 2
# number_of_occurrences(3, sample) == 1



def number_of_occurrences(element, sample):
    return sample.count(element)


import codewars_test as test

@test.describe("Example tests")
def test_group():
    sample = [0, 1, 2, 2, 3]
    @test.it("Elements that not in list")
    def test_not_in_list():
        test.assert_equals(number_of_occurrences(4, sample), 0)
        test.assert_equals(number_of_occurrences(6, sample), 0)
        test.assert_equals(number_of_occurrences(-1, sample), 0)
    @test.it("Elements that's occur on list one or more times")
    def test_cases():
        test.assert_equals(number_of_occurrences(0, sample), 1)
        test.assert_equals(number_of_occurrences(2, sample), 2)
        test.assert_equals(number_of_occurrences(3, sample), 1)