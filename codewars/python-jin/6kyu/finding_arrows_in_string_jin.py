# https://www.codewars.com/kata/63744cbed39ec3376c84ff4a/train/python
import re

def arrow_search(string: str) -> int:
    arrows = re.findall("<?-+>?|<?=*>?",string)
    total = 0
    for arrow in arrows:
        sign = ('>' in arrow) - ('<' in arrow)
        if '=' in arrow:
            total += 2*sign*len(arrow)
        else:
            total += sign*len(arrow)
    return total