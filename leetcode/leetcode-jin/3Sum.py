# https://leetcode.com/problems/3sum/description/
class Solution:
    def find_pairs(self,arr,i,target):
        j = len(arr)-1
        triplets = []
        while i < j:
            if arr[i] + arr[j] == target:
                triplets.append([-target,arr[i],arr[j]])
                i += 1
                j -= 1
                while i < j and arr[i] == arr[i-1]:
                    i += 1
                while i < j and arr[j] == arr[j+1]:
                    j -= 1
            elif arr[i] + arr[j] > target:
                j -= 1
            else:
                i += 1
        return triplets

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            dummy = self.find_pairs(nums,i+1,-nums[i])
            if dummy:
                res.extend(dummy)
        return res
Console
