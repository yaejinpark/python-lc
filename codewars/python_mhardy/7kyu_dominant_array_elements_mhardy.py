# An element in an array is dominant if it is greater than all 
# elements to its right. You will be given an array and 
# your task will be to return a list of all dominant elements. For example:

# solve([1,21,4,7,5]) = [21,7,5] because 21, 7 and 5 are 
# greater than elments to their right. 
# solve([5,4,3,2,1]) = [5,4,3,2,1]

# Notice that the last element is always included. 
# All numbers will be greater than 0.



def solve(arr):
    res = []
    for i in range(len(arr)-1):
        temp = arr[i:]
        if temp[0] == max(temp) and temp[0] not in res:
            res.append(temp[0])
    if arr[-1] not in res:
        res.append(arr[-1])        
    return res


import codewars_test as test
# from solution import solve

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(solve([16,17,14,3,14,5,2]),[ 17,14,5,2])
        test.assert_equals(solve([ 92,52,93,31,89,87,77,105]),[105])
        test.assert_equals(solve([ 75,47,42,56,13,55]), [75,56,55])
        test.assert_equals(solve([ 67,54,27,85,66,88,31,24,49]),[88,49])
        test.assert_equals(solve([ 76,17,25,36,29]),[76,36,29])
        test.assert_equals(solve([ 104,18,37,9,36,47,28]),[104,47,28])