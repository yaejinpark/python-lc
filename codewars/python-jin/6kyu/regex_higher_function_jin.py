# https://www.codewars.com/kata/637d1d6303109e000e0a3116/train/python
import re

def find_matched_by_pattern(pattern):
    def get_match(strng):
        p1,p2,p3 = pattern[0],pattern[1],pattern[2]
        reg = re.compile(f"[^{p2}{p3}]*{p1}[^{p3}]*{p2}.*{p3}.*").fullmatch
        return bool(reg(strng))
    
    return get_match