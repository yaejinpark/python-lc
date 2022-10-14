# Most football fans love it for the goals and excitement. Well, this Kata doesn't. 
# You are to handle the referee's little notebook and count the players who were sent off for fouls and misbehavior.

# The rules: Two teams, named "A" and "B" have 11 players each; players on each team are numbered from 1 to 11. 
# Any player may be sent off the field by being given a red card. A player can also receive a yellow warning card, 
# which is fine, but if he receives another yellow card, he is sent off immediately (no need for a red card in that case). 
# If one of the teams has less than 7 players remaining, the game is stopped immediately by the referee, 
# and the team with less than 7 players loses.

# A card is a string with the team's letter ('A' or 'B'), player's number, and card's color ('Y' or 'R') - 
# all concatenated and capitalized. e.g the card 'B7Y' means player #7 from team B received a yellow card.

# The task: Given a list of cards (could be empty), return the number of remaining players on each team at the 
# end of the game (as a tuple of 2 integers, team "A" first). If the game was terminated by the referee for 
# insufficient number of players, you are to stop the game immediately, and ignore any further possible cards.

# Note for the random tests: If a player that has already been sent off receives another card - ignore it.

import re

def men_still_standing(cards):
    a = 0
    b = 0
    player_dict_a = {}
    player_dict_b = {}
    if cards:
        for card in cards:
            match = re.match(r'([AB])(\d+)([YR])', card)
            team = match.groups()[0]
            player = match.groups()[1]
            card_type = match.groups()[2]
            if team == 'A':
                if card_type == 'Y':
                    if player not in player_dict_a:
                        player_dict_a[player] = 1
                    else:
                        if player_dict_a[player] == 2:
                            pass
                        else:
                            player_dict_a[player] += 1
                            a += 1
                            if a == 5:
                                return (6, 11-b)
                elif card_type == 'R':
                    if player not in player_dict_a:
                        player_dict_a[player] = 2
                        a += 1
                        if a == 5:
                            return (6, 11-b)
                    else:
                        if player_dict_a[player] == 1:
                            player_dict_a[player] += 1
                            a += 1
                            if a == 5:
                                return (6, 11-b)
                        else:
                            pass
            if team == 'B':
                if card_type == 'Y':
                    if player not in player_dict_b:
                        player_dict_b[player] = 1
                    else:
                        if player_dict_b[player] == 2:
                            pass
                        else:
                            player_dict_b[player] += 1
                            b += 1
                            if b == 5:
                                return (11-a, 6)
                elif card_type == 'R':
                    if player not in player_dict_b:
                        player_dict_b[player] = 2
                        b += 1
                        if b == 5:
                            return (11-a, 6)
                    else:
                        if player_dict_b[player] == 1:
                            player_dict_b[player] += 1
                            b += 1
                            if b == 5:
                                return (11-a, 6)
                        else:
                            pass

        return (11-a, 11-b)
    else:
        return (11, 11)


import codewars_test as test

test.assert_equals(men_still_standing([]),(11,11))
test.assert_equals(men_still_standing(["A4Y", "A4Y"]),(10,11))
test.assert_equals(men_still_standing(["A4Y", "A4R"]),(10,11))
test.assert_equals(men_still_standing(["A4Y", "A5R", "B5R", "A4Y", "B6Y"]),(9,10))
test.assert_equals(men_still_standing(["A4R", "A4R", "A4R"]),(10,11))
test.assert_equals(men_still_standing(["A4R", "A6R", "A8R", "A10R", "A11R"]),(6,11))