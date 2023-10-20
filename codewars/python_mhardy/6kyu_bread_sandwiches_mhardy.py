# If you're not familiar with the fantastic culinary delights of the British Isles you may not know about the bread sandwich.

# The idea is very simple - if you have a slice of bread between two other slices of bread, then it's a bread sandwich. Additionally, if you have a bread sandwich between two other slices of bread, you get a bread sandwich sandwich, and so on.

# In this kata, we will define the following terms like so:

# Sandwich - Two slices of bread which may or may not have a filling
# Bread Sandwich - Two slices of bread which contains one slice of bread in the middle as a filling
# You will need to build two functions:

# Given the number of slices of bread, return the phrase used to refer to the sandwich
#  2 - 'sandwich'
#  5 - 'bread sandwich sandwich'
# The reverse function - given the name of the sandwich, return how many slices of bread there are in the sandwich
# 'bread sandwich' - 3
# 'sandwich sandwich' - 4
# You should return None/null if there is no input / the input is invalid / there is no sandwich
# Maximum 100 slices of bread

def slices_to_name(n):
    
    if isinstance(n, int) and n >= 2:
        meal = ""
        if n % 2 == 0:
            meal += ("sandwich "*(n//2))
            return meal.rstrip()
        else:
            meal = "bread sandwich "
            meal += "sandwich "*(n//2 - 1)
            return meal.rstrip()
    else:
        return None

def name_to_slices(name):
    if name and isinstance(name, str) and 'bread' not in name.split(' ')[1:]:
        slice_dict = {"bread":1, "sandwich":2}
        total = 0
        for i in name.split(" "):
            if i in slice_dict.keys():
                total += slice_dict[i]
        if total >= 2:
            return total
        else:
            return None
    else:
        return None
    

# from solution import slices_to_name, name_to_slices
import codewars_test as test

@test.describe("slices_to_name")
def tests():
    @test.it("should return the name of the sandwich")
    def test_slices_to_name():
        test.assert_equals(slices_to_name(0), None)
        test.assert_equals(slices_to_name(1), None)
        test.assert_equals(slices_to_name(-2), None)
        test.assert_equals(slices_to_name('bread'), None)
        test.assert_equals(slices_to_name(2), 'sandwich')
        test.assert_equals(slices_to_name(3), 'bread sandwich')
        test.assert_equals(slices_to_name(11),'bread sandwich sandwich sandwich sandwich sandwich')
        test.assert_equals(slices_to_name(8), 'sandwich sandwich sandwich sandwich')
        
        
@test.describe("name_to_slices")
def tests():
    @test.it("should return the number of slices")
    def test_name_to_slices():
        test.assert_equals(name_to_slices(12), None)
        test.assert_equals(name_to_slices(''), None)
        test.assert_equals(name_to_slices('sandwich bread sandwich'), None)
        test.assert_equals(name_to_slices('sand wich'), None)
        test.assert_equals(name_to_slices('sandwich sandwich sandwich sandwich'), 8)
        test.assert_equals(name_to_slices('bread'), None)
        test.assert_equals(name_to_slices('bread sandwich sandwich sandwich'), 7)
        test.assert_equals(name_to_slices('bread sandwich bread sandwich'), None)