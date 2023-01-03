# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates(nums: List[int]) -> int:
    i = 0
    nd = 1

    while i < len(nums):
        if nums[i] != nums[nd-1]:
            nums[nd] = nums[i]
            nd += 1
        i += 1
    return nd