evil = [i for i in range(10**100) if str(bin(i)).split('b')[1].count('1')%2==0]
def get_evil(n):
    print(n)
    return evil[n-1]

import codewars_test as test

sample_test_cases = [
#     n  expected  
    ( 1,   0),
    ( 2,   3),
    ( 3,   5),
    (10,  18),
    (11,  20),
]

@test.describe('Sample tests')
def sample_tests():
    for n, expected in sample_test_cases:
        @test.it(f'get_evil({n})')
        def _():
            test.assert_equals(get_evil(n), expected)