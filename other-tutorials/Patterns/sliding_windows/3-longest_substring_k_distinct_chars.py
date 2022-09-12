"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.

You can assume that K is less than or equal to the length of the given string.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
"""

# My Attempt 1
def longest_substring(str,k):
	dist_chr_count = 1
	i = 0
	str_start = 0
	max_len = -1

	while i < len(str):
		if str[str_start] != str[i]:
			dist_chr_count += 1
			print(f"distinct letters. str_start:{str_start}, str[i]:{str[i]}")
		else:
			print(f"same consecutive letters. str_start:{str_start}, str[i]:{str[i]}")
		while dist_chr_count > k:
			print(f"consecutive string so far: {str[str_start:i-1]}")
			max_len = max(max_len, len(str[str_start:i-1]))
			print(f"max_len:{max_len}")
			# print(str[str_start:max_len])
			str_start += 1
			dist_chr_count = 0
		i+=1
	return max_len

# Well that didn't work.

# My Attempt 2 - Hint: Use HashMap

def longest_substring2(str,k):
	char_freq = {}
	max_len = 0
	window_start = 0

	for window_end in range(len(str)):
		window_right = str[window_end]

		if window_right not in char_freq:
			char_freq[window_right] = 0
		char_freq[window_right] += 1

		while len(char_freq) > k:
			max_len = max(max_len, sum(char_freq.values()))
			char_freq[str[window_start]] -= 1
			window_start += 1

	return max_len


test_str1 = "araaci"
test_str2 = "cbbebi"

print(longest_substring2(test_str1,2)) # Should return 4
# print(longest_substring(test_str1,1)) # Should return 2
# print(longest_substring(test_str2,3)) # Should return 5
