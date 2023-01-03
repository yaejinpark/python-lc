# https://leetcode.com/problems/squares-of-a-sorted-array/description/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i,j = 0, len(nums) - 1
        highest_index = j
        res = [0 for i in range(len(nums))]

        while i <= j:
            left_squared = nums[i] ** 2
            right_squared = nums[j] ** 2

            if left_squared > right_squared:
                res[highest_index] = left_squared
                i += 1
            else:
                res[highest_index] = right_squared
                j -= 1
            highest_index -= 1
        return res