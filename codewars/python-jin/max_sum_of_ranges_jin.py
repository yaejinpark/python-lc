# https://www.codewars.com/kata/583d10c03f02f41462000137/train/python
def max_sum(arr,ranges): 
    sums = []
    for range_val in ranges:
        current_sum = 0
        for i in range(range_val[0],range_val[1]+1):
            current_sum += arr[i]
        sums.append(current_sum)
    return max(sums)

# cleaned up code
def max_sum(arr,ranges): 
    sums = [sum(arr[range[0]:range[1]+1]) for range in ranges]
    return max(sums)