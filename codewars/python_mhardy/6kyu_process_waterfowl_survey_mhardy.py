# A wildlife study involving ducks is taking place in North America. 
# Researchers are visiting some wetlands in a certain area taking a survey of what they see. 
# The researchers will submit reports that need to be processed by your function.

# Input
# The input for your function will be an array with a list of common duck names along with the 
# counts made by the researchers. The names and counts are separated by spaces in one array element. 
# The number of spaces between the name and the count could vary; but, there will always be at least one. 
# A name may be repeated because a report may be a combination of surveys from different locations.

# An example of an input array would be:

# ["Redhead 3", "Gadwall 1", "Smew 4", "Greater Scaup 10", "Redhead 3", "Gadwall 9", "Greater Scaup 15", "Common Eider 6"]
# Processing
# Your function should change the names of the ducks to a six-letter code according to given rules (see below). 
# The six-letter code should be in upper case. The counts should be summed for a species if it is repeated.

# Output
# The final data to be returned from your function should be an array sorted by the species codes and 
# the total counts as integers. The codes and the counts should be individual elements.

# An example of an array to be returned (based on the example input array above) would be:

# ["COMEID", 6, "GADWAL", 10, "GRESCA", 25, "REDHEA", 6, "SMEW", 4]
# The codes are strings in upper case and the totaled counts are integers.

# Special Note
# If someone has "Labrador Duck" in their list, the whole list should be thrown out as this 
# species has been determined to be extinct. The person who submitted the list is obviously unreliable. 
# Their lists will not be included in the final data. In such cases, return an array with a single string element in it: "Disqualified data"

# Rules for converting a common name to a six-letter code:

# Hyphens should be considered as spaces.
# If a name has only one word, use the first six letters of the name. If that name has less than six letters, use what is there.
# If a name has two words, take the first three letters of each word.
# If a name has three words, take the first two letters of each word.
# If a name has four words, take the first letters from the first two words, and the first two letters from the last two words.


import re
from collections import OrderedDict

def encode(name):
    new_name = ""
    
    x = name.replace('-', ' ').split(' ')
    if len(x) == 4:
        new_name += "{}{}{}{}".format(x[0][0], x[1][0], x[2][0:2], x[3][0:2])
    elif len(x) == 3:
        new_name += "{}{}{}".format(x[0][0:2], x[1][0:2], x[2][0:2])
    elif len(x) == 2:
        new_name += "{}{}".format(x[0][0:3], x[1][0:3])
    else:
        new_name += "{}".format(x[0][0:6])

    return new_name

def create_report(names):
    name_dict = {}
    output = []
    print(names)
    for i in names:
        name = re.match('([a-zA-Z\']+\s?[\-]?[a-zA-Z\']+?\s?[\-]?[a-zA-Z\']+?\s?[\-]?[a-zA-Z\']+?)\s+(\d+)', i)
        if name.groups()[0] == "Labrador Duck":
            output.append("Disqualified data")
            return output
        else:
            name1 = name.groups()[0].upper()
            coded_name = encode(name1)
            num1 = int(name.groups()[1])
            if coded_name not in name_dict:
                name_dict[coded_name] = num1
            else:
                name_dict[coded_name] += num1

    name_dict1 = OrderedDict(sorted(name_dict.items()))
    for key, value in name_dict1.items():
        output.append(key)
        output.append(value)

    return output

import codewars_test as test


test.assert_equals(create_report(["Redhead 3", "Gadwall  1", "Smew 4", "Greater Scaup 10", "Redhead 3", "Gadwall 9", "Greater Scaup  15", "Common Eider 6"]), ["COMEID", 6, "GADWAL", 10, "GRESCA", 25, "REDHEA", 6, "SMEW", 4])