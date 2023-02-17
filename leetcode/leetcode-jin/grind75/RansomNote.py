# https://leetcode.com/problems/ransom-note/description/

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    letters = {c:ransomNote.count(c) for c in set(ransomNote)}
    for c in magazine:
        if c in letters and letters[c] > 0:
            letters[c] -= 1
    return all(x == 0 for x in letters.values())