# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]


    # Jin's more efficient solution

    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     value_dict = {}
    #     for count,val in enumerate(nums):
    #         if target - val in value_dict:
    #             return [value_dict[target-val],count]
    #         value_dict[val] = count


import codewars_test as test

test.assert_equals(Solution.twoSum(Solution, [3,2,4], 6), [1,2])
test.assert_equals(Solution.twoSum(Solution, [2,7,11,15], 9), [0,1])