# Given two arrays of strings a1 and a2 return a sorted array r in lexicographical 
# order of the strings of a1 which are substrings of strings of a2.

# Example 1:
# a1 = ["arp", "live", "strong"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns ["arp", "live", "strong"]

# Example 2:
# a1 = ["tarp", "mice", "bull"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns []

# Notes:
# Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
# In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
# Beware: r must be without duplicates.


def in_array(array1, array2):
    results = []
    for i in array1:
        if any(f"{i}" in entry for entry in array2):
            results.append(i)
    res = set(results)
    return sorted(res)



import codewars_test as test
    
@test.describe("in_array")
def tests():
    def testing(array1, array2, expect):
        actual = in_array(array1, array2)
        test.assert_equals(actual, expect)
    @test.it("Basic tests")
    def basics():
        a1 = ["live", "arp", "strong"] 
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        r = ['arp', 'live', 'strong']
        testing(a1, a2, r)          
        a1 = ["arp", "mice", "bull"] 
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        r = ['arp']
        testing(a1, a2, r)    