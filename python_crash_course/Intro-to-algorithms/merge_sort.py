def merge_sort(list):

    list_len = len(list)


    if list_len <= 1:
        return list 


    mid_point = list_len // 2 

    left = merge_sort(list[:mid_point])
    right = merge_sort(list[mid_point:])


    return merge(left, right)


def merge(left, right): 

    new_list = []
    
    lticker = 0
    rticker = 0
   


    while rticker < len(right) and lticker < len(left):
        if left[lticker] < right[rticker]:

            new_list.append(left[lticker])

            lticker += 1 
        
        else: 
            new_list.append(right[rticker])

            rticker += 1 
        
    new_list.extend(left[lticker:])
    new_list.extend(right[rticker:])

    return new_list


unsorted_list = [4, 1, 5, 7, 2, 6, 1, 1, 6, 4, 10, 33, 5, 7, 23]

print(merge_sort(unsorted_list))