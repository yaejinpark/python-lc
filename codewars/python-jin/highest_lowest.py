# Code Wars - Highest and Lowest

def high_and_low(numbers):
	numbers_list = list(map(int,numbers.split(" ")))
	return " ".join(map(str,[max(numbers_list),min(numbers_list)]))

def high_and_low2(numbers):
	numbers_list = [int(x) for x in numbers.split(" ")]
	return "{} {}".format(max(numbers_list),min(numbers_list)) 

numbers1 = "8 3 -5 42 -1 0 0 -9 4 7 4 -4"
numbers2 = "1 2 3"

# print(high_and_low(numbers1))
# print(high_and_low(numbers2))
# print(high_and_low2(numbers1))
# print(high_and_low2(numbers2))

