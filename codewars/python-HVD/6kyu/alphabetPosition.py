def alphabet_position(text):
    x=[*text]
    pos=[]
    for char in x:
        if char.isalpha():
            if char.isupper():
                pos.append(ord(char)-64)
            else:
                pos.append(ord(char)-96)
    return(" ".join(str(c) for c in pos))
