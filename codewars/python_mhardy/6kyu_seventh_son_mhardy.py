
# According to Wikipedia : "The seventh son of a seventh son is a concept from 
# folklore regarding special powers given to, or held by, such a son. 
# The seventh son must come from an unbroken line with no female siblings born 
# between, and be, in turn, born to such a seventh son."

# Your task
# You will be given a string of JSON, consisting of a family tree containing 
# people's names, genders and children. Your task will be to find the seventh 
# sons of seventh sons in the family tree, and return a set of their names. 
# If there are none, return an empty set.

# Tips
# Have a good look at the sample test cases.

# For a seventh son to be a seventh son, there must not be any 
# daughters in the line leading to him. There may be daughters after him, though.

# You may want to use the json module for this one.

import json

def find_seventh_sons_of_seventh_sons(jstring):
    parsed_data = json.loads(jstring)
    
    sons = 0
    
    for i in parsed_data['children']:
        if i['gender'] == 'male':
            sons += 1
    if sons == 7:
        sons_of_sons = 0
        for i in parsed_data['children'][6]['children']:
            if i['gender'] == 'male':
                sons_of_sons += 1
        if sons_of_sons == 7:
            return {parsed_data['children'][6]['children'][6]['name']}
        else:
            return set()
    else:
        return set()

    
    # return#the list of seventh sons of seventh sons




import codewars_test as test

test.describe('Contains seventh son of seventh son')
contains_seventh_son_of_seventh_son = {
    'name': 'A',
    'gender': 'male',
    'children': [
        {'name': 'B',
         'gender': 'male',
         'children': []},
        {'name': 'C',
         'gender': 'male',
         'children': []},
        {'name': 'D',
         'gender': 'male',
         'children': []},
        {'name': 'E',
         'gender': 'male',
         'children': []},
        {'name': 'F',
         'gender': 'male',
         'children': []},
        {'name': 'G',
         'gender': 'male',
         'children': []},
        {'name': 'H', # This is the seventh son
         'gender': 'male',
         'children':[
            {'name': 'I',
             'gender': 'male',
             'children': []},
            {'name': 'J',
             'gender': 'male',
             'children': []},
            {'name': 'K',
             'gender': 'male',
             'children': []},
            {'name': 'L',
             'gender': 'male',
             'children': []},
            {'name': 'M',
             'gender': 'male',
             'children': []},
            {'name': 'N',
             'gender': 'male',
             'children': []},
            {'name': 'O', # This is the sventh son of the seventh son
             'gender': 'male',
             'children': []}
         ]}
    ]
}
test.assert_equals(find_seventh_sons_of_seventh_sons(json.dumps(contains_seventh_son_of_seventh_son)), {'O'}) 

test.describe('Would-be seventh son of seventh son is a daughter')
does_not_contain_seventh_son_of_seventh_son = {
    'name': 'A',
    'gender': 'male',
    'children': [
        {'name': 'B',
         'gender': 'male',
         'children': []},
        {'name': 'C',
         'gender': 'male',
         'children': []},
        {'name': 'D',
         'gender': 'male',
         'children': []},
        {'name': 'E',
         'gender': 'male',
         'children': []},
        {'name': 'F',
         'gender': 'male',
         'children': []},
        {'name': 'G',
         'gender': 'male',
         'children': []},
        {'name': 'H', # This is the seventh son
         'gender': 'male',
         'children':[
            {'name': 'I',
             'gender': 'male',
             'children': []},
            {'name': 'J',
             'gender': 'male',
             'children': []},
            {'name': 'K',
             'gender': 'male',
             'children': []},
            {'name': 'L',
             'gender': 'male',
             'children': []},
            {'name': 'M',
             'gender': 'male',
             'children': []},
            {'name': 'N',
             'gender': 'male',
             'children': []},
            {'name': 'O',
             'gender': 'female', # The seventh son of the seventh son is in fact a daughter!
             'children': []}
         ]}
    ]
}
test.assert_equals(find_seventh_sons_of_seventh_sons(json.dumps(does_not_contain_seventh_son_of_seventh_son)), set()) 

test.describe('Chain of sons is broken')
does_not_contain_seventh_son_of_seventh_son = {
    'name': 'A',
    'gender': 'male',
    'children': [
        {'name': 'B',
         'gender': 'male',
         'children': []},
        {'name': 'C',
         'gender': 'male',
         'children': []},
        {'name': 'D',
         'gender': 'male',
         'children': []},
        {'name': 'E',
         'gender': 'female', # The chain of sons is broken!
         'children': []},
        {'name': 'F',
         'gender': 'male',
         'children': []},
        {'name': 'G',
         'gender': 'male',
         'children': []},
        {'name': 'H',
         'gender': 'male',
         'children':[
            {'name': 'I',
             'gender': 'male',
             'children': []},
            {'name': 'J',
             'gender': 'male',
             'children': []},
            {'name': 'K',
             'gender': 'male',
             'children': []},
            {'name': 'L',
             'gender': 'male',
             'children': []},
            {'name': 'M',
             'gender': 'male',
             'children': []},
            {'name': 'N',
             'gender': 'male',
             'children': []},
            {'name': 'O',
             'gender': 'male',
             'children': []}
         ]}
    ]
}
test.assert_equals(find_seventh_sons_of_seventh_sons(json.dumps(does_not_contain_seventh_son_of_seventh_son)), set()) 


test.describe('Seventh son does not have children')
does_not_contain_seventh_son_of_seventh_son = {
    'name': 'A',
    'gender': 'male',
    'children': [
        {'name': 'B',
         'gender': 'male',
         'children': []},
        {'name': 'C',
         'gender': 'male',
         'children': []},
        {'name': 'D',
         'gender': 'male',
         'children': []},
        {'name': 'E',
         'gender': 'female',
         'children': []},
        {'name': 'F',
         'gender': 'male',
         'children': []},
        {'name': 'G',
         'gender': 'male',
         'children': []},
        {'name': 'H', # This is the seventh son, but he has no children
         'gender': 'male',
         'children':[]
        }
    ]
}
test.assert_equals(find_seventh_sons_of_seventh_sons(json.dumps(does_not_contain_seventh_son_of_seventh_son)), set()) 
