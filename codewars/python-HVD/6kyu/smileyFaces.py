def count_smileys(arr):
    smile = [')','D']
    count =0
    for face in arr:
        if face [-1:] in smile:
             count += 1

    return count




import codewars_test as test


test.describe("Basic tests")
test.assert_equals(count_smileys([]), 0)
test.assert_equals(count_smileys([':D',':~)',';~D',':)']), 4)
test.assert_equals(count_smileys([':)',':(',':D',':O',':;']), 2)
test.assert_equals(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)