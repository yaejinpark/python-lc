def kangaroo(x1, v1, x2, v2):
    #Equation: x1 + jumps*v1 = x2 + jumps*v2
    # x1 - x2 = (v2 - v1) * jumps
    # jumps = (x1 - x2)/(v2 - v1)

    if (v1>v2) and (x1-x2) % (v2-v1) == 0:
        return('YES')
    else:
        return('NO')