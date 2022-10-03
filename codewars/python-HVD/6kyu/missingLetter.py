def find_missing_letter(chars):
    y=0
    for char in chars:
        x = ord(char)
        if x == y+2:
            print (chr(x-1))
        else:
            y = x

chars= ['a','b','c','d','f']
find_missing_letter(chars)