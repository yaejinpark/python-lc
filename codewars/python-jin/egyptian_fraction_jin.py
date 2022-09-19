# https://www.codewars.com/kata/54f8693ea58bce689100065f/train/python
def input_parser(n):
    if '/' in n: return n.split('/')
    if '.' in n:
        if float(n) > 1:
            dummy = str(float(n) - 1)
        dummy = n.split('.')
        numer = dummy[1]
        denom = '1' + '0'*len(numer)
        return [numer,denom] if float(n) < 1 else ['1',numer,denom]
    else: return int(n)

def decompose(n):
    # your code
    if n == '0': return [] # if given n is 0, return empty list

    n_parsed = input_parser(n)
    
    res = []
    numer = 0
    denom = 0

    if len(n_parsed) == 2: # if there is a fraction less than 1, assign numerator and denominator to separate variables
        numer = int(n_parsed[0])
        denom = int(n_parsed[1])
    else:
        res.append(n_parsed[0])
        numer = int(n_parsed[1])
        denom = int(n_parsed[2])
        
    if numer > denom: # if fraction is greater than 1...
        res.append(str(int(numer/denom)))
        return res
    
    if numer == 1: # if the numerator is 1, just return the fraction
        res.append(f"{numer}/{denom}")
        return res

    while numer != 0:
        x = -(denom//-numer)
        res.append(f"1/{x}")
        numer = x * numer - denom
        denom = denom * x
        
    return res