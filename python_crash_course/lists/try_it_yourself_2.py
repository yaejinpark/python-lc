users = ['admin', 'bera', 'rabia', 'alp']

for user in users:
    print(f"Hello {user.title()}, thank you for logging in again\n")


for user in users:
    if user == 'admin':
        print(f'Hello {user.title()}, would you like to see a status report?\n')
    else:
        print(f'Hello {user.title()}, thank you for logging in again.\n')


# Case where there is no users 

members = []

if members: 
    for member in members: 
        print(f"Welcome {member}, have a wonderful day!")

else: 
    print(f"We need to find new members!")

# Case where we check to lists! 

current_users = ['alp', 'rabia', 'didem', 'sila', 'bera']



new_users = ['Bera', 'Rabia', 'sila', 'kasim', 'can']

if current_users: 
    for new_user in new_users:
        if new_user.lower() in current_users:
            print(f"The user name is already taken.")
        else: 
            print(f'Welcome onboard {new_user.title()}')
else: 
    print('We need to find new users')



for numbers in range(1,10):
    if numbers == 1 :
        print(f"{numbers}st")
    elif numbers == 2:
        print(f'{numbers}nd')
    elif numbers == 3:
        print(f"{numbers}rd")
    else:
        print(f"{numbers}th")