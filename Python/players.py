#Slicing
players = ['charles', 'martina', 'micheal', 'florance', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

#Looking Through a Slice
players = ['charles', 'martina', 'micheal', 'florance', 'eli']
for player in players[:3]:
    print(player.title())

#Copy a List
my_foods = ['pizza', 'felafe', 'carrot cake']
friend_foods = my_foods[:]
#this doesn't work
#friend_foods =  my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favourite foods are:")
print(my_foods)

print("n\My favourite foods are:")
print(friend_foods)



