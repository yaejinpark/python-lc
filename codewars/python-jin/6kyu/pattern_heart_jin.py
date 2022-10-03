# https://www.codewars.com/kata/56e8d06029035a0c7c001d85/train/python

def draw(n):
    res = ''
    first_line = 2*('◢' + (n//2 - 2)*'■' + '◣') + '\n' # first line of the heart
    res += first_line
    
    for i in range(n//6):
        res += n * '■' + '\n' # full square lines of the heart
    
    for i in range(0,n//2): # remaining lines of the heart
        new_line = i*'\u2003' + '◥' + (n-2*i-2)*'■' + '◤' + i*'\u2003'+'\n'
        res += new_line
    
    return res[:len(res)-1] # -1 to crop out the extra line break