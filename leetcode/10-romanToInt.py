def romanToInt(s):
    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    totalSum = 0
    val = "I"

    for numeral in s[::-1]:
        print("numeral",numeral)
        print("val",val)
        if dict[numeral] < dict[val]:
            totalSum -= dict[numeral]
        else:
            totalSum += dict[numeral]
            val = numeral
    return totalSum
print(romanToInt("IVX"))