def fish(shoal): 
    total=0
    size=1
    pond= sorted([*shoal])
    if len(pond) == 0:
        return size
    else:
        for fish in pond:
            if int(fish) <= size:
                total += int(fish)
                if total >= (size*4):
                    total = total-(size*4)
                    size+=1
                    
        else:
            return size


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