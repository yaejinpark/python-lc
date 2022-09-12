def containsNearbyDuplicate(nums, k):
    # if length of array is less than 2, return False
    if len(nums) < 2: return False

    # first check: duplicate elements exist
    if len(set(nums)) < len(nums):
        i,j = 0, 1
        while j < len(nums): # applying sliding window
            # print("i and j are: ",(i,j))
            if nums[i] == nums[j] and abs(i - j) <= k:
                print("Hit True. nums[i] and nums[j] are: ",(nums[i],nums[j]))
                return True
            else:
                j += 1
            if j - i >= k: # if the difference between the indices greater than k, move i up and move j back right ahead of i
                i += 1
                j = i + 1
        print("No Hit. Returning False.")
        return False
    else:
        print("No Duplicates Exist.")
        return False

containsNearbyDuplicate([1,2,3,1,2,3],2) # Should return False
containsNearbyDuplicate([1,2,3,1],3) # Should return True
containsNearbyDuplicate([4,1,2,3,1,5],3) # Should return True
containsNearbyDuplicate([1,0,1,1],1) # Should return True
containsNearbyDuplicate([1,2,3,4,5,6,7,8,9,9],3) # Should return True

# https://leetcode.com/problems/contains-duplicate-ii/