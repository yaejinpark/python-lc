# https://www.codewars.com/kata/5531abe4855bcc8d1f00004c/train/python
"""
Spares
Represented in this challenge as '/'

A spare is scored when a player knocks down all ten pins in two rolls. 
In the first 9 frames this will be scored as 10 points plus the next roll. 
So if a player were to have two frames 9/ 54, the total score of the two frames would be 24.
The first frame would be worth 15 (10 + 5) and the second frame would be worth 9 (5 + 4).

"""

def bowling_score(frames):
    scoreboard = [i for i in frames.split()]
    score = 0

    for i in range(len(scoreboard)-1):
        if scoreboard[i] != 'X' and scoreboard[i].isdigit():
            score += (int(scoreboard[i][0])+int(scoreboard[i][1]))
        elif scoreboard[i] != 'X' and '/' in scoreboard[i]:
            print('spare')
        else:
            score += 10
            
    final_index = len(scoreboard) - 1

    if scoreboard[final_index].isdigit():
        score += int(scoreboard[final_index][0]) + int(scoreboard[final_index][1])
    else:
        score += 10
        strike_count = scoreboard[final_index].count('X')
        if strike_count > 1:
            score += 100*(scoreboard[final_index].count('X')-1)
        else:
            # score += int(scoreboard[final_index][0] + scoreboard[final_index][1])
            print('spare')
    
    return score

# print(bowling_score('11 11 11 11 11 11 11 11 11 11')) # should return 20
# print(bowling_score('X X X X X X X X X XXX')) # should return 300
print(bowling_score('00 5/ 4/ 53 33 22 4/ 5/ 45 XXX')) # should return 115
print(bowling_score('5/ 4/ 3/ 2/ 1/ 0/ X 9/ 4/ 8/8')) # should return 150