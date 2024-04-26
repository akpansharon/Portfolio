#person
person = {
    'first name':'Cleopatra',
    'last name': 'Thea Philopator',
    'age': 20,
    'POB':'Alexandria',
    'COB':'Egypt',
}
print(person['first name'])
print(person['last name'])
print( person['age'])
print(person['POB'])
print(person['COB'])

#favorite number
favorite_number ={
    'mac':'2',
    'leo':'56',
    'ruth': '36',
    'valerie': '100',
    'kate': '25',
}
print(favorite_number)

#Glossery
glossery = {
    'IDLE' : "is a text editor that's included with Python",  
    'Conditional statement' : 'an expression that can be evalueted as True or False',
    'Tuple' : 'Unmodifiable list',
    'pop' : 'removes last item in a list',
    'float': 'number with a decimal point',
    'set': ' is a collection in which each item must be unique',
    'sort': "it allows you to sort list in alphabetical order",
    'dictionary': 'is a colleciton of key value pairs'
    
}

word = glossery['IDLE'].title()
word1 = glossery['Conditional statement'].title()
word2 = glossery['Tuple'].title()
word3 = glossery['pop'].title()
word4 = glossery['float'].title()
print(f"IDLE: {word}")
print(f"Conditional statement: {word}")
print(f"Tuple: {word}")
print(f"pop: {word}")
print(f"float: {word}")

#another way of doing the same exercise
for key, value in glossery.items():
    print(f'\nWord: {key.title()}')
    print(f'Meaning: {value.capitalize()}')

#rivers
rivers ={
    'nile': 'egypt',
    'amazon river': 'peru',
    'yamgtze river': 'china',
    'mississipi river': 'america',
    'yenisei river': 'russia',
}
for river, country in sorted(rivers.items()):
    print(f"\nThe {river.title()} runs through {country.title()}")
    
for river in rivers:
    print(f"Here are all the names of each river: {river.title()}")

for country in rivers:
    print(f"Here are all the name of the country the rivers flow through: {country.title()}")
    
#polling
favourite_languges = {
    'claire' : 'javasctipt',
    'micheal' : 'c++',
    'kate' : 'java',
    'luke' : 'python',
    'carmen':'c++',
    'irene': 'python',
    'carmen':'python'
}
new_names = ['irene', 'kate', 'luke', 'carmen','sasha']
for name in favourite_languges.keys():
    if name in new_names:
        language = favourite_languges[name].title()
        print(f"{name.title()}, thank you for responding")
    else:
        print(f"{name.title()}, please take the poll, is not that hard")

#people
people ={
    'ctheaphilopator':{
        'first':'cleopatra',
        'last':'thea philopator',
        'location':'egypt',
    },
    'aboleyn':{
        'first':'anne',
        'last':'boleyn',
        'location':'england',
    },
    'zseptimia ':{
        'first':'zenobia',
        'last':'septimia',
        'location':'siria',
    }
}
for person, person_details in people.items():
    print("\nHere is the Person ddetails:"
          f"Person username: {person}")
    full_name = f"{person_details['first']} {person_details['last']}"
    location = f"{person_details['location']}"
    print(f"\tFull Name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    
#pets
pet_cat ={
    'pet_name':['Bobby'],
    'family':['Felidae'],
    'owner_details':['wilma', 'cameron'],
    'vaccinated':['yes'],},
pet_dog={
    'pet_name':['Charlie'],
    'family':['Canidae'],
    'owner_details':['max', 'arabella'],
    'vaccinated':['yes'],
    },
pet_fish={
    'pet_name':['Ruby'],
    'family':['Cyprinidae'],
    'owner_details':['dean', 'riddle'],
    'vaccinated':['yes']},
pet_horse={
    'pet_name':['Livia'],
    'family':['Equus caballus'],
    'owner_details':['bailey', 'haney'],
    'vaccinated':['not needed']},

pets = [pet_cat, pet_dog, pet_fish, pet_horse]
for pet in pets:
    print(pet)
    
#favourite places
favourite_places ={
     'lilly':['library', 'coffe shops', 'park'],
     'eboby':['church', 'book shop', 'museaum'],
     'trevor':['gym','cinema', 'park'],
    }
for name, places in favourite_places.items():
    print(f"{name.title()}'s favourate place are:")
    for place in places:
        print(f"\t{place.title()}")

#favourite number 2.0
favorite_numbers ={
    'mac':['23','2'],
    'leo':['56','34','65'],
    'ruth': ['36','67','1'],
    'valerie': ['1','2','100'],
    'kate': ['5','10','25','50'],
}
for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favourite number are:")
    for number in numbers:
        print(f"\t{number}")
#cities
cities ={
    'venezia':{
        'country':'Italy',
        'population': '261.905',
        'fact': 'The city rests on 118 islands separated by 150 canals.',
    },
    'london':{
        'country':'United Kingdom',
        'population': '8.982 million',
        'fact': 'The City of London is the smallest city in the UK.',
        
    },
    'vienna':{
        'country':'Austria',
        'population': '1.897 million',
        'fact': 'Vienna invented the snow globe',
    },
}
for city, info in cities.items():
    print(f"City Name: {city.title()}"),
    country = f"{info['country']}"
    population = f"{info['population']}"
    fact = f"{info['fact']}"
    
    print(f"This city is in {country.title()}")
    print(f"It has {population} in population and"
          f"and here is a fun fact {fact}")

        