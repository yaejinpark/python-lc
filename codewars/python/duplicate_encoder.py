"""
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 

"""

def duplicate_encode(word):
    #your code here
    freq = {}
    word = word.lower()
    for char in word:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    
    return ''.join("(" if freq[char] == 1 else ")" for char in word)

# Even better - O(n) instead of O(n^2) that uses .count()

#This solution is O(n) instead of O(n^2) like the methods that use .count()
#because .count() is O(n) and it's being used within an O(n) method.
#The space complexiety is increased with this method.
import collections
def duplicate_encode2(word):
    new_string = ''
    word = word.lower()
    #more info on defaultdict and when to use it here:
    #http://stackoverflow.com/questions/991350/counting-repeated-characters-in-a-string-in-python
    d = collections.defaultdict(int)
    for c in word:
        d[c] += 1
    for c in word:
        new_string = new_string + ('(' if d[c] == 1 else ')')
    return new_string

print(duplicate_encode("Success")) # Should return )())())
print(duplicate_encode("(( @")) # Should return ))((