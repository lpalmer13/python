low_vote = 'empty'
flop_movie = ''
high_votes = 0
hit_movie = ''
g_high = 0
g_movie = ''

user_genre = input('What genre would you like? ')

with open("python/w12-data.csv") as file:
    header = file.readline()
    header_parts = header.split(', ')
    for line in file:
        parts = line.strip().split(',')
        movie = parts[0].strip()
        votes = int(parts[1].strip())
        genre = parts[2].strip()
        print(parts)
        print(f"'{movie}'\t '{votes}'\t '{genre}'")

        if low_vote == 'empty' or votes < low_vote:
            low_vote = votes
            flop_movie = movie

        if high_votes > votes:
            high_votes = votes
            hit_movie = votes
        
        if genre.upper() == user_genre.upper():
            if g_high < votes:
                g_high = votes
                g_movie = movie

print(f'Flop movie is "{flop_movie}" with {low_vote}')
print(f'Hit movie is "{hit_movie}" with {high_votes} votes. ')
print(f'Hit movie for {user_genre} is "{g_movie}"  with {g_high} votes. ')