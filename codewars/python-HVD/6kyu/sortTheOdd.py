def sort_array(source_array):
    odds=[]
    x=0
    for num in source_array:
        if (num%2)==0:x+=1
        else:
            odds.append(num)
            x+=1
    odds.sort()
    y=0
    z=0
    for num in source_array:
        if (num%2)==0:y+=1
        else:
            source_array[y]=odds[z]
            y+=1
            z+=1
    return source_array



import codewars_test as test

test.assert_equals(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
test.assert_equals(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
test.assert_equals(sort_array([]),[])