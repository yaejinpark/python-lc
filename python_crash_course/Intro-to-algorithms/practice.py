
# First define the list I want to sort


def merge_sort(arr):

   

# Consider if it is an emply list or a list with one value 

    if len(arr) <= 1:

            return arr 

    # Divide the list into two; right side and left side 

    mid = len(arr) // 2 

    right = merge_sort(arr[mid:])
    left = merge_sort(arr[:mid])


    return merge(right, left)


# Second start sorting the algorithm 

def merge(right, left):


# Make an emply list and run tickers to go through the left and right portion of the list

    output = []

    r = 0 
    l = 0 

# See if the index value of the right side is greater than the left side

    while r < len(right) and l < len(left): 
        if right[r] < left[l]:

            output.append(right[r])

            r += 1 
        else: 
            output.append(left[l])

            l += 1 

    output.extend(right[r:])
    output.extend(left[l:])

    return output

def run_merge_sort():

    unsorted_list = [4, 1, 5, 7, 2, 6, 1, 1, 6, 4, 10, 33, 5, 7, 23]
    print(unsorted_list)

    sorted_list = merge_sort(unsorted_list)
    print(sorted_list)


run_merge_sort()







# 