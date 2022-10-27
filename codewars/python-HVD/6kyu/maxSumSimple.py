def max_sum(arr,ranges): 
    y=0
    for range in ranges:
        x=0
        i= range[0]
        while i <= range[1]:
            x += arr[i]
            i += 1
            
        if y < x: 
            y=x
            
    return y



# arr=[1,-2,3,4,-5,-4,3,2,1]
# ranges=[[1,4],[2,5]]

# max_sum(arr,ranges)

import codewars_test as test


test.it("Basic test")
test.assert_equals(max_sum([1,-2,3,4,-5,-4,3,2,1], [[1,3],[0,4],[6,8]]), 6)
test.assert_equals(max_sum([1,-2,3,4,-5,-4,3,2,1], [[1,3]]), 5)
test.assert_equals(max_sum([1,-2,3,4,-5,-4,3,2,1], [[1,4],[2,5]]), 0)
test.assert_equals(max_sum([11,-22,31,34,-45,-46,35,32,21], [[1,4],[0,3],[6,8],[0,8]]), 88)