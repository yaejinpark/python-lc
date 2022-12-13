# The 'water pouring' problem (a.k.a 'two water jug' problem, or the even cooler 
# 'Die Hard with a vengeance' puzzle) is a puzzle involving a finite number of 
# water jugs with integer capacities (in this case, measured in litres). 
# For this problem, we are using only two jugs. Initially, each jug is empty. 
# We want to find a series of 'steps' to reach a state where one of the two 
# jugs contain the desired quantity of water.

# Inputs:
# Volume of the first jug, a
# Volume of the second jug, b (a<=b)
# The desired quantity of water, n
# Range of possible inputs 0<a,b,n<=100000
# Outputs:
# A list of tuples, with the state of the two jugs after every step starting from the first step. 
# This need not be the 'path' with the minimum number of steps, but it will surely help for some random performance tests
# Valid 'Steps':
# Emptying one jug and doing nothing with the other
# Filling one jug and doing nothing with the other
# Emptying one jug into the other
# Using one jug to fill the other (refer to steps 2 and 6 in the example)
# In short, a valid step consists of pouring water from a source container (either of the 
# two jugs or from the infinite source of water) to a destination (either of the two jugs or poured 
# outside) until either the source container is empty or the destination container is full.

# Example:
# If a=3, b=5, n=4, the steps could be:

# Start from (0,0)

# Fill the second jug (0,5) (Note that the first step is the first step with either of the jugs filled)
# Empty 3 litres from second jug to first jug (3,2)
# Empty first jug (0,2)
# Empty 2 litres from second jug to first jug (2,0)
# Fill second jug (2,5)
# Empty 1 litre from second jug to first jug (3,4). We've reached a state where one of the jugs contains the desired quantity of water n=4.
# (The next step of emptying the first jug is redundant, but having the last step as (0,4) does not amount to a wrong answer)

# (0,0)->(0,5)->(3,2)->(0,2)->(2,0)->(2,5)->(3,4)

# The function can return

# [(0,5), (3,2), (0,2), (2,0), (2,5), (3,4)]
# Note:
# Assume that you have an infinite supply of water to use.
# Both jugs start out empty, you can choose to fill either of them.
# If the goal cannot be reached in one jug alone return an empty list [].
# All inputs will be > 0


def wpp(a, b, n):
    
    pass



