#Dictionaires is a collection of key value pair
#a key value pair is a pair associated with each other
alien_0 = {'color': 'green', 'points': 5}
alien_1= {'color':'pink'}
print(alien_0['color'])
print(alien_0['points'])

new_points = (alien_0['points'])
print(f'You just earned {new_points} points!')
print(alien_0)

alien_0['x_position'] = 0
alien_0['y-position'] = 25
alien_0['speed'] = 'fast'
print(alien_0)
print(f'Original position: {alien_0["x_position"]}')

# Move the alien to the right
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed']  == 'medium':
    x_increment = 2
else:
    #this must be a fast elien
    x_increment = 3

#The new position is the olf position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

#starting with an empy dictionary
alien_2 = {}
alien_2['color'] = 'pink'
alien_2['points'] = 10
print(alien_2)

#modifying value in dictonary
alien_2['color'] = 'blue'
print(f'The alien is now {alien_2["color"]}')
print(alien_2)

#removing key value pairs
#IMPORTANT the deleted key value pair is removed permently
del alien_0['points']
print(alien_0)

#favourite languages
favourite_languges = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python',
    'sharon': 'python',
}
language = favourite_languges['sharon'].title()
print(f"Sharon's favourite language is {language}")

#another way of doing favourite languages exercise
for name, language in favourite_languges.items():
    print(f"\n {name.title()}'s favourite language is {language.title()} ")
for name in favourite_languges.keys():
    print(name.title())

#print message to a couple of friends about the language they choose
friends = ['phil', 'sarah']
for name in favourite_languges.keys():
    print(f"Hi, {name.title()}")
    if name in friends:
        language = favourite_languges[name].title()
        print(f"\t{name.upper()}, I see you love {language}")

#find out if a particular person or item was polled
if 'erin' not in favourite_languges.keys():
    print("Erin, please take our poll")

#looping through a dictionary's key in a particular order
for name in sorted(favourite_languges.keys()):
    print(f"{name.title()}, thank you for taking the poll")
    
#looping thoufh all values in a dictionary
print("the following languages have been mentioned:")
for language in favourite_languges.values():
    print(language.title())
    
#using a set is a collection in which each item must be unique
for language in set(favourite_languges.values()):
    print(language.title())
    
favourite_languges = {
    'jen' : ['python', 'rust'],
    'sarah' : ['c'],
    'edward' : ['rust', 'go'],
    'phil' : ['python', 'haskell'],
    'sharon': ['python', 'javascript'],
}

#using 2 loops to run though the list of languages associated with each person
for name, languages in favourite_languges.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
       print(f"\t{language.title()}")

#using get to access values 
point_value = alien_0.get('points', 'No points value assigned')
print(point_value)

#nesting store mutiple dictionary in a list or a list of items as a value in a dictionary
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

#make en empty list for storing aliens
aliens = []

#make 30 green aliens
for alien_number in range(30):
    new_alien = {'color':'green', 'points': 5, 'speed':'slow' }
    aliens.append(new_alien)
    
#change the first 3 aliens to yello, medium speed aliens worth 10 points each
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    #expanding adding elif statement 
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
    
#show the first 5 aliens
for alien in aliens[:10]:
    print(alien)
print('...')

#Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")

#store information about a pizza being ordered
pizza = {
    'crust':'thick',
    'toppings':['mushrooms', 'extra cheeses'],
}
#summerize the order
print(f'You ordered a {pizza["crust"]}-crust pizza'
      'with the following toppings:')
for topping in pizza['toppings']:
    print(f'\t{topping}')
    
#many users
users ={
    "aeinstein":{
        'first':'albert',
        'last':'eistein',
        'location':'princenton'
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")