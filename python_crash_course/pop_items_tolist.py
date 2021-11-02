from typing import SupportsAbs


cars = ['Honda', 'Nissan', 'Toyota', 'BMW']

firts_owned = cars.pop(0)

print(f'The first car I owned was a {firts_owned.upper()}')
print(f'The first car I owned was a {firts_owned.title()}')

cars.remove('Nissan')

print(cars)

cars.append('Mini')
print(cars)


too_expensive = 'Mini'


cars.remove(too_expensive)

print(cars)
print(f'\n A {too_expensive.title()} is too expensive for me')


guest_list = ['Selcuk', 'Rabia', 'Beste', 'Tugrul', 'Didem', 'Alp']

for i in guest_list: 
    print(f'Hey {i}, \n Hope this message finds you well! You are invited to my dinner party')

print(f"Unfortunately {guest_list[4]} can't make it")

guest_list[4] = 'Sule'

print(guest_list)

for i in guest_list: 
    print(f'Hey {i}, \n Hope this message finds you well! You are invited to my dinner party')


print(f'Hey all, I found a bigger table, I am inviting more people to the dinner table')

guest_list.insert(0,'Ahmet')

guest_list.insert(3, 'Sude')

guest_list.insert(8, 'Omer')

print(guest_list)

for i in guest_list: 
    print(f'Hey {i}, \n\n Hope this message finds you well! You are invited to my dinner party \n')

print(f'Sorry for the inconveniences I will only invite two people for the dinner party')

sule_sorry = guest_list.pop(6)

print(f'\n Sorry {sule_sorry}, due to the unexpected circumstances I will have to postpone you to another day')

alp_sorry = guest_list.pop(6)
print(f'\n Sorry {alp_sorry}, due to the unexpected circumstances I will have to postpone you to another day')

beste_sorry = guest_list.pop(4)
print(f'\n Sorry {beste_sorry}, due to the unexpected circumstances I will have to postpone you to another day')


rabia_sorry = guest_list.pop(2)
print(f'\n Sorry {rabia_sorry}, due to the unexpected circumstances I will have to postpone you to another day')

print(guest_list)

for i in guest_list: 
    print(f'Hey {i}, \n\n Hope this message finds you well! You are still invited to my dinner party \n')


del guest_list[0:5]

print(guest_list)

animals = ['dog', 'cat', 'rabbit', 'bee', 'elephant']

animals.sort()
print(animals)

print(sorted(animals, key=lambda k: k[1]))

animals.sort(reverse=True)

print(animals)

names = ['John', 'Adele', 'Jack', 'Dua Lipa', 'Ricardo']

print('Here is the original list')
print(names)

print('\n Here is the sorted list')
print(sorted(names))

print('\n Here is the original list')
print(names)

names.reverse()
print(names)

print(len(names))


locations = ['Paris', 'London', 'Nairobi', 'Cape Town', 'Istanbul', 'Venice']
print(locations)

print('\n Print list using the sorted method')
print(sorted(locations))

print('\n Show that the original list is unchanged')
print(locations)

print('\n Print the sorted list in reverse order')
print(sorted(locations, reverse=True))

print('\n Show that the original list is unchanged')
print(locations)

print('\n Print the list in reverse order')
locations.reverse()
print(locations)

print('\n Print the list in reverse order again')
locations.reverse()
print(locations)

locations.sort()
print('\n Print locations using the sort fuction')
print(locations)

locations.sort(reverse=True)
print("\n Print list using the sort and reverse method")
print(locations)


print(f'\n{len(names)}')

print(f'\n{len(locations)}')


natural_beauties = ['Lakes', 'Mountains', 'Rivers', 'Oceans', 'Forests']

for i in range(1, 3, 1):
    new_list = natural_beauties.pop(i)
    print(f'The places I went to are {new_list}')

print(natural_beauties)


