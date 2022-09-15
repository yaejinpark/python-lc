# The drawing below gives an idea of how to cut a given "true" rectangle into 
# squares ("true" rectangle meaning that the two dimensions are different).

# Can you translate this drawing into an algorithm?

# You will be given two dimensions

# a positive integer length
# a positive integer width
# You will return a collection or a string (depending on the language; Shell bash, PowerShell, 
# Pascal and Fortran return a string) with the size of each of the squares.



# def sq_in_rect(lng, wdth):
    
#     if lng == wdth:
#         return None
#     else:
#         gldn_cir(lng, wdth)

# def gldn_cir(lng, wdth):
#     # your code
#     dimensions = [lng, wdth]
#     sqr_list.append(min(dimensions))
#     while min(dimensions) > 1:
#         if dimensions[0] < dimensions[1]:
#             dimensions[1] = max(dimensions) - min(dimensions)
#             gldn_cir(dimensions[0], dimensions[1])
#         else:
#             dimensions[0] = max(dimensions) - min(dimensions)
#             gldn_cir(dimensions[0], dimensions[1])
#     return sqr_list
#     # print(sq_list)

# print(sq_in_rect(5, 3))

def sq_in_rect(lng, wdth):
    sqr_list = []
    dimensions = [lng, wdth]
    if lng == wdth:
        return None
    else: 
        sqr_list.append(min(dimensions))
        sqr_list.append(gldn_cir(lng, wdth))
    return sqr_list

def gldn_cir(lng, wdth):
    dimensions = [lng, wdth]
    while min(dimensions) > 1:
        new_dimensions = []
        if dimensions[0] < dimensions[1]:
            new_dimensions.append(dimensions[1] % dimensions[0])
            gldn_cir(new_dimensions[0], dimensions[0])
            
        else:
            new_dimensions.append(dimensions[0] % dimensions[1])
            gldn_cir(new_dimensions[0], dimensions[1])
        return new_dimensions
            
    

print(sq_in_rect(5, 3))
# import codewars_test as test
# from random import randint


# @test.describe("Tests...")
# def _():

#     @test.it("Basic Tests")
#     def _():
#         test.assert_equals(sq_in_rect(5, 5), None)
#         test.assert_equals(sq_in_rect(5, 3), [3, 2, 1, 1])
#         test.assert_equals(sq_in_rect(3, 5), [3, 2, 1, 1])
#         test.assert_equals(sq_in_rect(20, 14), [14, 6, 6, 2, 2, 2])
