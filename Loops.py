option = int(input('Would you like to:\n1) Go running\n2) Take a nap\n3) \
Eat ice cream/nOption( 1-3): '))

if option < 1 or option > 3:
    print('Please enter a 1, 2 or 3.')
    option = int(input('Would you like to:\n1) Go running\n2) Take a nap\n3) \
    Eat ice cream\nOption(1-3): '))

while True:
    print('Im Stuck')

end_char = '_'

word = 'mosiah'
print(word[2])
print(len(word))
i = 0
while i < len(word) - 1:
    print(word[i], end = end_char)
    i += 1 # i = i + 1
print()
print(word[3])