for values in range(1, 5):
    print(values)

for numbers in range(8):
    print(numbers)

number = list(range(10))
print(number)

numbers = tuple(range(10))

print(numbers)

even_numebrs = list(range(2, 11 , 2))
print(even_numebrs)


squares = []

for value in range(2, 11, 2):
    square = value ** 2
    squares.append(square)
print(squares)


odd_squares = []

for value in range(1, 11, 2):
    odd_square = value ** 2
    odd_squares.append(odd_square)

print(odd_squares)


square_numbers = []

for i in range(1,11):
    square_numbers.append(i ** 2)

print(square_numbers)