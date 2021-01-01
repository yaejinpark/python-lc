
#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    counter = 0
    aMax = max(a)
    bMin = min(b)

    #from numbers between maximum of a and minimum of b,
    for num in range(aMax,bMin+1):
        #return true for each number if it is divisible by elements of a
        aFactor = all([num%aNum ==0 for aNum in a])
        #return true for each number if elements of b are divisible by number
        bFactor = all([bNum%num ==0 for bNum in b])
        #count only if conditions are true for both cases
        counter += aFactor and bFactor
    return counter

