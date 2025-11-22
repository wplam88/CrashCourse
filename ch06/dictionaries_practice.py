"This exercise works with dictionaries"

#6.1 Person
# need to fix to print values
Person = {'first_name': 'Preston', 'last_name': 'Lam', 'age': '21','city': 'Chicago'}
for k, v in Person.items():
    print(f'\nKey:{k}')
    print(f'Value:{v}')

#6.2 Favorite Numbers
favorite_numbers = {'Preston': 7, 'Will': 88, 'Dad': 72, 'Mom': 4}
for k, v in favorite_numbers.items():
    print(f'\nKey:{k}')
    print(f'Value:{v}')

#6.34 Glossary
glossary = {
    'if': 'conditional', 
    'elif': 'else if', 
    '0 indexing': 'indexes start at 0, not 1', 
    'list comprehension': 'syntax: list_name = [value_operation for value in range(start(inc):end(exc)) ]'
}

for term, definition in glossary.items():
    print(f'\n{term}')
    print(definition)

#6.5 Rivers
rivers = {'nile': 'egypt', 'tigis': 'turkey', 'euphrates': 'turkey'}
for river, country in rivers.items():
    print(f'\nThe {river.title()} runs through {country.title()}')

#6.6 Polling
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil': 'python'}
should_take_poll = ['jen', 'peter', 'piper']
for name in should_take_poll:
    if name == favorite_languages:
        #why is this not working
        print(f'\nThanks {name}, thanks for taking the poll')
    else:
        print(f'\nThanks {name}, please take the poll')

#6.7 People
person_0 = {'first_name': 'Preston', 'last_name': 'Lam', 'age': '21','city': 'Atlanta'}
person_1 = {'first_name': 'Will', 'last_name': 'Lam', 'age': '24','city': 'Charlotte'}
person_2 = {'first_name': 'Santi', 'last_name': 'Checa' , 'age': '24','city': 'Boston'}

people = [person_0, person_1, person_2]

for person in people:
    print(person)

#6.8 Pets
pet_0 = {'animal': 'dog', 'name': 'gemma', 'owner': 'kurt'}
pet_1 = {'animal': 'dog', 'name': 'pancho', 'owner': 'travis'}
pet_2 = {'animal': 'dog', 'name': 'sarge', 'owner': 'mason'}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(pet)

#6.9 Favorite Places
favorite_places = {
    'will': {
        'first': 'sycamore',
        'second': 'atlanta',
        'third': 'chicago'
    },

    'preston': {
       'first': 'raleigh',
        'second': 'boone',
        'third': 'wilmington' 
    },

    'dad': {
       'first': 'raleigh',
        'second': 'wilmington',
        'third': 'europe' 
    }
}

for name, places in favorite_places.items():
    print(f'\nName: {name.title()}')
    print(f'\t1st: {places['first'].title()}')
    print(f'\t2nd: {places['second'].title()}')
    print(f'\t3rd: {places['third'].title()}')

#6.10 Favorite Numbers
#why does this work but keep telling me incompatible types
favorite_numbers = {
    'will': {
        'first': 88,
        'second': 4
    },

    'preston': {
       'first': 12,
        'second': 7
    },

    'dad': {
       'first': 72,
        'second': 81
    }
}
for name, numbers_ranked in favorite_numbers.items():
   print(name.title())
   print(numbers_ranked['first'])
   print(numbers_ranked['second'])