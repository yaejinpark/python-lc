# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

def alphabet_position(text):
    if type(text) != str: return ''
    text_int_string = [str(ord(s)-96) for s in text.lower() if ord(s)-96 > 0]
    return ' '.join(text_int_string)