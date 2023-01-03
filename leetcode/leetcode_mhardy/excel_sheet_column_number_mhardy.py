# Given a string columnTitle that represents the column title as 
# appears in an Excel sheet, return its corresponding column number.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 

# Example 1:

# Input: columnTitle = "A"
# Output: 1
# Example 2:

# Input: columnTitle = "AB"
# Output: 28
# Example 3:

# Input: columnTitle = "ZY"
# Output: 701
 

# Constraints:

# 1 <= columnTitle.length <= 7
# columnTitle consists only of uppercase English letters.
# columnTitle is in the range ["A", "FXSHRXW"].

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        if len(list(columnTitle)) == 1:
            return ord(columnTitle) - 64
        else:
            col_list = list(columnTitle)[::-1]
            col_num = ord(col_list[0]) - 64
            exp = 1
            for i in col_list[1:]:
                col_num += (ord(i) - 64) * (26**exp)
                exp += 1

        return col_num

import codewars_test as test

test.assert_equals(Solution.titleToNumber(Solution, 'A'), 1)
test.assert_equals(Solution.titleToNumber(Solution, 'AB'), 28)
test.assert_equals(Solution.titleToNumber(Solution, 'ZY'), 701)
