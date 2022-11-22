# The set of words is given. Words are joined if the last letter of one word 
# and the first letter of another word are the same. Return true if all words 
# of the set can be combined into one word, or return false.

# Input
# List of 3 to 7 words of random length. There are no capital letters. Words in list may be repeated.

# Example true
# Set: excavate, endure, desire, screen, theater, excess, night.
# Millipede: desirE EndurE ExcavatE ExcesS ScreeN NighT Theater.

# Example false
# Set: trade, pole, view, grave, ladder, mushroom, president.
# Millipede: presidenT Trade.

# def solution(arr):
#     counter = 1
#     i = 0
    
#     while i < len(arr) - 1:
#         word, next_word = arr[i], arr[i+1]
#         print(word, next_word)
#         if word[-1] == next_word[0]:
#             counter += 1
#         i+=1

#     if counter == len(arr) + 1:
#         return True
#     else:
#         return False

# def unique(mtch_lst):
#     unique_list = []

#     for x in mtch_lst:
#         if x not in 
import itertools
from itertools import permutations

# def solution(arr):
#     match_list = []
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if arr[i][-1] == arr[j][0]:
#                 if arr[i] not in match_list:
#                     match_list.append(arr[i])
#                 if arr[j] not in match_list:
#                     match_list.append(arr[j])
#     return len(match_list) + 1 == len(arr)

def solution(arr):
    matches = []
    combos = list(permutations(arr, 2))
    for i, j in zip(arr, arr[1:]):
        if i[-1]==j[0]:
            matches.append(i)
    # combos = list(itertools.product(arr, repeat=len(arr)))
    # for i in combos:

    #     # print(i[1][0])
    #     if i[0][-1] == i[1][0]:
    #         matches.append((i[0], i[1]))
    print(arr)
    print(list(combos))
    print(matches)
    
    # match_dict = {}
    # for i in matches:
    #     if i[0] not in match_dict.keys() or i[1] not in match_dict.keys():
    #         match_dict[i[0]] = 1
    #         match_dict[i[1]] = 1
    #     elif i[0] in match_dict.keys():
    #         match_dict[i[0]] += 1
        
    print(match_dict)
    return sorted(arr) == sorted(match_dict.keys())


    



import codewars_test as test
# from solution import solution

@test.describe("Test case in description")
def test_group():
    @test.it("Example true")
    def test_case():
        test.assert_equals(solution(["excavate", "endure", "screen", "desire", "theater", "excess", "night"]), True)
    @test.it("Example false")
    def test_case():
        test.assert_equals(solution(["trade", "pole", "view", "grave", "ladder", "mushroom", "president"]), False)
        
        