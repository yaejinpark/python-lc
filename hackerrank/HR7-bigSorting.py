def solution (unsorted):

    #Cost of parsing an integer to a string is quite big.
    #Adding key=int does the string to int conversion internally during the sort process
    unsorted.sort(key=int)
    for s in unsorted:
        print(s)