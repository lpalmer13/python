with open("python/life-expectancy.csv") as data:
    header = data.readline
    for line in data:
        line = line.strip()
        items = line.split(',')
        entity = items[0]
        code = items[1]
        year = items[2]
        life_expectancy = items[3]
        print(f'{entity} {code} {year} {life_expectancy}')