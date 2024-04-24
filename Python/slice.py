#Slices
my_foods = ['pizza', 'pasta', 'tteokbokki', 'Gimbap', 'Japchae', 'Soju']
print("The first three items in the list are:")
print(my_foods[0:3])
print("The middle three items in the list are:")
print(my_foods[2:3])
print("The last three items in the list are:")
print(my_foods[-3:])

#My pizza, Your Pizza
pizzas = ['margerita', 'prosciutto funchi', 'carbornara']
friend_pizza = pizzas[:]
pizzas.append('sgombri e frutti di mare')
friend_pizza.append('legumi')
print("My favourite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My freind favourite pizzas are:")
for pizza in friend_pizza:
    print(pizza)

#More Loops
my_foods = ['pizza', 'felafe', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favourite foods are:")
for food in my_foods:
    print(food)
print("My freind favourite food are:")
for food in friend_foods:
    print(food)
