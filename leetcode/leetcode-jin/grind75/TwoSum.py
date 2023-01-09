# Example of hash tables (dictionaries)
# https://leetcode.com/problems/two-sum/description/

def twoSum(nums: List[int], target: int) -> List[int]:
    value_dict = {}
    for count,val in enumerate(nums):
        if target - val in value_dict:
            return [value_dict[target-val],count]
        value_dict[val] = count