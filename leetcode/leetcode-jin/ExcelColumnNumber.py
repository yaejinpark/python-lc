# https://leetcode.com/problems/excel-sheet-column-number/submissions/867702121/

def titleToNumber(columnTitle: str) -> int:
    if len(columnTitle) == 1: return ord(columnTitle) - 64
    cycles = [ord(c) - 64 for c in columnTitle]
    powers = [26**(len(cycles) - i) for i in range(1,len(cycles)+1)]
    res = [i1 * i2 for i1,i2 in zip(cycles,powers)]
    return sum(res)

print(titleToNumber('A')) # 1
print(titleToNumber('AB')) # 28
print(titleToNumber('ZY')) # 701