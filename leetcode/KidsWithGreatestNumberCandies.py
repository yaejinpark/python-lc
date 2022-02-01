"""
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

 

Example 1:

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
Example 2:

Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false] 
Explanation: There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.
Example 3:

Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]
"""

# Attempt 1
def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    max_candies = max(candies)
    res = []
    
    for kid in candies:
        if kid + extraCandies >= max_candies:
            res.append(True)
        else:
            res.append(False)
    return res

# Time Complexity: O(2N) = O(N) - Goes through list once to find the max, then goes through again for a for loop.

# One-Liner
def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    return [candy + extraCandies >= max(candies) for candy in candies]

# Time Complexity: O(N^2) because max is called for each iteration in the for loop.
# Pros of One-Liner: Uses two variables less than Attempt 1
# Cons: O(N^2). Yikes.

# Optimized Code - Combination of Attempt 1 and One-Liner
def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    candy_limit = max(candies) - extraCandies
    return [candy >= candy_limit for candy in candies]




