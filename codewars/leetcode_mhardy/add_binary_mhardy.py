# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.



class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        bin_1, bin_2 = int(a), int(b)
        dec_1, i, dec_2, j = 0, 0, 0, 0
        while(bin_1 != 0):
            dec = bin_1 % 10
            dec_1 = dec_1 + dec * pow(2, i)
            bin_1 = bin_1//10
            i += 1
        while(bin_2 != 0):
            dec = bin_2 % 10
            dec_2 = dec_2 + dec * pow(2, j)
            bin_2 = bin_2//10
            j += 1
        result = bin(dec_1 + dec_2).lstrip('0b')
        return result if result else '0'


# Jin's best practices solution:

# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         return bin(int('0b'+a,2) + int('0b'+b,2))[2:]