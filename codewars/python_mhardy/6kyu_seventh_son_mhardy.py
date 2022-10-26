
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

# import json

# def chain_of_sons(data, generation):
#     if generation == 0:
#         yield data['name']
#         return
#     children = data['children']
#     if len(children) >= 7 and all(child['gender'] == 'male' for child in children[:7]):
#         yield from chain_of_sons(children[6], generation-1)
#     for child in children:
#         yield from chain_of_sons(child, 2)

# def find_seventh_sons_of_seventh_sons(jstring):
#     parsed_data = json.loads(jstring)
#     return set(chain_of_sons(parsed_data, 2))



# BETTER SOLUTION:
import json
def find_seventh_sons_of_seventh_sons(jstring):
    result, stack = set(), [json.loads(jstring)]
    while stack:
        person = stack.pop()
        if (len(person['children'])) >= 7 and \
            all(child['gender'] == 'male' for child in person['children'][:7]) and \
            len(person['children'][6]['children']) >= 7 and \
            all(child['gender'] == 'male' for child in person['children'][6]['children'][:7]):
            result.add(person['children'][6]['children'][6]['name'])
        stack.extend(person['children'])
    return result



# def find_seventh_sons_of_seventh_sons(jstring):
#     parsed_data = json.loads(jstring)
#     sons = 0
#     for i in parsed_data['children']:
#         if i['gender'] == 'male':
#             sons += 1
#         elif i['gender'] == 'female':
#                 # return set()
#                 break
#     if sons == 7:
#         sons_of_sons = 0
#         for i in parsed_data['children'][6]['children']:
#             if i['gender'] == 'male':
#                 sons_of_sons += 1
#             elif i['gender'] == 'female':
#                 # return set()
#                 break
#         if sons_of_sons == 7:
#             seventh_son = parsed_data['children'][6]['children'][6]['name']
#             return {seventh_son}
        
#         else:
#             return set()
#     else:
#         return set()

    
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


