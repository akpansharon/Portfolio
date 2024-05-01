""" 
#rental_car
car = input("What kind of car are you looking for? ")
print(f"Let me see if I can find you the, {car}")

#restaurant seating
greetings = input("Welcome asteemed guess, how many people are in the dinner group? ")
greetings = int(greetings)
if greetings >= 8 :
    print("Apologies, because of the number of guess, you will have to wait for a table")
else:
    print(f"Great, there is a table avaible for the {greetings} of you!")

#multiple of ten
number = input("please enter a number: ")
number = int(number)

if number % 10 == 0:
    print("This number is muipliable by 10")
else:
    print("this number is not multipliable by 10")

#pizza toppings

promt = "\tPlease enter the desire topping"
promt += "\nEnter 'quit' to end the program "
topping = ""
while topping != 'quit':
    topping = input(promt) 
    if topping != 'quit':
        print(f" I will be adding the {topping} to your pizza")
        break

#movie tickets
promt = ("How old are you? ")
promt += "\nEnter 'quit' to end the program "
age = ""
while True:
    age = input(promt)
    age = int(age)
    if age <= 3:
        print("Because you're less than 3, the ticket is free")
    elif age > 3 and age <=12:
        print("The movie ticket is $10")
    else:
        print("The movie ticket is $15")   

#Deli
sandwich_order = ['chiken sandwich', 'egg sandwich', 'seafood sandwich', 'roasted beef', 'grilled cheese sandwich',
                  'ham and cheese sandwich', 'nutella sandwich', 'grilled chiken sandwich']
finished_sandwichs = []
while sandwich_order:
    current_sandwich = sandwich_order.pop()
    print(f"I made you {current_sandwich}")
    finished_sandwichs.append(current_sandwich)
#print the completed finished order
print("\nHere are the list of the sandwich that have been completed: ")
for finished_sandwich in finished_sandwichs:
    print(finished_sandwich)
"""
#Dream Vacation
responses ={}
polling_active = True
while polling_active:
    name  = input("\n What's your name? ")
    response = input("If you could visit one place in the world, where would you go? ")
    responses[name] =  response
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to go to {response.title()}")
     





