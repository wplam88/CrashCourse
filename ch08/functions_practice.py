"This program practices functions which will help to clean up code moving forward"

#8.1 Message
def display_message():
    print("This chapter is about functions")

display_message()

#8.2 Favorite Book
def favorite_book(title: str):
    """This function takes a book title and prints it in a string20"""
    print(f'One of my favorite books is {title.title()}')

favorite_book('zen and the art of motorcycle maintenance')

#8.3 T-Shirt
def t_shirt(size: str, message: str):
    """this function takes a shirt size and message and prints them in a string"""
    print(f'Your shirt is size {size.title()} and says {message.title()}!')

t_shirt('L', 'grind sold separate')
t_shirt(message = 'grind sold separate', size = 'L')

#8.4 Large Shirts
def make_shirt(size = 'Large', message = 'I love python'):
    """this function takes a default large shirt and default message and prints them in a string"""
    print(f'Your shirt is size {size.title()} and says {message.title()}!')

make_shirt()
make_shirt('Medium')
make_shirt('Small', 'I like Kendrick')

#8.5 Cities
def describe_city(name, country):
    print(f'{name.title()} is in {country.title()}')

describe_city('Raleigh', 'America')

#8.6 City Names
def city_country(city, country):
    print(f'{city.title()}, {country.title()}')

city_country('santiago', 'chile')

#8.7 Album
def make_album(artist_name, album_title):
    """Creates a dictionary given an artist name and album title"""
    album = {'name': artist_name.title(), 'title': album_title.title()}
    print(album)

make_album('kendrick lamar', 'DAMN')
make_album('drake', 'iceman')
make_album('j cole', '2014 forest hills drive')

#8.8 User Albums - NOT FINISHED!!!!
""" def user_make_album(artist_name, album_title):
    #Creates a dictionary given an artist name and album title from the end user
    album = {'name': artist_name.title(), 'title': album_title.title()}

    while True:
        print('\nWhats your favorite artist and album?')
        print("(enter 'q' at anytime to quit)")
        artist = input("Artist Name: ")
        if artist == 'q':
            break

        album = input("Album Title: ")
        if album == 'q':
            break  
        
        user_input = user_make_album(artist_name, album_title)
        print(album) """

#8.91011 Messages
messages: list[str] = ['hiiiiiii', 'heyyyyy']
sent_messages: list[str] = []

"""def show_messages(messages):
    for message in messages:
        print(message)
    
show_messages(messages)"""

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        sent_messages.append(current_message)
        print(current_message)

"""messages[:] below uses a copy of messages to retain the previous list"""
send_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)

#8.12 Sandwiches
def make_sandwiches(*args):
    print(args)

make_sandwiches('ham', 'club', 'cheese')

#8.13 User Profile
def build_profile(first, last, **user_info):
    """Build a dictionary of everything we know about the user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile('Will', 'Lam', fav_hobby= 'run', fav_team= 'UNC', fav_movie= 'Good Will Hunting')
print(my_profile)

#8.14 Cars
def build_car(manufacturer, model, **kwargs):
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs

my_car = build_car('Honda', 'Accord', color = 'Silver', sport = True)
print(my_car)

