
#parrot
promt = "\t Tell me something and I will repeat it back to you: "
promt += "\nEnter 'quit' to end the program "
message = ""
while message != 'quit':
    message = input(promt)
    if message != 'quit':
        print(message)

#flag: acts as a signal to the program example: a program shoudl run only as long as many conditions are trye
promt = "\t Tell me something and I will repeat it back to you: "
promt += "\nEnter 'quit' to end the program "
active = True
while active:
    message = input(promt)
    if message == 'quit':
        print(message)
    else:
        print(message)

#cities
promt = "\t Please enter the name of a city you have cisited: "
promt += "\n(Enter 'quit' to end the program) = "

while True:
    city = input(promt)
    
    if city == 'quit':
        break
    else:
        print(f"i' love to go to {city.title()}!")
        
#counting
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

#infinite loops
x = 1
while x <=5:
    print(x)
    
#greeter
name = input("Please tell me your name: ")
print(f"\nHello, {name}") 

promt = "If you share your name, we cna personalise the message you see"
promt += "\n What is your first name? "
name = input(promt)
print(f"\nHello, {name}")

#age
age = input("How old are you? ")
print(type(age))
age =  int(age)
age >= 18

#rollercoster
height = input("How tall are you in inches? ")
height = int(height)

if height >= 48:
    print("You are tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're little older")

#The modulo operator(%) returns the remonter of the number which is divided by another number
#even or odd
number = input("Enter a number, and I'll tell you if it's even or odd ")
number = int(number)

if number % 2 == 0:
    print(f"The number {number} is even number")
else:
    print(f"The number{number} is an odd number")

#counting
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
    
#confirm_users
#start wit users that need to be verified
#and an empy list to hold confirmed users
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

#verify each users until there is no more confirmed users
#move each verified user into the list of confirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verify user: {current_user.title()}")
    confirmed_users.append(current_user)
#display all confirmed users
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#pets
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#mountain_polly
responses = {}
#set a flag to indicate that polling is active
polling_active = True
while polling_active:
    #promot for the person name and response
    name = input("\nWhat's your name? ")
    response = input("which mountain would you like to climb someday? ")
    #store the response in a dictionary
    responses[name] = response 
    #found out if anyone is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
#Polling is complete
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}")
    

