# https://www.codewars.com/kata/584e93a70f60247eb8000132/train/python
def perfect_square(square):
    parsed = square.split('\n')
    return all('.'*len(parsed) == i for i in parsed)