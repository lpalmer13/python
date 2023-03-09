print('Enter the names and balances of bank accounts (type: quit when done)')

accounts = []
balances = []

account = ''

while account != 'quit':
    account = input('What is the name of this account? ')
    if account != 'quit':
        balance = float(input('What is the balance? '))
        accounts.append(account)
        balances.append(balance)

total = 0

print()

print("Account Information:")
for i in range(len(accounts)):
    print(f'{accounts[i]} - ${balances[i]}')
    total += balances[i]
average = total / len(balances)
print()
print(f'Total: ${total:.2f}')
print(f'Average: ${average:.2f}')

print()

highest_account = ''
highest_balance = -1

for i in range(len(accounts)):
    account = accounts[i]
    balance = balances[i]

    if balance > highest_balance:
        highest_balance = balance
        highest_account = account

print(f'Highest balance: {highest_account} - ${highest_balance:.2f}')

change = 'yes'

while change == 'yes':
    change = input('Do you want to update an account? ')

    print()

    if change == 'yes':
        index = int(input('What account index do you want to update? '))
        new = float(input('What is the new amount? '))

        balances[index] = new

    print()

    print('Account Information:')

    for i in range(len(accounts)):
        print(f'{i}. {accounts[i]} - ${balances[i]:.2f}')

print()