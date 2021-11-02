# building list comprehensions

from typing import Sequence


squares = [i ** 2 for i in range(1,11)]

print(squares)

odd_squares = [value ** 2 for value in range(1, 11, 2)]
print(odd_squares)

