# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'

def expanded_form(num):
    num_lst = []
    x = [int(d) for d in str(num)]
    for i in range(len(x)):
        if x[i] == 0:
            pass
        else:
            num_lst.append(x[i]*(10**(len(x)-i-1)))
    return " + ".join(str(y) for y in num_lst)


import codewars_test as test

test.assert_equals(expanded_form(12), '10 + 2');
test.assert_equals(expanded_form(42), '40 + 2');
test.assert_equals(expanded_form(70304), '70000 + 300 + 4');