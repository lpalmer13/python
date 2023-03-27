# tithe = 20
# def get_income():
#     income = float(input('What is your income? '))

# def compute_tithing():
#     income = float(input('What is your income? '))
#     tithe = 0.1 * income
#     return tithe

# # print(compute_tithing(200))
# # print(compute_tithing(150))
# # print(compute_tithing(0.35))
# print(compute_tithing(get_income()))

def ask_yes_no(prompt, affirmative = 'YES', negative = 'NO'):
    response = ''
    while response != affirmative.upper() and response != negative.upper():
        response = input(f'{prompt} ({affirmative.upper()})')
        if response == 'YES':
            return True
        elif response == 'NO':
            return False
        else:
            print('Response not recognized, please repond with only YES or NO')

is_raining = ask_yes_no('Is it raining? ')
if is_raining:
    print('DON\'T GO RUNNING')
else:
    print('Maybe you should go running')