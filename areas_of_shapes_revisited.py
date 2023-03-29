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