# construct randomized array of length 'size';
# each element is randomly selected from the range 0 up to 100 
def create_array(size = 10, max = 100):
    from random import randint

    return [randint(0, max) for _ in range(size)]


def merge(right, left): 

    result = []

    r, l = 0, 0

    while r < len(right) and l < len(left):
        if right[r] < left[l]:
            result.append(right[r])
            r += 1
        else:
            result.append(left[l])
            l += 1

    if r == len(right):
        result.extend(left[l:])
    
    else:
        result.extend(right[r:])

    return result

def merge_sort(arr):

    if len(arr) <= 1: 
        return arr 

    mid = len(arr) // 2 

    right = merge_sort(arr[mid:])
    left = merge_sort(arr[:mid])

    return merge(right, left)

def output():

    arr = create_array()
    print(f"Unsorted List: {arr}")

    sort_list = merge_sort(arr)

    print(f"Sorted List: {sort_list}")


output()



    

