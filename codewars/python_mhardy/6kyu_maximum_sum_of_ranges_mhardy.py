# Description:
# For example:

#  Given arr = [1,-2,3,4,-5,-4,3,2,1], 
#        range = [[1,3],[0,4],[6,8]]
#  should return 6
 
#  calculation process:
#  range[1,3] = arr[1]+arr[2]+arr[3] = 5
#  range[0,4] = arr[0]+arr[1]+arr[2]+arr[3]+arr[4] = 1
#  range[6,8] = arr[6]+arr[7]+arr[8] = 6
#  So the maximum sum value is 6
# Note:
# arr/$a always has at least 5 elements;
# range/$range/ranges always has at least 1 element;
# All inputs are valid;


def max_sum(arr,ranges): 
    totals = []
    for i in range(len(ranges)):
        totals.append(sum(arr[(ranges[i][0]):(ranges[i][1]+1)]))
    return max(totals)


import codewars_test as test

test.it("Basic test")
test.assert_equals(max_sum([1,-2,3,4,-5,-4,3,2,1], [[1,3],[0,4],[6,8]]), 6)
test.assert_equals(max_sum([1,-2,3,4,-5,-4,3,2,1], [[1,3]]), 5)
test.assert_equals(max_sum([1,-2,3,4,-5,-4,3,2,1], [[1,4],[2,5]]), 0)
test.assert_equals(max_sum([11,-22,31,34,-45,-46,35,32,21], [[1,4],[0,3],[6,8],[0,8]]), 88)