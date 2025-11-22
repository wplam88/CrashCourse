"This lesson introduces if statements"

#5.12 Conditional Tests

    #True
player_0 = 'Lebron'
player_2 = 'Oubre'
player_3 = 'lebron'
players =['zo', 'gelo', 'melo']
print("Is player == 'Lebron'? Prolly.")
print(player_0 == 'Lebron')

print(player_0 != player_2)
print(player_0.lower() == player_3)
print(1 <= 1 and 2 > 1)
print(1 >= 1 or 1 > 2)
print('zo' in players)

print (2 > 1)

    #False
player_1 = 'Jordan'
print("Is player == 'Lebron'? Nah.")
print(player_1 == 'Lebron')

print (1 > 2)

#5.3 Alien Colors #1 (if)
alien_color = 'red'
if alien_color == 'green':
    print('Player earned 5 points')
if alien_color == 'yellow':
    print()

#5.4 Alien Colors #2 (if-else)
if alien_color == 'green':
    print('Player earned 5 points')
else:
    print('Player earned 10 points')

#5.5 Alien Colors #3 (if-elif-else)
if alien_color == 'green':
    print('Player earned 5 points')
elif alien_color == 'yellow':
    print('Player earned 10 points')
elif alien_color == 'red':
    print('Player earned 15 points')

#5.6 Stages of Life 
age = 10
if age < 2:
    print('baby')
elif 2 <= age < 4:
    print('toddler')
elif 4 <= age < 13:
    print('kid')
elif 13 <= age < 20:
    print('teen')
elif 20 <= age < 65:
    print('adult')
else:
    print('senior')

#5.7 Favorite Fruit
fav_fruits = ['apple', 'blueberry', 'grape']
if 'apple' in fav_fruits:
    print("I like apples!")

#5.89 Hello Admin, No Users
users = ['admin', 'anna', 'bryce', 'clarke', 'dino', 'elanor']
if users:
    for user in users:
        if user == 'admin':
            print(f'Hello {user}, would you like to see a status report?')
        else:
            print(f'Hello {user}, thank you for logging in again.')
else: 
    print('We need to find some users')

#5.10 Checking Username
current_users = ['admin11', 'anna22', 'bryce33', 'clarke44', 'dino55', 'elanor66']
new_users = ['admin11', 'anna77', 'bryce88', 'clarke99', 'dino100', 'elanor110']
i = 0
for user in new_users:
    if user == current_users[i]:
        print(f'Hello, {user} is already taken. Please try again')
    else:
        print(f'{user} is available!')
    i+=i

#5.11 Ordincal Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')