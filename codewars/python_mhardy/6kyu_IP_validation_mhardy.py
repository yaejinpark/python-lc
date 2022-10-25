# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. 
# IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

# Valid inputs examples:
# Examples of valid inputs:
# 1.2.3.4
# 123.45.67.89
# Invalid input examples:
# 1.2.3
# 1.2.3.4.5
# 123.456.78.90
# 123.045.067.089
# Notes:
# Leading zeros (e.g. 01.02.03.04) are considered invalid
# Inputs are guaranteed to be a single string

def is_valid_IP(strng):
    octets = strng.split(".")
    if len(octets) != 4:
        return False
    for octet in octets:
        for i in octet:
            if i.isspace() or i.isalpha() or i == '':
                return False
        if octet == '':
            return False
        elif len(str(octet)) != 1 and octet[0] == '0':
            return False
        elif int(octet) > 255 or int(octet) < 0:
            return False
        
    return True



import codewars_test as test
# from solution import is_valid_IP

@test.describe("Sample tests")
def _():
    @test.it("Tests")
    def __():
        test.assert_equals(is_valid_IP('12.255.56.1'),     True)
        test.assert_equals(is_valid_IP(''),                False)
        test.assert_equals(is_valid_IP('abc.def.ghi.jkl'), False)
        test.assert_equals(is_valid_IP('123.456.789.0'),   False)
        test.assert_equals(is_valid_IP('12.34.56'),        False)
        test.assert_equals(is_valid_IP('12.34.56 .1'),     False)
        test.assert_equals(is_valid_IP('12.34.56.-1'),     False)
        test.assert_equals(is_valid_IP('123.045.067.089'), False)
        test.assert_equals(is_valid_IP('127.1.1.0'),        True)
        test.assert_equals(is_valid_IP('0.0.0.0'),          True)
        test.assert_equals(is_valid_IP('0.34.82.53'),       True)
        test.assert_equals(is_valid_IP('192.168.1.300'),   False)