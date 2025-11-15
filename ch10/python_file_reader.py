from pathlib import Path
import json

# 10.1
# finds, reads, and prints the file
path = Path("learning_python.txt")
contents = path.read_text()
print(contents)

# splits lines, creates one string, and prints
pi_string = ""
for line in contents.splitlines():
    pi_string += line
print(pi_string)

# 10.2
# replaces words in a string
contents2 = contents.replace("Python","C")
print(contents2)

# 10. 4
# asks user for their name and stores it in guest.txt
name = input("Please enter your name. ")
path2 = Path("guest.txt")
path2.write_text(name)

# 10.5
# prompts users for their names and creates a guest list
guest_list = ""

while True:
    full_name = input("What is your first and last name? (Type 'quit' to stop) ")

    if full_name.lower() == "quit":
        break

    guest_list += full_name + "\n"

path3 = Path("guest_list.txt")
path3.write_text(guest_list)

# 10.6
# prompts the user for 2 numbers, raises a ValueError exception, adds if able
while True:
    answer1 = input("Please enter a number or 'q' to quit: ")
    if answer1.lower() == 'q':
        break
    answer2 = input("Please enter a number or 'q' to quit: ")
    if answer2.lower() == 'q':
        break  
    try:
        number1 = int(answer1)
        number2 = int(answer2)
    except ValueError:
        print("Sorry, please ensure you enter numbers only!")
    else:
        result = number1 + number2
        print(f"your numbers add up to {result}")

# 10.8
# read and print the files
# wrap code in try-except block for FileNotFoundError
# fail silently if file is missing
filenames = ['dogs.txt', 'birds.txt', 'cats.txt']

for file in filenames:
    file_path = Path(file)
    try:
        contents = file_path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(contents)

# 10.11

path = Path('fav_number.json')

if path.exists():
    # reads the file and prints it
    contents = path.read_text()
    fav_number = json.loads(contents)
    print(f'I know your favorite number is {fav_number}')

else:
    # prompt for user favorite number and stores it
    fav_number = input("What is your favorite number? ")
    contents = json.dumps(fav_number)
    path.write_text(contents)


# 10.13
# create a path
path = Path('user_attributes.json')

# ask for multiple pieces of info about a user
username = input("What is your username? ")
email = input("What is your email? ")
password = input("What is your password? ")

# store all of the info you collect into a dictionary
attributes = {
    "username": username, 
    "email": email, 
    "password": password
}

# write the dictionary to a file using json.dumps()
contents = json.dumps(attributes)
path.write_text(contents)

# read it back using json.loads()
contents2 = path.read_text()
attributes2 = json.loads(contents2)

# print a summary showing what your program remembers about a user
print(f'Hey, {attributes2['username']}! Your email is {attributes2['email']} and your password is {attributes2['password']}')




    