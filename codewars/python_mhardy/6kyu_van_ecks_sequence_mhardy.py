# 0, 0, 1, 0, 2, 0, 2, 2, 1, 6, 0, 5, 0, 2, 6, 5, 4, 0, 5, 3, 0, 3, …

# This is the Van Eck's Sequence.

# Let's go through it step by step.

# Term 1: The first term is 0.
# Term 2: Since we haven’t seen 0 before, the second term is 0.
# Term 3: Since we had seen a 0 before, one step back, the third term is 1
# Term 4: Since we haven’t seen a 1 before, the fourth term is 0
# Term 5: Since we had seen a 0 before, two steps back, the fifth term is 2.
# And so on...

# Your task is to find the n_th number in Van Eck's Sequence. (1-based)

# There are 200 random tests of range 100 to 1000.

# def seq_bldr

def seq(n):
    seq_list = [0]*1001
    for i in range(1000):
        for j in range( i - 1, -1, -1):
            if (seq_list[j] == seq_list[i]):
                seq_list[i + 1] = i - j
                break
    return seq_list[n-1]

import codewars_test as test

@test.describe("Sample tests:")
def tests():
    @test.it("Small numbers")
    def _():
        s = [0, 0, 1, 0, 2, 0, 2, 2, 1, 6, 0, 5, 0, 2, 6]
        for i in range (len(s)):
            test.assert_equals(seq(i+1), s[i])