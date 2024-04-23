motorcycles = ['honda', 'yamaha', 'suziki']
print(motorcycles)

#modifying elements in a list
motorcycles[0] = 'ducati'
print(motorcycles)

#Adding Elements to a List
motorcycles.append('honda')
print(motorcycles)

#Adding Elelements to an Empty List
car = []
car.append('Audi')
car.append('Mercedes')
car.append('Fiat')
car.append('Ford')
print(car)

#Inserting Elements to a List
motorcycles.insert(0, 'kawasaki')
print(motorcycles)

#Removing Elements to a List
del motorcycles[0]
print(motorcycles)

#Removing Elements Item Using the pop() Method
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

#Popping Items from Any Position in a List
first_owned = motorcycles.pop(0)
print(f"The last motorcycle I owned was a {first_owned.title()}.")

#Remove an Item by Value
car.remove('Audi')
print(car)

#Remove an Item by Value-2
too_expensive = 'Mercedes'
car.remove(too_expensive)
print(car)
print(f"\nA {too_expensive.title()} is too expensive for me")



