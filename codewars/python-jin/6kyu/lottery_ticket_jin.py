# https://www.codewars.com/kata/57f625992f4d53c24200070e/train/python
def bingo(ticket,win):
    mini_win = 0
    for i in range(len(ticket)):
        for c in ticket[i][0]:
            if ord(c) == ticket[i][1]:
                mini_win += 1
                break
    return 'Winner!' if mini_win >= win else 'Loser!'