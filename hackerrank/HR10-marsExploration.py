#useful when you have to check adjacent elements in string or list
#but don't want to risk out of bounds error for index by using notations
#such as i+n

def marsExploration(s):
    counter = 0
    for i in range(len(s)):
        if i%3 == 0 and s[i] != "S":
            counter += 1
        elif i%3 == 1 and s[i] != "O":
            counter += 1
        elif i%3 == 2 and s[i] != "S":
            counter += 1
    return counter