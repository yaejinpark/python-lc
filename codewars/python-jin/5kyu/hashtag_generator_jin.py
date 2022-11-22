# https://www.codewars.com/kata/52449b062fb80683ec000024/train/python
def generate_hashtag(s):
    word = ''.join([c.capitalize() for c in s.strip().split(' ')])
    return '#' + word if s and len(word) <= 140 else False

# ... Or I can be an asshole and do this
def generate_hashtag(s):
    return '#' + ''.join([c.capitalize() for c in s.strip().split(' ')]) if s and len(s) <= 140 else False