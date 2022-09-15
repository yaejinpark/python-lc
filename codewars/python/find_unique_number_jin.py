# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python
def find_uniq(arr):
    # your code here
    nums_dict = {}
    for num in arr:
        if num not in nums_dict:
            nums_dict[num] = 1
        else:
            nums_dict[num] += 1
    for k,v in nums_dict.items():
        if v == 1:
            return k

# i like this solution by another person
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b