# A phrase is a palindrome if, after converting all uppercase letters into lowercase 
# letters and removing all non-alphanumeric characters, it reads the same 
# forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        good_chars = set('abcdefghijklmnopqrstuvwxyz0123456789')
        new_str = ""
        for word in s:
            for letter in word:
                if letter.lower() in good_chars:
                    new_str += letter.lower()
        if len(new_str) == 1:
            return True
        middle = len(list(new_str))//2
        left = list(new_str)[:int(middle)]
        right = list(new_str)[-int(middle):]
        if left == right[::-1]:
            return True
        else:
            return False

# JIN'S MASSIVELY CLEVER "TWO POINTER" SOLUTION

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = ''.join([c.lower() for c in s if c.isalnum()])
#         i,j = 0,len(s)-1

#         while i < j:
#             if s[i] != s[j]:
#                 return False
#             i += 1
#             j -= 1
#         return True


import codewars_test as test

test.assert_equals(Solution.isPalindrome(Solution, "A man, a plan, a canal: Panama"), True)
test.assert_equals(Solution.isPalindrome(Solution, "race a car"), False)
test.assert_equals(Solution.isPalindrome(Solution, " "), True)
test.assert_equals(Solution.isPalindrome(Solution, "0P"), False)
test.assert_equals(Solution.isPalindrome(Solution, "a"), True)