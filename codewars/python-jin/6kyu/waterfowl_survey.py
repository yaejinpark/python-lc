'''
A wildlife study involving ducks is taking place in North America. 
Researchers are visiting some wetlands in a certain area taking a survey of what they see. 
The researchers will submit reports that need to be processed by your function.

Input
The input for your function will be an array with a list of common duck names along with the counts made by the researchers. 
The names and counts are separated by spaces in one array element. The number of spaces between the name and the count could vary; 
but, there will always be at least one. A name may be repeated because a report may be a combination of surveys from different locations.

An example of an input array would be:

["Redhead 3", "Gadwall 1", "Smew 4", "Greater Scaup 10", "Redhead 3", "Gadwall 9", "Greater Scaup 15", "Common Eider 6"]
Processing
Your function should change the names of the ducks to a six-letter code according to given rules (see below). 
The six-letter code should be in upper case. The counts should be summed for a species if it is repeated.

Output
The final data to be returned from your function should be an array sorted by the species codes and the total counts as integers. 
The codes and the counts should be individual elements.

An example of an array to be returned (based on the example input array above) would be:

["COMEID", 6, "GADWAL", 10, "GRESCA", 25, "REDHEA", 6, "SMEW", 4]
The codes are strings in upper case and the totaled counts are integers.

Special Note
If someone has "Labrador Duck" in their list, the whole list should be thrown out as this species has been determined to be extinct. 
The person who submitted the list is obviously unreliable. Their lists will not be included in the final data. 
In such cases, return an array with a single string element in it: "Disqualified data"

Rules for converting a common name to a six-letter code:

Hyphens should be considered as spaces.
If a name has only one word, use the first six letters of the name. If that name has less than six letters, use what is there.
If a name has two words, take the first three letters of each word.
If a name has three words, take the first two letters of each word.
If a name has four words, take the first letters from the first two words, and the first two letters from the last two words.
'''

def create_report(names):
    names_only = []
    name_converter = {}
    final_survey = {}
    res = []
        
    for name in names:
        new_name = ""
        for i in range(len(name)):
            if not name[i].isdigit() and name[i] != '-':
                new_name += name[i]
            if name[i] == '-': # replace '-'s with spaces
                new_name += ' '
        # What's wrong with a Labrador Duck? Very Long Name Duck exists too...
        if "Labrador Duck" in new_name:
            return ["Disqualified data"]
        names_only.append(new_name.strip())
    survey_only = [int(x) for x in " ".join(names).split() if x.isdigit()] # Numeric part of the survey only
    data = list(zip(names_only,survey_only))
    
    unique_names = set(names_only)
    
    for name in unique_names:
        name_parts = name.split(" ")
        new_name = ""
        if len(name_parts) < 2:
            new_name = name[:6]
        elif len(name_parts) == 2:
            for parts in name_parts:
                new_name += parts[:3]
        elif len(name_parts) == 3:
            for parts in name_parts:
                new_name += parts[:2]
        else: 
            for i in range(2):
                new_name += name_parts[i][0]
            for i in range(2,4):
                new_name += name_parts[i][:2]
        name_converter[name] = new_name.upper()
        
    for i in data:
        duck_name = i[0]
        if name_converter[duck_name] not in final_survey:
            final_survey[name_converter[duck_name]] = i[1]
        else:
            final_survey[name_converter[duck_name]] += i[1]
    
    for k in sorted(final_survey.keys()):
        res.append(k)
        res.append(final_survey[k])
    return res

test1 = [
    'Ring-necked Duck     181', 
    'White-cheeked Pintail  658', 
    'Common Goldeneye     962', 
    'American Black Duck  670', 
    'Spectacled Eider    628', 
    'White-cheeked Pintail 853', 
    'Very Long Name Duck    2', 
    'Common Goldeneye 758', 
    'Spectacled Eider     63']
test2 = [
    'Ring-necked Duck 927', 
    'Black-Bellied Whistling-Duck     961', 
    'Surf Scoter   703', 'Common Eider 987', 
    'Black-Bellied Whistling-Duck 989', 
    'Black-Bellied Whistling-Duck  292', 
    'Black-Bellied Whistling-Duck     936', 
    'Very Long Name Duck  416', 
    'Bufflehead    761', 
    'Northern Pintail     455', 
    'Gadwall   792', 
    'Common Eider    735', 
    'Black-Bellied Whistling-Duck 902']

print(create_report(test1))
print(create_report(test2))