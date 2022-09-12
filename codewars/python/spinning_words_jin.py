# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python
def spin_words(sentence):
    # Your code goes here
    words = [i for i in sentence.split(" ")]
    return " ".join(words[j][::-1] if len(words[j]) >= 5 else words[j] for j in range(len(words)))