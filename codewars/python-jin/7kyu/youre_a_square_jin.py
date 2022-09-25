# https://www.codewars.com/kata/54c27a33fb7da0db0100040e
"""
Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the square of an integer; 

in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages.
"""

def is_square(n):    
    square_root = n**0.5
    return True if square_root ** 2 == n else False