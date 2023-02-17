# An infinite number of shelves are arranged one above the other in a staggered fashion.
# The cat can jump either one or three shelves at a time: from shelf i to shelf i+1 or i+3 
# (the cat cannot climb on the shelf directly above its head), according to the illustration:

#                  ┌────────┐
#                  │-6------│
#                  └────────┘
# ┌────────┐       
# │------5-│        
# └────────┘  ┌─────► OK!
#             │    ┌────────┐
#             │    │-4------│
#             │    └────────┘
# ┌────────┐  │
# │------3-│  │     
# BANG!────┘  ├─────► OK! 
#   ▲  |\_/|  │    ┌────────┐
#   │ ("^-^)  │    │-2------│
#   │ )   (   │    └────────┘
# ┌─┴─┴───┴┬──┘
# │------1-│
# └────────┘
# Input
# Start and finish shelf numbers (always positive integers, finish no smaller than start)

# Task
# Find the minimum number of jumps to go from start to finish

# Example
# Start 1, finish 5, then answer is 2 (1 => 4 => 5 or 1 => 2 => 5)

def solution(start, finish):  
    return ((finish-start)//3)+((finish-start)%3)


import codewars_test as test

@test.describe("Cats")
def test_group():
    @test.it("Example test case")
    def test_case():
        test.assert_equals(solution(1,5), 2)
    @test.it("One more test case")
    def test_case():
        test.assert_equals(solution(2,4), 2)