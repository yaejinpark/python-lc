# https://www.codewars.com/kata/5286b2e162056fd0cb000c20/train/python
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