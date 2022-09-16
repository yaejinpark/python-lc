# Usually when you buy something, you're asked whether your credit card number, 
# phone number or answer to your most secret question is still correct. However, 
# since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

# Your task is to write a function maskify, which changes all but the last four characters into '#'.

# return masked string


def maskify(cc):
    return f"{'#'*len(cc[:-4])}{cc[-4:]}"

import codewars_test as test

@test.describe('Sample tests')
def sample_tests():
    @test.it("masking: ''")
    def test1():
        test.assert_equals(maskify(''), '')
    
    @test.it("masking: '123'")
    def test2():
        test.assert_equals(maskify('123'), '123')
    
    @test.it("masking: 'SF$SDfgsd2eA'")
    def test3():
        test.assert_equals(maskify('SF$SDfgsd2eA'), '########d2eA')