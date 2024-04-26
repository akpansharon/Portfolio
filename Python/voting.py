age = 19
if age >= 18:
    print("ypu are old enough to vote")
    print("have you registered to vote")

#if-else statement
age = 17
if age >= 18:
    print("ypu are old enough to vote")
    print("have you registered to vote")
else:
    print("Sorry, you are too young to vote")
    print("Please register to vote as soon as you turn 18")

#amusement_park
age = 18
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $25")
else:
    print("Your admission cost is $40")

#amusement_park_2
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 45:
    price = 20
print(f"Your admission cost is ${price}")

#pizzeria
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms')
if 'pepperoni' in requested_toppings:
    print('Adding peperoni')
if 'extra cheese' in requested_toppings:
    print('adding extra cheese')
print("\nFinished making your pizza!")

#toppings
requested_toppings = ['mushrooms', 'extra cheese', 'green peppers']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry we are out of green peppers')
    else:
        print(f"Adding {requested_topping}.")  
print('\nFinish making your pizza')

#check list is empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f'Adding {requested_topping}')
    print('\nFinishing making your pizza')
else:
    print('Are you sure you want a plain pizza')

#multiple list
available_toppings = ['mushrooms', 'olives', 'green peppers', 
                      'peperoni', 'pineaple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}')
    else:
        print(f"Sorry, we don't have {requested_topping}")
print('\nFinish making your pizza')




