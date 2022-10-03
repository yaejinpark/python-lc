def stock_list(books, cat):
    if len(books) == 0 or len(cat) == 0:
        return ""
    stock = {}
    for i in cat:
        stock[i]= 0
    for book in books:
        x = book.split()
        c = x[0][0]
        if c in cat:
            stock[c]=stock[c]+int(x[1])
            print(stock)
    summary = [f"({k} : {v})" for k,v in stock.items()]
    output = " - ".join(summary)
    return output



import codewars_test as test

@test.describe("Testing")
def _():
    @test.it("Tests")
    def _():
        b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
        c = ["A", "B", "C", "D"]
        test.assert_equals(stock_list(b, c), "(A : 0) - (B : 1290) - (C : 515) - (D : 600)")

        b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
        c = ["A", "B"]
        test.assert_equals(stock_list(b, c), "(A : 200) - (B : 1140)")