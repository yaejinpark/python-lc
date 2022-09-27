# Ten-Pin Bowling
# In the game of ten-pin bowling, a player rolls a bowling ball down a lane to knock over pins.
#  There are ten pins set at the end of the bowling lane. Each player has 10 frames to roll a 
#  bowling ball down a lane and knock over as many pins as possible. The first nine frames are ended 
#  after two rolls or when the player knocks down all the pins. The last frame a player will receive 
#  an extra roll every time they knock down all ten pins; up to a maximum of three total rolls.

# The Challenge
# In this challenge you will be given a string representing a player's ten frames. It will look 
# something like this: 'X X 9/ 80 X X 90 8/ 7/ 44' (in Java: "X X 9/ 80 X X 90 8/ 7/ 44"), where each 
# frame is space-delimited, 'X' represents strikes, and '/' represents spares. Your goal is take in 
# this string of frames into a function called bowlingScore and return the players total score.

# Scoring
# The scoring for ten-pin bowling can be difficult to understand, and if you're like most people, 
# easily forgotten if you don't play often. Here is a quick breakdown:

# Frames
# In Ten-Pin Bowling there are ten frames per game. Frames are the players turn to bowl, which can be multiple rolls. 
# The first 9 frames you get 2 rolls maximum to try to get all 10 pins down. On the 10th or last frame a player will 
# receive an extra roll each time they get all ten pins down to a maximum of three total rolls. 
# Also on the last frame bonuses are not awarded for strikes and spares moving forward.

# In this challenge, three frames might be represented like this: 54 72 44. In this case, the player has had three frames. 
# On their first frame they scored 9 points (5 + 4), on their second frame they scored 9 points (7 + 2) and on their third 
# frame they scored 8 points (4 + 4). This is a very simple example of bowling scoring. It gets more complicated when we 
# introduce strikes and spares.

# Strikes
# Represented in this challenge as 'X'

# A strike is scored when a player knocks all ten pins down in one roll. In the first 9 frames this will 
# conclude the players turn and it will be scored as 10 points plus the points received from the next two rolls. 
# So if a player were to have two frames X 54, the total score of those two frames would be 28. The first frame 
# would be worth 19 (10 + 5 + 4) and the second frame would be worth 9 (5 + 4).

# A perfect game in bowling is 12 strikes in a row and would be represented like this 'X X X X X X X X X XXX' 
# (in Java: "X X X X X X X X X XXX"). This adds up to a total score of 300.

# Spares
# Represented in this challenge as '/'

# A spare is scored when a player knocks down all ten pins in two rolls. In the first 9 frames this will be scored 
# as 10 points plus the next roll. So if a player were to have two frames 9/ 54, the total score of the two frames 
# would be 24. The first frame would be worth 15 (10 + 5) and the second frame would be worth 9 (5 + 4).

def bowling_score(frames):
    total = 0
    frames = []
    for frame in frames.split(' '):
        for roll in range(len(frame)+1):
            turn = 0
            if type(frame[roll]) == int:
                frame.append(roll)
            elif frame[roll] == 'X':
                frames.append(10)
                turn += 1
            elif roll == '/':
                frames.append

            score = int(roll)

def bowling_score(frames):
    total = 0
    frames = []
    turn = 0
    for frame in frames.split(' '):
        for roll in frame:
            if roll == 'X':
                

            score = int(roll)




import codewars_test as test

test.describe('Basic Tests')
test.it('maybe this bowler should put bumpers on')
test.assert_equals(bowling_score('11 11 11 11 11 11 11 11 11 11'), 20)
test.it('woah! Perfect game!')
test.assert_equals(bowling_score('X X X X X X X X X XXX'), 300)