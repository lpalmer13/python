print('Welcome to the word guessing game!')
print()
answer = 'mosiah'
your_guess = ''
count = 1
while your_guess != answer:
    your_guess = input('What is your guess? ')
    if your_guess != answer:
        print('Your guess was not correct.')
        count += 1
    elif your_guess == answer:
        print('Your guess was correct.')
        count += 1
print(f'Congratulations! You guessed it in {count} times!')