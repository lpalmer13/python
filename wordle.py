print('Welcome to the word guessing game!')
print()
print('Your hint is: _ _ _ _ _ _ ')

word = 'mosiah'
guess = input('What is your guess? ')
number_of_letters = len(word)
count = 0
while guess != word:
    guess = input('What is your guess? ').lower()
    # if guess != word:
    #     print('Your guess was not correct.')
    #     count += 1
    # elif guess == word:
    #     print('Your guess was correct.')
    #     count += 1

    for i in range(number_of_letters):
        if word[i] == guess:
            print(word[i].upper(), end='')
            print('_', end='')
        else:
            print(word[i], end='')
            print('_', end='')
print()
print(f'Congratulations! You guessed it in {count} times!')
    
