do_if = input('Should I do it? ')
if do_if.upper() == 'yes':
    print('Ok, I did it! ')
if do_if == 'yes':
    print('You answered in lower case, and I did it. ')
elif do_if.lower() == 'maybe':
    print('Well, let me know when you know for sure. ')

answer = input('Should I do it? ').lower()
how_many_times = int(input('How many times?'))
if (answer == 'yes' or answer == 'maybe') and (how_many_times == 1 or how_many_times > 10):
    print(f'I did it\n' * how_many_times)

print()
print('Welcome to the Running Decision Maker')
temp = float(input('What is the temperature outside? '))
if temp >= 55:
    if temp >= 65:
        print('You should probably go running')
    else:
        is_raining = input('Is it raining outside? ')
        if is_raining.lower() == 'yes':
            print('You should NOT go running!')
        else:
            print('You should probable go running')
else:
    print('You shoud NOT go running!')
