# Complete the solution so that the function will 
# break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

import re

def solution(s):
    split_string = re.split('(?=[A-Z])', s)
    new_string = " ".join(split_string)
    return new_string


import codewars_test as test

test.assert_equals(solution("helloWorld"), "hello World")
test.assert_equals(solution("camelCase"), "camel Case")
test.assert_equals(solution("breakCamelCase"), "break Camel Case")