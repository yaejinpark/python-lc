# Given an array containing only zeros and ones, find the index of the zero that, 
# if converted to one, will make the longest sequence of ones.

# For instance, given the array:

# [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1]
# replacing the zero at index 10 (counting from 0) forms a sequence of 9 ones:

# [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1]
#                   '------------^------------'
# Your task is to complete the function that determines where to replace a zero 
# with a one to make the maximum length subsequence.

# Notes:

# If there are multiple results, return the last one:
# [1, 1, 0, 1, 1, 0, 1, 1] ==> 5

# The array will always contain only zeros and ones.
# Can you do this in one pass?


# def replace_zero(arr):
#     maximum = 0
#     start_idx = 0
#     zero_flag = False
#     hot_idx = 0
#     result = -1
#     for i in range(start_idx, len(arr)):
#         if arr[i] == 1:
#             counter = 1
#             for y in range(i+1, len(arr)):
#                 print(counter, arr[i], arr[y])
#                 if arr[y] == 1:
#                     counter += 1
#                 elif arr[y] == 0 and zero_flag == False:
#                     hot_idx = y
#                     zero_flag = True
#                     counter += 1
#                 elif arr[y] == 0 and zero_flag == True:
#                     if counter > maximum:
#                         maximum = counter
#                         result = hot_idx
#                     else:
#                         pass
#     if result > -1:
#         return result
#     else:
#         return 0

# def replace_zero(arr):
#     maximum = 0
#     zero_flag = False
#     result = 0
#     hot_idx = 0
#     for i in range(len(arr)):
#         counter = 0
#         print(arr[i], counter)
#         if arr[i] == 1:
#             counter += 1
#             for y in range(i+1, len(arr)):
                
#                 if arr[y] == 1:
#                     counter += 1
#                     hot_idx += 1
#                     print(arr[y], counter)
#                 if arr[y] == 0:
#                     if zero_flag == False:
#                         counter += 1
#                         zero_flag = True
#                         hot_idx += 1
#                         print(arr[y], counter)
#                     else:
#                         if counter > maximum:
#                             maximum = counter
#                             result += y
#                         else:
#                             counter = 0
#         else:
#             pass
#     return result

# def replace_zero(arr):
#     maximum = 0
#     result = 0
#     for idx, val in enumerate(arr):
#         if val == 1:
#             zero_flag = False
#             counter = 1
#             sublist = arr[idx:]
#             for yidx, yval in enumerate(sublist):

#                 if yval == 1:
#                     counter +=1
#                 elif yval == 0 and zero_flag == False:
#                     if yidx < len(sublist)-1:
#                         counter +=1
#                         zero_flag = True
#                     elif yidx == len(sublist)-1:
#                         counter += 1
#                         if counter > maximum:
#                             maximum = counter
#                             result = idx + yidx
#                 elif yval == 0 and zero_flag == True:
#                     if counter > maximum:
#                         maximum = counter
#                         result = yidx
#         else:
#             pass
#     return result

# def replace_zero(arr):
#     maximum = 0
#     hot_idx = 0

#     for idx, val in enumerate(arr):

#         if val == 1:
#             sub_list = arr[idx+1:]
#             res_list = [1]
#             for yidx, yval in enumerate(sub_list):
#                 if yval == 1:
#                     res_list.append(yval)
#                 elif yval == 0 and res_list.count(0) == 0:
#                     if int(yidx) < len(sub_list)+1:
#                         res_list.append(yval)
#                     elif int(yidx) == len(sub_list)+1:
#                         res_list.append(yval)
#                         if len(res_list) > maximum:
#                             maximum = len(res_list)
#                             hot_idx = int(idx) + int(yidx)
#                 elif yval == 0 and res_list.count(0) > 0:
#                     if len(res_list) > maximum:
#                             maximum = len(res_list)
#                             hot_idx = int(idx) + int(yidx) + 1
#                     else:
#                         break
#         else:
#             pass
#     return hot_idx

def replace_zero(arr):
    maximum = 0
    result = 0
    current_len = 0
    current_idx = None
    for idx, val in enumerate(arr):
        if val == 1:
            current_len += 1
        else:
            if current_len >= maximum:
                maximum = current_len
                result = current_idx
            if current_idx is None:
                current_len +=1
            elif idx - current_idx < 2:
                current_len = 1
            else:
                current_len = idx - current_idx
            current_idx = idx
    if current_len >= maximum:
        maximum, result = current_len, current_idx

    return result



import codewars_test as test
# from solution import replace_zero

@test.describe("Sample tests")
def sample_tests():
    @test.it("Examples")
    def examples():
        test.assert_equals(replace_zero([1,1,1,0,1,1,0,1,1,1]), 6)
        test.assert_equals(replace_zero([0,1,1,1]), 0)
        test.assert_equals(replace_zero([1,1,1,0]), 3)
        test.assert_equals(replace_zero([1,1,1,0,0,1,1,1,1,1,0,1]), 10)
        test.assert_equals(replace_zero([0,1,0,0,0,0]), 2)