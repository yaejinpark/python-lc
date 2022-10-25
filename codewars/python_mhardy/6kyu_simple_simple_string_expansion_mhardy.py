# Given a string that includes alphanumeric characters ("3a4B2d") return the expansion of that string: 
# The numeric values represent the occurrence of each letter preceding that numeric value. There should be no numeric characters in the final string.

# Notes
# The first occurrence of a numeric value should be the number of times each character behind it is repeated, until the next numeric value appears
# If there are multiple consecutive numeric characters, only the last one should be used (ignore the previous ones)
# Empty strings should return an empty string.
# Your code should be able to work for both lower and capital case letters.

# "3D2a5d2f"  -->  "DDDaadddddff"    # basic example: 3 * "D" + 2 * "a" + 5 * "d" + 2 * "f"
# "3abc"      -->  "aaabbbccc"       # not "aaabc", nor "abcabcabc"; 3 * "a" + 3 * "b" + 3 * "c"
# "3d332f2a"  -->  "dddffaa"         # multiple consecutive digits: 3 * "d" + 2 * "f" + 2 * "a"
# "abcde"     -->  "abcde"           # no digits
# "1111"      -->  ""                # no characters to repeat
# ""          -->  ""                # empty string


def string_expansion(s):
    if len(s) == 0 or s.isdigit(): return ""
    new_string = ""
    digit = 1

    for i in s:
        if i.isdigit():
            digit = int(i)
        else:
            new_string += digit*i
    return new_string




import codewars_test as test
# from solution import string_expansion


@test.describe("Sample Tests")
def sample_tests():
    @test.it("Normal cases")
    def _():
        test.assert_equals(string_expansion('3D2a5d2f'), 'DDDaadddddff')
        test.assert_equals(string_expansion('4D1a8d4j3k'), 'DDDDaddddddddjjjjkkk')
        test.assert_equals(string_expansion('4D2a8d4j2f'), 'DDDDaaddddddddjjjjff')
        test.assert_equals(string_expansion('3n6s7f3n'), 'nnnssssssfffffffnnn')
        test.assert_equals(string_expansion('0d4n8d2b'), 'nnnnddddddddbb')
        test.assert_equals(string_expansion('0c3b1n7m'), 'bbbnmmmmmmm')
        test.assert_equals(string_expansion('7m3j4ik2a'), 'mmmmmmmjjjiiiikkkkaa')
        test.assert_equals(string_expansion('3A5m3B3Y'), 'AAAmmmmmBBBYYY')
        test.assert_equals(string_expansion('5M0L8P1'), 'MMMMMPPPPPPPP')
        test.assert_equals(string_expansion('2B'), 'BB')
        test.assert_equals(string_expansion('7M1n3K'), 'MMMMMMMnKKK')
        test.assert_equals(string_expansion('A4g1b4d'), 'Aggggbdddd')

    @test.it("Repeated numerals")
    def _():
        test.assert_equals(string_expansion('111111'), '')
        test.assert_equals(string_expansion('4d324n2'), 'ddddnnnn')
        test.assert_equals(string_expansion('5919nf3u'), 'nnnnnnnnnfffffffffuuu')
        test.assert_equals(string_expansion('2n1k523n4i'), 'nnknnniiii')
        test.assert_equals(string_expansion('6o23M32d'), 'ooooooMMMdd')
        test.assert_equals(string_expansion('1B44n3r'), 'Bnnnnrrr')
        test.assert_equals(string_expansion('M21d1r32'), 'Mdr')
        test.assert_equals(string_expansion('23M31r2r2'), 'MMMrrr')
        test.assert_equals(string_expansion('8494mM25K2A'), 'mmmmMMMMKKKKKAA')
        test.assert_equals(string_expansion('4A46D6B3C'), 'AAAADDDDDDBBBBBBCCC')
        test.assert_equals(string_expansion('23D42B3A'), 'DDDBBAAA')
        test.assert_equals(string_expansion('143D36C1A'), 'DDDCCCCCCA')

    @test.it("Repeated alphabetic characters")
    def _():
        test.assert_equals(string_expansion('asdf'), 'asdf')
        test.assert_equals(string_expansion('23jbjl1eb'), 'jjjbbbjjjllleb')
        test.assert_equals(string_expansion('43ibadsr3'), 'iiibbbaaadddsssrrr')
        test.assert_equals(string_expansion('123p9cdbjs'), 'pppcccccccccdddddddddbbbbbbbbbjjjjjjjjjsssssssss')
        test.assert_equals(string_expansion('2309ew7eh'), 'eeeeeeeeewwwwwwwwweeeeeeehhhhhhh')
        test.assert_equals(string_expansion('312987rfebd'), 'rrrrrrrfffffffeeeeeeebbbbbbbddddddd')
        test.assert_equals(string_expansion('126cgec'), 'ccccccggggggeeeeeecccccc')
        test.assert_equals(string_expansion('1chwq3rfb'), 'chwqrrrfffbbb')
        test.assert_equals(string_expansion('389fg21c'), 'fffffffffgggggggggc')
        test.assert_equals(string_expansion('239vbsac'), 'vvvvvvvvvbbbbbbbbbsssssssssaaaaaaaaaccccccccc')
        test.assert_equals(string_expansion('davhb327vuc'), 'davhbvvvvvvvuuuuuuuccccccc')
        test.assert_equals(string_expansion('cvyb239bved2dv'), 'cvybbbbbbbbbbvvvvvvvvveeeeeeeeedddddddddddvv')

    @test.it("Empty string")
    def _():
        test.assert_equals(string_expansion(''), '')