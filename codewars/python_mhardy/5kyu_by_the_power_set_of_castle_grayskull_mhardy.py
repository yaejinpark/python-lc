# Write a function that returns all of the sublists of a list/array.

# Example:

# power([1,2,3]);=>[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

from itertools import combinations

def power(a):
    comb = []
    for i in range(len(a)+1):
        comb += [list(j) for j in combinations(a, i)]

    return comb


import codewars_test as test
# from solution import power

def normalize(s):
	return sorted(sorted(x) for x in s)

@test.describe("Sample tests")
def _():
    @test.it("Tests")
    def __():
        test.assert_equals(normalize(power([1, 2, 3])),
                           normalize([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]))