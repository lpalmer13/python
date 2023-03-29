import math

def compute_area_square(square):
    area = square ** 2
    return area


side = float(input('What is the length of a side of the square? '))
area_square = compute_area_square(side)
print(area_square)


def compute_area_rectangle(length, width):
    area = length * width
    return area

length = float(input('What is the length of the rectangle? '))
width = float(input('What is the width of the rectangle? '))
area_rectangle = compute_area_rectangle(length, width)
print(area_rectangle)

def compute_area_circle(radius):
    area = 3.14 * (radius ** 2)
    return area

radius = float(input('What is the radius of the circle? '))
area_circle = compute_area_circle(radius)
print(area_circle)

shape = ''

while shape != 'quit':
    shape = input('What shape do you have? ')

    shape = shape.lower()

    if shape == 'square':
        side = float(input('What is the length of a side of the square? '))
        area_square = compute_area_square(side)
        print(f'The area is {area_square}')

    if shape == 'rectangle':
        length = float(input('What is the length of the rectangle? '))
        width = float(input('What is the width of the rectangle? '))
        area_rectangle = compute_area_rectangle(length, width)
        print(f'The area is {area_rectangle}')

    if shape == 'circle':
        radius = float(input('What is the radius of the circle? '))
        area_circle = compute_area_circle(radius)
        print(f'The area is {area_circle}')