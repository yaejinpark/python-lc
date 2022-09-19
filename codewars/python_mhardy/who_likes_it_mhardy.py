# You probably know the "like" system from Facebook and other pages. 
# People can "like" blog posts, pictures or other items. We want to create the 
# text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of people that like an item. 
# It must return the display text as shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# Note: For 4 or more names, the number in "and 2 others" simply increases.


def likes(names):
    if not names:
        return "no one likes this"
    result = ""
    i = 0
    if len(names) >= 4:
        for i in range(0, 1):
            result = "{}, {} and {} others like this".format(names[0], names[1], len(names)-2)
    elif len(names) == 1:
        result += "{} likes this".format(names[i])
    else:
        while i < len(names)-2:
            result += f"{names[i]}, "
            i += 1
        if i == len(names)-2:
            result += "{} and {} like this".format(names[i], names[i+1])
    
    return result




import codewars_test as test


@test.it('Basic tests')
def _():
    test.assert_equals(likes([]), 'no one likes this')
    test.assert_equals(likes(['Peter']), 'Peter likes this')
    test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
    test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
    test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')