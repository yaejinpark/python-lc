# Code Wars - xes and Ohs
def xo(s):
    x_counter, o_counter = 0,0
    for char in s:
        if char.lower() == "x":
            x_counter += 1
        elif char.lower() == "o":
            o_counter += 1
    return True if x_counter == o_counter else False