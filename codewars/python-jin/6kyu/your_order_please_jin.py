# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python
def order(sentence):
    # code here
    if len(sentence) == 0 : return ""
    str_list = [i for i in sentence.split(" ")]
    str_list_sorted = []
    
    for j in range(1,10):
        for substr in str_list:
            if str(j) in substr:
                str_list_sorted.append(substr)
    return " ".join(str_list_sorted)

# I love this solution from another person
def extract_number(word):
    for l in word: 
        if l.isdigit(): return int(l)
    return None

def order(sentence):
    return ' '.join(sorted(sentence.split(), key=extract_number))