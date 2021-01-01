def countApplesAndOranges(s, t, a, b, apples, oranges):
    appleCount = 0
    orangeCount = 0

    for apple in range(0, len(apples)):
        applePosition = a + apples[apple]
        if applePosition >= s and applePosition <= t:
            appleCount += 1

    for orange in range(0, len(oranges)):
        orangePosition = b + oranges[orange]
        if orangePosition >= s and orangePosition <= t:
            orangeCount += 1

    print(appleCount)
    print(orangeCount)