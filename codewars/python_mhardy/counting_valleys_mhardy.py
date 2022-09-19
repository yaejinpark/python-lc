# You need count how many valleys you will pass.

# Start is always from zero level.

# Every time you go down below 0 level counts as an entry of a valley, and as you go up to 0 level from valley counts as an exit of a valley.

# One passed valley is equal one entry and one exit of a valley.

def counting_valleys(s): 
    count = 0
    valleys = 0
    for i in list(s):
        if i == 'U':
            count -= 1
            if count == 0:
                valleys += 1
        elif i == 'D':
            count += 1
        else:
            continue
    return valleys




import codewars_test as test

@test.describe('Example Tests')
def example_tests():
    test.assert_equals(counting_valleys('UFFFD'), 0)
    test.assert_equals(counting_valleys('DFFFD'), 0)
    test.assert_equals(counting_valleys('UFFFU'), 0)
    test.assert_equals(counting_valleys('DFFFU'), 1)
    test.assert_equals(counting_valleys('UFFDDFDUDFUFU'), 1)
    test.assert_equals(counting_valleys('UFFDDFDUDFUFUUFFDDFDUDFUFU'), 2)
    test.assert_equals(counting_valleys('UFFDDFDUDFUFUUFFDDUFFDDUFFDDUDUDUDUDUDUUUUUUUUU'), 3)
    test.assert_equals(counting_valleys('UFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFU'), 4)
    test.assert_equals(counting_valleys('UFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFU'), 6)