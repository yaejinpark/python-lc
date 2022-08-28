"""
Write a program that takes an array A and an index i rnto A, 
and rearranges the elements such that all elements less than A[r] (the "pivot") appear first, 
followed by elements equal to the pivot, followed by elements greater than the pivot.
"""

def dutch_flag(arr,pivot):
    left_arr, right_arr = [],[]

    # Append all elements smaller than pivot to left_arr, bigger to right_arr
    for elem in arr:
        if arr[pivot] >= elem:
            left_arr.append(elem)
        else:
            right_arr.append(elem)
    print(left_arr,right_arr)
    # Extend doesn't work since None is returned
    # The book mentioned using recursion... might look into it
    return left_arr + right_arr

test1 = [0,1,2,0,2,1,1]
test1_pivot = 3

print(dutch_flag(test1,test1_pivot))