# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([c.lower() for c in s if c.isalnum()])
        i,j = 0,len(s)-1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True