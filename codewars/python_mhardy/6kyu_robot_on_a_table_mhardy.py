# Bob has finally found a class that he's interested in -- robotics! He needs help to find out where 
# to put his robot on a table to keep it on the table for the longest.

# The size of the table is n feet by m feet (1 <= n, m <= 10000), and is labeled from 1 to n (top to bottom) 
# and from 1 to m (left to right). Directions are given to the robot as a string consisting of 'U', 'D', 'L', 
# and 'R', corresponding to up, down, left, and right respectively, and for each instruction given, the robot 
# moves one foot in the given direction. If the robot moves outside the bounds of the table, it falls off. 
# Your task is to find the coordinates at which the robot must start in order to stay on the table for the longest.

# Return your answer as a tuple. If there are multiple solutions, return the one with the smallest coordinate values.

# Example:

# robot(3, 3, "RRDLUU") => (2, 1)


# MATT'S SLOPPY AS HELL BRUTE FORCE METHOD:

# def robot(n, m, s):
   
    # num_dict = {}
    # count_dict = {}
    # for num1 in range(1, n+1):
    #     for num2 in range(1, m+1):
    #         count_dict[num1, num2] = 0

    # for x in range(1, n+1):
    #     for y in range(1, m+1):
    #         num_dict[x, y] = [x, y]
    #         for i in [*s]:
    #             if i == 'R':
    #                 if num_dict[x, y][1] < m:
    #                     num_dict[x, y][1] += 1
    #                     count_dict[x, y] += 1
    #                 else:
    #                     break                  
    #             elif i == 'L':
    #                 if num_dict[x, y][1] > 1:
    #                     num_dict[x, y][1] -= 1
    #                     count_dict[x, y] += 1
    #                 else:
    #                     break
    #             elif i == 'D':
    #                 if num_dict[x, y][0] < n:
    #                     num_dict[x, y][0] += 1
    #                     count_dict[x, y] += 1
    #                 else:
    #                     break
    #             elif i == 'U':
    #                 if num_dict[x, y][0] > 1:
    #                     num_dict[x, y][0] -= 1
    #                     count_dict[x, y] += 1
    #                 else:
    #                     break
    # # print(num_dict)
    # # print(count_dict)
    # max_value = max(count_dict, key=count_dict.get)
            
    # return max_value


# THE ABOVE SOLUTION


# SECOND ATTEMPT: REFACTORING MORE ELEGANT SOLUTION


def robot(n, m, s):
    moves = {
        'R': (0, 1),
        'D': (1, 0),
        'L': (0, -1),
        'U': (-1, 0)
    }

    x, y = 0, 0
    xmin, ymin = 0, 0
    xmax, ymax = 0, 0
    xres, yres = 0, 0
    for i in [*s]:
        a, b = moves[i]
        x, y = x+a, y+b
        xmin, ymin = min(xmin, x), min(ymin, y)
        xmax, ymax = max(xmax, x), max(ymax, y)
        if xmax - xmin >= n or ymax - ymin >= m:
            break
        xres, yres = -xmin, -ymin

    return xres+1, yres+1
    

import codewars_test as test


@test.describe("Example Test")
def tests():
    @test.it("Test 1")
    def test_1():
        test.assert_equals(robot(3, 3, "RRDLUU"), (2, 1))
    @test.it("Test 2")
    def test_2():
        test.assert_equals(robot(1, 1, "L"), (1, 1))
    @test.it("Test 3")
    def test_3():
        test.assert_equals(robot(1, 2, "L"), (1, 2))
    @test.it("Test 4")
    def test_4():
        test.assert_equals(robot(4, 3, "LUURRDDLLLUU"), (3, 2))
    @test.it("Test 5")
    def test_5():
        test.assert_equals(robot(5, 3, "URDL"), (2, 1))
    @test.it("Test 6")
    def test_6():
        test.assert_equals(robot(3, 3, "LURDRDLU"), (2, 2))