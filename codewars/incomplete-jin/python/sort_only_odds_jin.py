# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python
def sort_array(source_array):
    odds = [n for n in source_array if n%2 != 0]
    odds_index = [source_array.index(n) for n in source_array if n%2 != 0]
    odds_data = dict(list(zip(sorted(odds),sorted(odds_index))))
    res = [0] * len(source_array) # initialize final array with same size as given array

    print(odds_data)
    
    return source_array

print(sort_array([5, 3, 2, 8, 1, 4]))
# print(sort_array([5, 3, 1, 8, 0]))