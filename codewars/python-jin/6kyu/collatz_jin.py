# https://www.codewars.com/kata/5286b2e162056fd0cb000c20/train/
# Preface
# A collatz sequence, starting with a positive integern, is found by repeatedly applying the following function to n until n == 1 :

# f(n)={n/2, if n is even3n+1, if n is oddf(n) = \begin{cases} n/2, \text{ if $n$ is even} \\ 3n+1, \text{ if $n$ is odd} \end{cases}f(n)={ 
# n/2, if n is even
# 3n+1, if n is odd
# ​
 

# A more detailed description of the collatz conjecture may be found on Wikipedia.

# The Problem
# Create a function collatz that returns a collatz sequence string starting with the positive integer argument passed into the function, in the following form:

# "X0->X1->...->XN"

# Where Xi is each iteration of the sequence and N is the length of the sequence.

# Sample Input
# Input: 4
# Output: "4->2->1"

# Input: 3
# Output: "3->10->5->16->8->4->2->1"
# Don't worry about invalid input. Arguments passed into the function are guaranteed to be valid integers >= 1.

def seq_builder(n):
    while n > 1:
        yield n
        if n%2 == 0:
            n = n//2
        else:
            n = 3*n + 1
        seq_builder(n)
    yield 1

def collatz(n):
    return '->'.join(str(n) for n in seq_builder(n))

print(collatz(4))
print(collatz(3))