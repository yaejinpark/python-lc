# Given a lottery ticket (ticket), represented by an array of 2-value arrays, 
# you must find out if you've won the jackpot.

# Example ticket:

# [ [ 'ABC', 65 ], [ 'HGR', 74 ], [ 'BYHT', 74 ] ]
# To do this, you must first count the 'mini-wins' on your ticket. 
# Each subarray has both a string and a number within it. 
# If the character code of any of the characters in the string matches the number,
# you get a mini win. Note you can only have one mini win per sub array.

# Once you have counted all of your mini wins, compare that number to the other input 
# provided (win). If your total is more than or equal to (win), return 'Winner!'. Else return 'Loser!'.

# All inputs will be in the correct format. Strings on tickets are not always the same length.

def bingo(ticket,win):
    wins = 0
    for i in ticket:
        for y in list(i[0]):
            if ord(y) == i[1]:
                wins += 1
                break
    if wins >= win:
        return 'Winner!'
    else:
        return 'Loser!'

# from solution import bingo
import codewars_test as test


@test.it("Basic tests")
def _():
    test.assert_equals(bingo([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 2), 'Loser!')
    test.assert_equals(bingo([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 1), 'Winner!')
    test.assert_equals(bingo([['HGTYRE', 74], ['BE', 66], ['JKTY', 74]], 3), 'Loser!')
