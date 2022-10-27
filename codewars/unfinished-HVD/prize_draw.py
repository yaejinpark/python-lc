def rank(st, we, n):
    # your code
    if len(st) < 1:
        return "No participants"
    else:
        names = st.split(",")
        if n > len(names):
            return "Not enough participants"
        else:
            con = {}
            for name in names:
                letters=list(name)
                for l in letters:
                    total= ord(l)-97
                som = (len(letters) + total)
                con.update(name=som)
            print(con)
            con = dict(sorted(con.items(), key = lambda x: x[1], reverse = True))
            print(con)
            numbers = list(con.values())
            winner = numbers[0]
        for name, som in con.items(): 
            if som == winner:
                 return(name)


import codewars_test as test


@test.describe("Rank")
def _():
    @test.it("Basic Tests")
    def _():
        test.assert_equals(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4), "Benjamin")
        test.assert_equals(rank("Elijah,Chloe,Elizabeth,Matthew,Natalie,Jayden", [1, 3, 5, 5, 3, 6], 2), "Matthew")
        test.assert_equals(rank("Aubrey,Olivai,Abigail,Chloe,Andrew,Elizabeth", [3, 1, 4, 4, 3, 2], 4), "Abigail")
        test.assert_equals(rank("Lagon,Lily", [1, 5], 2), "Lagon")