test.describe('Multiple Generations')
multiple_generations = {
    'gender': 'male', 
    'name': 'Favian',
    'children': [
        {'gender': 'male', 
        'name': 'Walter deGrey', 
        'children': [
            {'gender': 'male', 
            'name': 'Walter deGrey', 
            'children': []}, 
            {'gender': 'male', 
            'name': 'Benedict', 
            'children': []}, 
            {'gender': 'male', 
            'name': 'Doran', 
            'children': []}, 
            {'gender': 'male', 
            'name': 'Lord Crewe', 
            'children': []}, 
            {'gender': 'male', 
            'name': 'Leo',
            'children': []}, 
            {'gender': 'male', 
            'name': 'Favian', 
            'children': []}, 
            {'gender': 'male', 
            'name': 'Carac',
            'children': []}, 
            {'gender': 'male', 
            'name': 'Carac', 
            'children': []}, 
            {'gender': 'male', 
            'name': 'Rulf', 
            'children': []}, 
            {'gender': 'male', 
            'name': 'Gavin', 
            'children': []}, 
            {'gender': 'male', 
            'name': 'Sir Clifton Writingham', 
            'children': []}, 
            {'gender': 'male', 
            'name': 'Althalos', 
            'children': []}, 
            {'gender': 'male',
            'name': 'Josef', 
            'children': []}
            ]
        }, 
        {'gender': 'male', 
        'name': 'Lord Cornwallis', 
        'children': [
            {'gender': 'male', 
            'name': 'Frederick', 
            'children': []}, 
            {'gender': 'male', 
            'name': 'Lord Cornwallis', 
            'children': []}, 
            {'gender': 'male', 
            'name': 'Benedict', 
            'children': []}, {'gender': 'male', 'name': 'Justice McKinnon', 'children': []}, {'gender': 'male', 'name': 'Sadon', 'children': []}, {'gender': 'male', 'name': 'Walter deGrey', 'children': []}, {'gender': 'male', 'name': 'Xalvador', 'children': []}, {'gender': 'male', 'name': 'Walter deGrey', 'children': []}, {'gender': 'male', 'name': 'John of Gaunt', 'children': []}, {'gender': 'male', 'name': 'Rulf', 'children': []}, {'gender': 'male', 'name': 'Cassius', 'children': []}, {'gender': 'male', 'name': 'Favian', 'children': []}, {'gender': 'male', 'name': 'Berinon', 'children': []}, {'gender': 'male', 'name': 'Roger de Mowbray', 'children': []}]}, {'gender': 'male', 'name': 'Peyton', 'children': [{'gender': 'male', 'name': 'Lord Crewe', 'children': []}, {'gender': 'male', 'name': 'Gavin', 'children': []}, {'gender': 'male', 'name': 'Gavin', 'children': []}, {'gender': 'male', 'name': 'Carac', 'children': []}, {'gender': 'male', 'name': 'Sadon', 'children': []}, {'gender': 'male', 'name': 'Cassius', 'children': []}, {'gender': 'male', 'name': 'Henry', 'children': []}, {'gender': 'male', 'name': 'Cedric', 'children': []}, {'gender': 'male', 'name': 'Althalos', 'children': []}, {'gender': 'male', 'name': 'Hadrian', 'children': []}, {'gender': 'male', 'name': 'Cedric', 'children': []}, {'gender': 'male', 'name': 'Henry', 'children': []}, {'gender': 'male', 'name': 'Lord Cornwallis', 'children': []}, {'gender': 'male', 'name': 'Ulric', 'children': []}, {'gender': 'male', 'name': 'Robin', 'children': []}, {'gender': 'male', 'name': 'Doran', 'children': []}, {'gender': 'male', 'name': 'Ulric', 'children': []}, {'gender': 'male', 'name': 'William of Orange', 'children': []}]}, {'gender': 'male', 'name': 'Justice McKinnon', 'children': [{'gender': 'male', 'name': 'Terrowin', 'children': []}, {'gender': 'male', 'name': 'Lord Cornwallis', 'children': []}, {'gender': 'male', 'name': 'Jarin', 'children': []}, {'gender': 'male', 'name': 'Merek', 'children': []}, {'gender': 'male', 'name': 'William of Orange', 'children': []}, {'gender': 'male', 'name': 'Sadon', 'children': []}, {'gender': 'male', 'name': 'Leftholdus', 'children': []}, {'gender': 'male', 'name': 'Thomas', 'children': []}, {'gender': 'male', 'name': 'Lord Montagu', 'children': []}, {'gender': 'male', 'name': 'Asher', 'children': []}, {'gender': 'male', 'name': 'Walter', 'children': []}, {'gender': 'male', 'name': 'Tybalt', 'children': []}, {'gender': 'male', 'name': 'Fendrel', 'children': []}, {'gender': 'male', 'name': 'Tybalt', 'children': []}, {'gender': 'male', 'name': 'Brom', 'children': []}, {'gender': 'male', 'name': 'Leofrick', 'children': []}, {'gender': 'male', 'name': 'Donald', 'children': []}]}, {'gender': 'male', 'name': 'Jarin', 'children': [{'gender': 'male', 'name': 'John of Gaunt', 'children': []}, {'gender': 'male', 'name': 'Gregory', 'children': []}, {'gender': 'male', 'name': 'Terryn', 'children': []}, {'gender': 'male', 'name': 'Simon de Montfort', 'children': []}, {'gender': 'male', 'name': 'Benedict', 'children': []}, {'gender': 'male', 'name': 'Lord Crewe', 'children': []}, {'gender': 'male', 'name': 'Bryce', 'children': []}, {'gender': 'male', 'name': 'Xalvador', 'children': []}]}, {'gender': 'male', 'name': 'Quinn', 'children': [{'gender': 'male', 'name': 'Walter', 'children': []}, {'gender': 'male', 'name': 'Frederick', 'children': []}, {'gender': 'male', 'name': 'Charles the Bald', 'children': []}, {'gender': 'male', 'name': 'Justice McKinnon', 'children': []}, {'gender': 'male', 'name': 'Ulric', 'children': []}, {'gender': 'male', 'name': 'Walter', 'children': []}, {'gender': 'male', 'name': 'Gregory', 'children': []}, {'gender': 'male', 'name': 'Charles the Bald', 'children': []}]}, {'gender': 'male', 'name': 'Thomas', 'children': [{'gender': 'male', 'name': 'Jarin', 'children': []}, {'gender': 'male', 'name': 'William of Wykeham', 'children': []}, {'gender': 'male', 'name': 'Cedric', 'children': []}, {'gender': 'male', 'name': 'Arthur', 'children': []}, {'gender': 'male', 'name': 'Janshai', 'children': []}, {'gender': 'male', 'name': 'Josef', 'children': []}, {'gender': 'male', 'name': 'Lord Crewe', 'children': []}, {'gender': 'male', 'name': 'Francis Drake', 'children': []}, {'gender': 'male', 'name': 'Sir John Fenwick of Wallington', 'children': []}, {'gender': 'male', 'name': 'Walter De Bolbec', 'children': []}, {'gender': 'male', 'name': 'Fendrel', 'children': []}, {'gender': 'male', 'name': 'Borin', 'children': []}, {'gender': 'male', 'name': 'Francis Drake', 'children': []}, {'gender': 'male', 'name': 'Geoffrey Chaucer', 'children': []}, {'gender': 'male', 'name': 'Leo', 'children': []}, {'gender': 'male', 'name': 'Justice McKinnon', 'children': []}, {'gender': 'male', 'name': 'Walter De Bolbec', 'children': []}, {'gender': 'male', 'name': 'Carac', 'children': []}, {'gender': 'male', 'name': 'Sir John Fenwick of Wallington', 'children': []}, {'gender': 'male', 'name': 'Francis Drake', 'children': []}]}, {'gender': 'male', 'name': 'Cassius', 'children': [{'gender': 'male', 'name': 'Ronald', 'children': []}, {'gender': 'male', 'name': 'Dain', 'children': []}, {'gender': 'male', 'name': 'Sadon', 'children': []}, {'gender': 'male', 'name': 'Gavin', 'children': []}, {'gender': 'male', 'name': 'William of Wykeham', 'children': []}, {'gender': 'male', 'name': 'Ulric', 'children': []}, {'gender': 'male', 'name': 'Asher', 'children': []}, {'gender': 'male', 'name': 'Peyton', 'children': []}, {'gender': 'male', 'name': 'Zane', 'children': []}, {'gender': 'male', 'name': 'Zane', 'children': []}, {'gender': 'male', 'name': 'Justice McKinnon', 'children': []}, {'gender': 'male', 'name': 'Peter', 'children': []}, {'gender': 'male', 'name': 'Leftholdus', 'children': []}]}, {'gender': 'male', 'name': 'Oliver Cromwell', 'children': [{'gender': 'male', 'name': 'Lief', 'children': []}, {'gender': 'male', 'name': 'Donald', 'children': []}, {'gender': 'male', 'name': 'Peter', 'children': []}, {'gender': 'male', 'name': 'Ulric', 'children': []}, {'gender': 'male', 'name': 'Sir Clifton Writingham', 'children': []}, {'gender': 'male', 'name': 'Rowan', 'children': []}, {'gender': 'male', 'name': 'William of Wykeham', 'children': []}, {'gender': 'male', 'name': 'Rowan', 'children': []}, {'gender': 'male', 'name': 'Tristan', 'children': []}, {'gender': 'male', 'name': 'Sadon', 'children': []}, {'gender': 'male', 'name': 'Edmund Cartwright', 'children': []}, {'gender': 'male', 'name': 'Brom', 'children': []}, {'gender': 'male', 'name': 'Forthwind', 'children': []}, {'gender': 'male', 'name': 'Thomas', 'children': []}, {'gender': 'male', 'name': 'Leftholdus', 'children': []}, {'gender': 'male', 'name': 'William of Orange', 'children': []}, {'gender': 'male', 'name': 'Terryn', 'children': []}, {'gender': 'male', 'name': 'Peyton', 'children': []}, {'gender': 'male', 'name': 'Terrin', 'children': []}]}, {'gender': 'male', 'name': 'Walter deGrey', 'children': [{'gender': 'male', 'name': 'Janshai', 'children': []}, {'gender': 'male', 'name': 'Cedric', 'children': []}, {'gender': 'male', 'name': 'Hadrian', 'children': []}, {'gender': 'male', 'name': 'Sadon', 'children': []}, {'gender': 'male', 'name': 'Leo', 'children': []}, {'gender': 'male', 'name': 'Roger de Mowbray', 'children': []}, {'gender': 'male', 'name': 'Janshai', 'children': []}, {'gender': 'male', 'name': 'Thomas', 'children': []}, {'gender': 'male', 'name': 'Ulric', 'children': []}]}, {'gender': 'male', 'name': 'Berinon', 'children': [{'gender': 'male', 'name': 'Henry', 'children': []}, {'gender': 'male', 'name': 'Donald', 'children': []}, {'gender': 'male', 'name': 'Robin', 'children': []}, {'gender': 'male', 'name': 'Leofrick', 'children': []}, {'gender': 'male', 'name': 'Merek', 'children': []}, {'gender': 'male', 'name': 'Hadrian', 'children': []}, {'gender': 'male', 'name': 'Sir Clifton Writingham', 'children': []}]}, {'gender': 'male', 'name': 'Zane', 'children': [{'gender': 'male', 'name': 'Zane', 'children': []}, {'gender': 'male', 'name': 'Joseph Rowntree', 'children': []}, {'gender': 'male', 'name': 'Quinn', 'children': []}, {'gender': 'male', 'name': 'Francis Drake', 'children': []}, {'gender': 'male', 'name': 'Borin', 'children': []}, {'gender': 'male', 'name': 'Cedric', 'children': []}, {'gender': 'male', 'name': 'Janshai', 'children': []}, {'gender': 'male', 'name': 'Joseph Rowntree', 'children': []}, {'gender': 'male', 'name': 'Roger de Mowbray', 'children': []}, {'gender': 'male', 'name': 'Rulf', 'children': []}]}, {'gender': 'male', 'name': 'Earl of Derwintwater', 'children': [{'gender': 'male', 'name': 'Doran', 'children': []}, {'gender': 'male', 'name': 'Carac', 'children': []}, {'gender': 'male', 'name': 'Gregory', 'children': []}, {'gender': 'male', 'name': 'Sir Clifton Writingham', 'children': []}, {'gender': 'male', 'name': 'Charles the Bald', 'children': []}, {'gender': 'male', 'name': 'Josef', 'children': []}, {'gender': 'male', 'name': 'Hadrian', 'children': []}, {'gender': 'male', 'name': 'Geoffrey Chaucer', 'children': []}, {'gender': 'male', 'name': 'Earl of Derwintwater', 'children': []}, {'gender': 'male', 'name': 'Janshai', 'children': []}]}, {'gender': 'male', 'name': 'Lief', 'children': [{'gender': 'male', 'name': 'Arthur', 'children': []}, {'gender': 'male', 'name': 'Francis Drake', 'children': []}, {'gender': 'male', 'name': 'Lord Cornwallis', 'children': []}, {'gender': 'male', 'name': 'Peyton', 'children': []}, {'gender': 'male', 'name': 'Sadon', 'children': []}, {'gender': 'male', 'name': 'Tristan', 'children': []}, {'gender': 'male', 'name': 'Dain', 'children': []}, {'gender': 'male', 'name': 'Terrowin', 'children': []}, {'gender': 'male', 'name': 'Borin', 'children': []}, {'gender': 'male', 'name': 'Lord Falk', 'children': []}, {'gender': 'male', 'name': 'Arthur', 'children': []}]}, {'gender': 'male', 'name': 'Ronald', 'children': [{'gender': 'male', 'name': 'Fendrel', 'children': []}, {'gender': 'male', 'name': 'Robin', 'children': []}, {'gender': 'male', 'name': 'Merek', 'children': []}, {'gender': 'male', 'name': 'Oliver Cromwell', 'children': []}, {'gender': 'male', 'name': 'Benedict', 'children': []}, {'gender': 'male', 'name': 'Barda', 'children': []}, {'gender': 'male', 'name': 'Doran', 'children': []}, {'gender': 'male', 'name': 'William of Wykeham', 'children': []}]}, {'gender': 'male', 'name': 'John of Gaunt', 'children': [{'gender': 'male', 'name': 'Simon de Montfort', 'children': []}, {'gender': 'male', 'name': 'Peyton', 'children': []}, {'gender': 'male', 'name': 'Josef', 'children': []}, {'gender': 'male', 'name': 'Merek', 'children': []}, {'gender': 'male', 'name': 'Lord Crewe', 'children': []}, {'gender': 'male', 'name': 'Walter deGrey', 'children': []}, {'gender': 'male', 'name': 'Frederick', 'children': []}, {'gender': 'male', 'name': 'Dain', 'children': []}, {'gender': 'male', 'name': 'Rulf', 'children': []}, {'gender': 'male', 'name': 'Gregory', 'children': []}, {'gender': 'male', 'name': 'Walter', 'children': []}, {'gender': 'male', 'name': 'Simon de Montfort', 'children': []}]}, {'gender': 'male', 'name': 'Donald', 'children': [{'gender': 'male', 'name': 'Terrowin', 'children': []}, {'gender': 'male', 'name': 'Doran', 'children': []}, {'gender': 'male', 'name': 'Borin', 'children': []}, {'gender': 'male', 'name': 'Lord Crewe', 'children': []}, {'gender': 'male', 'name': 'Peyton', 'children': []}, {'gender': 'male', 'name': 'Lord Crewe', 'children': []}, {'gender': 'male', 'name': 'Lief', 'children': []}, {'gender': 'male', 'name': 'William of Orange', 'children': []}, {'gender': 'male', 'name': 'Gregory', 'children': []}, {'gender': 'male', 'name': 'Walter', 'children': []}, {'gender': 'male', 'name': 'Thomas', 'children': []}, {'gender': 'male', 'name': 'Benedict', 'children': []}, {'gender': 'male', 'name': 'Dain', 'children': []}]}, {'gender': 'male', 'name': 'Cedric', 'children': [{'gender': 'male', 'name': 'Frederick', 'children': []}, {'gender': 'male', 'name': 'Lord Crewe', 'children': []}, {'gender': 'male', 'name': 'Ulric', 'children': []}, {'gender': 'male', 'name': 'Frederick', 'children': []}, {'gender': 'male', 'name': 'Walter deGrey', 'children': []}, {'gender': 'male', 'name': 'William of Orange', 'children': []}, {'gender': 'male', 'name': 'Tybalt', 'children': []}, {'gender': 'male', 'name': 'Zane', 'children': []}, {'gender': 'male', 'name': 'Lief', 'children': []}, {'gender': 'male', 'name': 'Ronald', 'children': []}]}, {'gender': 'male', 'name': 'Sir Clifton Writingham', 'children': [{'gender': 'male', 'name': 'Fendrel', 'children': []}, {'gender': 'male', 'name': 'Destrian', 'children': []}, {'gender': 'male', 'name': 'William of Wykeham', 'children': []}, {'gender': 'male', 'name': 'Joseph Rowntree', 'children': []}, {'gender': 'male', 'name': 'Charles the Bald', 'children': []}, {'gender': 'male', 'name': 'Asher', 'children': []}, {'gender': 'male', 'name': 'Terrowin', 'children': []}, {'gender': 'male', 'name': 'Barda', 'children': []}, {'gender': 'male', 'name': 'Berinon', 'children': []}, {'gender': 'male', 'name': 'Simon de Montfort', 'children': []}, {'gender': 'male', 'name': 'Robin', 'children': []}, {'gender': 'male', 'name': 'Robin', 'children': []}, {'gender': 'male', 'name': 'Justice McKinnon', 'children': []}, {'gender': 'male', 'name': 'Forthwind', 'children': []}, {'gender': 'male', 'name': 'Gregory', 'children': []}, {'gender': 'male', 'name': 'Merek', 'children': []}]}, {'gender': 'male', 'name': 'Robin', 'children': [{'gender': 'male', 'name': 'Rowan', 'children': []}, {'gender': 'male', 'name': 'Donald', 'children': []}, {'gender': 'male', 'name': 'Tristan', 'children': []}, {'gender': 'male', 'name': 'Francis Drake', 'children': []}, {'gender': 'male', 'name': 'Francis Drake', 'children': []}, {'gender': 'male', 'name': 'Thomas', 'children': []}, {'gender': 'male', 'name': 'Gorvenal', 'children': []}, {'gender': 'male', 'name': 'Favian', 'children': []}, {'gender': 'male', 'name': 'Sir Clifton Writingham', 'children': []}, {'gender': 'male', 'name': 'Althalos', 'children': []}, {'gender': 'male', 'name': 'Sir John Fenwick of Wallington', 'children': []}, {'gender': 'male', 'name': 'Lord Crewe', 'children': []}, {'gender': 'male', 'name': 'Ulric', 'children': []}, {'gender': 'male', 'name': 'Josef', 'children': []}, {'gender': 'male', 'name': 'Berinon', 'children': []}, {'gender': 'male', 'name': 'Terrin', 'children': []}, {'gender': 'male', 'name': 'Asher', 'children': []}]}]}

test.assert_equals(find_seventh_sons_of_seventh_sons(json.dumps(multiple_generations)), {'Lord Crewe'})

