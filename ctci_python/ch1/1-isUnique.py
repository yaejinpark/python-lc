"""
Ask the interviewer... 
1. if spaces count as characters
2. if this is "case sensitive (do lowercases and uppercases count differently)"

"""

def isUnique(input_str):
	input_str = input_str.lower()

	return len(input_str) == len(set(input_str))

test_str1 = "abcdef"
test_str2 = "aaabbb"
test_str3 = "abc de f"

print(isUnique(test_str1))
print(isUnique(test_str2))
print(isUnique(test_str3))