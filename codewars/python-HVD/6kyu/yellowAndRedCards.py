def men_still_standing(cards):

    A= list(range(1,12))
    B= list(range(1,12))

    for card in cards:
        team=eval(card[0])
        pos=(int(card[1:-1])-1)
        player=team[pos]
        if player == "Y":team[pos]="R"
        elif player == "R": continue
        else:      
            team[pos]=card[-1]
        if A.count("R")>4 or B.count("R")>4: return ((len(A)-A.count("R")),(len(B)-B.count("R")))

    return ((len(A)-A.count("R")),(len(B)-B.count("R")))

import codewars_test as test    

# test.assert_equals(men_still_standing([]),(11,11))
test.assert_equals(men_still_standing(["A4Y", "A4Y"]),(10,11))
test.assert_equals(men_still_standing(["A4Y", "A4R"]),(10,11))
test.assert_equals(men_still_standing(["A4Y", "A5R", "B5R", "A4Y", "B6Y"]),(9,10))
test.assert_equals(men_still_standing(["A4R", "A4R", "A4R"]),(10,11))
test.assert_equals(men_still_standing(["A4R", "A6R", "A8R", "A10R", "A11R"]),(6,11))
test.assert_equals(men_still_standing(['B4Y', 'B7Y', 'B2Y', 'B10R', 'B6R', 'A9Y', 'B10Y', 'B1Y', 'A7R', 'B2Y', 'B5Y', 'A6Y', 'B11R', 'A4R', 'A3R', 'A4R', 'B3R', 'B5Y', 'B3Y', 'B11Y', 'A10Y', 'B7Y', 'B2R', 'A5Y']),(8,6))