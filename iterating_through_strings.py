word = input('What is your favorite word? ').lower()

letter = input('What is your favorite letter? ').lower()

for x in range(len(word)):
    if word[x] == letter:
        print(word[x].upper(), end='')
        print('_', end='')
    else:
        print(word[x], end='')
        print('_', end='')
print()