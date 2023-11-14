# Input:

# a string strng
# an array of strings arr
# Output of function contain_all_rots(strng, arr) 
# (or containAllRots or contain-all-rots):

# a boolean true if all rotations of strng are included in arr
# false otherwise
# Examples:
# contain_all_rots(
#   "bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]) -> true

# contain_all_rots(
#   "Ajylvpy", ["Ajylvpy", "ylvpyAj", "jylvpyA", "lvpyAjy", "pyAjylv", "vpyAjyl", "ipywee"]) -> false)
# Note:
# Though not correct in a mathematical sense

# we will consider that there are no rotations of strng == ""
# and for any array arr: contain_all_rots("", arr) --> true


def contain_all_rots(strng, arr):
    res_lst = []
    for i in range(len(strng)):
        word = strng[-i:]+strng[:-i]
        res_lst.append(word)
    return set(res_lst).issubset(arr)



import codewars_test as test

def testing(actual, expected):
    test.assert_equals(actual, expected)
    
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        testing(contain_all_rots("bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]), True)
        testing(contain_all_rots("XjYABhR", ["TzYxlgfnhf", "yqVAuoLjMLy", "BhRXjYA", "YABhRXj", "hRXjYAB", "jYABhRX", "XjYABhR", "ABhRXjY"]), False)
        testing(contain_all_rots("QJAhQmS", ["hQmSQJA", "QJAhQmS", "QmSQJAh", "yUgUXoQE", "AhQmSQJ", "mSQJAhQ", "SQJAhQm", "JAhQmSQ"]), True)
        testing(contain_all_rots("Etsshp", ["nVOETcaxdvuk", "shpEts", "hpEtss", "Etsshp", "OuIiQ", "sXrDdPXIaW", "tsshpE", "pEtssh"]), False)
        testing(contain_all_rots("Ajylvpy", ["Ajylvpy", "ylvpyAj", "jylvpyA", "lvpyAjy", "pyAjylv", "vpyAjyl"]), False)
        testing(contain_all_rots("MqhWvHF", ["numMfygcH", "HFMqhWv", "qhWvHFM", "ZJKKxM", "hWvHFMq", "MqhWvHF", "hfZWYSqk", "BTcSoEdchPlL", "WvHFMqh", "vHFMqhW", "FMqhWvH"]), True)
        testing(contain_all_rots("UDvG", ["vGUD", "UDvG", "GUDv", "DvGU"]), True)
        testing(contain_all_rots("sObPfw", ["ObPfws", "Cofuhqrmmzq", "wFvfcqU", "sObPfw", "bPfwsO", "PfwsOb", "wsObPf", "fwsObP"]), True)
        testing(contain_all_rots("KUckM", ["MKUck", "EDjfbQB", "GUPwzk", "SKZvilwnL", "UckMK", "KUckM", "kMKUc"]), False)
        testing(contain_all_rots("FDIe", ["DIeF", "IeFD", "FDIe", "eFDI"]), True)
        testing(contain_all_rots("12341234", ["DIeF", "IeFD", "12341234", "41234123", "34123412", "23412341"]), True)