# https://www.codewars.com/kata/554910d77a3582bbe300009c/train/python
from collections import Counter

def get_winner(ballots):
    poll = Counter(ballots).most_common(1)[0]
    return poll[0] if poll[1] > len(ballots)/2 else None