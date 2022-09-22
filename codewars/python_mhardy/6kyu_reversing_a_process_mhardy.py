# Suppose we know the process by which a string s was encoded to a string r 
# (see explanation below). The aim of the kata is to decode this string r to get back the original string s.

# Explanation of the encoding process:
# input: a string s composed of lowercase letters from "a" to "z", and a positive integer num
# we know there is a correspondence between abcde...uvwxyzand 0, 1, 2 ..., 23, 24, 25 : 0 <-> a, 1 <-> b ...
# if c is a character of s whose corresponding number is x, apply to x the function f: x-> f(x) = num * x % 26, 
# then find ch the corresponding character of f(x)
# Accumulate all these ch in a string r
# concatenate num and r and return the result
# For example:

# encode("mer", 6015)  -->  "6015ekx"

# m --> 12,   12 * 6015 % 26 = 4,    4  --> e
# e --> 4,     4 * 6015 % 26 = 10,   10 --> k
# r --> 17,   17 * 6015 % 26 = 23,   23 --> x

# So we get "ekx", hence the output is "6015ekx"
# Task
# A string s was encoded to string r by the above process. complete the function to get back s whenever it is possible.

# Indeed it can happen that the decoding is impossible for strings composed of whatever letters from "a" to "z" when 
# positive integer num has not been correctly chosen. In that case return "Impossible to decode".

# Examples
# decode "6015ekx" -> "mer"
# decode "5057aan" -> "Impossible to decode"

import re

def decode(str):
    if (first_digit := re.search(r"[a-zA-Z]", str)) is None:
        return "Impossible to decode"
    else:
        numkey = int(str[0:first_digit.start()])
        chars = str[first_digit.start():]

    result_str = ""

    for char in chars:
        index = ord(char) - ord('a')
        found = False
        
        for num in range(0, 26):
            if num * numkey % 26 == index:
                
                if found:
                    return "Impossible to decode"
                else:
                    result_str += chr(ord('a') + num)
                    found = True

        if not found:
            return "Impossible to decode"

    return result_str


import codewars_test as test

@test.describe('Tests')
     
def fixed_tests():
    def testing_decode(s, exp):
        actual = decode(s)
        test.assert_equals(actual, exp)
        
    @test.it('Basic Tests')
    def basic_tests1():
        testing_decode("1273409kuqhkoynvvknsdwljantzkpnmfgf", "uogbucwnddunktsjfanzlurnyxmx")
        testing_decode("761328qockcouoqmoayqwmkkic", "Impossible to decode")
        testing_decode("1544749cdcizljymhdmvvypyjamowl", "mfmwhbpoudfujjozopaugcb")
        testing_decode("1122305vvkhrrcsyfkvejxjfvafzwpsdqgp", "rrsxppowmjsrclfljrajtybwviqb")