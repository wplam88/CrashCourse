"This activity familiarizes me with lists"

#3.1 List of Friends
names = ['saad', 'preston', 'nate', 'garrett']
print(names[1])

#3.2 Message to Friends
message = "What's up, "
print(f"{message}{names[1].title()}?")

#3.3 Compile make and mode lists
make = ['honda', 'aston martin']
mode = ['truck', 'suv', 'coupe']
print(f"I want a {make[-1].title()} {mode[2].title()} when I am older.")

#3.4 Guest List
guests = ['Lauryn Hill', 'Toni Morrison', 'Andre 3000']
print(f"Welcome to my dinner party, {guests[0]}")
print(f"Welcome to my dinner party, {guests[1]}")
print(f"Welcome to my dinner party, {guests[-1]}")

#3.5 Changing Guest List
print(f"{guests[1]} cannot make it :(")
guests[1] = 'Lil Baby'
print(guests)

#3.6 Bigger Table
guests.insert(0, 'Travis Scott')
guests.insert(3,'Jessie Murph')
guests.append('Koe Wetzel')

#3.7 Shrinking Guest List
print("I only have room for two guests")
guests.pop(-1)
del guests[0]
del guests[0]
del guests[0]
del guests[0]
del guests[0]
print(guests)
