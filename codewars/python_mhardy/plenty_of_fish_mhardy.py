# Fish are an integral part of any ecosystem. Unfortunately, fish are often seen as high maintenance. 
# Contrary to popular belief, fish actually reduce pond maintenance as they graze on string algae and 
# bottom feed from the pond floor. They also make very enjoyable pets, providing hours of natural entertainment.

# In this Kata you are fish in a pond that needs to survive by eating other fish. You can only eat fish that are the same size or smaller than yourself. 
# You must create a function called fish that takes a shoal of fish as an input string. From this you must work out how many fish 
# you can eat and ultimately the size you will grow to.

# Rules
# 1.  Your size starts at 1

# 2.  The shoal string will contain fish integers between 0-9

# 3.  0 = algae and wont help you feed.

# 4.  The fish integer represents the size of the fish (1-9).

# 5.  You can only eat fish the same size or less than yourself.

# 6.  You can eat the fish in any order you choose to maximize your size.

# 7   You can and only eat each fish once.

# 8.  The bigger fish you eat, the faster you grow. A size 2 fish equals two size 1 fish, size 3 fish equals three size 1 fish, and so on.

# 9.  Your size increments by one each time you reach the amounts below.

def fish(shoal):
    size_list = [*shoal]
    current_size = 1
    fish_eaten = 0
    for i in sorted(size_list):
        if i == 0:
            continue
        elif int(i) <= current_size:
            fish_eaten += int(i)
            if fish_eaten >= (current_size*4):
                fish_eaten = fish_eaten % current_size
                current_size += 1
        else:
            continue
    return current_size

import codewars_test as test

@test.describe('Example Tests')

def example_tests():
    @test.it("Should return 1")
    def example_test_case1():
        test.assert_equals(fish(""), 1, "Should return '1'")

    @test.it("Should return 1")
    def example_test_case2():
        test.assert_equals(fish("0"), 1, "Should return '1'")

    @test.it("Should return 1")
    def example_test_case3():
        test.assert_equals(fish("6"), 1, "Should return '1'")

    @test.it("Should return 2")
    def example_test_case4():
        test.assert_equals(fish("1111"), 2, "Should return '2'")

    @test.it("Should return 3")
    def example_test_case5():
        test.assert_equals(fish("11112222"), 3, "Should return '3'")

    @test.it("Should return 4")
    def example_test_case6():
        test.assert_equals(fish("111122223333"), 4, "Should return '4'")

    @test.it("Should return 3")
    def example_test_case7():
        test.assert_equals(fish("111111111111"), 3, "Should return '3'")

    @test.it("Should return 5")
    def example_test_case8():
        test.assert_equals(fish("111111111111111111112222222222"), 5, "Should return '5'")

    @test.it("Should return 5")
    def example_test_case9():
        test.assert_equals(fish("151128241212192113722321331"), 5, "Should return '5'")