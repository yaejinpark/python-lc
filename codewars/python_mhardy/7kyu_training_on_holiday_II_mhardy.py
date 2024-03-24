# Finding your seat on a plane is never fun, particularly for a long haul flight... 
# You arrive, realise again just how little leg room you get, and sort of climb 
# into the seat covered in a pile of your own stuff.

# To help confuse matters (although they claim in an effort to do the opposite) 
# many airlines omit the letters 'I' and 'J' from their seat naming system.

# the naming system consists of a number (in this case between 1-60) that denotes 
# the section of the plane where the seat is (1-20 = front, 21-40 = middle, 40+ = back). 
# This number is followed by a letter, A-K with the exclusions mentioned above.

# Letters A-C denote seats on the left cluster, D-F the middle and G-K the right.

# Given a seat number, your task is to return the seat location in the following format:

# '2B' would return 'Front-Left'.

# If the number is over 60, or the letter is not valid, return 'No Seat!!'.

def plane_seat(a):
    row, seat = int(a[:-1]), ord(a[-1])-64
    res = ""
    if row not in range(1, 61) or seat not in range(1, 12) or a[-1] in "IJ":
        return "No Seat!!"
    if row in range(1,21):
        res += "Front"
    elif row in range(21, 41):
        res += "Middle"
    else:
        res += "Back"
        
    if seat in range(1, 4):
        res += "-Left"
    elif seat in range(4, 7):
        res += "-Middle"
    else:
        res += "-Right"
        
    return res


import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(plane_seat('2B'), 'Front-Left')
        test.assert_equals(plane_seat('20B'), 'Front-Left')
        test.assert_equals(plane_seat('58I'), 'No Seat!!')
        test.assert_equals(plane_seat('60D'), 'Back-Middle')
        test.assert_equals(plane_seat('17K'), 'Front-Right')