# https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python

def find_missing_letter(chars):
    # if capital , subtract 64. if lower, subtract 96
    chars_int = [ord(char) for char in chars]
    min_char,max_char = min(chars_int),max(chars_int)
    all_chars = [i for i in range(min_char,max_char+1)]
    
    return "".join([chr(c) for c in all_chars if not c in chars_int])