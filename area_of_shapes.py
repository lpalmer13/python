square = float(input('What is the length of a side of the square? '))
print(f'The area of the square is: {square ** 2}')
print()
length = float(input('What is the length of the rectangle? '))
width = float(input('What is the width of the rectangle? '))
print(f'The area of the rectangle is: {length * width}')
print()
radius = float(input('What is the radius of the circle? '))
print(f'The area of the circle is: {3.14 * (radius ** 2)}')
print()
# stretch 1
import math
radius = float(input('What is the radius of the circle? '))
print(f'The area of the circle is: {math.pi * (radius ** 2)}')
print()
# stretch 2
value = float(input('What is the value to be used? '))
import math
square = value ** 2
circle = math.pi * (value ** 2)
cube = value ** 3
sphere = (4/3) * math.pi * (value ** 3)
print(f'Area of a square: {square}')
print(f'Area of a circle: {circle}')
print(f'Volume of a cube: {cube}')
print(f'Volume of a sphere: {sphere}')
print()
# stretch 3
side = float(input('What is the length of a side of the square (in cm)? '))
area = side ** 2
print(f'The area of the square is: {area} cm^2')
print(f'The area of the square is: {area / 10000} m^2')
length = float(input('What is the length of rectangle (in cm)? '))
width = float(input('What is the width of the rectangle (in cm)? '))
area = length * width
print(f'The area of the rectangle is: {area} cm^2')
print(f'The area of the rectangle is: {area / 10000} m^2')
radius = float(input('What is the radius of the circle (in cm)? '))
area = 3.14 * (radius ** 2)
print(f'The area of the circle is: {area} cm^2')
print(f'The area of the circle is: {area / 10000} m^2')