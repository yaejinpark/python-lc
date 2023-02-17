# https://www.codewars.com/kata/5a3f2925b6cfd78fb0000040/train/python
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