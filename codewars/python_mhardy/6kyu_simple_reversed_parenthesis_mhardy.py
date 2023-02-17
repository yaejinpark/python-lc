# Given a string, return the minimal number of parenthesis reversals needed to make balanced parenthesis.

# For example:

# solve(")(") = 2 Because we need to reverse ")" to "(" and "(" to ")". These are 2 reversals. 
# solve("(((())") = 1 We need to reverse just one "(" parenthesis to make it balanced.
# solve("(((") = -1 Not possible to form balanced parenthesis. Return -1.
# Parenthesis will be either "(" or ")".


# JIN'S BRILLIANT SOLUTION
def solve(s):
    if len(s) % 2 != 0: return -1
    
    while "()" in s:
        s = s.replace("()","")
        
    possible = {"((":1,"))":1,")(":2}
    counter = 0
    
    s_list = [s[i]+s[i+1] for i in range(len(s)-1) if i % 2 == 0]
    
    for pair in s_list:
        counter += possible[pair]
    return counter


import codewars_test as test

test.it("Basic tests")
test.assert_equals(solve(")()("),2)
test.assert_equals(solve("((()"),1)
test.assert_equals(solve("((("),-1)
test.assert_equals(solve("())((("),3)
test.assert_equals(solve("())()))))()()("),4)