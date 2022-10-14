def solution(s):
    x=0
    for char in s:
        if char.isupper():
            s=s[:x] + ' ' + s[x:]
            x+=1
            print(x)
        else:
            x+=1
        
    return s




import codewars_test as test

test.assert_equals(solution("helloWorld"), "hello World")
test.assert_equals(solution("camelCase"), "camel Case")
test.assert_equals(solution("breakCamelCase"), "break Camel Case")