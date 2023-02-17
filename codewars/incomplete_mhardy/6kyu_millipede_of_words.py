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


def solution(words):
    # create a dictionary to store the words that can be joined
    join_dict = {}
    for word in words:
        # add the word to the dictionary with its last letter as the key
        join_dict[word[-1]] = join_dict.get(word[-1], []) + [word]
    # create a list to store the millipede of words
    millipede_list = []
    # start with any word as the first word in the millipede
    start_word = words[0]
    millipede_list.append(start_word)
    # keep adding words to the millipede until all words have been used
    while len(words) > 0:
        # get the last letter of the current word in the millipede
        last_letter = millipede_list[-1][-1]
        # find a word in the list that starts with the last letter
        if last_letter in join_dict and len(join_dict[last_letter]) > 0:
            next_word = join_dict[last_letter].pop()
            millipede_list.append(next_word)
            words.remove(next_word)
        else:
            # if there are no words that start with the last letter, try rearranging the remaining words
            for i in range(1, len(words)):
                if words[i][0] == last_letter:
                    words[0], words[i] = words[i], words[0]
                    start_word = words[0]
                    millipede_list.append(start_word)
                    words.remove(start_word)
                    break
            else:
                # if no rearrangement works, the words cannot be joined
                return False
    # if all words have been used, return the millipede of words
    return True
    



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
        
        