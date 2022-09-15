# Question Link: https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
def find_it(seq):
    freq = {}
    
    for i in seq:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    print(freq)
    for key,val in freq.items():
        if val % 2 != 0:
            return key

# Attempt for more elegant solution
def find_it(seq):
    for num in seq:
        if seq.count(num) % 2 != 0:
            return num


test1 = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5] # Should return 5 since it appears 3 times
test2 = [1,1,2,-2,5,2,4,4,-1,-2,5] # Should return -1 because it appears once
test3 = [10] # Should return 10