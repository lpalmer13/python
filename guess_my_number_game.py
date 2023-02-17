from random import randint
play_again = 'yes'
while play_again == 'yes':
    magic_number = randint(1,100)
    guess = 0
    count = 0
    while guess != magic_number:
        guess = int(input('What is your guess? '))
        if guess > magic_number:
            print('Lower')
            count += 1
        elif guess < magic_number:
            print('Higher')
            count += 1
        else:
            print('You guessed it!')
            count += 1
    print(f'You guessed the number in {count} times.')
    play_again = input('Would you like to play again? (yes/no) ').lower()
print('Thanks for playing.')