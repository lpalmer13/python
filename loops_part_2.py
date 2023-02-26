word = "secret"

# for x in [1, 2, 3, 4]:
#     for x in "secret":
#         print(x)
# print()

# i = 0
# while i < len(word):
#     print(word[i])
#     i += 1

# print(word)
# for letter in word:
#     print(letter)
# print(word)

# for x in range(1, 70, 5):
#     total = 0
#     print(x)
#     total = total + x

# print(total)

# import random
# letters = "abcdefghijklmnopqrstuvwxyz"
# for letter in range(len(word)):
#     for col in range(len(word)):
#         if row == col:
#             print(word[row], end = " ")
#         else:
#             print(" ", end=" ")
#     print()
#     print(f'row: {row}, col: {col}')

for letter in word:
    print(letter)
for i in range(len(word)):
    letter = word[i]
    print(letter)
for i, letter in enumerate(word):
    print(f"{i} = {letter}")