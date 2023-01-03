# A collatz sequence, starting with a positive integer, is found 
# by repeatedly applying the following function to n until n == 1 :
def collatz(number):
    def even_number(num):
        result = num // 2
        return result

    def odd_number(num):
        result = (3 * num) + 1
        return result

    numbers = []

    def seq_builder(n):
        if n == 1:
            return "1"
        elif n % 2 == 0:
            result = even_number(n)
            numbers.append(result)
            seq_builder(result)
        else:
            result = odd_number(n)
            numbers.append(result)
            seq_builder(result)
        return numbers

    def final_string(n):
        if n == 1:
            return '1'
        return f'{str(n)}->' + '->'.join(str(n) for n in seq_builder(n))

    return final_string(number)


import codewars_test as test


@test.describe("Basics test")
def test_basics():
    @test.it("should return the correct sequence")
    def test_collatz():
        test.assert_equals(collatz(1), "1");
        test.assert_equals(collatz(2), "2->1")
        test.assert_equals(collatz(3), "3->10->5->16->8->4->2->1")
        test.assert_equals(collatz(4), "4->2->1")
        test.assert_equals(
            collatz(27), 
            "27->82->41->124->62->31->94->47->142->71->214->107->322->161->484->242->121->364->182->91->274->137->412->206->103->"
            "310->155->466->233->700->350->175->526->263->790->395->1186->593->1780->890->445->1336->668->334->167->502->251->"
            "754->377->1132->566->283->850->425->1276->638->319->958->479->1438->719->2158->1079->3238->1619->4858->2429->7288->"
            "3644->1822->911->2734->1367->4102->2051->6154->3077->9232->4616->2308->1154->577->1732->866->433->1300->650->325->"
            "976->488->244->122->61->184->92->46->23->70->35->106->53->160->80->40->20->10->5->16->8->4->2->1"
        )