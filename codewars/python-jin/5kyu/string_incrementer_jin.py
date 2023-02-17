# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python
def increment_string(strng):
    alpha = strng.rstrip("1234567890")
    nums = strng[len(alpha):]
    return alpha + "1" if len(nums) == 0 else alpha + str(int(nums)+1).zfill(len(nums))