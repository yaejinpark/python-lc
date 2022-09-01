# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.



def find_it(seq):
    num_dict = {}
    for i in seq:
        if i not in num_dict:
            num_dict[i] = 1
        else:
            num_dict[i] += 1

    for i, j in num_dict.items():
        if j % 2 == 1:
            return i
            



import codewars_test as test

@test.describe("Sample tests")
def sample_tests():
    
    @test.it("find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) should return 5 (because it appears 3 times)")
    def _():
        test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
        
    @test.it("find_it([1,1,2,-2,5,2,4,4,-1,-2,5]) should return -1 (because it appears 1 time)")
    def _():
        test.assert_equals(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1);
        
    @test.it("find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]) should return 5 (because it appears 3 times)")
    def _():
        test.assert_equals(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5);
        
    @test.it("find_it([10]) should return 10 (because it appears 1 time)")
    def _():
        test.assert_equals(find_it([10]), 10);