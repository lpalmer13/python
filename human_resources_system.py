with open("python/hr_system.txt") as data:
    header = data.readline
    for line in data:
        line = line.strip()
        items = line.split(' ')
        name = items[0]
        id_number = items[1]
        job_title = items[2]
        print(f'Name: {name}, Title: {job_title}')
        
with open("python/hr_system.txt") as data:
    header = data.readline
    for line in data:
        line = line.strip()
        items = line.split(' ')
        name = items[0]
        id_number = items[1]
        job_title = items[2]
        salary = float(items[3])
        paycheck = salary/24
        if job_title.lower() == 'engineer':
            paycheck += 1000
        print(f'{name} (ID: {id_number}), {job_title} - ${paycheck:.2f}')