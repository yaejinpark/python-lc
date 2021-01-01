#Is s2 a "rotation of s1?
#Example - s1: waterbottle, s2: erbottlewat

def isSubstring(s1,s2):
    #Both strings need to be of the same length
    if len(s1) != len(s2):
        return False

    #None of the strings can be empty
    if len(s1) == 0 or len(s2) == 0:
        return False

    s1extended = s1+s1

    if s2 not in s1extended:
        return False
    else:
        return True

string1 = "waterbottle"
string2 = "erbottlewat"
string3 = "computer"
string4 = "putercom"
string5 = "cputomer"
print(isSubstring(string1,string2))
print(isSubstring(string3,string4))
print(isSubstring(string3,string5))

#TL;DR
#If s2 is a rotation of s1, it should be a part of s1extended.
#s1 = xy, s2 = yx
#s1+s1 = xyxy