do_if = input('Should I do it? ')
if do_if.upper() == 'yes':
    print('Ok, I did it! ')
if do_if == 'yes':
    print('You answered in lower case, and I did it. ')
elif do_if.lower() == 'maybe':
    print('Well, let me know when you know for sure. ')
print()
print('Welcome to the Running Decision Maker')
temp = float(input('What is the temperature outside? '))
if temp >= 55:
    if temp >= 65:
        print('You should probably go running')
