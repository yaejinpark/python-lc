# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python
def solution(s):
    final_s = s if len(s) % 2 == 0 else s+"_"
    return [final_s[i]+final_s[i+1] for i in range(len(final_s)-1) if i%2 == 0]