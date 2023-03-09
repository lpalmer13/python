print('Welcome to the Shopping Cart Program!')
print()

shopping_cart = []
shopping_cart.append('1. Add item')
shopping_cart.append('2. View cart')
shopping_cart.append('3. Remove item')
shopping_cart.append('4. Compute total')
shopping_cart.append('5. Quit')


selection = 0
selections = []
while selection != 5:
    print('Please select one of the following: ')
    for item in shopping_cart:
        print(f'{item}')
    
    selection = int(input('Please enter an action: '))
    add = input('What item would you like to add? ')
    if selection == 1:
        print(add)
        print(add + ' has been added to the cart.')