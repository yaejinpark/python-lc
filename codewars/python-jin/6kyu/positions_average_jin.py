# https://www.codewars.com/kata/59f4a0acbee84576800000af/train/python

def pos_average(s):
    nums = s.split(", ")
    total_combo = 0
    count = 0
    i = 0
    
    while i < len(nums)-1:
        for j in range(i+1, len(nums)):
            for k in range(len(nums[i])):
                if nums[i][k] == nums[j][k]:
                    count += 1
                total_combo += 1
        i += 1
    return count/total_combo * 100