# https://www.codewars.com/kata/578553c3a1b8d5c40300037c
def binary_array_to_number(arr):
    return int('0b'+''.join(map(str,arr)),2)