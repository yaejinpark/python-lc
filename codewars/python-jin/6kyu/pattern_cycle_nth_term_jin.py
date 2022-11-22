# Totally different title from the problem, but it's for me to find it easily later on
# https://www.codewars.com/kata/55ffb44050558fdb200000a4/train/python

def sumDig_nthTerm(initVal, patternL, nthTerm):
    n = nthTerm - 1
    num_cycle,current_position = divmod(n,len(patternL))
    passed_complete_cycles = num_cycle*sum(patternL) # calculate the sum of whole cycles completed
    passed_partial_cycle = sum(patternL[:current_position])# calculating the partial cycle, which is the last
    
    finalVal = initVal + passed_complete_cycles + passed_partial_cycle
    
    return sum([int(c) for c in str(finalVal)])