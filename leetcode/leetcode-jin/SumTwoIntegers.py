#Sum two integers without + or -

def getSum(self, a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    newList = [a, b]

    #sum() needs an interable, that's why the integers are stored in a list
    return (sum(newList, 0))