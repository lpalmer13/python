print('Please enter the items of the shopping list (type: quit to finish):')

list = []
item = ''

while item != 'quit':
    item = input('Item: ')
    if item != 'quit':
        list.append(item)

print()
print('The shopping list is:')

for item in list:
    print(item)

print()
print('The shopping list with indexes is:')

for i in range(len(list)):
    item = list[i]
    print(f'{i + 1}. {item}')

print()

change = int(input('Which item would you like to change? '))
new = input('What is the new item? ')
list[change] = new

print()
print('The shopping list with indexes is:')

for i in range(len(list)):
    item = list[i]
    print(f'{i}. {item}')
    
print()