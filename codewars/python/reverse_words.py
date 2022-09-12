# Code Wars - Reverse words

def reverse_words(text):
	split_text = text.split(" ")
	space_counter = len(split_text) - 1
	reverse = ""

	for word in split_text:
		reverse += word[::-1]
		if space_counter > 0:
			reverse += " "
			space_counter -= 1
	return reverse

def reverse_words2(text):
	reverse = []
	for word in text.split(" "):
		reverse.append(word[::-1])
	return ' '.join(reverse)

text1 = "a b c d"
text2 = "double  spaced  words"
text3 = 'The quick brown fox jumps over the lazy dog.'
# reverse_words(text1)
reverse_words(text3)
print(reverse_words2(text3))

'''
Some things to remember:
split("") and split(" ") difference. This was the key that solved the double spaced words string.
The first totally threw out all spaces whereas the latter kept on a single space, which was needed.

' '.join() joins all elements in an array with spaces in between into a string

space_counter - 1 and space_counter -= 1 ARE NOT THE SAME
'''