# https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/python
def expanded_form(num):
    num_string = str(num)
    strings = [int(num_string[i])*10**(len(num_string)-i-1) for i in range(len(num_string))]
    return ' + '.join(str(s) for s in strings if s != 0)

print(expanded_form(12))
print(expanded_form(70304))