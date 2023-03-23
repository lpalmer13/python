youngest_age = 9999
youngest_person = ''

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

for person in people:
    parts = person.split()
    name = parts[0]
    age = int(parts[1])
    if age < youngest_age:
        youngest_age = age
        youngest_person = name
print(f'The youngest person is: {youngest_person} with an age of {youngest_age}')