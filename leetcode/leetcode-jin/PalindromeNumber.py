# https://leetcode.com/problems/palindrome-number/
def isPalindrome(x):
    return str(x) == str(x)[::-1]