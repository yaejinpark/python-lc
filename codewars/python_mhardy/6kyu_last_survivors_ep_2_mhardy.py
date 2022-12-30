# Substitute two equal letters by the next letter of the alphabet (two letters convert to one):

# "aa" => "b", "bb" => "c", .. "zz" => "a".
# The equal letters do not have to be adjacent.
# Repeat this operation until there are no possible substitutions left.
# Return a string.

# Example:

# let str = "zzzab"
#     str = "azab"
#     str = "bzb"
#     str = "cz"
# return "cz"
# Notes
# The order of letters in the result is not important.
# The letters "zz" transform into "a".
# There will only be lowercase letters.

def last_survivors(string):
    new_string = ""
    str_list = [*string]
    str_set = set(string)
    for i in str_set:
        if str_list.count(i) > 1:
            if i == 'z':
                new_string += (str_list.count(i) // 2)*'a' + (str_list.count(i) % 2)*i
            else:
                new_string += (str_list.count(i) // 2) * chr(ord(i)+1) + (str_list.count(i) % 2)*i
        else:
            new_string += i
    if len(set(new_string)) == len(new_string):
        return new_string
    else:
        return last_survivors(new_string)


import codewars_test as test
# from solution import last_survivors

def is_valid(v):
    if not isinstance(v, str):
        test.fail(f"expected a string but got {v}")
    return v

def fix(s):
    return ''.join(sorted(list(s)))

@test.describe("Sample Tests")
def sample():
    @test.it("Given abaa")
    def _():
        user_result = is_valid(last_survivors('abaa'))
        test.assert_equals(fix(user_result), 'ac')
    @test.it("Given zzab")
    def _():
        user_result = is_valid(last_survivors('zzab'))
        test.assert_equals(fix(user_result), 'c')

@test.describe("Zero Length")
def zero_length():
    @test.it("Given ''")
    def _():
        user_result = is_valid(last_survivors(''))
        test.assert_equals(fix(user_result), '')

@test.describe("New Edge")
def new_edge():
    @test.it("Given xsdlafqpcmjytoikojsecamgdkehrqqgfknlhoudqygkbxftivfbpxhxtqgpkvsrfflpgrlhkbfnyftwkdebwfidmpauoteahyh")
    def _():
        user_result = is_valid(last_survivors('xsdlafqpcmjytoikojsecamgdkehrqqgfknlhoudqygkbxftivfbpxhxtqgpkvsrfflpgrlhkbfnyftwkdebwfidmpauoteahyh'))
        test.assert_equals(fix(user_result), 'acdeghlmnqrvyz')