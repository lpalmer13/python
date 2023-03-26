max_life_expectancy = 0
min_life_expectancy = 9999
max_life_expectancy_country = ''
min_life_expectancy_country = ''
max_life_expectancy_year = 0
min_life_expectancy_year = 9999
year_max_life_expectancy = 0
year_min_life_expectancy = 9999
country_max_life_expectancy = 0
country_min_life_expectancy = 9999
year_count = 0
year_life_expectancy = 0
country_count = 0
country_life_expectancy = 0

year_of_interest = int(input('Enter the year of interest: '))

with open("python/life-expectancy.csv") as data:
    for line in data:
        line = line.strip()
        items = line.split(',')
        country = items[0]
        code = items[1]
        year = int(items[2])
        life_expectancy = float(items[3])

        if max_life_expectancy < life_expectancy:
            max_life_expectancy = life_expectancy
            max_life_expectancy_country = country
            max_life_expectancy_year = year

        if min_life_expectancy > life_expectancy:
            min_life_expectancy = life_expectancy
            min_life_expectancy_country = country
            min_life_expectancy_year = year

    print()
    print(f'The overall max life expectancy is: {max_life_expectancy} from {max_life_expectancy_country} in {max_life_expectancy_year}')
    print(f'The overall min life expectancy is: {min_life_expectancy} from {min_life_expectancy_country} in {min_life_expectancy_year}')
    print()

with open("python/life-expectancy.csv") as data:
    for line in data:
        line = line.strip()
        items = line.split(',')
        country = items[0]
        code = items[1]
        year = int(items[2])
        life_expectancy = float(items[3])

        if year_of_interest == year:
            year_count += 1
            year_life_expectancy += life_expectancy
            if year_max_life_expectancy < life_expectancy:
                year_max_life_expectancy = life_expectancy
                year_max_life_expectancy_country = country

            if year_min_life_expectancy > life_expectancy:
                year_min_life_expectancy = life_expectancy
                year_min_life_expectancy_country = country

    year_average_life_expectancy = year_life_expectancy / year_count

    print()
    print(f'For the year {year_of_interest}:') 
    print(f'The average life expectancy across all countries was {year_average_life_expectancy:.2f}')
    print(f'The max life expectancy was in {year_max_life_expectancy} with {year_max_life_expectancy_country}')
    print(f'The min life expectancy was in {year_min_life_expectancy} with {year_min_life_expectancy_country}')
    print()

country_of_interest = input('Enter the country of interest: ')

with open("python/life-expectancy.csv") as data:
    for line in data:
        line = line.strip()
        items = line.split(',')
        country = items[0]
        code = items[1]
        year = int(items[2])
        life_expectancy = float(items[3])

        if country_of_interest == country:
            country_count += 1
            country_life_expectancy += life_expectancy
            if country_max_life_expectancy < life_expectancy:
                country_max_life_expectancy = life_expectancy

            if country_min_life_expectancy > life_expectancy:
                country_min_life_expectancy = life_expectancy

    country_average_life_expectancy = country_life_expectancy / country_count

    print()
    print(f'For the country {country_of_interest}:')
    print(f'The average life expectancy in {country_of_interest} is {country_average_life_expectancy:.2f}')
    print(f'The max life expectancy was {country_max_life_expectancy}')
    print(f'The min life expectancy was {country_min_life_expectancy}')
    print()