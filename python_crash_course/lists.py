# In this page I pracitce printing indexies 

biycycles = ['trek', 'cannondale', 'redline', 'specialized']

print(biycycles)

print(biycycles[0])

print(biycycles[3].title())

print(biycycles[-2].title())


message = f'My first biycyle is a {biycycles[2].title()}'

print(message)


names = ['Selcuk', 'Rabia', 'Sila', 'Alp Ahmet', 'Didem', 'Fatih', 'Anil', 'Tugrul', 'Ahmet']

print(names[-1])

highschool_friends = f'My friends from highschool are {names[-2]} and {names[-1]}'

print(highschool_friends)

univeristy_friends = f'My friends from university are {names[0]}, {names[1]}, {names[2]}, {names[3]}, {names[4]}, {names[5]}, and {names[6]}.'
print(univeristy_friends)


modes_transport = ['airplane', 'car', 'train']

print(f'I like using the {modes_transport[2]} when going on long trips')

print(f'I use the {modes_transport[1]} everyday to earn money')

print(f"Although I am afraid of riding a {modes_transport[0]}, I still like the feeling of flying over the clouds")


# How to change elements in a list 

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles[0] = 'ducati'

print(motorcycles)

# How to add new values to the list using the append() method 
motorcycles.append('honda')

print(motorcycles)


# How to add values to an empty list 

fruits = []

fruits.append('banana')
fruits.append('watermelon')
fruits.append('strawberry')
fruits.append('orange')

print(fruits)



# Inserting elements into a list using the insert() method

fruits.insert(4, 'apple')

fruits.insert(4, 'grapes')
print(fruits)

# Removing value from a list using the del statement 

del motorcycles[0]

print(motorcycles)

del fruits[1]

print(fruits)


# Removing value from a list using the pop() method

popped_motorcycles = motorcycles.pop()

print(motorcycles)
print(popped_motorcycles)


popped_fruits = fruits.pop()

print(f'The last fruit I ate was a/an {popped_fruits}')