first_name = 'sharon'
last_name = 'akpan'
full_name = f'{first_name} {last_name}'
message = f"Hello, {full_name.title()}"
print(message)

#to add tab to the text
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#stripping right white space
favourite_language = 'python '
favourite_language.rstrip()
favourite_language = favourite_language.rstrip()

#stripping left white space
favourite_language1 = 'python '
favourite_language1.lstrip()
favourite_language1 = favourite_language1.lstrip()

#removing prefixes
nostarch_url = 'https://nostarch.com'
nostarch_url.removeprefix('https://')
simple_url = nostarch_url.removeprefix('https://')
print (simple_url)








