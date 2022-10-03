def order(sentence):
    words=sentence.split()
    sort_sen= [0]*len(words)
    for word in words:
        char=[*word]
        for x in char:
            if x.isnumeric():
                sort_sen[int(x)-1]= word
            else:
                continue
    return ' '.join(sort_sen)

import codewars_test as test

@test.describe('Your order, please')
def desc1():
    @test.it('Sample tests')
    def it1():
        test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
        test.assert_equals(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
        test.assert_equals(order(""), "")