# https://leetcode.com/problems/valid-anagram/description/

# Is this cheating? lol
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_s = [c for c in s]
        char_t = [c for c in t]
        char_s.sort()
        char_t.sort()
        return char_s == char_t