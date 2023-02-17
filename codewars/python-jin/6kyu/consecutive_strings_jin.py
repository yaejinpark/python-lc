# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python
def longest_consec(s, k):
    res = ""
    if len(s) == 0 or k <= 0: return res
    if len(s) < k : return res
    
    for i in range(len(s)-k+1):
        dummy = ''.join(s[i:i+k])
        if len(dummy) > len(res):
            res = dummy
    return res