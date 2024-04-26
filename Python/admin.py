#Hello Admin and No User
usernames = ['admin', 'apple94', 'luna86', 'alba76', 'mitch243']
if usernames:
    for username in usernames:
        if username == 'admin':
            print(f'hello {username}, would you like to see a status report')
        else:
            print(f'Hello {username}, thank you for loggin in again')
else:
    print('Please log in using your username')

#cheecking usernames
correct_users = ['admin', 'apple94', 'luna86', 'alba76', 'mitch243', 'lulu']
new_users = ['captain503', 'cider49913', 'moon573', 'dawn876', 'clack5286', 'lulu']
for user in new_users:
    if user in correct_users:
        print(f'Please enter a new username as {user} is already in use')
    else:
        print(f'The username: {user} is avaible to be used')

#ordinary numbers
numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if  number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')
        



