def decode(r):
    x=[*r]
    numb= ""
    string=[]
    code=[]
    decode=[]
    # print(x)
    for char in x:
        if char.isnumeric():
            numb += char
        else:
            string.append(char)
    print(int(numb))
    print(string)
    for let in string:
        y=(ord(let)-97)* int(numb)
        # print (y)
        hash = (y) % 26
        # print(hash)
        code.append(hash)
        print(ord(let)-97)
    print(code)
    for num in code:
        decode.append(chr(num+96))
    # print(decode)
    # return ' '.join(decode)
    print(' '.join(decode))






r="6015ekx"
decode(r)

print(12*6015 %26)



# import codewars_test as test

# @test.describe('Tests')
     
# def fixed_tests():
#     def testing_decode(s, exp):
#         actual = decode(s)
#         test.assert_equals(actual, exp)
        
#     @test.it('Basic Tests')
#     def basic_tests1():
#         testing_decode("1273409kuqhkoynvvknsdwljantzkpnmfgf", "uogbucwnddunktsjfanzlurnyxmx")
#         testing_decode("761328qockcouoqmoayqwmkkic", "Impossible to decode")
#         testing_decode("1544749cdcizljymhdmvvypyjamowl", "mfmwhbpoudfujjozopaugcb")
#         testing_decode("1122305vvkhrrcsyfkvejxjfvafzwpsdqgp", "rrsxppowmjsrclfljrajtybwviqb")