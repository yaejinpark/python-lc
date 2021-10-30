def merged(l1,l2):
    # If either of the arrays are empty, return the non-empty array.
    # If both are empty, return either.
    if len(l1) == 0:
        return l2
    if len(l2) == 0:
        return l1
    if len(l1) == 0 and len(l2) == 0:
        return []
    
    merged = []
    
    l1_index, l2_index = 0,0

    # Find the index where the shorter array ends
    end_index = min(len(l1),len(l2))

    # While loop lasting until the shorter array ends
    while l1_index < end_index and l2_index < end_index:
        if l1[l1_index] <= l2[l2_index]:
            merged.append(l1[l1_index])
            l1_index += 1
        elif l2[l2_index] <= l1[l1_index]:
            merged.append(l2[l2_index])
            l2_index += 1

    remainder = 0

    # Append remaining values in the longer array
    if len(l1) - end_index != 0:
        for i in range(l1_index,len(l1)):
            merged.append(l1[i])
    elif len(l2) - end_index != 0:
        for i in range(l2_index,len(l2)):
            merged.append(l2[i])

    return merged

l1 = [1,2,3]
l2 = [1,2,4,5]
l3 = []
l4 = [1,2,3]

print(merged(l1,l2))
