# You are given a string representing a website's address. 
# To calculate the IP4 address you must convert all the 
# characters into ASCII code, then calculate the sum of the values.

# the first part of the IP number will be the result mod 256
# the second part of the IP number will be the double of the sum mod 256
# the third will be the triple of the sum mod 256
# the fourth will be the quadruple of the sum mod 256
# Input
# A string representing the website address

# Output
# An array containing the four parts of the IP value

# Examples
# "www.codewars.com"  --->  [88, 176, 8, 96]
# "www.starwiki.com"  --->  [110, 220, 74, 184]
# Restrictions
# Code length <= 59 characters
# import is forbidden as a part of anti-cheat


# def f(URL):
#     url_string = list(URL)
#     total = 0
#     for letter in url_string:
#         total += (ord(letter) - 96)

#     return [(total % 256), ((total * 2) % 256), ((total * 3) % 256), ((total * 4) % 256)]


f=lambda u:[i*sum(map(ord,u))%256for i in[1,2,3,4]]


import codewars_test as test

test.assert_equals(f('www.codewars.com'), [88, 176, 8, 96])
test.assert_equals(f('www.starwiki.com'), [110, 220, 74, 184])
test.assert_equals(f('www.winnerss.win'), [136, 16, 152, 32])