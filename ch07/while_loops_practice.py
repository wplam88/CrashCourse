"This helps to make code interactive, with user inputs and while loops"

#7.1 Rental Car
rental = input("What kind of car would you like? ")
print(f'Let me see if I can find you a {rental.title()}!')

#7.2 Restaurant Seating
guests = input("How many people will be dining with you this evening? ")
if int(guests) > 8:
    print("There will be a wait!")
else:
    print("Your table is ready!")

#7.3 Multiple of 10
number = input("Type a number: ")
if int(number) % 10 == 0:
    print(f'{number} is a multiple of 10!')
else:
    print(f'{number} is NOT a multiple of 10!')

#7.4 Pizza Toppings
prompt = "\nWhat would you like on your pizza?:"
prompt += "\n(Enter 'quit' when you are finished)"

#could ideate on this to then print  the indicies here
pizza: list[str] = []

making_pizza = True
while making_pizza:
    topping = input(prompt)
    if topping == 'quit':
        making_pizza = False
        print('You are finished making your pizza!')
    else:
        pizza.append(topping)
        print(f'Adding {topping.title()}!')

#7.56 Movie Tickets
prompt = "\nHow old are you?:"
prompt += "\n(Enter 'quit' when you are finished)"

while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        if int(age) < 3:
            print("Your ticket is free!")
        elif 3 <= int(age) <= 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")

#7.7 Infinite Loop (press CTRL + C to end, this will never end because x is not incremented upwards)
#x = 1
#while x < 5:
    #print(x)

#7.89 Deli w/ No Pastrami
print("\nThe deli has run out of Pastrami")

sandwich_orders = ['italian', 'club', 'steak and cheese', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f'I made your {current_sandwich.title()} sandwich!')
    finished_sandwiches.append(current_sandwich.title())

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)

#7.10 Dream Vacation
poll_results = {}
polling = True

while polling:
    name = input("\nWhat is your name? ")
    destination = input("What is your dream vaction? ")

    poll_results[name] = destination

    repeat = input("Would you like another person to go? (yes/no) ")
    if repeat == 'no':
        polling = False

print("\n--Poll Results--")
for name, destination in poll_results.items():
    print(f'{name.title()} would like to go to {destination.title()}!')









