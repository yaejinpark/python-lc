from typing import AsyncIterable, Counter


cars = ['audi', 'bmw', 'subatu', 'toyota'] 

for car in cars: 
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


car = 'bmc'

car == 'bmc'


requested_topping = 'anchovies'

if requested_topping != 'anchovies':
    print('Hold the anchovies!')
else: 
    print('We have mushrooms for dinner ')


answer = 12 

if answer !=  41:
    print('That is not the correct answer. Please try again!')


age = 12 
print(age < 122)

#   USING THE AND CONDITION 
age_1 = 45 
age_2 = 11 

if age_1 > 21 and age_2 > 21: 
    print('Both can enter')
elif age_1 > 21 and age_2 < 21: 
    print(f'Only age {age_1} can enter')

elif age_1<21 and age_2>21: 
     print(f'Only age {age_2} can enter')

else: 
    print('None can enter')


# USING THE 'OR' CONDITION 

if age_1 > 21 or age_2> 21: 
    print('The good can be sold ')

#   CHECKING FOR VALUES IN LIST USING THE 'IN' CONDITION 
requested_toppings = ['mushrooms', 'onions', 'pineapple']

print('mushrooms' in requested_toppings)

print('mushrooms' not in requested_toppings)

banned_names = ['james', 'alice', 'ronald', 'ricardo']

user = 'fatma'

if user not in banned_names:
    print(f'{user.title()}, you can post a response!')


# TRY IT YOURSELF PRACTICE QUESTIONS 

personal_items = ['keys', 'shoes', 'bag', 'computer', 'water bottle']

print('shoes' in personal_items)

my_item = 'shoes'

print('desktop' in personal_items)

if my_item == 'shoes': 
    print(f'I predicted {my_item} to be True')


print("Is my_item == 'shoes'? I predict True.")
print(my_item == 'shoes')

print("\nIs my_item == 'DVD'? I predict False")
print(my_item == 'DVD')


print('\nIs "keys in personal items? I predict to be true')
print('keys' in personal_items)

print('\n Is car in personal item? I predict to be false')
print('car'  in personal_items) 


print("\nIs dog in personal items? I predict false")
print('dog' in personal_items)


car = 'bmw'

print(car == 'bmw')

print(car == 'honda')


name = 'John'

print(f"Is {name.lower()} equal to John?" )

print(name.lower() == 'john')

print(name.lower() != 'john' )

numbers = list(range(11))
print(numbers)

for i in numbers: 
    print(i)


counts = 21

print(counts >= 11)
print(counts <= 33)

print(counts == 21)
print(counts != 21)

variable = 21 

if counts> 18 and variable > 18: 
    print('Both are legal to drink')

if counts< 12 or variable>22: 
    print('It is hard to go')
else:
    print('Free to go')

team = ['jackson', 'ahmed', 'abdullah', 'aysa']

print('ahmed' not in team)
print('abdullah' in team)


#age = input('Enter your age ')

#if age > str(18): 
    #print('You are old enough to vote!')
    #print('Are you registered to vote!')
#else: 
    #print('You are not old enough to vote!')
    #print('Please register to vote once you turn 18')



#age = int(input('Enter your age? '))

#if age <= 4:
    #price = 0
#elif age <= 18:
    #price = 25
#else: 
    #price = 40
#print(f'Your admission price is ${price} ')

if age <= 4:
    price = 0 
elif age <= 18: 
    price = 25
elif age < 65: 
    price = 40
elif age >= 65: 
    price= 20
print(f'Your admission price is ${price} ') 


requests_pizza = ["mushrooms", "extra cheese"]

if 'mushrooms' in requests_pizza:
    print('Adding mushrooms')
if 'pepperoni' in requests_pizza:
    print('Adding pepperoni.')
if 'extra cheese' in requests_pizza:
    print('Adding extra cheese')

print(f'\nFinished preparring your pizza!')



# TRY IT YOURSELF SECTION 

alien_color = "red"

if alien_color == 'red':
    print("You've just earned 5 points")

if alien_color != "blue":
    print("You've just earned 0 points")



if alien_color == 'green':
    print("You've just earned 5 points")
else:
    print("You've just earned 10 points")


if alien_color == 'green':
    print("You've just earned 5 points")
elif alien_color =='yellow':
    print("You've just earned 10 points")
elif alien_color == 'red':
    print("You've just earned 15 points")

variable_age = int(input("What is your age?"))

if variable_age < 2:
    print("The person is a baby")
elif variable_age < 4: 
    print("The person is a toddler")
elif variable_age < 13: 
    print("The person is a kid")
elif variable_age < 20:
    print("The person is a teenager")
elif variable_age < 65: 
    print("The person is an adult")
elif variable_age >= 65: 
    print("The person is an elder")


favorite_fruits = ['apple', 'banana', 'strawberry']

if 'apple' in favorite_fruits:
    print("You really like apples!")
if 'banana' in favorite_fruits:
    print('You really like bananas')
if 'peach' in favorite_fruits:
    print("You really like peaches")
if 'melon' not in favorite_fruits:
    print("You don't like melon?")
if 'strawberry' in favorite_fruits:
    print("You really like strawberries")