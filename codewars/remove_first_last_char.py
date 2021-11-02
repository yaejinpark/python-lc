def remove_char(s):
    dummy = s[1:len(s)-1]

    result = dummy[0:len(dummy)]

    print(result)

def remove_char_better(s):
    print(s[1:-1])
    return s[1:-1]

teststring1 = "eloquent"

remove_char_better(teststring1)