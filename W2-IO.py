name = 'Levi'
surname = 'Palmer'
print()
print('1 ' + name + ' ' + surname)
print('2 {} {}' .format(name, surname))
print('3 {0} {1}' .format(name, surname))
print(f'4 {name} {surname}')
full_name = f'5 {name}, {surname}'
print(full_name)
print('6', name, ',', surname)

words = '''this is a
really long sentence!'''

print(words.upper())
print(words.lower())
print(words.capitalize())
print(words.title())
print(words.title().upper().count('L'))
words = input(print('what is your name: '))
print(words)