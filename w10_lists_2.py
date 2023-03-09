movies = [
    "Batman",
    "Interstellar",
    "Hot Rod",
    "Inception"
]

votes = [11, 2, 1, 2]

# Adding items to a list
movies.append("Iron Man")
votes.append(13)
movies.insert(0, "Dune")
votes.insert(0, 6)

# Removing items from a list
movies.pop(4)
print(f'After removes: {movies}')
movies.pop()
movies.remove("Batman")

print(f'After removes: {movies}')

print()
print("Movies in the list:")
# print(f'Length of movies is:{len(movies)} so we are looping with "for i in range({len(movies)})')
for i in range(len(movies)):
    # print(i)
    movie = movies[i]
    vote_count = votes[i]
    print(f'  {i + 1} -{movie} with {vote_count}')
    # print(f'  -{movies[i]}')
# print(movies)
# to_remove = int(input("Which movie to remove? "))
# movies.pop(to_remove - 1)
# print(movies)

to_update = int(input('Which movie to change? '))
new_name = input('What is the new movie title? ')
movies[to_update - 1] = new_name
print(movies)
