#Names of friends
names = ['ian', 'alice', 'anna', 'hannah', 'maria']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[-1])

#Greetings
for g in names:
    print(f'welcome to my humble adobe {g}')

# Your own List
transport_mode= ['car','bus', 'metro', 'subway']
messege = f"I would like to own an Audi {transport_mode[0].title()}."
print(messege)

#Guest List
guest_names = ['Moses', 'Mary', 'Ruth', 'The Romanov', 'Hitler', 'Queen Elizabeth II']
for guest in guest_names:
    print(f'{guest}, are cordially invited to the extravegant dinner')

#Changing Guest List
unavailable_guesy = guest_names.pop(4)
print(f'Unfortunetly, {unavailable_guesy.title()} cannot make it')
guest_names.insert(4, 'Alexander the Great')
for guest in guest_names:
    print(f'{guest}, are cordially invited to the extravegant dinner')


#More Guest
guest_names.insert(0, 'Jesus')
guest_names.insert(4, 'Augustus')
guest_names.append('Julius Caesar')
for guest in guest_names:
    print(f'{guest}, are cordially invited to the extravegant dinner')

#Shrinking Guest List
print("Apologies, I am able to invite only two people for dinner")
i = 2
while i < len(guest_names):
    univited_guest = guest_names.pop()
    print(f"Apologies, I receend my invite from {univited_guest} to dinner")
for guest in guest_names:
    print(f'{guest}, are cordially invited to the extravegant dinner')
del guest_names[1]
del guest_names[0]
print(guest_names)

#Seeing the world
placses = ['seoul', 'cairo', 'vienna', 'stockholm', 'tokyo', 'beijin']
print(placses)
print(sorted(placses))
print(placses)
placses.reverse()
print(placses)
placses.reverse()
print(placses)
placses.sort()
print(placses)
placses.sort(reverse=True)
print(placses)

#Dinner Guest
print(len(univited_guest))
print(len(guest_names))

#Every function
lists = ['english', 'italian', 'spanish', 'french', 'korean']
print(sorted(lists))
lists.reverse()
print(lists)
lists.sort()
print(lists)
print(lists[0])
print(lists[1])
mother_language = lists.pop(1)
print(mother_language)








