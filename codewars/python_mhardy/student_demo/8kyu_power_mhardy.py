# The goal is to create a function of two inputs number and power, 
# that "raises" the number up to power (ie multiplies number by itself power times).

# Examples
# number_to_pwr(3, 2)  # -> 9 ( = 3 * 3 )
# number_to_pwr(2, 3)  # -> 8 ( = 2 * 2 * 2 )
# number_to_pwr(10, 6) # -> 1000000
# Note: math.pow and some others math functions are disabled on final tests.



# not-so-longform variable assignment method
# def number_to_pwr(number, p): 
#     num = number ** p
#     return num


# Most elegant approach
def number_to_pwr(number, p): 
    result = 1
    for i in range(p):
        result *= number
    return result
    
import codewars_test as test
# from solution import number_to_pwr

@test.describe('Example Tests')
def example_tests():
    @test.it('Example Test Case')
    def example_test_case():
        test.assert_equals(number_to_pwr(4, 2), 16)
        test.assert_equals(number_to_pwr(10, 4), 10000)
        
    @test.it('Edge Test Case')
    def edge_test_case():
        test.assert_equals(number_to_pwr(10, 0), 1)