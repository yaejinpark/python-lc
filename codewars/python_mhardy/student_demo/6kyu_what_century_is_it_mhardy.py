# Return the century of the input year. 
# The input will always be a 4 digit string, 
# so there is no need for validation.

# Examples
# "1999" --> "20th"
# "2011" --> "21st"
# "2154" --> "22nd"
# "2259" --> "23rd"
# "1124" --> "12th"
# "2000" --> "20th"


def what_century(year):
    result = (int(year)//100)+1
    res_dict = {"st": [1], "nd": [2], "rd": [3], "th": [4, 5, 6, 7, 8, 9, 10, 11, 12, ]}
    print(res_dict)
    if result < 5 or result > 13:
        end_num = int(str(result)[-1])
        suffix = [i for i in res_dict.keys() if end_num in res_dict[i]][0]
        print(suffix)
    else:
        suffix = "th"
    return f"{result}{suffix}"



import codewars_test as test
# from solution import what_century

def dotest(y, expected):
    actual = what_century(y)
    test.assert_equals(actual, expected, f"Test failed with year = \"{y}\"")
    
@test.describe("Tests")
def fixed_tests():
    @test.it('Sample tests')
    def basic_test_cases():
        dotest("2011", "21st")
        dotest("2154", "22nd")
        dotest("2259", "23rd")
        dotest("1234", "13th")
        dotest("1023", "11th")