# # list = [12, 3,4, 45] #DON'T DO THIS!!!
# movies = list()
# movies = [
#     "Batman"
#     "Interstellar"
#     "Hot Rod"
#     "Inception"
# ]
# movies.append("Iron Man")
# print("Movies in the list:")
# for movies in movies:
#     print(f"\t-{movies}")
# print(movies)

print('Fast Food Menu Demo')

print()

menu = [
    '1 - Drink'
    '2 - Entree'
    '3 - Side'
    '4 - Dessert'
    '5 - Order Complete'
]

drinks = []
drinks.append('Guarana')
drinks.append('Water')
drinks.append('Root Beer')
drinks.append('lemonade')

entrees = [
    'Hamburger',
    'Hot Dog',
    'Chivito',
    'Pizza'
]

selection = 0
selections = []
while selection != 5:
    print("Menu")
    for item in menu:
        print(f' {item}')

    selection = int(input('What would you like to order? '))
    if selection == 1:
        print('For drinkds we have:')
        for drink in drinks:
            print(drink)
        selections.append(input('What would you like? '))
    if selection == 2:
        print('For drinkds we have:')
        for drink in drinks:
            print(drink)
        selections.append(input('What would you like? '))
    if selection != 5:
        selections.append(selection)

    print(f'You selected {selection}')
    print()