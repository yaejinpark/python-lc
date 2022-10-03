
def bowling_score(frames):
    
    frames += '0'
    frames= frames.split(' ')
    score=0
    x=0
    for frame in frames:
        if len(frame) <= 2: frame+= frames[x+1]
        if len(frame) <= 2: frame+= frames[x+2]
        x+=1
        if frame[0]=="X":
            score+=10
            if frame[1]=="X" or frame[2]=="/":
                score+=10
                if frame[2]=="X":
                    score+=10
                elif frame[2]!="/":score += int(frame[2])
            else: score +=int(frame[1])+int(frame[2])
        elif frame[1]=="/":
            score += 10
            if frame[2]=="X":
                score+=10
            else: score += int(frame[2])
        else: score += (int(frame[0])+int(frame[1]))
        # if frame[0] == "X":
        #     score += strike(three)
        #     else:
        #         score += no_strike(three)
        # elif x==8:
        #         three =[frame, end[0]+end[1], end[2]]
        #         x+=1
        #         if frame == "X":
        #             score += strike(three)
        #         else:
        #             score += no_strike(three)
        # elif x==9:
        #     if len(frame)!=3:
        #         score+= int(frame[0])+int(frame[1])
        #     elif frame[0]=="X":
        #         score +=10        
        #         if frame[1]=="X":
        #             score +=10
        #         else:
        #             score+
        #             if frame[3]=="X":
        #                 score +=10
            
        #         three =[frame, end[0]+end[1], end[2]]
        #         x+=1
        #         if frame[0] == "X":
        #             score += strike(three)
        #         else:
        #             score += no_strike(three)
    return score

# def strike(three):
#     score = 10
#     print(three)
#     if three[1][0]=="X":
#         score+=10
#         if three[2][0]=="X":
#             score+=10
#         else: score +=int(three[2][0])
#     elif three[1][-1]=="/":
#         score += 10
#     else: score += (int(three[1][0])+int(three[1][-1]))
#     print(score)
#     return score

# def no_strike(three):
#     rolls=[*three[0]]
#     print(three)
#     if rolls[1]=='/':
#         if three[1][0] == "X" or rolls[-1]=="X": score = 20
#         else: score = (10 + int([*three[1]][0]))
#     else:
#         score = int(rolls[0])+int(rolls[1])
#     print(score)
#     return score


import codewars_test as test

test.describe('Basic Tests')
# test.it('maybe this bowler should put bumpers on')
test.assert_equals(bowling_score('11 11 11 11 11 11 11 11 11 11'), 20)
# test.it('woah! Perfect game!')
test.assert_equals(bowling_score('X X X X X X X X X XXX'), 300)
test.assert_equals(bowling_score('00 00 00 00 00 00 00 00 X 0/X'), 40)
test.assert_equals(bowling_score('5/ 4/ 3/ 2/ 1/ 0/ X 9/ 4/ 7/2'), 143)
test.assert_equals(bowling_score('52 X 21 90 52 60 71 70 0/ XX1'), 101)