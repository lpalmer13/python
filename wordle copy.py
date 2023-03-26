print('Welcome to the word guessing game!')
print()
print('Your hint is: _ _ _ _ _ _ ')

word = 'mosiah'
guess = '_ _ _ _ _ _'
number_of_letters = len(word)
count = 0
while guess != word:
    print()
    guess = input('What is your guess? ').lower()
    count += 1

    for i in range(number_of_letters):
        w = word[i]
        g = guess[i]
        if word[i] == guess[i]:
            print(word[i].upper(), end=' ')
        elif g in word:
            print(g.lower(), end=' ')
        else:
            print('_', end=' ')
            
print()
print(f'Congratulations! You guessed it in {count} times!')