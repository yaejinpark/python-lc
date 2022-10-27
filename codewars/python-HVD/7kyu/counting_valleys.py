def counting_valleys(s): 
    height=0
    valley=0
    actions= ([*s])
    #print (actions)
    for move in actions:
        if move == "U":
            height += 1
            if height == 0:
                valley += 1
        elif move == "D":
            height -= 1
    return valley


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