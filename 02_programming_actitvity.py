print('Please enter the following information:')
print()
name = input ('First name: ')
surname = input ('Last name: ')
email = input ('Email address: ')
phone = input ('Phone number: ')
job = input ('Job title: ')
id = input ('ID Number: ')
print()
print('The ID Card is: ')
print('----------------------------------------')
print(f'{surname.upper()}, {name.capitalize()}')
print(job.title())
print(f"ID: {id}")
print()
print(email.lower())
print(phone)
print('----------------------------------------')