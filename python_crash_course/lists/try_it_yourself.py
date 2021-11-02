from os import PRIO_USER


for values in range(1,21):
    print(values)

#one million
one_million = []

for i in range(1000001):
    one_million.append(i)

print(one_million)

# summing a million
print(min(one_million))
print(max(one_million))
print(sum(one_million))


# odd numbers

odd_numbers = []

for i in range(1, 21, 2):
    odd_numbers.append(i)

print(odd_numbers)

# multiple of thress 
multiple_threes = []

for value in range(3, 31, 3):
    multiple_threes.append(value)

print(multiple_threes)


# find the cubes 

cubes = []

for i in range(1,11):
    cube = i ** 3
    cubes.append(cube)
print(cubes)


# generate a list of cubes using list comprehension 

cubes = [i ** 3 for i in range(1,11)]

print(cubes)