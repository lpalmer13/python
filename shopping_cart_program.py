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

cart = []
prices = []
total_quantity = []
total_cost = []

while selection != 5:
    if selection > 5:
        print()
        print("Please only select a number between '1' and '5'. ")

    print()
    print('Please select one of the following: ')
    
    for item in shopping_cart:
        print(f'{item}')
    
    selection = int(input('Please enter an action: '))

    if selection == 1:
        print()
        add = input('What item would you like to add? ')
        price = float(input(f"What is the price of '{add}'? $"))
        quantity = int(input('How many do you want? '))
        total_price = (price) * (quantity)
        
        cart.append(add)
        prices.append(price)
        total_quantity.append(quantity)
        total_cost.append(total_price)

        print(f"'{add}' has been added to the cart.")

    elif selection == 2:
        print()
        print('The contents of the shopping cart are:')
        for i in range(len(cart)):
            total_price = total_cost[i]
            quantity = total_quantity[i]
            price = prices[i]
            add = cart[i]
            print(f'{i + 1}. {add} x{quantity} - ${total_price:.2f}')

    elif selection == 3:
        print()
        print('The contents of the shopping cart are:')
        for i in range(len(cart)):
            total_price = total_cost[i]
            quantity = total_quantity[i]
            price = prices[i]
            add = cart[i]
            print(f'{i + 1}. {add} x{quantity} - ${total_price:.2f}')

        print()
        remove = int(input('Which item would you like to remove? '))
        for i in range(len(cart)):
            item = total_cost[i]
            item = total_quantity[i]
            item = prices[i]
            item = cart[i]
        cart.pop(remove - 1)
        prices.pop(remove - 1)
        total_quantity.pop(remove - 1)
        total_cost.pop(remove - 1)
        print(f"'{item}' has been removed from cart.")

        print()
        print('The contents of the shopping cart are:')
        for i in range(len(cart)):
            total_price = total_cost[i]
            quantity = total_quantity[i]
            price = prices[i]
            add = cart[i]
            print(f'{i + 1}. {add} x{quantity} - ${total_price:.2f}')

    elif selection == 4:
        print()
        subtotal = 0
        for number in total_cost:
            subtotal += number
        print(f'The subtotal price of the items in the shopping cart is ${subtotal:.2f}')
        print()
        sales_tax_rate = int(input('What is the sales tax rate? '))
        sales_tax = (sales_tax_rate * 0.01) * (subtotal)
        total = (subtotal + sales_tax)
        print()
        print(f'The total price of the items in the shopping cart with tax is ${total:.2f}')
    
    elif selection == 5:
        print()
        print('Thank you. Goodbye.')
        print()