""" 
Ask the interviewer...

1. If input strings are given in a specific order (shorter first? longer first?)

"""

def permu(string1,string2):
	shorter,longer = "",""
	if len(string1) > len(string2):
		shorter = string2
		longer = string1
	elif len(string2) > len(string1):
		shorter = string1
		longer = string2
	else:
		shorter = string1
		longer = string2

	return shorter in longer

test_str1 = "abc"
test_str2 = "abcdef"
test_str3 = "abdefdc"
test_str4 = "ab"

print(permu(test_str1,test_str2))
print(permu(test_str1,test_str4))
print(permu(test_str1,test_str3))