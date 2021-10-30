def numJewelsInStones(J, S):
    jewelCounter = 0

    for stone in S:
        if stone in J:
            jewelCounter = jewelCounter + 1

    return jewelCounter

jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))
