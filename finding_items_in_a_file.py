largest_number_of_chapters = 0
largest_book = ''

with open("python/books_and_chapters.txt") as data:
    for line in data:
        line = line.strip()
        line = line.split(':')
        book = line[0]
        chapter = int(line[1])
        scripture = line[2]
        print(f'Scritpture: {scripture}, Book: {book}, Chapter: {chapter}')
        if largest_number_of_chapters < chapter:
            largest_number_of_chapters = chapter
            largest_book = book

    print(f'The book with the most chapters is: {largest_book}')
    print(f'It has {largest_number_of_chapters} chapters.')