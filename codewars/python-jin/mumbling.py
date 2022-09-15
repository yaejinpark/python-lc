"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.

"""

def accum(s):
	return "-".join("%s%s"%(char.upper(),char.lower()*(ind))for ind, char in enumerate(list(s)))

# Much cleaner version - I don't have to convert string to a list... just need to enumerate
def accum2(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

print(accum("abcd"))
print(accum("RqaEzty"))
print(accum("cwAt"))