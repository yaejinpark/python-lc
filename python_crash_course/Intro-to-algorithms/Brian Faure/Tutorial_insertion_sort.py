
# create randomized arrays for string 
def create_array(size = 10, max = 50): 
    from random import randint
    return [randint(0, max) for _ in range(size)]


# applies insertion sort to input array 'a'
def insertion_sort(a): 
    for sort_len in range(1, len(a)): 
        current_item = a[sort_len] # next unsorted item 
        insert_idx = sort_len # current index of item

        # iterate until we reach correct insert spot 
        while insert_idx > 0 and current_item < a[insert_idx - 1]: 
            a[insert_idx] = a[insert_idx - 1]

            insert_idx += -1 # decrement insert spot 
        
        a[insert_idx] = current_item
    
    return a 
    

a = create_array()

print(a)

s = insertion_sort(a)

print(s)