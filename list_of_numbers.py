print("Enter a list of numbers, type 0 when finished.")

numbers = []
number = None

while number != 0:
    number = int(input("Enter number: "))
    if number != 0:
        numbers.append(number)

sum = 0

for number in numbers:
    sum += number

print(f"The sum is: {sum}")

count = len(numbers)
average = sum / count

print(f"The average is: {average}")

largest_number = -1

for number in numbers:
    if number > largest_number:
        largest_number = number

print(f"The largest number is: {largest_number}")