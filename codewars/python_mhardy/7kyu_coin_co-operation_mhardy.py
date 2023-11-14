# Let's say that there exists a machine that gives out free coins, but with a twist!

# Separating two people is a wall, and this machine is placed in 
# such a way that both people are able to access it. Spending a coin in 
# this machine will give the person on the other side 3 coins and vice versa.

# If both people continually spend coins for each other (SHARING), then they'll 
# both gain a net profit of 2 coins per turn. However, there is always the possibility 
# for someone to act selfishly (STEALING): they spend no coins, yet they still receive 
# the generous 3 coin gift from the other person!

# Here's an example of Red taking advantage of Green!Red chose to betray

# The Challenge
# Assuming that both people start with 3 coins each, create a function that calculates 
# both people's final number of coins. You will be given two arrays of strings, 
# with each string being the words "share" or "steal".

# Examples
# ["share"], ["share"] ➞ (5, 5)
# // Both people spend one coin, and receive 3 coins each.

# ["steal"], ["share"] ➞ (6, 2)
# // Person 1 gains 3 coins, while person 2 loses a coin.

# ["steal"], ["steal"] ➞ (3, 3)
# // Neither person spends any coins and so no one gets rewarded.

# ["share", "share", "share"], ["steal", "share", "steal"] ➞ (3, 11)
# Notes
# No tests will include a negative number of coins.
# All words will be given in lowercase.

def get_coin_balances(lst1, lst2):
    total1, total2 = 3, 3
    for i in range(len(lst1)):
        if lst1[i] == 'steal':
            if lst2[i] == 'share':
                total1+=3
                total2-=1
        elif lst1[i] == 'share':
            if lst2[i] == 'share':
                total1+=2
                total2+=2
            else:
                total1-=1
                total2+=3
    return (total1, total2)

import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(get_coin_balances(['share'], ['share']), (5, 5))
        test.assert_equals(get_coin_balances(['steal'], ['share']), (6, 2))
        test.assert_equals(get_coin_balances(['share'], ['steal']), (2, 6))
        test.assert_equals(get_coin_balances(['steal'], ['steal']), (3, 3))
        test.assert_equals(get_coin_balances(['share', 'share', 'share'], ['steal', 'share', 'steal']), (3, 11))
        test.assert_equals(get_coin_balances(['share', 'share', 'steal', 'share'], ['steal', 'steal', 'steal', 'steal']), (0, 12))
        test.assert_equals(get_coin_balances(['steal', 'steal', 'steal'], ['share', 'share', 'share']), (12, 0))
        test.assert_equals(get_coin_balances(['share', 'share'], ['share', 'share']), (7, 7))
        test.assert_equals(get_coin_balances(['share', 'steal', 'steal', 'steal'], ['share', 'share', 'steal', 'share']), (11, 3))
        test.assert_equals(get_coin_balances(['share', 'share', 'steal', 'share'], ['steal', 'share', 'steal', 'steal']), (3, 11))
        test.assert_equals(get_coin_balances(['steal', 'steal', 'steal', 'steal'], ['steal', 'steal', 'steal', 'steal']), (3, 3))
        test.assert_equals(get_coin_balances(['steal', 'share', 'steal', 'steal'], ['share', 'share', 'steal', 'steal']), (8, 4))
        test.assert_equals(get_coin_balances(['steal', 'steal'], ['share', 'share']), (9, 1))
        test.assert_equals(get_coin_balances(['steal', 'share'], ['share', 'steal']), (5, 5))