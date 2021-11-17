def create_arr(size = 11, max = 100): 
    from random import randint
    return [randint(0, max) for _ in range(size)]

def merge_sort(right, left): 

    output = []

    r, l = 0, 0 

    while r < len(right) and l < len(left): 
        if right[r] < left[l]:
            output.append(right[r])
            r += 1
        
        else:
            output.append(left[l])
            l += 1

    
    output.extend(left[l:])
    output.extend(right[r:])

    return output

def merge(arr): 
    
    if len(arr) <= 1: 
        return arr 


    mid = len(arr) // 2 

    right = merge(arr[mid:])
    left = merge(arr[:mid])

    return merge_sort(right, left)

def result():

    arr = create_arr()

    print(f"Unsorted List: {arr}")

    sort_list = merge(arr)

    print(f"Sorted List: {sort_list}")


result()

