first_rider_age = int(input('What is the age of the first rider? '))
first_rider_height = int(input('What is the height of the first rider? '))
second_rider = input('Is there a second rider (yes/no)? ')
if first_rider_age >= 18:
    print('Welcome to the ride. Please be safe and have fun!')
elif second_rider == 'no':
    if first_rider_height <= 62:
        print('Sorry, you may not ride. ')
else:
    print('Sorry, you may not ride. ')
second_rider_age = int(input('What is the age of the second rider? '))
second_rider_height = int(input('What is the height of the second rider? '))
if second_rider_height < 36:
    print('Sorry, you may not ride. ')
elif second_rider_height >= 36:
    print('Welcome to the ride. Please be safe and have fun!')
else:
    print('Sorry, you may not ride. ')