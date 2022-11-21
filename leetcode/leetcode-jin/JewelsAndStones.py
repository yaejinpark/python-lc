"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
"""

# Brute Force:

def numJewelsInStones(J, S):
    jewelCounter = 0

    for stone in S:
        if stone in J:
            jewelCounter = jewelCounter + 1

    return jewelCounter

jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))

"""
Complexity Analysis

Time Complexity: O(J.length * S.length)).

Space Complexity: O(1) additional space complexity in Python. 
In Java, this can be O(J.length * S.length)) because of the creation of new arrays.

"""

# Attempt 2:
def numJewelsInStones(self, jewels: str, stones: str) -> int:
    jewels_dict = {jewel:0 for jewel in jewels}
    
    for s in stones:
        if s in jewels_dict:
            jewels_dict[s] += 1
    
    return sum(jewels_dict.values())

# Not that different from Brute Force, tbh...


# Attempt 3:
def numJewelsInStones(self, jewels: str, stones: str) -> int:
    jewels_set = set(jewels)
    return sum(stone in jewels_set for stone in stones)

"""
Complexity Analysis

Time Complexity:O(J.length+S.length). 
The O(J.length) part comes from creating J. The O(S.length) part comes from searching S.

Space Complexity: O(J.length).
"""
