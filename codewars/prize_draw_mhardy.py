# To participate in a prize draw each one gives his/her firstname.

# Each letter of a firstname has a value which is its rank in the English alphabet. 
# A and a have rank 1, B and b rank 2 and so on.

# The length of the firstname is added to the sum of these ranks hence a number som.

# An array of random weights is linked to the firstnames and each som is multiplied by 
# its corresponding weight to get what they call a winning number.

def winning_number(name):
    values = []
    for i in list(name):
        values.append(ord(i.lower())-96)
    return (int(len(name)) + sum(values))

def rank(st, we, n):
    if len(st) == 0:
        return "No participants"
    if n > len(st.split(",")):
        return "Not enough participants"
    score_dict = {}
    split_list = [x for x in st.split(",")]
    for i in range(len(split_list)):
        score = int(winning_number(split_list[i])) * we[i]
        score_dict.update({split_list[i]:(score)})
    # score_dict = dict(sorted(score_dict.items(), key = lambda x: x[1], reverse = True))
    score_dict = {val[0] : val[1] for val in sorted(score_dict.items(), key = lambda x: (-x[1], x[0]))}
    name_list = list(score_dict.keys())
    return str(name_list[n-1])


import codewars_test as test


@test.describe("Rank")
def _():
    @test.it("Basic Tests")
    def _():
        test.assert_equals(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4), "Benjamin")
        test.assert_equals(rank("Elijah,Chloe,Elizabeth,Matthew,Natalie,Jayden", [1, 3, 5, 5, 3, 6], 2), "Matthew")
        test.assert_equals(rank("Aubrey,Olivai,Abigail,Chloe,Andrew,Elizabeth", [3, 1, 4, 4, 3, 2], 4), "Abigail")
        test.assert_equals(rank("Lagon,Lily", [1, 5], 2), "Lagon")