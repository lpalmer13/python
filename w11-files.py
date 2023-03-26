# .strip()
test_string = "\ttest\n".strip()
print(test_string)
print(test_string.strip())

# .split()
split_test = "This is a really long string with spaces"
split_reasult = split_test.strip().split(',')
for entry in split_reasult:
    print(f'"{entry.strip()}"')
print(split_reasult)

data = [
    "Chivito, 2",
    "Pizza, 2",
    "French Fries, 3"
]

total = 0
# with open("/Users/levipalmer/Desktop/Visual Studio Code/python/data.csv") as data:
with open("python/data.csv") as data:
    header = data.readline
    for entry in data:
        items = entry.split(',')
        food = items[0]
        qty = int(items[1].strip())
        total += qty
        print(f'{food} - {qty}')

print(f"Total items ordered: {total}")

print()
print()
with open("python/data2.py") as file:
    for line in file:
        print(line.strip())
print()