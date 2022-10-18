# https://www.codewars.com/kata/5cde4e3f52910d00130dc92c/train/python

def men_still_standing(cards):
    if len(cards) == 0: return (11,11)

    card_tracker = {'AY':[],'BY':[],'AR':[],'BR':[]}
    player_tracker = {'A':[str(i) for i in range(1,12)],'B':[str(i) for i in range(1,12)]}
        
    for card in cards:
        card_col = card[-1]
        team = card[0]
        player = card[1:-1]
        if player in player_tracker[team] and card_col == 'R': # boot off red card receiver
            player_tracker[team].remove(player)
        elif card_col == 'Y' and player in card_tracker[team+card_col] and player in player_tracker[team]: # boot off player with two yellow cards
            player_tracker[team].remove(player)
        else: # keep track of player with no yellow card but receives one
            card_tracker[team+card_col].append(player)
        if len(player_tracker['A']) < 7 or len(player_tracker['B']) < 7: # end the game when there are less than 7 players and do a head count
            break
        
    return (len(player_tracker['A']),len(player_tracker['B']))