# Good example of using stacks
# https://leetcode.com/problems/valid-parentheses/description/

def isValid(self, s: str) -> bool:
    pairs = {"(":")","{":"}","[":"]"}
    open_parens = ["(","{","["]
    dummy = []

    for c in s:
        if c in open_parens:
            dummy.append(c) # add all open parentheses to a stack
        elif len(dummy) > 0 and c == pairs[dummy[-1]]:
            dummy.pop() # if there's a matching closing parenthesis, pop from the stack of open parentheses
        else: return False # if there's no matching closing parenthesis, return False (e.g. only one closing bracket in whole string, which means dummy is empty and meets True condition when it's not.)
    return dummy == [] # return True if all the elements in stack are gone since that indicates all pairs match
