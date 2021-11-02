players = ['charles', 'martina', 'ayse', 'ahmed', 'fatma']

print(players[0:3])

print(players[1:4])


print(f'\nHere are the players in my team:\n')
for player in players[:4]:
    print(player.title())


my_foods = ["pizza", "burger", "tika masala", "doner", "karniyarik"]

my_friends = my_foods[:]

print(f'\nMy favorite food list is:')
print(my_foods)

print(f'\n My friends favorite food list is:')
print(my_friends)


my_foods.append('dolma')
print(f'\nMy favorite food list is:')
print(my_foods)

print(f'\n My friends favorite food list is:')
my_friends.append('ravioli')
print(my_friends)


# TRY IT YOURSELF
locations = ['Paris', 'London', 'Nairobi', 'Cape Town', 'Istanbul', 'Venice']

three_items = []
for i in locations[0:3]:
    
    three_items.append(i)
print(f'\n First three items are:')
print(three_items)

print(f'\n First three items are:')
print(locations[0:3])


print(f'\n The three items from the middle are:')
print(locations[2:4])

print(f'\n The last three items are:')
print(locations[3:])




# original pizza list 

original_list = ['pies', 'apples', 'carrots', 'drinks']

print('\n This is the original list:')
print(original_list)

copy_list = original_list[:]

print('\n This is a copy list:')
print(copy_list)

original_list.append('houses')
print('\n This is the original list:')
print(original_list)


copy_list.append('vegitables')
print('\n This is a copy list:')
print(copy_list)


print('\n My favorite titles (original list) are:')
for values in original_list[:]: 
    print(values.title())



print('\n My favorite titles (copy list) are:')
for values in copy_list[:]: 
    print(values.title())

locations = ['Paris', 'London', 'Nairobi', 'Cape Town', 'Istanbul', 'Venice']

print('\n List of locations:')

for i in locations[:]:
    print(i)