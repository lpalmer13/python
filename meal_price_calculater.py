print('Welcome to the meal price calculator program!')
print()

appetizer = float(input("What is the price of an appetizer? "))

childs_meal = float(input("What is the price of a child's meal? "))

adults_meal = float(input("What is the price of an adult's meal? "))

small_drink = float(input('What is the price of a small drink? '))

large_drink = float(input('What is the price of a large drink? '))

dessert = float(input("What is the prise of a dessert? "))

children = int(input("How many children are there? "))

adults = int(input("How many adults are there? "))

sales_tax_rate = int(input("What is the sales tax rate? "))

print()
subtotal = (appetizer) + (childs_meal + small_drink) * (children) + (adults_meal + large_drink) * (adults) + (dessert)
print(f'Subtotal: ${subtotal}')
sales_tax = (sales_tax_rate * 0.01) * (subtotal)
print(f'Sales Tax: ${sales_tax:.2f}')
total = (subtotal + sales_tax)
print(f'Total: ${total:.2f}')

print()
payment_amount = float(input(f'What is the payment amount? '))
change = (payment_amount - total)
print(f'Change: ${change:.2f}')