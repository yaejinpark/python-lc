def merged(l1,l2):
    if len(l1) == 0:
        return l1
    if len(l2) == 0:
        return l2
    
    merged = []
    
    l1_index, l2_index = 0,0

    end_index = min(len(l1),len(l2))
    print(end_index)

    while l1_index < end_index-1 and l2_index < end_index-1:
        if l1[l1_index] <= l2[l2_index]:
            merged.append(l1[l1_index])
            l1_index += 1
        if l2[l2_index] <= l1[l1_index]:
            merged.append(l2[l2_index])
            l2_index += 1

        print(l1_index,l2_index)
    print(merged)

l1 = [1,2,3]
l2 = [1,2,4,5]

merged(l1,l2)